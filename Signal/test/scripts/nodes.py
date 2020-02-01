import ROOT
from ROOT import *
from optparse import OptionParser, make_option
import sys
import os
from math import sqrt
import json

filename = '/shome/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/out_20_02_2019_set2017/CMS-HGG_sigfit_nodes2017.root'
#filename = '/shome/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/out_20_02_2019_set2016/CMS-HGG_sigfit_nodes2016_GluGluToHHTo2B2G_node_0_13TeV_madgraph_DoubleHTag_0.root'
wsname = 'wsig_13TeV'

num_cat = 12
lumi_2016=35.9*1000
lumi_2017=41.5*1000
SMsignal=33.49*0.58*0.00227*2
#lumi_2016=1000.
#lumi_2017=1000.
#SMsignal=1
names=[]
tpMap = {}
for node in range(0,12):
 #  name = "GluGluToHHTo2B2G_node_%d_13TeV_madgraph"%node
 #  names.append(name)
 #  tpMap[name] = 'node%d'%node
   name = "GluGluToHHTo2B2G_node_%d_13TeV_madgraph_2017"%node
   names.append(name)
   tpMap[name] = 'node%d_2017'%node
sum_entries = dict()
sum_entries_bkg = dict()

entries_per_cat = dict()

tfile = TFile(filename)
ws = tfile.Get(wsname)
print names
for name in names:
	print name
#	print '%s\t'%(tpMap[name]),
	sum=0.
	lumi = 1./77.4
#	if '2017' in name : lumi = lumi_2017
#	else : lumi = lumi_2016
	entries_per_cat[tpMap[name]] = [] 
	for cat in range(0,12):
		ws_name = 'hggpdfsmrel_13TeV_%s_DoubleHTag_%d_normThisLumi'%(name,cat)
		var = (ws.var('MH'))
		var.setVal(125.)
		print ws_name
		entries = (ws.function(ws_name).getVal())
		sum_entries[name] = entries
		count = entries*lumi
	#	if 'node' in tpMap[name] : count*=SMsignal
		sum+=count
		entries_per_cat[tpMap[name]].append(count)
	#	print '%.2f\t'%(count),
		print '%.4f\t'%(count),'&',
	print '%.2f'%sum

