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

  TString HLFactoryname = "testRun";
  TString allCatFitsTemplate = "models_2D_higgs_mjj70.rs"; 
  HLFactory hlf(HLFactoryname,allCatFitsTemplate, false);
  RooWorkspace *w = (RooWorkspace*)hlf.GetWs();

  float minMjjMassFit = 70;
  float maxMjjMassFit = 190;
  float minSigFitMjj = 70;
  float maxSigFitMjj = 190;
  const int _NCAT = 12; //12
 
  std::vector<TString> procs = {"hh_node_SM","tth"}; 
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
      w->set(TString::Format("%s%sPdfParam_cat%d",proc_type_upper.Data(),iproc_type.Data(),c))->Print("v");
      //SetConstantParams(w->set(TString::Format("SigPdfParam_cat%d",c))); ///Why constant ????

      sigParams->Print("v");

		TCanvas* can = new TCanvas("can","can",900,750);
		auto frame = Mjj->frame();
		RooDataHist* hist=(RooDataHist*)sigToFit[c];
		hist->plotOn(frame);
      MjjSig[c]->plotOn(frame);
		frame->Draw("same");
		can->SaveAs(TString::Format("%sfit_%s_%s_%d.pdf",plotdir.Data(),iproc.Data(),year.Data(),c));

	   w->import(*MjjSig[c]);
	}

   w->writeToFile(TString::Format("%sworkspace_out_%s_%s.root",outdir.Data(),iproc.Data(),year.Data()));
}
}
