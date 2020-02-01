import ROOT
from ROOT import *
from optparse import OptionParser, make_option
import sys
import os
from math import sqrt
import json

date = '25_04_2019'
#date = '13_12_2018'
symbol = ''  #for keynote

filename_bkg_2016 = '/work/nchernya/DiHiggs/inputs/%s/output_DoubleEG_2016_%s.root'%(date,date)
filename_bkg_2017 = '/work/nchernya/DiHiggs/inputs/%s/output_DoubleEG_2017_%s.root'%(date,date)
filename_bkg_total = '/work/nchernya/DiHiggs/inputs/%s/output_DoubleEG_2016_2017_%s.root'%(date,date)
years=['2016','2017','Total']
num_cat=12
print 'Data with blinded 115 < Mgg < 135'
for num,name in enumerate([filename_bkg_2016,filename_bkg_2017,filename_bkg_total]):
	tfile = TFile(name)
	wsname_bkg = 'tagsDumper/cms_hgg_13TeV'
	ws_bkg = tfile.Get(wsname_bkg)
	sum_bkg=0.
	print 'Data %s\t'%years[num],
	for cat in range(0,num_cat):
		catname = 'Data_13TeV_DoubleHTag_%d'%(cat)
		entries = ws_bkg.data(catname).sumEntries()
		entries_blinded=0
		entries_left=0
		entries_right=0
		for event in range(0,ws_bkg.data(catname).numEntries()):
			if (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") > 135.) or (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") < 115.):
				entries_blinded+=1
				if (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") > 135.) : entries_right+=1
				if (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") < 115.) : entries_left+=1
		sum_bkg+=entries_blinded
#		print '%d\t'%(entries_blinded),'%s'%symbol,
		print '%d'%(entries_blinded),'%s'%symbol,
		print '(%d,'%(entries_left),'%s'%symbol,
		print '%d)\t'%(entries_right),'%s'%symbol,
	print '%d\t'%(sum_bkg)


