import ROOT
from ROOT import *
import numpy as np
from optparse import OptionParser, make_option
import sys
import os
import json


parser = OptionParser(option_list=[
   # make_option("--inp-files",type='string',dest='inp_files',default='GluGluToHHTo2B2G_12nodes_13TeV-madgraph_correctedcfg'),  #2017
    make_option("--inp-files",type='string',dest='inp_files',default='GluGluToHHTo2B2G_nodesPlusSM_13TeV-madgraph'),  #2016
    make_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/inputs/06_05_2019/systematics_nominal/'),
    make_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/inputs/06_05_2019/nominal_nodes_half/'),
    make_option("--year",type='string',dest="year",default='2016'),
    make_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11'),
    make_option("--config",type='string',dest="config",default='/work/nchernya/DiHiggs/inputs/25_04_2019/reweighting_normalization_25_04_2019.json'),
])

(options, args) = parser.parse_args()
cats = options.cats.split(',')
input_files = options.inp_files.split(',')
input_names = []
for num,f in enumerate(input_files):
	if options.year=='2017' : input_names.append(f.replace('-','_') +'_2017_13TeV_125') 
	else : input_names.append(f.replace('-','_') +'_13TeV_125') 
	if options.year=='2017' : input_files[num] = 'output_' + f + '_2017' 
	else : input_files[num] = 'output_' + f  

#options.inp_dir = options.inp_dir + options.year + '/'
#options.out_dir = options.out_dir + options.year + '/'

normalization_file = open(options.config).read()
normalizations = json.loads(normalization_file)

#systweights = ["PreselSF", "electronVetoSF", "TriggerWeight"] 
systnames = [] 
systweights = [] 
for direction in ["Up","Down"]:
	systnames.append("SigmaEOverEShift%s01sigma" % direction)
	systnames.append("JEC%s01sigma" % direction)
	systnames.append("JER%s01sigma" % direction)
systnames = [''] 

wsname = "tagsDumper/cms_hgg_13TeV"

for num,f in enumerate(input_files):
	print 'doing file ',f
	tfile = TFile(options.inp_dir + f+".root")  
	ws = tfile.Get(wsname)
	whichNodes = list(np.arange(0,12,1))
#	whichNodes = []
	whichNodes.append('SM')
	whichNodes.append('box')
	for benchmark_num in whichNodes:
		cat_datasets=[]
		print 'doing benchmark ',benchmark_num
		ws.Print()
		normalization_value = normalizations[options.year]["benchmark_%s_normalization"%benchmark_num]
		for syst in systnames:
			for cat in cats :
				print 'doing cat ',cat
				if syst=='' : name = input_names[num]+'_'+cat
				else : name = input_names[num]+'_'+cat+'_'+syst
			#	name_new = name.replace('12nodes','node_%s'%benchmark_num)
				name_new = name.replace('nodesPlusSM','node_%s'%benchmark_num)
			#	if '2017' in options.year : name_new = name_new.replace('13TeV_Do','2017_13TeV_Do').replace('_correctedcfg','')
				print 'name new ',name_new
				mass = RooRealVar("CMS_hgg_mass","CMS_hgg_mass",100,180) 
				dZ = RooRealVar("dZ","dZ",-20,20) 
				centralObjectWeight = RooRealVar("centralObjectWeight","centralObjectWeight",-999999.,999999.) 

				directions = ["Up01sigma", "Down01sigma"]
 				systematics_vars=[]
				for syst in systweights:
					for ddir in directions:
						systematics_vars.append(RooRealVar(str(syst)+str(ddir), str(syst)+str(ddir), -1000., 1000.))

				print name 
				benchmark = RooRealVar("benchmark_reweight_%s"%benchmark_num,"benchmark_reweight_%s"%benchmark_num,0,100.) 
				dataset = (ws.data(name))
			#	dataset_new = (ws.data(name)).emptyClone(name_new,name_new).reduce(RooArgSet(mass,dZ,centralObjectWeight,benchmark))
				dataset_new = (ws.data(name)).emptyClone(name_new,name_new)
				weight = RooRealVar("weight","weight",-100000,1000000)
				sum_weights_for_use=0.
				sum_weights=0.
				for i in range(0,dataset.numEntries()):
					mass.setVal(dataset.get(i).getRealValue("CMS_hgg_mass"))
					dZ.setVal(dataset.get(i).getRealValue("dZ"))
					centralObjectWeight.setVal(dataset.get(i).getRealValue("centralObjectWeight"))
					for i1,syst in enumerate(systweights):
						for i2,ddir in enumerate(directions):
							systematics_vars[i1*len(directions)+i2].setVal(dataset.get(i).getRealValue(str(syst)+str(ddir)))
					benchmark_value = dataset.get(i).getRealValue("benchmark_reweight_%s"%benchmark_num)
					benchmark.setVal(benchmark_value)
					new_weight=dataset.weight() * benchmark_value / normalization_value
					sum_weights+=new_weight
               #discard events on which the trainig was perfromed
					#if ((dataset.get(i).getRealValue("eventNumber"))%2!=0) :
					if ((dataset.get(i).getRealValue("event"))%2!=0) :
				#	if ((dataset.get(i).getRealValue("eventNumber"))%2!=0) or ((dataset.get(i).getRealValue("ttHScore"))<0.21): #already applied
						weight.setVal(0.) 
					else :
						new_weight*=2. # because discaring exactly half of events 
						weight.setVal(new_weight )
						sum_weights_for_use+=new_weight

					rooSet = RooArgSet(ws.var("IntLumi"))
					rooSet.add(mass)
					rooSet.add(dZ)
					rooSet.add(centralObjectWeight)
					rooSet.add(benchmark)
					rooSet.add(weight)
					for item in systematics_vars:
						rooSet.add(item)

				#	dataset_new.add(RooArgSet(mass, dZ, centralObjectWeight, benchmark, weight), weight.getVal() )
					dataset_new.add(rooSet,weight.getVal() )
				dataset_new.Print()
				cat_datasets.append(dataset_new)

			#f_new = f.replace('12nodes','node_%d'%benchmark_num).replace('_correctedcfg','')
		f_new = f.replace('nodesPlusSM','node_%s'%benchmark_num).replace('_correctedcfg','')
		#if '2017' in options.year : f_new = f_new+'_2017
		out = TFile(options.out_dir + f_new +".root","RECREATE")
		out.mkdir("tagsDumper")
		out.cd("tagsDumper")
		neww = RooWorkspace("cms_hgg_13TeV","cms_hgg_13TeV") ;
		for dat in cat_datasets:
			getattr(neww, 'import')(dat, RooCmdArg())
		neww.Write()
		out.Close()

#with open(options.config.replace(".json","_fit.josn"), 'w') as fp:
#	json.dump(normalizations_new, fp)



