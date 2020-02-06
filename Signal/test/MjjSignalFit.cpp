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

// RooFit headers
#include <RooWorkspace.h>
#include <RooFitResult.h>
#include <RooRealVar.h>
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


using namespace RooFit ;
using namespace RooStats ;
using namespace std;

/*
class RooWorkspace;
class RooRealVar;
class RooAbsPdf;
struct RooFitResult;
struct RooArgSet;

*/

int main(int argc, char *argv[]){

	//gROOT->SetBatch();

  TString HLFactoryname = "wsig_fit";
  TString allCatFitsTemplate = "models_2D_higgs_mjj70.rs"; 
  HLFactory hlf(HLFactoryname,allCatFitsTemplate, false);
  RooWorkspace *w = (RooWorkspace*)hlf.GetWs();
  RooWorkspace *wAll = new RooWorkspace("wsig_13TeV","wsig_13TeV");



  float minMjjMassFit = 70;
  float maxMjjMassFit = 190;
  float minSigFitMjj = 70;
  float maxSigFitMjj = 190;
  const int _NCAT = 12; //12
 
//  std::vector<TString> procs = {"hh_node_SM","tth","ggh","vh","qqh"}; 
  std::vector<TString> procs = {"hh_node_SM"}; 
  TString year = "2016";
  TString indir = "/work/nchernya/DiHiggs/inputs/04_02_2020/";
  TString plotdir = "/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/plots/mjj/";
  TString outdir = "/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/mjj/";
  
  for (TString &iproc:procs) {
  TString signalfile = indir+"output_"+iproc+"_"+year+".root";
  TFile *sigFile = TFile::Open(signalfile);
  RooWorkspace *w_original = (RooWorkspace*)sigFile->Get("tagsDumper/cms_hgg_13TeV");
  RooRealVar* Mjj  = (RooRealVar*)w_original->var("Mjj");

  TString proc_type = "hig";
  TString proc_type_upper = proc_type;
  proc_type_upper[0] = std::toupper(proc_type_upper[0]);
  TString iproc_type = TString::Format("_%s",iproc.Data());
  if (iproc == "hh_node_SM")  {
		proc_type = "sig";
		proc_type_upper = proc_type;
      proc_type_upper[0] = std::toupper(proc_type_upper[0]);
      iproc_type = "";
	}

  Mjj->setRange(TString::Format("%sFitRange",proc_type_upper.Data()),minSigFitMjj,maxSigFitMjj);
  RooRealVar *weight = (RooRealVar*)w_original->var("weight");

  RooDataSet* sigToFit[_NCAT];
  for (int c = 0; c < _NCAT; ++c)
    {
      sigToFit[c] = (RooDataSet*) w_original->data(TString::Format("%s_%s_13TeV_125_DoubleHTag_%d",iproc.Data(),year.Data(),c));
	}
	

  RooAbsPdf* MjjSig[_NCAT];
  for (int c = 0; c < _NCAT; ++c)
    {
      MjjSig[c] = (RooAbsPdf*) w->pdf(TString::Format("Mjj%s%s_cat%d",proc_type_upper.Data(),iproc_type.Data(),c));
      MjjSig[c]->Print();

      ((RooRealVar*) w->var(TString::Format("Mjj_%s_m0%s_cat%d",proc_type.Data(),iproc_type.Data(),c)))->setVal(125.);
      MjjSig[c]->fitTo(*sigToFit[c],Range(TString::Format("%sFitRange",proc_type_upper.Data())),SumW2Error(kTRUE),PrintLevel(3));

      RooArgSet *sigParams = 0;
	   sigParams = (RooArgSet*) MjjSig[c]->getParameters(RooArgSet(*Mjj));

      w->defineSet(TString::Format("%s%sPdfParam_cat%d",proc_type_upper.Data(),iproc_type.Data(),c), *sigParams);
      auto params = w->set(TString::Format("%s%sPdfParam_cat%d",proc_type_upper.Data(),iproc_type.Data(),c));

      std::vector<std::pair<TString,TString>> varsToChange;
  		TIterator* iter(params->createIterator());
  		for (TObject *a = iter->Next(); a != 0; a = iter->Next())
   	{
      	RooRealVar *rrv = dynamic_cast<RooRealVar *>(a);
      	if (rrv) rrv->setConstant(true);
        TString thisVarName(a->GetName());
         TString newVarName = TString(thisVarName);
         newVarName.ReplaceAll("_cat", TString::Format("_%s_DoubleHTag_",year.Data()));
         newVarName.ReplaceAll(TString::Format("%s%s_",proc_type.Data(),iproc_type.Data()), "");
         newVarName.ReplaceAll(TString::Format("%s",year.Data()), TString::Format("%s_%s",iproc.Data(),year.Data()));
       //  newVarName.ReplaceAll("Mjj", "CMS_hbb_mass"); //will do this later
         w->import( *rrv, RenameVariable( thisVarName, newVarName));
	      wAll->import(*rrv, RenameVariable( thisVarName, newVarName));  
			varsToChange.push_back(std::make_pair(thisVarName, newVarName));

   	}
    //  w->import(*w->var("Mjj"), RenameVariable("Mjj","CMS_hbb_mass" ) );
	//   wAll->import(*w->var("Mjj"), RenameVariable("Mjj","CMS_hbb_mass" ));  

      sigParams->Print("v");
     
      TString EditPDF = TString::Format("EDIT::hbbpdfsm_13TeV_%s_%s_DoubleHTag_%d(Mjj%s%s_cat%d",iproc.Data(),year.Data(),c,proc_type_upper.Data(),iproc_type.Data(),c);
      for (unsigned int iv = 0; iv < varsToChange.size(); iv++)
		{
        EditPDF += TString::Format(",%s=%s", varsToChange[iv].first.Data(), varsToChange[iv].second.Data());
      }
	   EditPDF += (")");
      std::cout << "STRINGTOCHANGE   ---  " << EditPDF << std::endl;
      w->factory(EditPDF);


		TCanvas* can = new TCanvas("can","can",900,750);
		auto frame = Mjj->frame();
		RooDataHist* hist=(RooDataHist*)sigToFit[c];
		hist->plotOn(frame);
      MjjSig[c]->plotOn(frame);
		frame->Draw("same");

		TPaveText *pave = new TPaveText(0.55,0.7,0.8,0.8,"NDC");
		pave->SetTextAlign(11);
		pave->SetFillStyle(-1);
		pave->SetBorderSize(0);
		pave->SetTextFont(42);
      pave->SetTextSize(.05);
		pave->SetTextColor(kBlue+1);
		pave->AddText(TString::Format("%s %s",iproc.Data(),year.Data()));
		pave->Draw("same");

		can->SaveAs(TString::Format("%sfit_%s_%s_%d.pdf",plotdir.Data(),iproc.Data(),year.Data(),c));

      wAll->import(*w->pdf(TString::Format("hbbpdfsm_13TeV_%s_%s_DoubleHTag_%d",iproc.Data(),year.Data(),c)));
	}

   wAll->writeToFile(TString::Format("%sworkspace_out_%s_%s.root",outdir.Data(),iproc.Data(),year.Data()));
}
}
