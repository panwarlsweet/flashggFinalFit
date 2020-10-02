YEAR="2016_2017_2018"
#YEAR="2018"
DATE="25_09_2020"
DO_SYSTEMATIC=0
btagReshapeFalse=1  #btagReshapeWeight was propagated with False in the flashgg trees
signal=$1
#mass=$2
#PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016"
PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016,bbhyb2_2016,bbhybyt_2016,tth_2017,ggh_2017,qqh_2017,vh_2017,bbhyb2_2017,bbhybyt_2017,tth_2018,ggh_2018,qqh_2018,vh_2018,bbhyb2_2018,bbhybyt_2018"
#,bbh_4FS_yb2_2018,bbh_4FS_ybyt_2018"  #2016+2017+2018 only


CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"

#Masses="260,270,280,300,320,350"                                                            
Masses="400,450,500,550,600,650,700,800,900,1000"                                 
set -x
for mass in $(echo $Masses | sed "s/,/ /g")
    do
    SYSINPUTFILE="final_workspaces/CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}_${signal}hh${mass}.root"

##if running with no systematcis use any file with ws

    SIGNALFILE="final_workspaces/CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}_${signal}hh${mass}.root"
    DATAFILE="final_workspaces/CMS-HGG_multipdf2D_DoubleEG_ftest_"${signal}${mass}"_HHbbgg_${YEAR}_${DATE}.root"
#NODESFILE="CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}.root"

    INTLUMI2016=35.91
    INTLUMI2017=41.53
    INTLUMI2018=59.35

    SCALES="HighR9EE,LowR9EE,HighR9EB,LowR9EB"
    SMEARS="HighR9EERho,LowR9EERho,HighR9EEPhi,LowR9EEPhi,HighR9EBPhi,LowR9EBPhi,HighR9EBRho,LowR9EBRho"
    SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward"
    SCALESGLOBAL="NonLinearity,Geant4,LightYield,Absolute"

    SCALES=""
    SMEARS=""
    SCALESCORR=""
    SCALESGLOBAL=""
    
    nodename=${signal}"hh"${mass}"_2016,"${signal}"hh"${mass}"_2017,"${signal}"hh"${mass}"_2018"
    outname="outputs/cms_HHbbgg_datacard_"${signal}${mass}"_${DATE}_${YEAR}.txt"
    if [ $DO_SYSTEMATIC -gt 0 ] 
    then
	outname="outputs/cms_HHbbgg_datacard_node${node}_"${signal}${mass}"_${DATE}_systematics_upd.txt"
    fi
    P=$nodename,$PROCS
    if [ $mass -gt 550 ]; then
	P=$nodename
    fi
    ./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --signalProc $nodename -d $DATAFILE -p $P -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --btagReshapeFalse $btagReshapeFalse --do2D
    done
set +x
