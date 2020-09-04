import pandas as pd
import root_pandas as rpd
import numpy as np
import ROOT
import json

from root_numpy import tree2array

from optparse import OptionParser

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_mc_vars_to_workspace(ws=None,mjjLow=70, systematics_labels=[],add_benchmarks = False):
  IntLumi = ROOT.RooRealVar("IntLumi","IntLumi",1000)
  IntLumi.setConstant(True)
  getattr(ws, 'import')(IntLumi)

  weight = ROOT.RooRealVar("weight","weight",1)
  weight.setConstant(False)
  getattr(ws, 'import')(weight)

  CMS_hgg_mass = ROOT.RooRealVar("CMS_hgg_mass","CMS_hgg_mass",125,100,180)
  CMS_hgg_mass.setConstant(False)
  #CMS_hgg_mass.setBins(160)
  #CMS_hgg_mass.setBins(80)
  CMS_hgg_mass.setBins(100)
  getattr(ws, 'import')(CMS_hgg_mass)

  Mjj = ROOT.RooRealVar("Mjj","Mjj",125,mjjLow,190)
  Mjj.setConstant(False)
  Mjj.setBins(100)
  #if mjjLow==90 : Mjj.setBins(25)
  #else : Mjj.setBins(30)
  getattr(ws, 'import')(Mjj)

  dZ = ROOT.RooRealVar("dZ","dZ",0.0,-20,20)
  dZ.setConstant(False)
  dZ.setBins(40)
  getattr(ws, 'import')(dZ)

#  ttHScore = ROOT.RooRealVar("ttHScore","ttHScore",0.5,0.,1.)
#  ttHScore.setConstant(False)
#  ttHScore.setBins(40)
#  getattr(ws, 'import')(ttHScore)


def apply_selection(data=None,reco_name=None):
  #function to split up ttree into recobins
  #if 'reco5' in reco_name: recobin_data = data[(data['pTH_reco']>=350.)]
  #recobin_data = recobin_data[((recobin_data['mgg']>=100.)&(recobin_data['mgg']<=180.))]
  return recobin_data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_dataset_to_workspace(data=None,ws=None,name=None,systematics_labels=[],add_benchmarks = False, benchmark_num = -1, benchmark_norm = 1.):

  #define argument set  
  arg_set = ROOT.RooArgSet(ws.var("weight"))
  variables = ["CMS_hgg_mass","Mjj","dZ" ]#, "ttHScore"] #ttHScore
  for var in variables :
      arg_set.add(ws.var(var))

  #define roodataset to add to workspace
  roodataset = ROOT.RooDataSet (name, name, arg_set, "weight" )

  #Fill the dataset with values
  for index,row in data.iterrows():
    for var in variables:
      if var=='dZ' :  #to ensure only one fit (i.e. all RV fit)
        ws.var(var).setVal( 0. )
        ws.var(var).setConstant()
      else : 
        ws.var(var).setVal( row[ var ] )

    w_val = row['weight']

    roodataset.add( arg_set, w_val )

  #Add to the workspace
  getattr(ws, 'import')(roodataset)

  return [name]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def get_options():

    parser = OptionParser()
    parser.add_option("--inp-files",type='string',dest='inp_files',default='GluGluToRadionToHHTo2B2G_M-300_narrow_13TeV-madgraph,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8,GluGluHToGG_M-125_13TeV_powheg_pythia8,bbHToGG_M-125_4FS_13TeV_amcatnlo')  
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/inputs/22_04_2020/trees/')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/inputs/22_04_2020/')
    parser.add_option("--outtag",type='string',dest="outtag",default='')
    parser.add_option("--MjjLow",type='float',dest="MjjLow",default='70')
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2')
    parser.add_option("--MVAcats",type='string',dest="MVAcats",default='0.37,0.62,0.78,1')
    parser.add_option("--MXcats",type='string',dest="MXcats",default='291,309')  #2d
    parser.add_option("--ttHScore",type='float',dest="ttHScore",default=0.26)
    parser.add_option("--doCategorization",action="store_true", dest="doCategorization",default=False)
    parser.add_option("--signal",type='string',dest="sig",default="Radion")
    parser.add_option("--mass",type='string',dest="mass",default="300")
    parser.add_option("--year",type='string',dest="year",default="2016")
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

#treeDirName = 'tagsDumper/trees/'
treeDirName = ''
(opt,args) = get_options()
cats = opt.cats.split(',')
MVAcats = opt.MVAcats.split(',')
MXcuts = opt.MXcats.split(',')
nMVA =len(MVAcats)-1 
#nMX = int(12/(len(MVAcats)-1))
cat_def = {}
for mva_num in range(0,nMVA):
    cat_num = mva_num
    cat_name = "DoubleHTag_%d"%(cat_num)
    cat_def[cat_name] = {"MVA" : []}
    cat_def[cat_name]["MVA"] = [float(MVAcats[nMVA - mva_num]),float(MVAcats[nMVA - (mva_num+1)])]


input_files = opt.inp_files.split(',')
target_names = []
sig = opt.sig
mass = opt.mass
year = opt.year
for num,f in enumerate(input_files):
  if f.find("HHTo2B2G") != -1:
    target_names.append(sig+"hh"+mass)
  elif f.find("VBFH") != -1:
    target_names.append("qqh") 
  elif f.find("VH") != -1:
    target_names.append("vh")
  elif f.find("GluGluH") != -1:
    target_names.append("ggh")
  elif f.find("4FS_ybyt") != -1:
    target_names.append("bbh_4FS_ybyt")
  elif f.find("4FS_yb2") != -1:
    target_names.append("bbh_4FS_yb2")
  elif f.find("ttH") != -1:
    target_names.append("tth")

  input_files[num] = 'output_' + f +".root" #comment out for ivan
  

for num,f in enumerate(input_files):
   print 'doing file ',f
   tfile = ROOT.TFile(opt.inp_dir + f)
   tfilename = opt.inp_dir +f
   #define roo fit workspace
   datasets=[]
   ws = ROOT.RooWorkspace("cms_hgg_13TeV", "cms_hgg_13TeV")
   #Assemble roorealvariable set
   add_mc_vars_to_workspace( ws,opt.MjjLow,'' )  # do not add them for the main systematics file
   for cat in cats : 
       print 'doing cat ',cat
       name = 'bbggtrees_13TeV'+'_'+cat
       initial_name = 'bbggtrees_13TeV_DoubleHTag_0'

       if opt.doCategorization :
          selection = "(MX <= %.2f and MX > %.2f) and (xmlMVAtransf <= %.2f and xmlMVAtransf > %.2f) and (ttHScore >= %.2f)" %(float(MXcuts[1]),float(MXcuts[0]),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],opt.ttHScore)

       print 'doing selection ', selection
       print tfilename, treeDirName+initial_name
       data = rpd.read_root(tfilename,'%s'%(treeDirName+initial_name)).query(selection)

       datasets += add_dataset_to_workspace( data, ws, name,'') #systemaitcs[1] : this should be done for nominal only, to add weights

   f_out = ROOT.TFile.Open("%s/%s"%(opt.out_dir,input_files[num]),"RECREATE")
   dir_ws = f_out.mkdir("tagsDumper")
   dir_ws.cd()
   ## renaming all the datasets
   data0=ROOT.RooDataSet()
   data0=ws.data("bbggtrees_13TeV_DoubleHTag_0")
   data0.SetNameTitle(target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_0',target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_0')
   data0.Print("V")

   data00=ROOT.RooDataSet()
   data00=data0.Clone(target_names[num]+'_'+year+'_13TeV_120_DoubleHTag_0')
   data00.Print("V")

   data000=ROOT.RooDataSet()
   data000=data0.Clone(target_names[num]+'_'+year+'_13TeV_130_DoubleHTag_0')
   data000.Print("V")

   data1=ROOT.RooDataSet()
   data1=ws.data("bbggtrees_13TeV_DoubleHTag_1")
   data1.SetNameTitle(target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_1',target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_1')
   data1.Print("V")
   
   data11=ROOT.RooDataSet()
   data11=data1.Clone(target_names[num]+'_'+year+'_13TeV_120_DoubleHTag_1')
   data11.Print("V")

   data111=ROOT.RooDataSet()
   data111=data1.Clone(target_names[num]+'_'+year+'_13TeV_130_DoubleHTag_1')
   data111.Print("V")

   data2=ROOT.RooDataSet()
   data2=ws.data("bbggtrees_13TeV_DoubleHTag_2")
   data2.SetNameTitle(target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_2',target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_2')
   data2.Print("V")
   
   data22=ROOT.RooDataSet()
   data22=data2.Clone(target_names[num]+'_'+year+'_13TeV_120_DoubleHTag_2')
   data22.Print("V")

   data222=ROOT.RooDataSet()
   data222=data1.Clone(target_names[num]+'_'+year+'_13TeV_130_DoubleHTag_2')
   data222.Print("V")

   getattr(ws, 'import')(data00)
   getattr(ws, 'import')(data11)
   getattr(ws, 'import')(data22)
   getattr(ws, 'import')(data000)
   getattr(ws, 'import')(data111)
   getattr(ws, 'import')(data222)
   ws.Write()
   f_out.Close()
