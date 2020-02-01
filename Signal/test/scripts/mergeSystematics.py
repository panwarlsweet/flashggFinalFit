import numpy as np

print 'cd /work/nchernya/CMSSW_9_4_9/src/flashgg/'
print 'cmsenv'
date = '06_05_2019'

filenames_2016 = 'VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,ttHToGG_M125_13TeV_powheg_pythia8_v2,VBFHToGG_M-125_13TeV_powheg_pythia8,GluGluHToGG_M-125_13TeV_powheg_pythia8,GluGluToHHTo2B2G_node_SM_13TeV-madgraph_generated'.split(',')
filenames_2017 = 'ttHToGG_M125_13TeV_powheg_pythia8,GluGluHToGG_M-125_13TeV_powheg_pythia8,VBFHToGG_M-125_13TeV_powheg_pythia8,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,GluGluToHHTo2B2G_node_SM_13TeV-madgraph_generated'.split(',')
dir_syst = '/work/nchernya/DiHiggs/inputs/%s/systematics/'%date
dir_nom = '/work/nchernya/DiHiggs/inputs/%s/systematics_nominal/'%date
dir_merged = '/work/nchernya/DiHiggs/inputs/%s/systematics_merged/'%date

for file in filenames_2016 :
	file = 'output_'+file+'.root'  
	print 'hadd_workspaces %s/%s %s/%s %s/%s'%(dir_merged,file,dir_syst,file,dir_nom,file) 
for file in filenames_2017 :  
	file = 'output_'+file+'_2017'+'.root'
	print 'hadd_workspaces %s/%s %s/%s %s/%s'%(dir_merged,file,dir_syst,file,dir_nom,file) 


#########Nodes##############

dir_syst = '/work/nchernya/DiHiggs/inputs/%s/'%date
dir_merged = '/work/nchernya/DiHiggs/inputs/%s/'%date

whichNodes = list(np.arange(0,12,1))
whichNodes.append('SM')
whichNodes.append('box')

for i in whichNodes:
	file = "output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph.root"%i
	file2 = "output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph_1*.root"%i
	print 'hadd_workspaces %s/%s %s/%s'%(dir_merged,file,dir_syst,file2) 

for i in whichNodes:
	file = "output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph_2017.root"%i
	file2 = "output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph_2017_1*.root"%i
	print 'hadd_workspaces %s/%s %s/%s'%(dir_merged,file,dir_syst,file2) 

###################Merge nodes for systematics :
#print  'hadd_workspaces /work/nchernya/DiHiggs/inputs/06_05_2019/systematics_merged/output_allprocs_nodes.root /work/nchernya/DiHiggs/inputs/06_05_2019/systematics/output_GluGluToHHTo2B2G_node_*_13TeV-madgraph_2017.root /work/nchernya/DiHiggs/inputs/06_05_2019/systematics/output_GluGluToHHTo2B2G_node_*_13TeV-madgraph.root /work/nchernya/DiHiggs/inputs/06_05_2019/systematics_nominal/output_GluGluToHHTo2B2G_node_*_13TeV-madgraph_2017.root /work/nchernya/DiHiggs/inputs/06_05_2019/systematics_nominal/output_GluGluToHHTo2B2G_node_*_13TeV-madgraph.root'
dir_syst = '/work/nchernya/DiHiggs/inputs/%s/systematics/'%date
dir_nom = '/work/nchernya/DiHiggs/inputs/%s/systematics_nominal/'%date
dir_merged = '/work/nchernya/DiHiggs/inputs/%s/systematics_merged/'%date
for i in whichNodes:
	file = "output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph.root"%i
#	print 'hadd_workspaces %s/%s %s/%s %s/%s'%(dir_merged,file,dir_syst,file,dir_nom,file) 

for i in whichNodes:
	file = "output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph_2017.root"%i
#	print 'hadd_workspaces %s/%s %s/%s %s/%s'%(dir_merged,file,dir_syst,file,dir_nom,file) 


#for i in whichNodes:
#	print "hadd_workspaces /work/nchernya/DiHiggs/inputs/06_05_2019/systematics_merged/output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph_all.root /work/nchernya/DiHiggs/inputs/06_05_2019/systematics_merged/output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph.root  /work/nchernya/DiHiggs/inputs/06_05_2019/systematics_merged/output_GluGluToHHTo2B2G_node_%s_13TeV-madgraph_2017.root"%(i,i,i)
