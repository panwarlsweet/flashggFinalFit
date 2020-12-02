import pandas as pd
import root_pandas as rpd
import numpy as np
import ROOT
import json
from bTagSF import *
from YFrac import *

from root_numpy import tree2array

from optparse import OptionParser

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_mc_vars_to_workspace(ws=None, mx=500, mxLow=450, mxHigh=1200, systematics_labels=[],add_benchmarks = False):
    IntLumi = ROOT.RooRealVar("IntLumi","IntLumi",1000)
    IntLumi.setConstant(True)
    getattr(ws, 'import')(IntLumi)

    weight = ROOT.RooRealVar("weight","weight",1)
    weight.setConstant(False)
    getattr(ws, 'import')(weight)

    CMS_hgg_mass = ROOT.RooRealVar("CMS_hgg_mass","CMS_hgg_mass",125,100,180)
    CMS_hgg_mass.setConstant(False)
    CMS_hgg_mass.setBins(100)
    getattr(ws, 'import')(CMS_hgg_mass)

    MX = ROOT.RooRealVar("MX","MX",mx,mxLow,mxHigh)
    MX.setConstant(False)
    MX.setBins(100)
    getattr(ws, 'import')(MX)

    dZ = ROOT.RooRealVar("dZ","dZ",0.0,-20,20)
    dZ.setConstant(False)
    dZ.setBins(40)
    getattr(ws, 'import')(dZ)

def apply_selection(data=None,reco_name=None):
    #function to split up ttree into recobins
    #if 'reco5' in reco_name: recobin_data = data[(data['pTH_reco']>=350.)]
    #recobin_data = recobin_data[((recobin_data['mgg']>=100.)&(recobin_data['mgg']<=180.))]
    return recobin_data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_dataset_to_workspace(data=None,ws=None,name=None,btag_norm=1.0,yfracfix=1.0,mjj=300,systematics_labels=[]):

  #define argument set  
  arg_set = ROOT.RooArgSet(ws.var("weight"))
  variables = ["CMS_hgg_mass","MX","dZ" ]#, "ttHScore"] #ttHScore
  for var in variables :
      arg_set.add(ws.var(var))

  #define roodataset to add to workspace
  roodataset = ROOT.RooDataSet (name, name, arg_set, "weight" )
  #Restore normalization from the btag reshaping weights#                                        
  data['weight'] *= (btag_norm * yfracfix)

  #Fill the dataset with values
  for index,row in data.iterrows():
    for var in variables:
      if var=='dZ' :  #to ensure only one fit (i.e. all RV fit)
        ws.var(var).setVal( 0. )
        ws.var(var).setConstant()
      else :
        if var=='MX':
          ws.var(var).setVal(row[var+"_Y"+str(mjj)])
        else:
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
    parser.add_option("--MjjLow",type='float',dest="MjjLow",default='230')
    parser.add_option("--MjjHigh",type='float',dest="MjjHigh",default='320')    
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2')
    parser.add_option("--MVAcats",type='string',dest="MVAcats",default='0.37,0.62,0.78,1')
    parser.add_option("--doCategorization",action="store_true", dest="doCategorization",default=True)
    parser.add_option("--signal",type='string',dest="sig",default="NMSSM")
    parser.add_option("--Mjj",type='int',dest="Mjj",default="300")
    
    
    
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

#treeDirName = 'tagsDumper/trees/'
treeDirName = ''
(opt,args) = get_options()
cats = opt.cats.split(',')
MVAcats = opt.MVAcats.split(',')
#MXcuts = opt.MXcats.split(',')
nMVA =len(MVAcats)-1 
cat_def = {}

target_names = []
sig = opt.sig
Mjj=opt.Mjj
MjjLow=opt.MjjLow
MjjHigh=opt.MjjHigh

years=["2016","2017","2018"]

### for NMSSM #####
if sig == "NMSSM":
  masses =[500,600,700,800,900,1000]

MX_cut1 = 450
MX_cut2 = 1200
if Mjj == 300:
    MjjLow = 230
    MjjHigh = 320
elif Mjj == 400:
    MjjLow = 330
    MjjHigh = 410
    MX_cut1 = 550
elif Mjj == 500:
    MjjLow = 400
    MjjHigh = 520
    MX_cut1 = 650
elif Mjj == 600:
    MjjLow = 460
    MjjHigh = 640
    MX_cut1 = 750
elif Mjj == 700:
    MjjLow = 560
    MjjHigh = 740
    MX_cut1 = 850
elif Mjj == 800:
    MjjLow = 600
    MjjHigh = 840
    MX_cut1 = 950
  
  
for i in range(len(masses)):
 print("i...=",i,"\t","mass==",masses[i])
 if masses[i]-Mjj-125 < 0 : continue
 for year in years:
    if year == "2016":
        bTagNF = 1
        lumi = 35.9
    elif year == "2017":
        bTagNF = 2
        lumi = 41.5
    elif year == "2018":
        bTagNF = 3
        lumi = 59.4

    inp_files="GluGluHToGG_M-125_13TeV_powheg_pythia8,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8,bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo,bbHToGG_M-125_4FS_ybyt_13TeV_amcatnlo,output_NMSSM_XToYHTo2b2g_MX-"+str((masses[i])+"_13TeV-madgraph_pythia8"

    input_files = inp_files.split(',')
    print(input_files)
  ## setting up ttHkiller cut #####
    ttHScore=0.0  
                                                                                            
  ## setting up categories ###
    if masses[i] >= 260 and masses[i] <= 400: 
      mass_range ="low"
      cat='0.236,0.443,0.699,1.0'
                                                                                        
    elif masses[i] > 400 and masses[i] <= 700: 
      mass_range ="mid"
      cat='0.236,0.443,0.699,1.0'
      if(MX > 250 && MX <= 500):
        cat='0.236,0.443,0.699,1.0'

    else:
      mass_range ="high"
      cat='0.236,0.443,0.699,1.0'
      if(MX > 250 && MX <= 500):
        cat='0.236,0.443,0.699,1.0'
      elif(MX > 500):
        cat='0.236,0.443,0.699,1.0'

    MVAcats=cat.split(',')
  
    for mva_num in range(0,nMVA):
      cat_num = mva_num
      cat_name = "DoubleHTag_%d"%(cat_num)
      cat_def[cat_name] = {"MVA" : []}
      cat_def[cat_name]["MVA"] = [float(MVAcats[nMVA - mva_num]),float(MVAcats[nMVA - (mva_num+1)])]

    for num,f in enumerate(input_files):

        if f.find("Radion") != -1 or f.find("BulkGraviton") != -1:
            target_names.append(sig+"hh")
        elif f.find("NMSSM") != -1:
            target_names.append("xtoyh")
        elif f.find("VBFH") != -1:
            target_names.append("qqh") 
        elif f.find("VH") != -1:
            target_names.append("vh")
        elif f.find("GluGluH") != -1:
            target_names.append("ggh")
        elif f.find("4FS_ybyt") != -1:
            target_names.append("bbhybyt")
        elif f.find("4FS_yb2") != -1:
            target_names.append("bbhyb2")
        elif f.find("ttH") != -1:
            target_names.append("tth")
      
    input_files[num] = 'output_' + f +".root" #comment out for ivan
  
    btag_SF = 1.0

    for num,f in enumerate(input_files):
      yfracfix = 1.0
      if sig == "Radion" or str(opt.signal) == "BulkGraviton": 
        SignalNodes = SignalNodes_WED
        SMHiggsNodes = SMHiggsNodes_WED
      else: 
        SignalNodes = SignalNodes_NMSSM
        SMHiggsNodes = SMHiggsNodes_NMSSM
        YFracfix = YFrac_+str(year)
        Y=str(Mjj)
        if f.find("NMSSM") != -1:
          for frac in YFracfix:
                if frac[0] == 'Y'+Y:
                        #print("testing2......",frac[0] )
                        yfracfix = frac[(int(masses[i])/100)-2]

      if f.find("Radion") != -1 or f.find("BulkGraviton") != -1 or f.find("NMSSM") != -1:
          for s in SignalNodes:
            if s[0] == sig+str(masses[i]):
              btag_SF = s[bTagNF]
      else:
          for s in SMHiggsNodes:
            if s[0] == target_names[num]:
              btag_SF = s[bTagNF]

      print 'doing file ',f, 'with bTag_SF = ', btag_SF, " with yfracfix = ",  YFracfix
      tfile = ROOT.TFile(opt.inp_dir+"flattening_"+mass_range+"mass_"+sig + year + "_L2-regression/analysistrees/" + f)
      tfilename = opt.inp_dir+"flattening_"+mass_range+"mass_"+sig + year + "_L2-regression/analysistrees/" +f

      #define roo fit workspace
      datasets=[]
      ws = ROOT.RooWorkspace("cms_hgg_13TeV", "cms_hgg_13TeV")
      #Assemble roorealvariable set
      add_mc_vars_to_workspace( ws,MX,MX_cut1,MX_cut2,'' )  # do not add them for the main systematics file
      for cat in cats : 
        print 'doing cat ',cat
        name = 'bbggtrees_13TeV'+'_'+cat
        initial_name = 'bbggtrees_13TeV_DoubleHTag_0'

        if opt.doCategorization :
          selection = "(MX_Y%d <= %.2f and MX_Y%d > %.2f) and (xmlMVAtransf <= %.2f and xmlMVAtransf > %.2f) and (ttHScore >= %.2f) and (Mjj >= %.2f and Mjj <= %.2f)" %(Mjj,Mjj,float(MX_cut2),float(MX_cut1),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],ttHScore,MjjLow,MjjHigh)
          
          if f.find("NMSSM") != -1:
            selection = "(genmbb >= %d and genmbb <= %d) and (MX_Y%d <= %.2f and MX_Y%d > %.2f) and (xmlMVAtransf <= %.2f and xmlMVAtransf > %.2f) and (ttHScore >= %.2f) and (Mjj >= %.2f and Mjj <= %.2f)" %(Mjj-2,Mjj+2,Mjj,Mjj,float(MX_cut2),float(MX_cut1),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],ttHScore,MjjLow,MjjHigh)

          print 'doing selection ', selection, 'to make categorised ws from following tree'
          print tfilename, treeDirName+initial_name
          print "bTagSF = ", btag_SF, " and yfracfix = ", yfracfix
          data = rpd.read_root(tfilename,'%s'%(treeDirName+initial_name)).query(selection)
          print 'created ws..', name
          datasets += add_dataset_to_workspace( data, ws, name, btag_SF,yfracfix,Mjj,'') #systemaitcs[1] : this should be done for nominal only, to add weights, yfracfix=since NMSSM sample has grid of Y masses so fixing normalization with yfracfix for each Y
          
      if target_names[num].find("Radion") != -1 or target_names[num].find("BulkGraviton") != -1:
        target_names[num]=sig+"hh"+str(masses[i])
      elif target_names[num].find("NMSSM") != -1:
        target_names[num]="X"+str(masses[i])+"To_Y"+str(Mjj)+"_H125"
      f_out = ROOT.TFile.Open("%s/%s_%s.root"%(opt.out_dir+sig+"/"+str(masses[i]),target_names[num],year),"RECREATE")
      #print("test......",masses[i]," ",target_names[num])
      dir_ws = f_out.mkdir("tagsDumper")
      dir_ws.cd()
      ## renaming all the datasets
      data0=ROOT.RooDataSet()
      data0=ws.data("bbggtrees_13TeV_DoubleHTag_0")
      data0.SetNameTitle(target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_0',target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_0')
      #data0.Print("V")
      
      data00=ROOT.RooDataSet()
      data00=data0.Clone(target_names[num]+'_'+year+'_13TeV_120_DoubleHTag_0')
     # data00.Print("V")
      
      data000=ROOT.RooDataSet()
      data000=data0.Clone(target_names[num]+'_'+year+'_13TeV_130_DoubleHTag_0')
     # data000.Print("V")
      
      data1=ROOT.RooDataSet()
      data1=ws.data("bbggtrees_13TeV_DoubleHTag_1")
      data1.SetNameTitle(target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_1',target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_1')
      #data1.Print("V")
      
      data11=ROOT.RooDataSet()
      data11=data1.Clone(target_names[num]+'_'+year+'_13TeV_120_DoubleHTag_1')
      #data11.Print("V")
      
      data111=ROOT.RooDataSet()
      data111=data1.Clone(target_names[num]+'_'+year+'_13TeV_130_DoubleHTag_1')
      #data111.Print("V")
      
      data2=ROOT.RooDataSet()
      data2=ws.data("bbggtrees_13TeV_DoubleHTag_2")
      data2.SetNameTitle(target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_2',target_names[num]+'_'+year+'_13TeV_125_DoubleHTag_2')
      #data2.Print("V")
      
      data22=ROOT.RooDataSet()
      data22=data2.Clone(target_names[num]+'_'+year+'_13TeV_120_DoubleHTag_2')
      #data22.Print("V")
      
      data222=ROOT.RooDataSet()
      data222=data1.Clone(target_names[num]+'_'+year+'_13TeV_130_DoubleHTag_2')
      #data222.Print("V")
      
      getattr(ws, 'import')(data00)
      getattr(ws, 'import')(data11)
      getattr(ws, 'import')(data22)
      getattr(ws, 'import')(data000)
      getattr(ws, 'import')(data111)
      getattr(ws, 'import')(data222)
      ws.Write()
      f_out.Close()
