import pandas as pd
import numpy as np
import ROOT

from root_numpy import tree2array

from optparse import OptionParser

###BSM nodes for HHbbgg
whichNodes = list(np.arange(0,12,1))
whichNodes.append('SM')
whichNodes.append('box')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getSystLabelsWeights(isMET = False):
    phosystlabels=[]
    jetsystlabels=[]
    metsystlabels=[]
    systlabels=['']
    for direction in ["Up","Down"]:
        phosystlabels.append("MvaShift%s01sigma" % direction)
        phosystlabels.append("SigmaEOverEShift%s01sigma" % direction)
        phosystlabels.append("MaterialCentralBarrel%s01sigma" % direction)
        phosystlabels.append("MaterialOuterBarrel%s01sigma" % direction)
        phosystlabels.append("MaterialForward%s01sigma" % direction)
        phosystlabels.append("FNUFEB%s01sigma" % direction)
        phosystlabels.append("FNUFEE%s01sigma" % direction)
        phosystlabels.append("MCScaleGain6EB%s01sigma" % direction)
        phosystlabels.append("MCScaleGain1EB%s01sigma" % direction)
        jetsystlabels.append("JEC%s01sigma" % direction)
        jetsystlabels.append("JER%s01sigma" % direction)
        jetsystlabels.append("PUJIDShift%s01sigma" % direction)
        metsystlabels.append("metJecUncertainty%s01sigma" % direction)
        metsystlabels.append("metJerUncertainty%s01sigma" % direction)
        metsystlabels.append("metPhoUncertainty%s01sigma" % direction)
        metsystlabels.append("metUncUncertainty%s01sigma" % direction)
        for r9 in ["HighR9","LowR9"]:
            for region in ["EB","EE"]:
                phosystlabels.append("ShowerShape%s%s%s01sigma"%(r9,region,direction))
                phosystlabels.append("MCScale%s%s%s01sigma" % (r9,region,direction))
                for var in ["Rho","Phi"]:
                    phosystlabels.append("MCSmear%s%s%s%s01sigma" % (r9,region,var,direction))
    systlabels += phosystlabels
    systlabels += jetsystlabels
    if isMET:
        systlabels += metsystlabels

    systweights = ["UnmatchedPUWeight", "MvaLinearSyst", "LooseMvaSF", "PreselSF", "electronVetoSF", "TriggerWeight", "FracRVWeight", "FracRVNvtxWeight", "ElectronWeight", "MuonIDWeight", "MuonIsoWeight", "JetBTagCutWeight"] #, "JetBTagReshapeWeight"]
    return systlabels,systweights


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_mc_vars_to_workspace(ws=None, systematics_labels=[],add_benchmarks = False):
  IntLumi = ROOT.RooRealVar("IntLumi","IntLumi",1000)
  IntLumi.setConstant(True)
  getattr(ws, 'import')(IntLumi)

  weight = ROOT.RooRealVar("weight","weight",1)
  weight.setConstant(False)
  getattr(ws, 'import')(weight)

  CMS_hgg_mass = ROOT.RooRealVar("CMS_hgg_mass","CMS_hgg_mass",125,100,180)
  CMS_hgg_mass.setConstant(False)
  CMS_hgg_mass.setBins(160)
  getattr(ws, 'import')(CMS_hgg_mass)

  dZ = ROOT.RooRealVar("dZ","dZ",0.0,-20,20)
  dZ.setConstant(False)
  dZ.setBins(40)
  getattr(ws, 'import')(dZ)

  ttHScore = ROOT.RooRealVar("ttHScore","ttHScore",0.5,0.,1.)
  ttHScore.setConstant(False)
  ttHScore.setBins(40)
  getattr(ws, 'import')(ttHScore)

  if add_benchmarks: 
     for benchmark_num in whichNodes:
         benchmark = ROOT.RooRealVar("benchmark_reweight_%s"%benchmark_num,"benchmark_reweight_%s"%benchmark_num,0,100.) 
         benchmark.setConstant(False)
         benchmark.setBins(40)
         getattr(ws, 'import')(benchmark)
     eventNumber = RooRealVar("eventNumber","eventNumber",0,1000000.) 
     eventNumber.setConstant(False)
     eventNumber.setBins(40)
     getattr(ws, 'import')(eventNumber)

  if systematics_labels!=[] :
     directions = ["Up01sigma", "Down01sigma"]
     for syst in systematics_labels:
          for ddir in directions:
             rrv = ROOT.RooRealVar(str(syst)+str(ddir), str(syst)+str(ddir), -1000, 1000)
             rrv.setConstant(False)
             rrv.setBins(40)
             getattr(ws, 'import')(rrv)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def apply_selection(data=None,reco_name=None):
  #function to split up ttree into recobins
  #if 'reco5' in reco_name: recobin_data = data[(data['pTH_reco']>=350.)]
  #recobin_data = recobin_data[((recobin_data['mgg']>=100.)&(recobin_data['mgg']<=180.))]
  return recobin_data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_dataset_to_workspace(data=None,ws=None,name=None,systematics_labels=[]):

  #apply selection to extract correct recobin
  #recobin_data = apply_selecetion(data,selection_name)

  #define argument set  
  arg_set = ROOT.RooArgSet(ws.var("weight"))
  arg_set.add(ws.var("CMS_hgg_mass"))
  arg_set.add(ws.var("dZ"))
  arg_set.add(ws.var("ttHScore"))
  #arg_set.add(ws.var("eventNumber"))
  if systematics_labels!=[] :
    for label in systematics_labels:
        arg_set.add(ws.var(label))

  #define roodataset to add to workspace
  roodataset = ROOT.RooDataSet (name, name, arg_set, "weight" )

  #Fill the dataset with values
  for index,row in data.iterrows():
    for var in ["CMS_hgg_mass"]:
      var_tree = var 
      if( mass == '125' ): ws.var(var).setVal( row[ var_tree ] )
      elif( mass == '130' ): ws.var(var).setVal( row[ var_tree ]+5. )
      elif( mass == '120' ): ws.var(var).setVal( row[ var_tree ]-5. )

    w_val = row['weight']
    roodataset.add( arg_set, w_val )

  #Add to the workspace
  getattr(ws, 'import')(roodataset)

  return [name]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def get_options():

    parser = OptionParser()
    parser.add_option("--inp-files",type='string',dest='inp_files',default='GluGluToHHTo2B2G_node_SM_13TeV-madgraph')  #2016
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/inputs/24_04_2019/')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/inputs/25_04_2019/')
    parser.add_option("--year",type='string',dest="year",default='2016')
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11')
    parser.add_option("--nosysts",action="store_true", dest="nosysts", default=False)
    parser.add_option('--M',
                       dest='mass', 
                       default='125',
                       help='')
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

(opt,args) = get_options()
if opt.nosysts : systematics = ['']
else : systematics = getSystLabelsWeights()
mass = opt.mass
masses = [-5,5.]
cats = opt.cats.split(',')
input_files = opt.inp_files.split(',')
input_names = []
for num,f in enumerate(input_files):
   input_names.append(f.replace('-','_') +'_13TeV') 
   input_files[num] = 'output_' + f 

#opt.inp_dir = opt.inp_dir + opt.year + '/'
#opt.out_dir = opt.out_dir + opt.year + '/'

for num,f in enumerate(input_files):
   print 'doing file ',f
   tfile = ROOT.TFile(opt.inp_dir + f+".root")
   systematics_datasets = [] 
   #define roo fit workspace
   ws = ROOT.RooWorkspace("cms_hgg_13TeV", "cms_hgg_13TeV")
   #Assemble roorealvariable set
   #add_mc_vars_to_workspace( ws,systematics[1] )  # do not add them for the main systematics fiel
   add_mc_vars_to_workspace( ws)
   for syst in systematics[0] : 
      for cat in cats : 
         print 'doing cat ',cat
         if syst!='' : name = input_names[num]+'_'+cat+'_'+syst
         else : name = input_names[num]+'_'+cat
         data = pd.DataFrame(tree2array(tfile.Get("tagsDumper/trees/%s"%name)))
         if syst!='' : newname = input_names[num]+'_'+mass+'_'+cat+'_'+syst
         else : newname = input_names[num]+'_'+mass+'_'+cat
 
        # if syst=='' : systematics_datasets += add_dataset_to_workspace( data, ws, name,systematics[1] )  #this should be done for nominal only, to add weights
        # else : systematics_datasets += add_dataset_to_workspace( data, ws, name )
         systematics_datasets += add_dataset_to_workspace( data, ws, newname )
         #print newname, " ::: Entries =", ws.data(newname).numEntries(), ", SumEntries =", ws.data(newname).sumEntries()
 
         for newmass in masses :
             value = newmass + int(mass) 
             if syst!='' : massname = input_names[num]+'_%d_'%value+cat+'_'+syst
             else : massname = input_names[num]+"_%d_"%value+cat
             newdataset = (ws.data(newname)).Clone(massname)
             newdataset.changeObservableName("CMS_hgg_mass","CMS_hgg_mass_old")
             oldmass = newdataset.get()["CMS_hgg_mass_old"]
             mass_new = ROOT.RooFormulaVar( "CMS_hgg_mass", "CMS_hgg_mass", "(@0+%.1f)"%float(mass),ROOT.RooArgList(oldmass) );
             newdataset.addColumn(mass_new).setRange(100,180)
             getattr(ws, 'import')(newdataset)
             systematics_datasets += massname
         
   #export ws to file
   f_out = ROOT.TFile.Open("%s/%s.root"%(opt.out_dir,f),"RECREATE")
   dir_ws = f_out.mkdir("tagsDumper")
   dir_ws.cd()
   ws.Write()
   f_out.Close() 
