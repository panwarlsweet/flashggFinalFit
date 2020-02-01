import ROOT
from ROOT import *
import numpy as np
from optparse import OptionParser, make_option
import sys
import os
import json


parser = OptionParser(option_list=[
    make_option("--inp-files",type='string',dest='inp_files',default='DoubleEG_2017_24_04_2019'),  #2016
  #  make_option("--inp-files",type='string',dest='inp_files',default='VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8_v2,VBFHToGG_M-125_13TeV_powheg_pythia8,GluGluHToGG_M-125_13TeV_powheg_pythia8,GluGluToHHTo2B2G_node_SM_13TeV-madgraph_generated'),  #2016
  #  make_option("--inp-files",type='string',dest='inp_files',default='ttHToGG_M125_13TeV_powheg_pythia8,GluGluHToGG_M-125_13TeV_powheg_pythia8,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,GluGluToHHTo2B2G_node_SM_13TeV-madgraph_generated'), #2017
    make_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/inputs/24_04_2019/'),
    make_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/inputs/25_04_2019/'),
    make_option("--year",type='string',dest="year",default='2017'),
    make_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11'),
])

(options, args) = parser.parse_args()
cats = options.cats.split(',')
input_files = options.inp_files.split(',')
input_names = []
for num,f in enumerate(input_files):
	if ('Data'  in f) : input_names.append(f.replace('-','_') +'_13TeV') 
	elif '2016' in options.year : input_names.append(f.replace('-','_') +'_13TeV') 
	elif '2017' in options.year : input_names.append(f.replace('-','_') +'_2017_13TeV')
	input_files[num] = 'output_' + f 

#options.inp_dir = options.inp_dir + options.year + '/'
#options.inp_dir = options.inp_dir + "renamed"+ options.year + '/'
#options.out_dir = options.out_dir + options.year + '/'
options.out_dir = options.out_dir +  '/'
options.inp_dir = options.inp_dir + '/'


wsname = "tagsDumper/cms_hgg_13TeV"

for num,f in enumerate(input_files):
	print 'doing file ',f
	if 'DoubleEG' in f : tfile = TFile(options.inp_dir + f+".root")  
	elif '2016' in options.year : tfile = TFile(options.inp_dir + f+".root")  #2016
	elif '2017' in options.year : tfile = TFile(options.inp_dir + f+"_2017.root") 
	ws = tfile.Get(wsname)
	cat_datasets=[]
	for cat in cats :
				print 'doing cat ',cat
				if "DoubleEG" in f : name = 'Data_13TeV_'+cat
				else : name = input_names[num]+'_'+cat
				mass = RooRealVar("CMS_hgg_mass","CMS_hgg_mass",100,180) 
				dZ = RooRealVar("dZ","dZ",-20,20) 
				centralObjectWeight = RooRealVar("centralObjectWeight","centralObjectWeight",-999999.,999999.) 
				dataset = (ws.data(name))
			#	dataset.Print()
				cuts_str = "(ttHScore>0.21)"
				dataset_new = dataset.reduce( RooFit.Cut(cuts_str) )
			#	dataset_new.Print()
				cat_datasets.append(dataset_new)
	f_new = f
	if '2017' in options.year : f_new = f+'_2017'
	out = TFile(options.out_dir + f_new +".root","RECREATE")
	out.mkdir("tagsDumper")
	out.cd("tagsDumper")
	neww = RooWorkspace("cms_hgg_13TeV","cms_hgg_13TeV") ;
	for dat in cat_datasets:
		getattr(neww, 'import')(dat, RooCmdArg())
	neww.Write()
	out.Close()



