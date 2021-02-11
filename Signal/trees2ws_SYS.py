import pandas as pd
import root_pandas as rpd
import numpy as np
import ROOT
import json
from bTagSF import *
from YFrac import *
import sys,os
from root_numpy import tree2array

from optparse import OptionParser

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~READ SYSTEMATICS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getSystLabelsWeights(year):
    phosystlabels=[]
    jetsystlabels=[]
    metsystlabels=[]
    systlabels=['']
    for direction in ["Up","Down"]:
      phosystlabels.append("MvaShift%s01sigma" % direction)
      phosystlabels.append("SigmaEOverEShift%s01sigma" % direction)
      jetsystlabels.append("JEC%s01sigma" % direction)
      jetsystlabels.append("JER%s01sigma" % direction)
      jetsystlabels.append("PUJIDShift%s01sigma" % direction)
      jetsystlabels.append("JetHEM%s01sigma" % direction) #2018 only
    systlabels += phosystlabels
    systlabels += jetsystlabels
    systweights = [ "PreselSF", "electronVetoSF", "TriggerWeight", "FracRVWeight",  "MuonIDWeight", "MuonIsoWeight", "ElectronIDWeight", "ElectronRecoWeight", "JetBTagReshapeWeight","JetBTagReshapeWeightHF","JetBTagReshapeWeightLF","JetBTagReshapeWeightJES","prefireProbability"]
    if year == "2018":
        del systweights[-1]
    return systlabels,systweights

      
#~~~~~~~~~~~~~~~~~~~~~~~Making WS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

  btagweight = ROOT.RooRealVar("btagReshapeWeight","btagReshapeWeight",1)
  btagweight.setConstant(False)
  getattr(ws, 'import')(btagweight)

  if systematics_labels!=[] :
     directions = ["Up01sigma", "Down01sigma"]
     for syst in systematics_labels:
          for ddir in directions:
             rrv = ROOT.RooRealVar(str(syst)+str(ddir), str(syst)+str(ddir), -1000, 1000)
             rrv.setConstant(False)
             rrv.setBins(40)
             getattr(ws, 'import')(rrv)
     rrv = ROOT.RooRealVar("centralObjectWeight","centralObjectWeight", -1000, 1000)
     rrv.setConstant(False)
     rrv.setBins(40)
     getattr(ws, 'import')(rrv)


#  ttHScore = ROOT.RooRealVar("ttHScore","ttHScore",0.5,0.,1.)
#  ttHScore.setConstant(False)
#  ttHScore.setBins(40)
#  getattr(ws, 'import')(ttHScore)


def apply_selection(data=None,reco_name=None):
  #function to split up ttree into recobins
  #if 'reco5' in reco_name: recobin_data = data[(data['pTH_reco']>=350.)]
  #recobin_data = recobin_data[((recobin_data['mgg']>=100.)&(recobin_data['mgg']<=180.))]
  return recobin_data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Make DataSet and ADD to WS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_dataset_to_workspace(data=None,ws=None,name=None,btag_norm=1.0,yfracfix=1.0,systematics_labels=[]):

  #define argument set  
  arg_set = ROOT.RooArgSet(ws.var("weight"))
  variables = ["CMS_hgg_mass","Mjj","dZ","btagReshapeWeight"]#, "ttHScore"] #ttHScore

  if systematics_labels!=[] :
    directions = ["Up01sigma", "Down01sigma"]
    for syst in systematics_labels:
        for ddir in directions:
           variables.append(syst+ddir)
    variables.append('centralObjectWeight')
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
        ws.var(var).setVal( row[ var ] )

    w_val = row['weight']

    roodataset.add( arg_set, w_val )

  #Add to the workspace
  getattr(ws, 'import')(roodataset)

  return [name]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Customize inputs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
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
    parser.add_option("--nosysts",action="store_true", dest="nosysts", default=False)
    parser.add_option("--doCategorization",action="store_true", dest="doCategorization",default=True)
    parser.add_option("--signal",type='string',dest="sig",default="Radion")
 #   parser.add_option("--mass",type='string',dest="mass",default="300")
  #  parser.add_option("--year",type='string',dest="year",default="2016")
    parser.add_option("--Mjj",type='int',dest="Mjj",default="125")
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  


treeDirName = 'tagsDumper/trees/'   ### path of directory from flashhgg trees

(opt,args) = get_options()

cats = opt.cats.split(',')
MVAcats = opt.MVAcats.split(',')
nMVA =len(MVAcats)-1 
cat_def = {}

target_names = []
sig = opt.sig
Mjj = opt.Mjj
opt.nosysts=False

Mgg = '125'   ## this is just to have dataset with Mgg = 120, 125, 130
points_Mgg = [-5,0,5.] ## this is just to have dataset with Mgg = 120, 125, 130

years=["2016","2017","2018"]   ### year we want to run for
#years=["2018"]
if sig=="Radion" or sig == "BulkGraviton":    
  ### for WED ######
  masses =[260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000]
  MX_cut1=[255,265,275,291,305,337,374,418,464,510,555,615,655,745,835,925]
  MX_cut2=[263,275,286,309,327,360,413,463,514,565,615,680,725,825,925,1025]

### for NMSSM #####
if sig == "NMSSM":
  masses =[400,500,600,800,900,1000]
  MX_cut1=[374,464,555,745,835,925]
  MX_cut2=[413,514,615,825,925,1025]
  #MX_cut1=[925]
  #MX_cut2=[1025]
  
for i in range(len(masses)):
 print("i...=",i,"\t","mass==",masses[i])
 #print(sys.argv[1])
 if masses[i] != int(sys.argv[1]): continue
 if masses[i]  - 125 - Mjj < 0:  
      print("skipping X =",masses[i],"for Mjj=",Mjj)
      continue

 for year in years:
  if opt.nosysts : systematics = [''],[]
  else :
      systematics = getSystLabelsWeights(year)                             
                
  print(systematics) 
  if year == "2016":
    bTagNF = 1      ### these are labels to pick value from bTagSF.py for btag normaization array
    lumi = 35.9

  elif year == "2017":
    bTagNF = 2
    lumi = 41.5
    
  elif year == "2018":
    bTagNF = 3
    lumi = 59.4

  ### below input files you can change according to names you have
  if sig == "Radion" or sig == "BulkGraviton":
    inp_files="GluGluHToGG_M-125_13TeV_powheg_pythia8,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8,bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo,bbHToGG_M-125_4FS_ybyt_13TeV_amcatnlo,GluGluTo"+opt.sig+"ToHHTo2B2G_M-"+str(masses[i])+"_narrow_13TeV-madgraph"
  else:
    if Mjj >= 300 :   ## since don't use single H processes for this case
      inp_files="NMSSM_XToYHTo2b2g_MX-"+str(masses[i])+"_13TeV-madgraph-pythia8"
    elif Mjj == 125:
      inp_files="GluGluHToGG_M-125_13TeV_powheg_pythia8,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8,bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo,bbHToGG_M-125_4FS_ybyt_13TeV_amcatnlo,NMSSM_XToYHTo2b2g_MX-"+str(masses[i])+"_13TeV-madgraph-pythia8"
      if masses[i] > 550:
        inp_files="NMSSM_XToYHTo2b2g_MX-"+str(masses[i])+"_13TeV-madgraph-pythia8"
    else:
      inp_files="GluGluHToGG_M-125_13TeV_powheg_pythia8,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8,bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo,bbHToGG_M-125_4FS_ybyt_13TeV_amcatnlo,NMSSM_XToYHTo2b2g_MX-"+str(masses[i])+"_13TeV-madgraph-pythia8"

  #inp_files="NMSSM_XToYHTo2b2g_MX-"+str(masses[i])+"_13TeV-madgraph-pythia8"  ##just for testing, remove it
  input_files = inp_files.split(',')
  print(input_files)
  ## setting up ttHkiller cut #####
  ttHScore=0.26
  if Mjj >= 200 or masses[i] >= 550:
    ttHScore=0.0

  ## setting up Mjj window ####
  MjjLow=opt.MjjLow
  MjjHigh=opt.MjjHigh
  Mjjbin="low"
  if Mjj > 150 and Mjj < 300:
    MjjLow = 70
    MjjHigh = 400
  elif Mjj >= 300 and Mjj <= 500:
    MjjLow = 200
    MjjHigh = 560
    Mjjbin="mid"
  elif Mjj > 500:
    MjjLow = 400
    MjjHigh = 1000
    Mjjbin="high"

    
  ## setting up categories ###
  if masses[i] >= 260 and masses[i] <= 400:
    mass_range ="low"
    cat='0.174,0.329,0.627,1.0'

  elif masses[i] > 400 and masses[i] <= 700:
    mass_range ="mid"
    cat='0.213,0.401,0.550,1.0'
    if Mjj > 250 and Mjj <= 500:
      cat='0.180,0.352,0.6,1.0'

  else:
    mass_range ="high"
    cat='0.215,0.304,0.500,1.0'
    if Mjj > 250 and Mjj <= 500:
      cat='0.177,0.239,0.35,1.0'
    elif Mjj > 500:
      cat='0.129,0.286,0.40,1.0'

  MVAcats=cat.split(',')
  
  for mva_num in range(0,nMVA):
    cat_num = mva_num
    cat_name = "DoubleHTag_%d"%(cat_num)
    cat_def[cat_name] = {"MVA" : []}
    cat_def[cat_name]["MVA"] = [float(MVAcats[nMVA - mva_num]),float(MVAcats[nMVA - (mva_num+1)])]

  for num,f in enumerate(input_files):

    if f.find("Radion") != -1 or f.find("BulkGraviton") != -1:
      target_names.append("hh")
    elif f.find("NMSSM") != -1:
      target_names.append("NMSSMX"+str(masses[i])+"ToY"+str(Mjj)+"H125")
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
      
    #input_files[num] = 'output_' + f +".root" #comment out for ivan
  
    btag_SF = 1.0

  for num,f in enumerate(input_files):
      yfracfix = 1.0   ## NMSSM samples are with grid mass generation, so need to fix normalization from YFrac.py which I calculate separately, yfracfix = total events in NMSSM sample without any cut / total events for particular Y (use gen mbb for this)
      
      if f.find("Radion") != -1 or f.find("BulkGraviton") != -1:
        SignalNodes = SignalNodes_WED
#        SMHiggsNodes = SMHiggsNodes_WED
      else: 
        SignalNodes = SignalNodes_NMSSM
        SMHiggsNodes = SMHiggsNodes_NMSSM
        if year == "2016": YFracfix = YFrac_2016
        elif year == "2017": YFracfix = YFrac_2017
        elif year == "2018": YFracfix = YFrac_2018
        Y=str(Mjj)
        if f.find("NMSSM") != -1:
          for frac in YFracfix:
                if frac[0] == 'Y'+Y:
                        print("testing2......",frac[0] )
                        yfracfix = frac[(int(masses[i])/100)-2]

      if f.find("Radion") != -1: 
          for s in SignalNodes:
            if s[0] == "Radion"+str(masses[i]):
              btag_SF = s[bTagNF]
      elif f.find("BulkGraviton") != -1:
           for s in SignalNodes:
            if s[0] == "BulkGraviton"+str(masses[i]):
              btag_SF = s[bTagNF]
      elif f.find("NMSSM") != -1:
           for s in SignalNodes:
       	    if s[0] == "NMSSM"+str(masses[i]):
              btag_SF = s[bTagNF]
      else:
          for s in SMHiggsNodes:
            if s[0] == target_names[num]:
              btag_SF = s[bTagNF]

      print 'doing file ',f, 'with bTag_SF = ', btag_SF
      tfile = ROOT.TFile(opt.inp_dir + year + "/" + str(mass_range)+"X_"+Mjjbin+"Y"+ "/output_" + f+".root")
      tfilename = opt.inp_dir + year + "/" + str(mass_range)+"X_"+Mjjbin+"Y"+ "/output_" +f+".root"
      tfile = ROOT.TFile(tfilename)
      print  tfilename
      
      #define roo fit workspace
      systematics_datasets=[]
      datasets=[]
      ws = ROOT.RooWorkspace("cms_hgg_13TeV", "cms_hgg_13TeV")
      systematics_to_run_with = systematics[0]
      if  not opt.nosysts : 
          systematics_to_run_with = systematics[1]
      #Assemble roorealvariable set
      add_mc_vars_to_workspace( ws,Mjj,MjjLow,MjjHigh,systematics_to_run_with,'' )  # do not add them for the main systematics file
      for syst in systematics[0] :
       for cat in cats : 
        print 'doing cat ',cat
        if f.find("Radion") != -1:
            target_names[num]="Radionhh"+str(masses[i])
        if f.find("BulkGraviton") != -1:
            target_names[num]="BulkGravitonhh"+str(masses[i])
        if f.find("NMSSM") != -1:
            target_names[num]="NMSSMX"+str(masses[i])+"ToY"+str(Mjj)+"H125"

        if syst!='' :
            newname = target_names[num]+'_'+year+'_13TeV_125_'+cat +'_'+syst
            initial_name = 'bbggtrees_13TeV_DoubleHTag_0' +'_'+syst
        else:
            newname = target_names[num]+'_'+year+'_13TeV_125_'+cat
            initial_name = 'bbggtrees_13TeV_DoubleHTag_0'

        if opt.doCategorization :
          selection = "(MX_Y%d <= %.2f and MX_Y%d > %.2f) and (HHbbggMVA <= %.2f and HHbbggMVA > %.2f) and (ttHScore >= %.2f) and (Mjj >= %.2f and Mjj <= %.2f)" %(Mjj,float(MX_cut2[i]),Mjj,float(MX_cut1[i]),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],ttHScore,MjjLow,MjjHigh)
          
          if f.find("NMSSM") != -1:
            selection = "(genmbb >= %d and genmbb <= %d) and (MX_Y%d <= %.2f and MX_Y%d > %.2f) and (HHbbggMVA <= %.2f and HHbbggMVA > %.2f) and (ttHScore >= %.2f) and (Mjj >= %.2f and Mjj <= %.2f)" %(Mjj-2,Mjj+2,Mjj,float(MX_cut2[i]),Mjj,float(MX_cut1[i]),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],ttHScore,MjjLow,MjjHigh)
          elif f.find("Radion") != -1 or f.find("BulkGraviton") != -1:
            selection = "(MX <= %.2f and MX > %.2f) and (HHbbggMVA <= %.2f and HHbbggMVA > %.2f) and (ttHScore >= %.2f) and (Mjj >= %.2f and Mjj <= %.2f)" %(float(MX_cut2[i]),float(MX_cut1[i]),cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],ttHScore,MjjLow,MjjHigh)
          
          print 'doing selection ', selection, 'to make categorised ws from following tree'
          print tfilename, treeDirName+initial_name
          print "bTagSF = ", btag_SF, " and yfracfix = ", yfracfix
          
          data = rpd.read_root(tfilename,'%s'%(treeDirName+initial_name)).query(selection)
          #else :
          # "USER WARNING : 0 events in ",f," syst ",syst," ,cat = ",cat
            
          print 'created ws..', newname

          if syst=='' and not opt.nosysts : systematics_labels = systematics[1] #systemaitcs[1] : this shouldq be done for nominal only, to add weights
          else : systematics_labels =[] #systemaitcs[1] : this should be done for nominal only, to add weight

          systematics_datasets += add_dataset_to_workspace( data, ws, newname, btag_SF,yfracfix,systematics_labels) #systemaitcs[1] : this should be done for nominal only, to add weights, yfracfix=since NMSSM sample has grid of Y masses so fixing normalization with yfracfix for each Y
           
          if f.find("Radion") != -1:
            target_names[num]="Radionhh"+str(masses[i])
          if f.find("BulkGraviton") != -1:
            target_names[num]="BulkGravitonhh"+str(masses[i])
          if f.find("NMSSM") != -1:
            target_names[num]="NMSSMX"+str(masses[i])+"ToY"+str(Mjj)+"H125"

          masses_array = points_Mgg
          if syst!='' and not opt.nosysts : masses_array = []
          for newmass in masses_array :
             value = newmass + int(Mgg)
             if syst!='' : 
               massname = target_names[num]+'_%d_'%value+cat+'_'+syst
             else : 
               massname = target_names[num]+"_%d_"%value+cat
               
             newdataset = (ws.data(newname)).Clone(massname)
             newdataset.changeObservableName("CMS_hgg_mass","CMS_hgg_mass_old")
             oldmass = newdataset.get()["CMS_hgg_mass_old"]
             mass_new = ROOT.RooFormulaVar( "CMS_hgg_mass", "CMS_hgg_mass", "(@0+%.1f)"%float(Mgg),ROOT.RooArgList(oldmass) );
             newdataset.addColumn(mass_new).setRange(100,180)
             getattr(ws, 'import')(newdataset)
             systematics_datasets += massname
      #for dataset in systematics_datasets:
      #    dataset.Print("V")
      print "root file = ", target_names[num]
      f_out = ROOT.TFile.Open("%s/%s/%s_%s.root"%(opt.out_dir+sig+"/"+str(masses[i]),str(Mjj),target_names[num],year),"RECREATE")
      #f_out = ROOT.TFile.Open("/%s/%s_%s.root"%(masses[i],target_names[num],year),"RECREATE")
      #print("test......",masses[i]," ",target_names[num])
      dir_ws = f_out.mkdir("tagsDumper")
      dir_ws.cd()
      
      ws.Write()
      f_out.Close()
