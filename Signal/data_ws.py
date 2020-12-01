import pandas as pd
import root_pandas as rpd
import numpy as np
import ROOT
import json
from bTagSF import *

from root_numpy import tree2array

from optparse import OptionParser

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_mc_vars_to_workspace(ws=None, mjj=125, mjjLow=70, mjjHigh=190, systematics_labels=[],add_benchmarks = False):
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

  Mjj = ROOT.RooRealVar("Mjj","Mjj",mjj,mjjLow,mjjHigh)
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
def add_dataset_to_workspace(data=None,ws=None,name=None,btag_norm=1.0,systematics_labels=[]):

  #define argument set  
  arg_set = ROOT.RooArgSet(ws.var("weight"))
  variables = ["CMS_hgg_mass","Mjj","dZ" ]#, "ttHScore"] #ttHScore
  for var in variables :
      arg_set.add(ws.var(var))

  #define roodataset to add to workspace
  roodataset = ROOT.RooDataSet (name, name, arg_set, "weight" )
  #Restore normalization from the btag reshaping weights#                                        
  data['weight'] *= btag_norm 
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
#    parser.add_option("--inp-files",type='string',dest='inp_files',default='GluGluToRadionToHHTo2B2G_M-300_narrow_13TeV-madgraph,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8,GluGluHToGG_M-125_13TeV_powheg_pythia8,bbHToGG_M-125_4FS_13TeV_amcatnlo')  
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/inputs/22_04_2020/trees/')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/inputs/22_04_2020/')
    parser.add_option("--outtag",type='string',dest="outtag",default='')
    parser.add_option("--MjjLow",type='float',dest="MjjLow",default='70')
    parser.add_option("--MjjHigh",type='float',dest="MjjHigh",default='190')
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2')
    parser.add_option("--MVAcats",type='string',dest="MVAcats",default='0.37,0.62,0.78,1')
 #   parser.add_option("--MXcats",type='string',dest="MXcats",default='291,309')  #2d
  #  parser.add_option("--ttHScore",type='float',dest="ttHScore",default=0.26)
    parser.add_option("--doCategorization",action="store_true", dest="doCategorization",default=True)
    parser.add_option("--signal",type='string',dest="sig",default="Radion")
 #   parser.add_option("--mass",type='string',dest="mass",default="300")
  #  parser.add_option("--year",type='string',dest="year",default="2016")
    parser.add_option("--Mjj",type='int',dest="Mjj",default="125")
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

#treeDirName = 'tagsDumper/trees/'
treeDirName = ''
(opt,args) = get_options()
cats = opt.cats.split(',')
MVAcats = opt.MVAcats.split(',')
#MXcuts = opt.MXcats.split(',')
nMVA =len(MVAcats)-1 
#nMX = int(12/(len(MVAcats)-1))
cat_def = {}

#input_files = inp_files.split(',')

target_names = []
sig = opt.sig
#mass = opt.mass
#year = opt.year
Mjj = opt.Mjj

years=["2016","2017","2018"]
if sig=="Radion" or sig == "BulkGraviton":
  ### for WED ######
  masses =[260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000]
  #masses=[260]
  MX_cut1=[255,265,275,291,305,337,374,418,464,510,555,615,655,745,835,925]
  MX_cut2=[263,275,286,309,327,360,413,463,514,565,615,680,725,825,925,1025]

### for NMSSM #####
if sig == "NMSSM":
  masses =[300,400,500,600,700,800,900,1000]
  MX_cut1=[291,374,464,555,655,745,835,925]
  MX_cut2=[309,413,514,615,725,825,925,1025]

for i in range(len(masses)):
  print("i...=",i,"\t","mass==",masses[i])
  ttHScore=0.26
  if(Mjj >= 200 or masses[i] >= 550):
    ttHScore=0.0

  ## setting up Mjj window ####
  MjjLow=opt.MjjLow
  MjjHigh=opt.MjjHigh
  if(Mjj >= 200 && Mjj <= 500):
    MjjLow = 150
    MjjHigh = 560
  elif(Mjj > 500)
    MjjLow = 300
    MjjHigh = 1000
                                                                                            
  ## setting up categories ###
  if masses[i] >= 260 and masses[i] <= 400: 
    mass_range ="low"
    cat='0.236,0.443,0.699,1.0'
                                                                                        
  elif masses[i] > 400 and masses[i] <= 700: 
    mass_range ="mid"
    cat='0.236,0.443,0.699,1.0'
    if(Mjj > 250 && Mjj <= 500):
      cat='0.236,0.443,0.699,1.0'

  else:
    mass_range ="high"
    cat='0.236,0.443,0.699,1.0'
    if(Mjj > 250 && Mjj <= 500):
      cat='0.236,0.443,0.699,1.0'
    elif(Mjj > 500):
      cat='0.236,0.443,0.699,1.0'

  MVAcats=cat.split(',')


  input_files=["Data_"+sig+"_"+mass_range+"mass"]
  print(input_files)
  target_names = ["Data"]

  for mva_num in range(0,nMVA):
    cat_num = mva_num
    cat_name = "DoubleHTag_%d"%(cat_num)
    cat_def[cat_name] = {"MVA" : []}
    cat_def[cat_name]["MVA"] = [float(MVAcats[nMVA - mva_num]),float(MVAcats[nMVA - (mva_num+1)])]

  for num,f in enumerate(input_files):
          
    input_files[num] =  f +".root" #comment out for ivan
  
    btag_SF = 1.0

  for num,f in enumerate(input_files):
    print 'doing file ',f, 'with bTag_SF = ', btag_SF
    print 'applying categorisation from...',mass_range, "..=",MVAcats
    tfile = ROOT.TFile(opt.inp_dir+ f)
    tfilename = opt.inp_dir+f
    datasets=[]
    ws = ROOT.RooWorkspace("cms_hgg_13TeV", "cms_hgg_13TeV")
    #Assemble roorealvariable set
    add_mc_vars_to_workspace( ws,opt.MjjLow,'' )  # do not add them for the main systematics file
    for cat in cats : 
        print 'doing cat ',cat
        name = 'Data_13TeV'+'_'+cat
        initial_name = 'Data_13TeV_DoubleHTag_0'

        if opt.doCategorization :
          selection = "(MX_Y%d <= %.2f and MX_Y%d > %.2f) and (xmlMVAtransf <= %.2f and xmlMVAtransf > %.2f) and (ttHScore >= %.2f) and (Mjj >= %.2f and Mjj <= %.2f)" %(Mjj,Mjj,float(MX_cut2[i]),float(MX_cut1[i]),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],ttHScore,MjjLow,MjjHigh)

          print 'doing selection from tree below for categorisation ', selection
          print tfilename, treeDirName+initial_name
          data = rpd.read_root(tfilename,'%s'%(treeDirName+initial_name)).query(selection)
          print "created workspace", name
          datasets += add_dataset_to_workspace( data, ws, name, btag_SF,'') #systemaitcs[1] : this should be done for nominal only, to add weights
   
    f_out = ROOT.TFile.Open("%s/DoubleEG.root"%(opt.out_dir+sig+"/"+str(masses[i])),"RECREATE")
    print("created Data ws for ......",sig+str(masses[i])),"_Mjj",Mjj
    dir_ws = f_out.mkdir("tagsDumper")
    dir_ws.cd()
    ws.Print()
      
    ws.Write()
    f_out.Close()
