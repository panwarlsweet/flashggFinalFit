#!/bin/bash

#DATE="04_02_2020"
#DATE="04_02_2020_mjjnorm"
DATE="18_02_2020"
#name2D=BG_MCbgbjets
#name2D=DoubleEG
#name2D=BG_MCbg
#outtag=ivanjson
#outtag=ivanjsonMC
name2D=$1
outtag=$2
combineout=HHbbgg2D_${name2D}_${outtag}_${DATE}_nlo_kl1
#DATACARD="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_wo_ggHvH_systematics.txt"  
#DATACARDroot="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_wo_ggHvH_systematics.root"
#DATACARD="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_MjjRenamed_ggHvH_05systematics.txt"  
#DATACARDroot="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_MjjRenamed_ggHvH_05systematics.root" 
#DATACARD="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_2018_vbfhh.txt"  
#DATACARDroot="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_2018_vbfhh.root"
DATACARD="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_nlo_kl1.txt" 
DATACARDroot="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_nlo_kl1.root" 
#DATACARD="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_MjjRenamed_systematics.txt" 
#DATACARDroot="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_MjjRenamed_systematics.root" 
#DATACARD="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_MjjRenamed.txt"  
#DATACARDroot="Datacards/cms_HHbbgg2D_${name2D}_${outtag}_datacard_nodeSM_${DATE}_cats90GeV_MjjRenamed.root"  

echo $name2D 
echo $outtag

text2workspace.py $DATACARD 

combine $DATACARDroot  -n $combineout  -M MultiDimFit -m 125. --saveWorkspace -t -1 --X-rtd TMCSO_AdaptivePseudoAsimov=0 --X-rtd TMCSO_PseudoAsimov=0 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2

combine higgsCombine${combineout}.MultiDimFit.mH125.root --snapshotName MultiDimFit -n $combineout  -M AsymptoticLimits -m 125. --saveWorkspace -t -1 --run=blind --X-rtd TMCSO_AdaptivePseudoAsimov=0 --X-rtd TMCSO_PseudoAsimov=0 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2

