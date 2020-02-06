import numpy as np
import ROOT
import json

from optparse import OptionParser


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def get_options():

    parser = OptionParser()
    #parser.add_option("--inp-files",type='string',dest='inp_files',default='qqh,tth,vh,ggh')  
    parser.add_option("--inp-procs",type='string',dest='inp_procs',default='hh_node_SM')  
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/out_fit_03_02_2020_nodes2016/')
    parser.add_option("--inp-dir-mjj",type='string',dest="inp_dir_mjj",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/mjj/')
    parser.add_option("--inp-files",type='string',dest="inp_files",default='CMS-HGG_sigfit_nodes2016_03_02_2020.root')
    parser.add_option("--inp-files-mjj",type='string',dest="inp_files_mjj",default='workspace_out_hh_node_SM_2016.root')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/')
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11')
    parser.add_option("--year",type='string',dest="year",default='2016')
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

(opt,args) = get_options()
year=opt.year
cats = opt.cats.split(',')
input_files = opt.inp_files.split(',')
input_procs = opt.inp_procs.split(',')

for num,f in enumerate(input_procs):
  tfile = ROOT.TFile(opt.inp_dir + input_files[0])
  ws = tfile.Get("wsig_13TeV")
  input_procs[num]+='_%s'%year
  tfile_mjj = ROOT.TFile(opt.inp_dir_mjj + opt.inp_files_mjj)
  ws2 = tfile_mjj.Get("wsig_13TeV")
  pdf = "hbbpdfsm_13TeV_hh_node_SM_2016_DoubleHTag_0"
  getattr(ws, 'import')(ws2.pdf(pdf),ROOT.RooFit.Rename((ws2.pdf(pdf)).GetName()))
  getattr(ws, 'import')(ws2.var("Mjj"),ROOT.RooFit.Rename("Mjj"))
  
  f_out = ROOT.TFile.Open("test_workspace_merge.root","RECREATE")
  ws.Print()
  ws.Write()
  f_out.Close()
