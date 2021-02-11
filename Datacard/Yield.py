import ROOT
from ROOT import *
from optparse import OptionParser, make_option
import sys
import os
from math import sqrt
import json

date = '27_12_2020'
sig="NMSSM"
#date="18_01_2021"
#sig="WED"

wsname = 'wsig_13TeV'
wsname_bkg = 'multipdf'

#symbol = ''  #for keynote
symbol = '&'  #for latex

lumi_2016=35.9*1000
lumi_2017=41.5*1000
lumi_2018=59.4*1000
#lumi_2016=1000
#lumi_2017=1000
#lumi_2018=1000
YHsignal=1.  #new most updated x-sec
HHsignal=0.58*0.00227*2  
if sig == "NMSSM": X = [300,400,500,600,800,900,1000]
else: X=[400,450,500,550,600,650,700,800,900,1000] 
#X = [260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000]
#Y = [90,100,125,150,200,250,300,400,500,600,700,800]
Y = []
Y.append(int(sys.argv[1]))
#signal = "NMSSMX"
#names="ggh_2016,qqh_2016,tth_2016,vh_2016,bbhyb2_2016,bbhybyt_2016,ggh_2017,qqh_2017,tth_2017,vh_2017,bbhyb2_2017,bbhybyt_2017,ggh_2018,qqh_2018,tth_2018,vh_2018,bbhyb2_2018,bbhybyt_2018".split(',')
names="ggh,qqh,tth,vh,bbhyb2,bbhybyt".split(',')

#names="hh_node_SM_2016,hh_node_SM_2017,hh_node_SM_2018".split(',')
for my in Y:
    for mx in X:
        if mx - my -125 < 0: continue
        if (my == 90 or my == 100) and (mx == 1000 or mx == 900): continue
        if sig == "NMSSM":
            filename = 'final_workspaces/NMSSM/CMS-HGG_sigfit_MggMjj_2016_2017_2018_'+date+'_NMSSMX'+str(mx)+'ToY'+str(my)+'H125.root'
            signal = ("NMSSMX"+str(mx)+"ToY"+str(my)+"H125")
        else:
            filename = 'final_workspaces/CMS-HGG_sigfit_MggMjj_2016_2017_2018_'+date+'_Radionhh'+str(mx)+'.root'
            signal = "Radionhh"+str(mx)+",BulkGravitonhh"+str(mx)

	names = "ggh,qqh,tth,vh,bbhyb2,bbhybyt,"+signal
        if mx > 550 or my > 250:
            names = signal
        names = names.split(',')
        sum_entries = dict()
        sum_entries_bkg = dict()
        
        entries_per_cat = dict()
        year=[2016,2017,2018]
        num_cat = 3
        for name in names:
            print '\n'
            print '%s & \t'%(name),
            lumi = 1.
            entries_per_cat[name] = []
            for cat in range(0,num_cat):
                sum=0.
                for y in range(0,3):
                    if year[y] == 2016 : lumi = lumi_2016
                    if year[y] == 2017 : lumi = lumi_2017
                    if year[y] == 2018 : lumi = lumi_2018
                    filename_in = filename
                    tfile = TFile(filename_in)
                    ws = tfile.Get(wsname)
                    ws_name = 'hhbbggpdfsm_13TeV_%s_%s_DoubleHTag_%d_norm'%(name,str(year[y]),cat)
                    var = (ws.var('MH'))
                    var.setVal(125.)
                    #print ws, ws_name
                    entries = (ws.function(ws_name).getVal())
                    sum_entries[name] = entries
                    #print entries , lumi
                    count = entries*lumi
                    if name.find("Radion")!=-1 or name.find("BulkGraviton")!=-1:
                        count*=HHsignal
                    elif name.find("NMSSM")!=-1:
                        count*=YHsignal  
                    sum+=count
                entries_per_cat[name].append(count)
            #	print '%.2f\t'%(count),
                if cat==2: symbol = '\\\\'
                else: symbol = '&'
                print '%.4f\t'%(count),'%s'%symbol,
            #	print '%.6f\t'%(count),'%s'%symbol
            #if symbol=='&' : 
            #        print '%.4f \\\\'%sum
            #else : print '%.2f'%sum
            #else : print '%.4f'%sum



        #filename_bkg_2016 = '/work/nchernya/DiHiggs/inputs/%s/output_DoubleEG_2016_%s.root'%(date,date)
        #filename_bkg_2017 = '/work/nchernya/DiHiggs/inputs/%s/output_DoubleEG_2017_%s.root'%(date,date)
        #filename_bkg_2018 = '/work/nchernya/DiHiggs/inputs/%s/output_DoubleEG_2018_%s.root'%(date,date)
        
        if sig == "NMSSM":
            filename_bkg_total = 'final_workspaces/NMSSM/CMS-HGG_multipdf2D_DoubleEG_ftest_NMSSM_X'+str(mx)+'_Y'+str(my)+'_HHbbgg_2016_2017_2018_'+date+'.root'
        else:
            filename_bkg_total = 'final_workspaces/CMS-HGG_multipdf2D_DoubleEG_ftest_WED_X'+str(mx)+'_HHbbgg_2016_2017_2018_'+date+'.root'
        print '\n'
        #years=['2016','2017','2018','Total']
        years=['Total']
        #print 'Data with blinded 115 < Mgg < 135'
        #for num,name in enumerate([filename_bkg_2016,filename_bkg_2017,filename_bkg_2018,filename_bkg_total]):
        for num,name in enumerate([filename_bkg_total]):
            sum_bkg=0.
            sum_bkg_sqr=0.
            sum_bkg_error=0.
            symbol='&'
            print 'Data side-band\t%s\t'%symbol,
            entries_per_cat['Data'+years[num]] = [] 
            for cat in range(0,num_cat):
                filename_in = name
                tfile = TFile(filename_in)
                wsname_bkg = 'multipdf'
                ws_bkg = tfile.Get(wsname_bkg)
                catname = 'Data_13TeV_DoubleHTag_%d'%(cat)
                entries = ws_bkg.data(catname).sumEntries()
                entries_blinded=0
                entries_blinded_sqr=0
                entries_blinded_error=0
                for event in range(0,ws_bkg.data(catname).numEntries()):
                    #print ws_bkg.data(catname).numEntries()
                    #if (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") > 135.) or (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") < 115.):
                    #if ((ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") > 0.) or (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") < 100000.)) and (ws_bkg.data(catname).get(event).getRealValue("Mjj") > 90.):
                    if ((ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") > 135.) or (ws_bkg.data(catname).get(event).getRealValue("CMS_hgg_mass") < 115.)):
                        entries_blinded_sqr+=(ws_bkg.data(catname).weight())**2
                        entries_blinded+=ws_bkg.data(catname).weight()
                        entries_blinded_error+=ws_bkg.data(catname).weightError()
                sum_entries_bkg[catname] = entries
                sum_bkg+=entries_blinded
                sum_bkg_sqr+=entries_blinded_sqr
                sum_bkg_error+=entries_blinded_error
                #print '%d \pm %.1f\t'%(entries_blinded,sqrt(entries_blinded_sqr)),'%s'%symbol,
                if cat==2: symbol = '\\\\'
                else: symbol = '&'
                print '%d\t'%(entries_blinded),'%s'%symbol,
                #print '%.2f\t'%(entries_blinded),'%s'%symbol,
                #print '%d\t'%(entries_blinded),'%s'%symbol
                #print '%d +- %.1f\t'%(entries_blinded,sqrt(entries_blinded_sqr)),'%s'%symbol,
                entries_per_cat['Data'+years[num]].append(entries_blinded)
        print '\n Data with blinded 115 < Mgg < 135'
        print 'from files = ', filename_bkg_total, filename
        
        
#result = open("output_txt/full_yields_latex_test_%s.txt"%date,"w")
#result.write(json.dumps(entries_per_cat))



