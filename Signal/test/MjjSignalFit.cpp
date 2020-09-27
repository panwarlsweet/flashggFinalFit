// C++ headers
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <string>

// ROOT headers
#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TCanvas.h>
#include <TPaveText.h>
#include "TGaxis.h"

// RooFit headers
#include <RooWorkspace.h>
#include <RooFitResult.h>
#include <RooRealVar.h>
#include <RooAbsReal.h>
#include <RooDataHist.h>
#include <RooCategory.h>
#include <RooArgSet.h>
#include "RooStats/HLFactory.h"
#include <RooDataSet.h>
#include <RooFormulaVar.h>
#include <RooGenericPdf.h>
#include <RooPlot.h>
#include <RooAbsPdf.h>
#include <RooBernstein.h>
#include <RooExtendPdf.h>
#include <RooMinimizer.h>
#include "RooStats/RooStatsUtils.h"
#include <RooMsgService.h>
#include <RooProdPdf.h>
#include <RooExponential.h>
#include <RooPolynomial.h>
#include <RooMoment.h>
#include <RooFitResult.h>

#include "boost/program_options.hpp"
#include "boost/algorithm/string/split.hpp"
#include "boost/algorithm/string/classification.hpp"
#include "boost/algorithm/string/predicate.hpp"
#include <boost/algorithm/string/replace.hpp>

#include "../interface/WSTFileWrapper.h"

#include "TGaxis.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TPaveText.h"
#include "TArrow.h"
#ifndef TDRSTYLE_C
#define TDRSTYLE_C
#include "../../tdrStyle/tdrstyle.C"
#include "../../tdrStyle/CMS_lumi.C"
#endif

using namespace RooFit ;
using namespace RooStats ;
using namespace std;

namespace po = boost::program_options;
string indir_;
string year_;
string mergeYearsStr_;
string lumiYearsStr_;
string templatefile_;
vector<string> signalproc_;
string signalprocStr_;
string outdir_;
string plotdir_;
string procStr_;
vector<string> procs_;
string flashggCatsStr_;
vector<string> flashggCats_;
string infilesStr_;
string infileWithAllYearsStr_;
vector<string> infiles_;
vector<string> mergeYears_;
vector<string> vecLumiYears_;
vector<double> lumiYears_;
bool mergeFitMVAcats_;
int nCats_;
int nMVA_;
int nMX_;
bool paper_;

void OptionParser(int argc, char *argv[]){
	po::options_description desc1("Allowed options");
	desc1.add_options()
		("indir,d", po::value<string>(&indir_), "Input file dir")
		("paper", po::value<bool>(&paper_)->default_value(false), "Style for paper")
		("infiles,i", po::value<string>(&infilesStr_)->default_value(""), "Input files (comma sep), without inputdir")
		("infileWithAllYears", po::value<string>(&infileWithAllYearsStr_)->default_value(""), "Files(comma sep) with all years if you want to merge 2016,2017 and 2018. Input dir should be already in the name")
		("template,t", po::value<string>(&templatefile_), "Fit template file name")
		("year,y", po::value<string>(&year_), "year")
		("mergeYears", po::value<string>(&mergeYearsStr_)->default_value(""), "Merge years or not, if yes a list of years should be given")
		("lumiYears", po::value<string>(&lumiYearsStr_)->default_value("35.9,41.2,59."), "lumi of the years to be merged")
		("outfiledir,o", po::value<string>(&outdir_)->default_value("test/"), "Output file dir")
		("plotdir,p", po::value<string>(&plotdir_)->default_value("test/"), "Plot dir")
		("procs", po::value<string>(&procStr_)->default_value("hh_node_SM,ggh,qqh,vh,tth"), "Processes (comma sep)")
		//("signalproc,s", po::value<string>(&signalproc_)->default_value("hh_node_SM"), "Name of the signal process")
		("signalproc,s", po::value<string>(&signalprocStr_)->default_value("hh_node_SM,ggHH_kl_0_kt_1,ggHH_kl_1_kt_1,ggHH_kl_2p45_kt_1,ggHH_kl_5_kt_1,qqHH_CV_1_C2V_1_kl_1,qqHH_CV_1_C2V_2_kl_1,qqHH_CV_1_C2V_1_kl_2,qqHH_CV_1_C2V_1_kl_0,qqHH_CV_0p5_C2V_1_kl_1,qqHH_CV_1p5_C2V_1_kl_1,qqHH_CV_1_C2V_0_kl_1"), "Name of the signal process")
//		("flashggCats,f", po::value<string>(&flashggCatsStr_)->default_value("DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11"), "Flashgg categories")
		("flashggCats,f", po::value<string>(&flashggCatsStr_)->default_value("DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"), "Flashgg categories")
		("nCats", po::value<int>(&nCats_)->default_value(3), "Numer of flashgg categories")
		("nMVA", po::value<int>(&nMVA_)->default_value(3), "Numer of MVA categories")
		("nMX", po::value<int>(&nMX_)->default_value(4), "Numer of MX categories")
		("mergeFitMVAcats,m", po::value<bool>(&mergeFitMVAcats_)->default_value(false), "Merge categories into 3 MVA for single Higgs fits ")
		;                                                                                             		
	po::options_description desc("Allowed options");
	desc.add(desc1);

	po::variables_map vm;
	po::store(po::parse_command_line(argc,argv,desc),vm);
	po::notify(vm);

	split(procs_,procStr_,boost::is_any_of(","));
	split(infiles_,infilesStr_,boost::is_any_of(","));
	split(signalproc_,signalprocStr_,boost::is_any_of(","));
	split(flashggCats_,flashggCatsStr_,boost::is_any_of(","));
	split(mergeYears_,mergeYearsStr_,boost::is_any_of(","));
	split(vecLumiYears_,lumiYearsStr_,boost::is_any_of(","));
	for (unsigned int iyear=0; iyear< mergeYears_.size();++iyear)
		lumiYears_.push_back(std::stod(vecLumiYears_[iyear]));
	system(Form("mkdir -p %s",plotdir_ .c_str()));
	system(Form("mkdir -p %s",outdir_.c_str()));
}



// get FWHHM
vector<double> getFWHM(TH1F *h) {
  cout << "Computing FWHM...." << endl;
  double hm = h->GetMaximum()*0.5;
  double low = h->GetBinCenter(h->FindFirstBinAbove(hm));
  double high = h->GetBinCenter(h->FindLastBinAbove(hm));

  cout << "FWHM: [" << low << "-" << high << " = " << high-low <<"] Max = " << hm << endl;
  vector<double> result;
  result.push_back(low);
  result.push_back(high);
  result.push_back(hm);
  result.push_back(h->GetBinWidth(1));
  return result;
}


pair<double,double> getEffSigma(RooRealVar *mass, RooAbsPdf *pdf, double wmin=90., double wmax=170., double step=0.5, double epsilon=1.e-2){
//pair<double,double> getEffSigma(RooRealVar *mass, RooAbsPdf *pdf, double wmin=90., double wmax=170., double step=0.5, double epsilon=1.e-1){

  RooAbsReal *cdf = pdf->createCdf(RooArgList(*mass));
  cout << "Computing effSigma...." << endl;
  TStopwatch sw;
  sw.Start();
  double point=wmin;
  vector<pair<double,double> > points;

  while (point <= wmax){
    mass->setVal(point);
    if (pdf->getVal() > epsilon){
      points.push_back(pair<double,double>(point,cdf->getVal())); 
    }
    point+=step;
  }
  double low = wmin;
  double high = wmax;
  double width = wmax-wmin;
  for (unsigned int i=0; i<points.size(); i++){
    for (unsigned int j=i; j<points.size(); j++){
      double wy = points[j].second - points[i].second;
      if (TMath::Abs(wy-0.683) < epsilon){
        double wx = points[j].first - points[i].first;
        if (wx < width){
          low = points[i].first;
          high = points[j].first;
          width=wx;
        }
      }
    }
  }
  sw.Stop();
  cout << "effSigma: [" << low << "-" << high << "] = " << width/2. << endl;
  //cout << "\tTook: "; sw.Print();
  pair<double,double> result(low,high);
  return result;
}


void RooDraw(TCanvas *can, TH1F *h, RooPlot* frame,RooDataHist* hist, RooAbsPdf* model,string iproc,string category, bool putyear, bool calc_width, pair<double,double> sigRange,vector<double> fwhmRange){

   double semin;
   double semax;
   double fwmin;
   double fwmax;
   double halfmax;
   double binwidth;
	TObject *seffLeg;

   if (calc_width) {
      semin=sigRange.first;
      semax=sigRange.second;
      fwmin=fwhmRange[0];
      fwmax=fwhmRange[1];
      halfmax=fwhmRange[2];
      binwidth=fwhmRange[3];
   }

  	can->SetLeftMargin(0.16);
  	can->SetTickx(); can->SetTicky();
	can->cd();
	frame->GetXaxis()->SetTitle("M_{bb} (GeV)");
	frame->SetTitle("");
	frame->GetXaxis()->SetTitle("m_{jj} (GeV)");
	frame->GetXaxis()->SetTitleSize(0.05);
	frame->GetYaxis()->SetTitleSize(0.05);
	frame->GetYaxis()->SetTitleOffset(1.5);
	frame->SetMinimum(0.0);
	TGaxis::SetExponentOffset(-0.09,0,"xy");
	TGaxis::SetMaxDigits(4);
   frame->GetYaxis()->SetTitle(Form("Events / ( %.1f GeV )",h->GetBinWidth(1)));
   frame->GetYaxis()->SetNdivisions(505);
	frame->GetYaxis()->SetRangeUser(0.,h->GetBinContent(h->GetMaximumBin())*1.2);
 	frame->Draw();
	hist->plotOn(frame,MarkerStyle(kOpenSquare));
	TObject *dataLeg = frame->getObject(int(frame->numItems()-1));
	double norm = h->Integral();
	if (norm<0) norm=0.;
	model->plotOn(frame,Normalization(norm,RooAbsReal::NumEvent),LineColor(kBlue),LineWidth(2),FillStyle(0));
	TObject *pdfLeg = frame->getObject(int(frame->numItems()-1));
	if (calc_width) {
   	model->plotOn(frame,Range(semin,semax),FillColor(19),DrawOption("F"),LineWidth(2),FillStyle(1001),VLines(),LineColor(15));
  		seffLeg = frame->getObject(int(frame->numItems()-1));
  		model->plotOn(frame,Range(semin,semax),LineColor(15),LineWidth(2),FillStyle(1001),VLines());
	}
	hist->plotOn(frame,MarkerStyle(kOpenSquare));
	model->plotOn(frame,Normalization(norm,RooAbsReal::NumEvent),LineColor(kBlue),LineWidth(2),FillStyle(0));
	frame->Draw("same");

	double offset =0.05;
	TString newtitle = iproc;
	if (iproc.find("vbfhh") != std::string::npos) newtitle = "VBF HH SM : H#rightarrow bb H#rightarrow#gamma#gamma"; 
	//	else if (iproc.find("hh") != std::string::npos) newtitle = "ggF HH SM : H#rightarrow bb H#rightarrow#gamma#gamma";
	else if (iproc.find("Radionhh") != std::string::npos) newtitle = "(Spin-0) X#rightarrow HH#rightarrow #gamma#gammab#bar{b}";
	else if (iproc.find("BulkGravitonhh") != std::string::npos) newtitle = "(Spin-2) X#rightarrow HH#rightarrow #gamma#gammab#bar{b}";
	else if (iproc.find("NMSSMhh") != std::string::npos) newtitle = "(Spin-0) X#rightarrow HY#rightarrow #gamma#gammab#bar{b}";
 
	if (paper_) if (iproc.find("hh_node_SM") != std::string::npos) newtitle = "ggF HH#rightarrow#gamma#gammab#bar{b}"; 
	if (paper_) if (iproc.find("qqHH") != std::string::npos) newtitle = "VBF HH#rightarrow#gamma#gammab#bar{b}"; 
	TLatex *lat1 = new TLatex(.129+0.03+offset,0.85,newtitle);
	lat1->SetNDC(1);
	lat1->SetTextSize(0.047);

	TString catLabel_humanReadable  = year_+" "+category;
	if (!putyear) catLabel_humanReadable  = category;
	if (paper_) catLabel_humanReadable  = category;
	catLabel_humanReadable.ReplaceAll("_"," ");
	catLabel_humanReadable.ReplaceAll("VBFDoubleHTag","VBF CAT");
	catLabel_humanReadable.ReplaceAll("DoubleHTag","ggF CAT");
	TLatex *lat2 = new TLatex(0.93,0.88,catLabel_humanReadable);
	lat2->SetTextAlign(33);
	lat2->SetNDC(1);
	lat2->SetTextSize(0.045);


	//TLegend *leg = new TLegend(0.15+offset,0.40,0.5+offset,0.82);
	TLegend *leg = new TLegend(0.6+offset,0.40,0.95+offset,0.82);
	leg->SetFillStyle(0);
	leg->SetLineColor(0);
	leg->SetTextSize(0.037);
	leg->SetBorderSize(0);
	leg->AddEntry(dataLeg,"#bf{Simulation}","lep");
	leg->AddEntry(pdfLeg,"#splitline{#bf{Parametric}}{#bf{model}}","l");


	if (calc_width) {
		leg->AddEntry(seffLeg,Form("#bf{#sigma_{eff} = %1.1f GeV}",0.5*(semax-semin)),"fl");
		halfmax*=(frame->getFitRangeBinW()/binwidth);
		TArrow *fwhmArrow = new TArrow(fwmin,halfmax,fwmax,halfmax,0.02,"<>");
		fwhmArrow->SetLineWidth(2.);
		//TPaveText *fwhmText = new TPaveText(0.17+offset,0.3,0.45+offset,0.40,"brNDC");
		TPaveText *fwhmText = new TPaveText(0.56+offset,0.3,.97+offset,0.40,"brNDC");
		//fwhmText->SetFillColor(0);
		fwhmText->SetBorderSize(0);
		fwhmText->SetFillStyle(0);
		fwhmText->SetLineColor(kWhite);
		fwhmText->SetTextSize(0.037);
		fwhmText->AddText(Form("FWHM = %1.1f GeV",(fwmax-fwmin)));	
		fwhmArrow->Draw("same <>");
		fwhmText->Draw("same");
	}

	lat2->Draw("same");
	lat1->Draw("same");
	leg->Draw("same");

	TString sim="Simulation Preliminary";
   writeExtraText = true;
	if (paper_) sim="Simulation"; //for the paper
	CMS_lumi( can, 0,0,sim);
	can->Update();
}


///copy and scale weight 
RooDataSet *scaleWeight(RooDataSet *indata, RooRealVar *mvar, RooRealVar *wvar, TString name, double weightscale) {
	RooDataSet *outdata = new RooDataSet(name,"",RooArgList(*mvar,*wvar),wvar->GetName());
	for (int ient=0; ient<indata->numEntries(); ++ient) {
		const RooArgSet *ent = indata->get(ient);		
		double val = static_cast<RooAbsReal*>(ent->find(mvar->GetName()))->getVal();
		mvar->setVal(val);
		outdata->add(*mvar,weightscale*indata->weight());
	}
  return outdata;
}


int main(int argc, char *argv[]){

	OptionParser(argc,argv);

	RooMsgService::instance().setGlobalKillBelow(RooFit::ERROR);
	RooMsgService::instance().setSilentMode(true);
	setTDRStyle();
	extraText  = "";  // default extra text is "Preliminary"
	lumi_13TeV  = "2.7 fb^{-1}"; // default is "19.7 fb^{-1}"
	lumi_sqrtS = "13 TeV";       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)


	gROOT->SetBatch();
	gStyle->SetTextFont(42);

	string HLFactoryname = "wsig_fit";
	string allCatFitsTemplate = templatefile_; 
	HLFactory hlf(HLFactoryname.c_str(),allCatFitsTemplate.c_str(), false);
	RooWorkspace *w = (RooWorkspace*)hlf.GetWs();
	RooWorkspace *wAll = new RooWorkspace("wsig_13TeV","wsig_13TeV");

	float minSigFitMjj = 70;
	float maxSigFitMjj = 190;
	const int NCAT = flashggCats_.size(); 

	unsigned int iproc_num = 0;
	for (auto &iproc:procs_) {
		string signalfile = indir_+iproc+"_"+year_+".root";
		if (!(infilesStr_.empty())){  //If inputfiles are provided by a user
			signalfile = indir_+infiles_[iproc_num];
		}
      WSTFileWrapper * w_original_all;
		if (!(infileWithAllYearsStr_.empty())){  //If inputfiles are provided by a user
      	w_original_all = new WSTFileWrapper(infileWithAllYearsStr_,"tagsDumper/cms_hgg_13TeV");
		}

		TFile *sigFile = TFile::Open(signalfile.c_str());
		RooWorkspace *w_original = (RooWorkspace*)sigFile->Get("tagsDumper/cms_hgg_13TeV");
		RooRealVar* Mjj  = (RooRealVar*)w_original->var("Mjj");
	
		string proc_type = "hig";	
		string proc_type_upper = proc_type;
		proc_type_upper[0] = std::toupper(proc_type_upper[0]);
		string iproc_type = "_"+iproc;
	//	if (iproc == signalproc_)  {
		if (signalprocStr_.find(iproc) != string::npos )  {
			proc_type = "sig";
			proc_type_upper = proc_type;
			proc_type_upper[0] = std::toupper(proc_type_upper[0]);
			iproc_type = "";
		}

		Mjj->setRange((iproc+"FitRange").c_str(),minSigFitMjj,maxSigFitMjj);
		int nbins = 24;
		Mjj->setBins(nbins); //70 - 190, reasonbale bins 5 GeV
		RooRealVar *weight = (RooRealVar*)w_original->var("weight");

		RooDataSet* sigToFit[NCAT];
		RooDataSet* sigToFitMVA[nMVA_];
		RooDataSet* sigToFitAllYears[NCAT];
		std::map<int,int> categories_scheme = {{0,0},{1,0},{2,0},{3,0},{4,1},{5,1},{6,1},{7,1},{8,2},{9,2},{10,2},{11,2}};
		for (int ic = 0; ic < NCAT; ++ic)
		{
			auto icat = flashggCats_[ic];
			sigToFit[ic] = (RooDataSet*) w_original->data((iproc+"_"+year_+"_13TeV_125_"+icat).c_str());
			if (!(mergeYearsStr_.empty())) {
				for (unsigned int iyear=0; iyear< mergeYears_.size();++iyear){
					RooDataSet *tmp = (RooDataSet*) w_original_all->data((iproc+"_"+mergeYears_[iyear]+"_13TeV_125_"+icat).c_str());	
					if (iyear==0) sigToFitAllYears[ic] = scaleWeight(tmp,Mjj,weight,(iproc+"_YearsMerged_13TeV_125_"+icat).c_str(),lumiYears_[iyear]);
					else sigToFitAllYears[ic]->append(*(scaleWeight(tmp,Mjj,weight,(iproc+"_YearsMerged_13TeV_125_"+icat).c_str(),lumiYears_[iyear])));
				}
			}
			if ((mergeFitMVAcats_) && (NCAT==nCats_)) { //only works in case the set of categories is complete
				int mva_cat = categories_scheme[ic];
				if (mergeYearsStr_.empty()) {
					if ( (ic+1)%nMX_ == 1 )
						sigToFitMVA[mva_cat] = ((RooDataSet*)sigToFit[ic]->Clone((iproc+"_"+year_+"_13TeV_125_MVA"+to_string(mva_cat)).c_str()));
					else 
						sigToFitMVA[mva_cat]->append(*((RooDataSet*)sigToFit[ic]));
				}
				else {
					if ( (ic+1)%nMX_ == 1 )
						sigToFitMVA[mva_cat] = ((RooDataSet*)sigToFitAllYears[ic]->Clone((iproc+"_"+year_+"_13TeV_125_MVA"+to_string(mva_cat)).c_str()));
					else 
						sigToFitMVA[mva_cat]->append(*((RooDataSet*)sigToFitAllYears[ic]));
				}
			}
		}

		RooAbsPdf* MjjSig[NCAT];
		//RooFitResult* fitResult[NCAT];
		for (int ic = 0; ic < NCAT; ++ic)
		{
			auto icat = flashggCats_[ic];
			int c = stoi(icat.substr(icat.find_last_of("_")+1)); //find category number used
			if (icat.find("VBFDoubleHTag") != string::npos ) c = 12+stoi(icat.substr(icat.find_last_of("_")+1)); //category number is 12+0/1/2.... if it is VBFDoubleHTAg
			
			if(iproc.find("ggh") != string::npos || iproc.find("qqh") != string::npos) {
					MjjSig[ic] = new RooBernstein(("MjjHig_"+iproc+"_cat"+std::to_string(c)).c_str(),"",*Mjj,
					RooArgList( *w->var( ("Mjj_hig_par1_"+iproc+"_cat"+std::to_string(c)).c_str()) ,
							*w->var(("Mjj_hig_par2_"+iproc+"_cat"+std::to_string(c)).c_str()) ,//))); //,
							*w->var(("Mjj_hig_par3_"+iproc+"_cat"+std::to_string(c)).c_str() )));
					w->import(*MjjSig[ic]);
			}
			else MjjSig[ic] = (RooAbsPdf*) w->pdf(("Mjj"+proc_type_upper+iproc_type+"_cat"+to_string(c)).c_str());

			MjjSig[ic]->Print();

			//Normalization per category
			double normalization_cat = 0.;	
			if ((c==10) || (c==11)) {
				Mjj->setRange((iproc+"CutRange").c_str(),90.,maxSigFitMjj);
				normalization_cat = (sigToFit[ic]->sumEntries("1",(iproc+"CutRange").c_str()))/1000.; //as for Hgg use fb
				cout<<"Setting normalization range to 90 GeV for cat "<<c<<" , "<<normalization_cat<<endl;
				cout<<sigToFit[ic]->sumEntries()/1000.<<endl;
			} else {
				normalization_cat = sigToFit[ic]->sumEntries()/1000.; //as for Hgg use fb
			}
	//		normalization_cat = sigToFit[ic]->sumEntries()/1000.; //as for Hgg use fb
			Mjj->setRange((iproc+"FitRange").c_str(),minSigFitMjj,maxSigFitMjj);
			if (normalization_cat < 0) normalization_cat = 0.;
			RooRealVar *MjjSig_normalization = new RooRealVar(("hbbpdfsm_13TeV_"+iproc+"_"+year_+"_"+icat+"_normalization").c_str(),("hbbpdfsm_13TeV_"+iproc+"_"+year_+"_"+icat+"_normalization").c_str(),normalization_cat,"");
			MjjSig_normalization->setConstant(true);
			RooFormulaVar *finalNorm = new RooFormulaVar(("hbbpdfsm_13TeV_"+iproc+"_"+year_+"_"+icat+"_norm").c_str(),("hbbpdfsm_13TeV_"+iproc+"_"+year_+"_"+icat+"_norm").c_str(),"@0",RooArgList(*MjjSig_normalization));
			w->import( *finalNorm);


			if (proc_type == "sig")  ((RooRealVar*) w->var(("Mjj_"+proc_type+"_m0"+iproc_type+"_cat"+to_string(c)).c_str()))->setVal(125.);
			if ((mergeFitMVAcats_) && (NCAT==nCats_)){  //only works in case the set of categories is complete
				MjjSig[ic]->fitTo(*sigToFitMVA[categories_scheme[ic]],Range((proc_type_upper+"FitRange").c_str()),SumW2Error(kTRUE),PrintLevel(3));
			} else if (!mergeYearsStr_.empty()){  
				MjjSig[ic]->fitTo(*sigToFitAllYears[ic],Range((proc_type_upper+"FitRange").c_str()),SumW2Error(kTRUE),PrintLevel(3));
			} else 
				MjjSig[ic]->fitTo(*sigToFit[ic],Range((proc_type_upper+"FitRange").c_str()),SumW2Error(kTRUE),PrintLevel(3));

			//fitResult[ic] =  (RooFitResult*)MjjSig[ic]->fitTo(*sigToFit[ic],Range((proc_type_upper+"FitRange").c_str()),SumW2Error(kTRUE),PrintLevel(3))->Clone();

			RooArgSet *sigParams = 0;
			sigParams = (RooArgSet*) MjjSig[ic]->getParameters(RooArgSet(*Mjj));

			w->defineSet((proc_type_upper+iproc_type+"PdfParam_cat"+to_string(c)).c_str(), *sigParams);
			auto params = w->set((proc_type_upper+iproc_type+"PdfParam_cat"+to_string(c)).c_str());

			std::vector<std::pair<string,string>> varsToChange;
			TIterator* iter(params->createIterator());
			for (TObject *a = iter->Next(); a != 0; a = iter->Next())
			{
				RooRealVar *rrv = dynamic_cast<RooRealVar *>(a);
				if (rrv) rrv->setConstant(true);
				string thisVarName(a->GetName());
				string newVarName = string(thisVarName);
				boost::replace_all(newVarName,"_cat", "_"+year_+"_"+icat.substr(0,icat.find_last_of("_")+1) );
				boost::replace_all(newVarName,proc_type+"_", "");
				boost::replace_all(newVarName,year_, (iproc+"_"+year_));
				//boost::replace_all(newVarName,"Mjj", "CMS_hbb_mass"); //will do this later
				w->import( *rrv, RenameVariable( thisVarName.c_str(), newVarName.c_str()));
				wAll->import(*rrv, RenameVariable( thisVarName.c_str(), newVarName.c_str()));  
				varsToChange.push_back(std::make_pair(thisVarName.c_str(), newVarName.c_str()));
			}
			//  w->import(*w->var("Mjj"), RenameVariable("Mjj","CMS_hbb_mass" ) );//will do this later
			//   wAll->import(*w->var("Mjj"), RenameVariable("Mjj","CMS_hbb_mass" ));  //will do this later if needed
			      
			sigParams->Print("v");

			string EditPDF = ("EDIT::hbbpdfsm_13TeV_"+iproc+"_"+year_+"_"+icat+"(Mjj"+proc_type_upper+iproc_type+"_cat"+to_string(c));
			for (unsigned int iv = 0; iv < varsToChange.size(); iv++)
			{
				EditPDF += (","+varsToChange[iv].first +"="+varsToChange[iv].second).c_str();		
			}
			EditPDF += (")");
			w->factory(EditPDF.c_str());

			///Plot everything 
			double putyear = 1;	
			bool calc_width=1;
			TH1F *h = new TH1F(("h_"+iproc+"_"+year_+"_"+icat).c_str(),("h_"+iproc+"_"+year_+"_"+icat).c_str(),nbins,minSigFitMjj,maxSigFitMjj);
			MjjSig[ic]->fillHistogram(h,RooArgList(*Mjj),sigToFit[ic]->sumEntries());
			TH1F *h_fine = new TH1F(("h_"+iproc+"_"+year_+"_"+icat+"_fine").c_str(),("h_"+iproc+"_"+year_+"_"+icat+"_fine").c_str(),nbins*50,minSigFitMjj,maxSigFitMjj);
			MjjSig[ic]->fillHistogram(h_fine,RooArgList(*Mjj),sigToFit[ic]->sumEntries());
			pair<double,double> thisSigRange = getEffSigma(Mjj,MjjSig[ic]);
			vector<double> fwhmRange = getFWHM(h_fine);		

			TCanvas* can = new TCanvas("can","can",650,650);
			RooDraw(can,h,Mjj->frame(),((RooDataHist*)sigToFit[ic]),MjjSig[ic],iproc,(icat),putyear,calc_width, thisSigRange,fwhmRange);
			string canname = plotdir_+"/fit_"+iproc+"_"+year_+"_"+icat;
			can->Print((canname+".pdf").c_str());
			can->Print((canname+".jpg").c_str());
  			delete can;

			if (!mergeYearsStr_.empty()) putyear=0;
			if ((mergeFitMVAcats_) && (NCAT==nCats_)){  //only works in case the set of categories is complete
				TH1F *hMVA = new TH1F(("hMVA_"+iproc+"_"+year_+"_"+icat).c_str(),("hMVA_"+iproc+"_"+year_+"_"+icat).c_str(),nbins,minSigFitMjj,maxSigFitMjj);
				MjjSig[ic]->fillHistogram(hMVA,RooArgList(*Mjj),sigToFitMVA[categories_scheme[ic]]->sumEntries());
				TH1F *hMVA_fine = new TH1F(("hMVA_"+iproc+"_"+year_+"_"+icat+"_fine").c_str(),("hMVA_"+iproc+"_"+year_+"_"+icat+"_fine").c_str(),nbins*50,minSigFitMjj,maxSigFitMjj);
				MjjSig[ic]->fillHistogram(hMVA_fine,RooArgList(*Mjj),sigToFitMVA[categories_scheme[ic]]->sumEntries());
				thisSigRange = getEffSigma(Mjj,MjjSig[ic]);
				fwhmRange = getFWHM(hMVA_fine);		


				TCanvas* canMVA = new TCanvas("canMVA","canMVA",650,650);
				RooDraw(canMVA,hMVA,Mjj->frame(),((RooDataHist*)sigToFitMVA[categories_scheme[ic]]),MjjSig[ic],iproc,("MVA "+to_string(categories_scheme[ic])),putyear,calc_width, thisSigRange,fwhmRange);
				string cannameMVA = plotdir_+"/fit_"+iproc+"_"+year_+"_MVA"+to_string(categories_scheme[ic]);
				canMVA->Print((cannameMVA+".pdf").c_str());
				canMVA->Print((cannameMVA+".jpg").c_str());
  				delete canMVA;
			}
			if (!mergeYearsStr_.empty()){  
				TH1F *hAllYears = new TH1F(("hAllYears_"+iproc+"_"+year_+"_"+icat).c_str(),("hAllYears_"+iproc+"_"+year_+"_"+icat).c_str(),nbins,minSigFitMjj,maxSigFitMjj);
				MjjSig[ic]->fillHistogram(hAllYears,RooArgList(*Mjj),sigToFitAllYears[ic]->sumEntries());
				TH1F *hAllYears_fine = new TH1F(("hAllYears_"+iproc+"_"+year_+"_"+icat+"_fine").c_str(),("hAllYears_"+iproc+"_"+year_+"_"+icat+"_fine").c_str(),nbins*50,minSigFitMjj,maxSigFitMjj);
				MjjSig[ic]->fillHistogram(hAllYears_fine,RooArgList(*Mjj),sigToFitAllYears[ic]->sumEntries());
				thisSigRange = getEffSigma(Mjj,MjjSig[ic]);
				fwhmRange = getFWHM(hAllYears_fine);		

				TCanvas* canAllYears = new TCanvas("canAllYears","canAllYears",650,650);
				RooDraw(canAllYears,hAllYears,Mjj->frame(),((RooDataHist*)sigToFitAllYears[ic]),MjjSig[ic],iproc,(icat),putyear,calc_width, thisSigRange,fwhmRange);
				string cannameAllYears = plotdir_+"/fit_"+iproc+"_"+year_+"_AllYears_"+icat;
				canAllYears->Print((cannameAllYears+".pdf").c_str());
				canAllYears->Print((cannameAllYears+".jpg").c_str());
  				delete canAllYears;
			}


			string finalpdfname = "hbbpdfsm_13TeV_"+iproc+"_"+year_+"_"+icat;
			wAll->import(*w->pdf(finalpdfname.c_str()));
			wAll->import( *w->function((finalpdfname+"_norm").c_str()));
		}
		wAll->writeToFile((outdir_+"/workspace_out_"+iproc+"_"+year_+".root").c_str());
		iproc_num+=1;
	}
	std::cout<<"All fits have finished, now merge the workspaces : mergeWorkspace.py workspace_out_mjj.root *.root"<<std::endl;	
}
