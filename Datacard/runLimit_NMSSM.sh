YEAR="2016_2017_2018"
#YEAR="2018"
DATE="27_12_2020"
Masses="300,400,500,600,800,900,1000"
#Masses="260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000"
signal=$1
massY=$2
set -x
for mass in $(echo $Masses | sed "s/,/ /g")
    do
    check=$((${mass}-$massY-125))
    echo ${check}
    if [ "${check}" -lt 0 ]; then
	continue;
    else
    combineout="ResHHbbgg_datacard_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}"
    DATACARD="final_workspaces/final_datacards/cms_HHbbgg_datacard_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.txt"
    #DATACARD="final_workspaces/final_datacards/cms_HHbbgg_datacard_node_NMSSM300Y125_27_12_2020_systematics_upd.txt"
    DATACARDroot="final_workspaces/final_datacards/cms_HHbbgg_datacard_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.root"
    #DATACARDroot="final_workspaces/final_datacards/cms_HHbbgg_datacard_node_NMSSM300Y125_27_12_2020_systematics_upd.root"
    #text2workspace.py -m 125  $DATACARD $DATACARDroot --channel-masks
    text2workspace.py -m 125 $DATACARD -o $DATACARDroot --channel-masks
    ##if running with no systematcis use any file with ws

    combine -M AsymptoticLimits $DATACARDroot --run blind -m 125 -n ${combineout}_SYS --saveWorkspace --X-rtd TMCSO_AdaptivePseudoAsimov=0 --X-rtd TMCSO_PseudoAsimov=0 -s -1 -t -1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 >&limit_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}_SYS.txt& 
    combine -M AsymptoticLimits $DATACARDroot --run blind -m 125 -n $combineout --saveWorkspace --X-rtd TMCSO_AdaptivePseudoAsimov=0 --X-rtd TMCSO_PseudoAsimov=0 -s -1 -t -1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --freezeParameters allConstrainedNuisances >&limit_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.txt& 
    #combine $DATACARDroot  -n $combineout  -M MultiDimFit -m 125. --saveWorkspace -t -1 --X-rtd TMCSO_AdaptivePseudoAsimov=0 --X-rtd TMCSO_PseudoAsimov=0 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=1 -s -1 --freezeParameters allConstrainedNuisances

    #combine higgsCombineResHHbbgg_datacard_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.MultiDimFit.mH125.*.root  --snapshotName MultiDimFit -n $combineout  -M AsymptoticLimits -m 125. --saveWorkspace -t -1 --run=blind --X-rtd TMCSO_AdaptivePseudoAsimov=0 --X-rtd TMCSO_PseudoAsimov=0 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=1 --freezeParameters allConstrainedNuisances -s -1 >&limit_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.txt&
    fi
    done
set +x
