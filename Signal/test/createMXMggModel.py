import numpy as np
import ROOT
import json

from optparse import OptionParser


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def get_options():

    parser = OptionParser()
    #parser.add_option("--date",type='string',dest='date',default='27_03_2020')  
    parser.add_option("--date",type='string',dest='date',default='22_04_2020')   
    parser.add_option("--inp-procs",type='string',dest='inp_procs',default='qqh,tth,vh,ggh,ggHH_kl_0_kt_1,ggHH_kl_1_kt_1,ggHH_kl_2p45_kt_1,ggHH_kl_5_kt_1,qqHH_CV_1_C2V_1_kl_1,qqHH_CV_1_C2V_2_kl_1,qqHH_CV_1_C2V_1_kl_2,qqHH_CV_1_C2V_1_kl_0,qqHH_CV_0p5_C2V_1_kl_1,qqHH_CV_1p5_C2V_1_kl_1')  
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Plots/FinalResults/inputs/')
    parser.add_option("--inp-dir-MX",type='string',dest="inp_dir_MX",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/MX/22_04_2020/')
    parser.add_option("--inp-file",type='string',dest="inp_file",default='CMS-HGG_sigfit_Mgg_2016_2017_2018_22_04_2020.root')
    parser.add_option("--inp-file-MX",type='string',dest="inp_file_MX",default='out_MX_22_04_2020.root')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/')
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_10,DoubleHTag_11')
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

(opt,args) = get_options()
cats = opt.cats.split(',')
input_procs = opt.inp_procs.split(',')


tfile = ROOT.TFile(opt.inp_dir + opt.inp_file)
tfile_MX = ROOT.TFile(opt.inp_dir_MX + opt.inp_file_MX)
ws_mgg = tfile.Get("wsig_13TeV")
ws_MX = tfile_MX.Get("wsig_13TeV")
for num,f in enumerate(input_procs):
 for year in '2016,2017,2018'.split(','):
 #for year in '2018'.split(','):
  for cat_num,cat in enumerate(cats) :
    pdf_MX = "hhbbggpdfsm_13TeV_%s_%s_%s"%(input_procs[num],year,cat)
    pdf_mgg = "hggpdfsmrel_13TeV_%s_%s_%s"%(input_procs[num],year,cat)
    #ws_MX.pdf(pdf_MX).Print("v")
    getattr(ws_mgg, 'import')(ws_MX.pdf(pdf_MX),ROOT.RooCmdArg())
    getattr(ws_mgg, 'import')(ws_MX.var("MX"),ROOT.RooCmdArg())
    prod_pdf = "MXMggpdfsm_13TeV_%s_%s_%s"%(input_procs[num],year,cat)
    #print ws_mgg.pdf(pdf_mgg)
    #print ws_MX.pdf(pdf_MX)
    sig_prod_pdf = ROOT.RooProdPdf(prod_pdf,"",ws_mgg.pdf(pdf_mgg),ws_MX.pdf(pdf_MX))
    #sig_prod_pdf.Print("v") 
    getattr(ws_mgg, 'import')(sig_prod_pdf,ROOT.RooFit.RecycleConflictNodes())
    #Save normalization for combine
    #sig_prod_pdf_norm = (ws_mgg.function(pdf_mgg+"_norm")).clone(prod_pdf+"_norm")
    sig_prod_pdf_norm = (ws_MX.function(pdf_MX+"_norm")).clone(prod_pdf+"_norm")  #take norm from MX?
    getattr(ws_mgg, 'import')(sig_prod_pdf_norm,ROOT.RooFit.RecycleConflictNodes())
    ##Printing normalization
   # ws_mgg.var("MH").setVal(125.)  #just to check that the normalization is the same for Mgg and MX, it is of course.
   # print 'mgg : ',ws_mgg.function(pdf_mgg+"_norm").getVal(),', MX : ',ws_MX.function(pdf_MX+"_norm").getVal(), ", imported product : ",ws_mgg.function(prod_pdf+"_norm").getVal() #just to check that the normalization is the same for Mgg and MX, it is of course.
    
 
f_out = ROOT.TFile.Open(opt.out_dir+"CMS-HGG_sigfit_MggMX_2016_2017_2018_%s_%s.root"%(opt.date,input_procs[0]),"RECREATE")
#f_out = ROOT.TFile.Open(opt.out_dir+"CMS-HGG_sigfit_MggMX_2018_%s.root"%opt.date,"RECREATE")
ws_mgg.Write()
f_out.Close()
