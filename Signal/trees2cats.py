import pandas as pd
import root_pandas as rpd
import numpy as np
import ROOT
import json
import os

from root_numpy import tree2array

from optparse import OptionParser

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def get_options():

    parser = OptionParser()
    #parser.add_option("--inp-files",type='string',dest='inp_files',default='qqh,tth,vh,ggh')  
    parser.add_option("--inp-files",type='string',dest='inp_files',default='hh')  
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='/work/nchernya/DiHiggs/inputs/24_01_2020/trees/')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='/work/nchernya/DiHiggs/inputs/24_01_2020/categorizedTrees/')
    parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11')
    parser.add_option("--MVAcats",type='string',dest="MVAcats",default='0.44,0.67,0.79,1')
    parser.add_option("--MXcats",type='string',dest="MXcats",default='250,385,470,640,10000,250,345,440,515,10000,250,330,365,545,10000')
    #parser.add_option("--MVAcats",type='string',dest="MVAcats",default='0.33,0.55,0.68,1')
    #parser.add_option("--MXcats",type='string',dest="MXcats",default='250,360,470,600,10000,250,330,365,540,10000,250,330,360,615,10000')
    parser.add_option("--ttHScore",type='float',dest="ttHScore",default=0.26)
    parser.add_option("--doCategorization",action="store_true", dest="doCategorization",default=False)
    parser.add_option("--year",type='string',dest="year",default='2016')
    parser.add_option("--add_gen",action="store_true", dest="add_gen",default=False)
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

(opt,args) = get_options()
year=opt.year

cats = opt.cats.split(',')
MVAcats = opt.MVAcats.split(',')
MXcats = opt.MXcats.split(',')
nMVA =len(MVAcats)-1 
nMX = int(len(cats)/(len(MVAcats)-1))
cat_def = {}
for mva_num in range(0,nMVA):
  for mx_num in range(0,nMX):
    cat_num = mva_num*nMX+mx_num 
    cat_name = "DoubleHTag_%d"%(cat_num)
    cat_def[cat_name] = {"MVA" : [],"MX":[]}
    cat_def[cat_name]["MVA"] = [float(MVAcats[nMVA - mva_num]),float(MVAcats[nMVA - (mva_num+1)])]
    cat_def[cat_name]["MX"] = [float(MXcats[mva_num*(nMX+1) + (nMX - mx_num)]),float(MXcats[mva_num*(nMX+1) + (nMX - (mx_num+1))])]
input_files = opt.inp_files.split(',')
input_names = []
target_names = []
target_files = []

for num,f in enumerate(input_files):
   name=f
   input_names.append(name+year+'_13TeV_125_13TeV')
   target_names.append(f +'_%s_13TeV'%year)
   target_files.append('output_' + f +'_%s'%year )


data_structure = pd.DataFrame(data=None)
data_all_cats = []
gen_data_all_cats = []
for num,f in enumerate(input_files):
 print 'doing file ',f,input_names[num]
 tfile = ROOT.TFile(opt.inp_dir + "output_"+f+"_%s.root"%year)
 tfilename = opt.inp_dir + "output_"+f+"_%s.root"%year
############Adding Gen info#############
 if opt.add_gen :
   initial_name = input_names[num]+'_DoubleHTag_0'
   gen_data_all_cats.append(rpd.read_root(tfilename,'genDiphotonDumper/trees/%s'%initial_name))
   initial_name = input_names[num]+'_NoTag_0'
   gen_data_all_cats.append(rpd.read_root(tfilename,'genDiphotonDumper/trees/%s'%initial_name))
########################################
 for cat_num,cat in enumerate(cats) : 
   print 'doing cat ',cat
   name = input_names[num]+'_'+cat
   initial_name = input_names[num]+'_DoubleHTag_0'
   selection = "(MX <= %.2f and MX > %.2f) and (HHbbggMVA <= %.2f and HHbbggMVA > %.2f) and (ttHScore >= %.2f)"%(cat_def[cat]["MX"][0],cat_def[cat]["MX"][1],cat_def[cat]["MVA"][0],cat_def[cat]["MVA"][1],opt.ttHScore)
   if (tfile.Get("tagsDumper/trees/%s"%initial_name).GetEntries())!=0 :
       data = rpd.read_root(tfilename,'tagsDumper/trees/%s'%initial_name).query(selection)
       if cat_num == 0 :  data_structure = pd.DataFrame(data=None, columns=data.columns) 
   else :
       "USER WARNING : 0 events in ",f," syst ",syst," ,cat = ",cat 
       data = data_structure 
   data_all_cats.append(data)
         
 #export trees file
 outname = target_files[num]
 f_out_name = "%s/%s_tmp.root"%(opt.out_dir,outname)
 if os.path.exists(f_out_name):
     os.remove(f_out_name)
 for df_num,df in enumerate(data_all_cats):
    name = input_names[num]+'_'+cats[df_num]
    if df_num==0 : mode = 'w'
    else : mode = 'a'
    if opt.add_gen :
      if df_num==0 : ##first lets add gen
        gen_data_all_cats[0].to_root(f_out_name,key='gen_'+name, mode=mode)
        mode = 'a'
        gen_data_all_cats[1].to_root(f_out_name,key='gen_'+name.replace('DoubleHTag_0','NoTag_0'), mode=mode)
    df.to_root(f_out_name,key=name, mode=mode)
     

 f_tree_name = "%s/%s_treesCats.root"%(opt.out_dir,outname)
 f_tree = ROOT.TFile.Open(f_out_name, "READ")
 out_file = ROOT.TFile.Open(f_tree_name, "RECREATE")
 outdir = out_file.mkdir("tagsDumper")
 outdir.cd()
 outdir2 = outdir.mkdir("trees")
 for cat in cats:
   name = input_names[num]+'_'+cat
   t_tree = (f_tree.Get(name)).CloneTree()
   t_tree.SetDirectory(outdir2)
   outdir2.cd()
   t_tree.Write()
 if opt.add_gen :
   outdir = out_file.mkdir("genDiphotonDumper")
   outdir.cd()
   outdir2 = outdir.mkdir("trees")
   for tag in ['DoubleHTag_0','NoTag_0']:
     name = 'gen_'+input_names[num]+'_'+tag
     t_tree = (f_tree.Get(name)).CloneTree()
     t_tree.SetDirectory(outdir2)
     outdir2.cd()
     t_tree.Write()
 out_file.Close()
 

