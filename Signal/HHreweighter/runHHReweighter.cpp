#include <iostream>
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include "TString.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TDirectory.h"
#include "TLorentzVector.h"
#include <map>
#include <fstream>
#include "HHReweight5D.h"
#include <vector>
#include <boost/algorithm/string/replace.hpp>


using namespace std;

//c++ -lm -o runHH runHHReweighter.cpp HHReweight5D.cpp `root-config --glibs --cflags`
int main ()
{
//	 float kl = 1.;
//	 float kt = 1.;
	 int Nkl=3;
    int Nkt=1;
	 float klmin=0;
	 float klmax=2;
	 float ktmin=1;
	 float ktmax=1;
	
	 TString s;
	 TString year = "2016";
	 TString addname = "_13TeV_125_13TeV_";
	 TString processName = "hh";
    TString inputDir = "/work/nchernya/DiHiggs/inputs/25_10_2019/trees/";
	 TString filename = s.Format("output_%s_%s.root",processName.Data(),year.Data()); 

    string coeffFile  = "coefficientsByBin_extended_3M_costHHSim_19-4.txt";
    TString inMapFile   = "HHreweight_2016nodes_18092019.root" ;
    TString inHistoName = "allHHNodeMap2D";
    TFile* fHHDynamicRew = new TFile(inputDir+inMapFile);
    TH2* hhreweighterInputMap =  (TH2*) fHHDynamicRew->Get(inHistoName);
    HHReweight5D* hhreweighter;
    hhreweighter = new HHReweight5D(((string)inputDir).append(coeffFile), hhreweighterInputMap,inputDir);

	 TString cats[13] = {}; 
	 TString cats_names[13] = {}; 
	 const int NCATS=12;
	 const int NGENCATS=13;
	 for (int i=0;i<NCATS;i++){
		cats[i] = s.Format("DoubleHTag_%d",i);
		cats_names[i] = s.Format("DoubleHTag_%d",i);
	 }
	 cats[NGENCATS-1] = "NoTag_0";

	 float  mhh, cosTheta, weight, benchmark_reweight_SM;
  
    TFile* fIn = TFile::Open(inputDir+filename);
	 TDirectory* dirGen1 = fIn->GetDirectory("genDiphotonDumper");
	 TDirectory* dirGen2 = dirGen1->GetDirectory("trees");
    float sum_gen_w_SM= 0;
	 std::vector<float> sum_gen_w(Nkl*Nkt, 0.);
	 for (int cat=0;cat<NGENCATS;cat++){
    	TTree *ch_gen = (TTree*)dirGen2->Get(s.Format("%s%s%s%s",processName.Data(),year.Data(),addname.Data(),cats[cat].Data()));
      ch_gen->SetBranchAddress("benchmark_reweight_SM", &benchmark_reweight_SM);
	   ch_gen->SetBranchAddress("weight", &weight);	
		ch_gen->SetBranchAddress("absCosThetaStar_CS", &cosTheta);
      ch_gen->SetBranchAddress("mhh", &mhh);
    	for (int iEv = 0; iEv<ch_gen->GetEntries(); ++iEv){
    		ch_gen->GetEntry(iEv);
    		if ((iEv % 100000 == 0) && (iEv!=0)) cout << "Event: " << iEv << endl;
			sum_gen_w_SM += weight*hhreweighter->getWeight(1.,1., 0., 0., 0., mhh, cosTheta); 			
			for(int ikl=0; ikl<Nkl; ++ikl){
				float kl = klmin + ikl*(klmax-klmin+1)/Nkl;
				for(int ikt=0; ikt<Nkt; ++ikt){
	  				float kt = ktmin + ikt*(ktmax-ktmin+1)/Nkt; 
					sum_gen_w[ikl+Nkl*ikt] += weight*hhreweighter->getWeight(kl, kt, 0., 0., 0., mhh, cosTheta);	
				}
			}		
      }
    }

	 TDirectory* dir1 = fIn->GetDirectory("tagsDumper");
	 TDirectory* dir2 = dir1->GetDirectory("trees");
	 float sum_w_cats_SM[NCATS] = {0,0,0,0,0,0,0,0,0,0,0,0};
	 std::vector<vector<float>> sum_w_cats(Nkl*Nkt, vector<float>(NCATS,0.));
	 for (int cat=0;cat<NCATS;cat++){
	   TTree *ch_reco = (TTree*)dir2->Get(s.Format("%s%s%s%s",processName.Data(),year.Data(),addname.Data(),cats[cat].Data()));
      ch_reco->SetBranchAddress("benchmark_reweight_SM", &benchmark_reweight_SM);
    	ch_reco->SetBranchAddress("weight", &weight);
   	ch_reco->SetBranchAddress("genAbsCosThetaStar_CS", &cosTheta);
    	ch_reco->SetBranchAddress("genMhh", &mhh);
   	for (int iEv = 0; iEv<ch_reco->GetEntries(); ++iEv){
       	ch_reco->GetEntry(iEv);
        	if ((iEv % 100000 == 0)&& (iEv!=0)) cout << "Event: " << iEv << endl;
			sum_w_cats_SM[cat] += weight*hhreweighter->getWeight(1.,1., 0., 0., 0., mhh, cosTheta); 			
			for(int ikl=0; ikl<Nkl; ++ikl){
				float kl = klmin + ikl*(klmax-klmin+1)/Nkl;
				for(int ikt=0; ikt<Nkt; ++ikt){
	  				float kt = ktmin + ikt*(ktmax-ktmin+1)/Nkt; 
    	 			sum_w_cats[ikl+Nkl*ikt][cat] += weight*hhreweighter->getWeight(kl, kt, 0., 0., 0., mhh, cosTheta);			
				}
			}		
    	}
 	 }

	//std::map<string, float> dictionary = {0};
	//dictionary[cats_names[cat]] = reweight_cat[cat];
	float reweight_cat_SM[NCATS] = {0,0,0,0,0,0,0,0,0,0,0,0};
	for (int cat=0;cat<NCATS;cat++)
		reweight_cat_SM[cat] = sum_w_cats_SM[cat]/sum_gen_w_SM;

	for(int ikl=0; ikl<Nkl; ++ikl){
		float kl = klmin + ikl*(klmax-klmin+1)/Nkl;
		for(int ikt=0; ikt<Nkt; ++ikt){
	  		float kt = ktmin + ikt*(ktmax-ktmin+1)/Nkt; 
	 		float reweight_cat[NCATS] = {0,0,0,0,0,0,0,0,0,0,0,0};

			ofstream out;
			std::string output_kl = boost::replace_all_copy(std::to_string(kl), ".", "d");
			output_kl = boost::replace_all_copy(output_kl, "-", "m");
			output_kl = boost::replace_all_copy(output_kl, "+", "p");
			std::string output_kt = boost::replace_all_copy(std::to_string(kt), ".", "d");
			output_kt = boost::replace_all_copy(output_kt, "-", "m");
			output_kt = boost::replace_all_copy(output_kt, "+", "p");
			string out_txt = (string)inputDir + "/reweighting_kl_"+output_kl+"_kt_"+output_kt+".txt";
			//out.open(s.Format("%s/reweighting_kl_%s_kt_%s.txt",inputDir.Data(),output_kl,output_kt));
			out.open(out_txt);

	 		for (int cat=0;cat<NCATS;cat++){
				reweight_cat[cat] = sum_w_cats[ikl+Nkl*ikt][cat]/sum_gen_w[ikl+Nkl*ikt];
				reweight_cat[cat] /= reweight_cat_SM[cat];
				cout<<reweight_cat[cat]<<endl;
				out<<reweight_cat[cat]<<endl;
	 		}
		}

	}
	fIn->Close();
}

