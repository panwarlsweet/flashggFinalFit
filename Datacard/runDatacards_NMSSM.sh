YEAR="2016_2017_2018"
DATE="06_12_2020"
DO_SYSTEMATIC=0
btagReshapeFalse=1  #btagReshapeWeight was propagated with False in the flashgg trees
signal=$1
massY=$2

PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016,bbhyb2_2016,bbhybyt_2016,tth_2017,ggh_2017,qqh_2017,vh_2017,bbhyb2_2017,bbhybyt_2017,tth_2018,ggh_2018,qqh_2018,vh_2018,bbhyb2_2018,bbhybyt_2018"

CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"

Masses="300,400,500,600,800,900,1000"            
set -x
for mass in $(echo $Masses | sed "s/,/ /g")
    do
    SYSINPUTFILE="final_workspaces/${signal}/CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}_${signal}X${mass}ToY${massY}H125.root"

##if running with no systematcis use any file with ws

    SIGNALFILE="final_workspaces/${signal}/CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}_${signal}X${mass}ToY${massY}H125.root"

    DATAFILE="final_workspaces/${signal}/CMS-HGG_multipdf2D_DoubleEG_ftest_${signal}_X${mass}_Y${massY}_HHbbgg_${YEAR}_${DATE}.root"
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
    
    #nodename="${signal}X${mass}ToY${massY}H125_2016,${signal}X${mass}ToY${massY}H125_2017,${signal}X${mass}ToY${massY}H125_2018"
    #nodename="Radionhh"${mass}"_2016,Radionhh"${mass}"_2017,Radionhh"${mass}"_2018"
    nodename="BulkGravitonhh"${mass}"_2016,BulkGravitonhh"${mass}"_2017,BulkGravitonhh"${mass}"_2018"
    #outname="outputs/cms_HHbbgg_datacard_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.txt"
    #outname="outputs/cms_HHbbgg_datacard_Radionhh_X${mass}_${DATE}_${YEAR}.txt"
    outname="outputs/cms_HHbbgg_datacard_BulkGravitonhh_X${mass}_${DATE}_${YEAR}.txt"
    if [ $DO_SYSTEMATIC -gt 0 ] 
    then
	outname="outputs/cms_HHbbgg_datacard_node${node}_"${signal}${mass}"Y${massY}_${DATE}_systematics_upd.txt"
    fi
    P=$nodename,$PROCS
    if [ $mass -gt 550 ]; then
	P=$nodename
    fi
    ./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --signalProc $nodename -d $DATAFILE -p $P -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --btagReshapeFalse $btagReshapeFalse --do2D
    done
set +x
