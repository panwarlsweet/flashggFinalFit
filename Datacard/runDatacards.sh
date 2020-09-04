YEAR="2016_2017_2018"
#YEAR="2018"
DATE="02_09_2020"
DO_SYSTEMATIC=0
btagReshapeFalse=0  #btagReshapeWeight was propagated with False in the flashgg trees

#PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016"
PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016,tth_2017,ggh_2017,qqh_2017,vh_2017,tth_2018,ggh_2018,qqh_2018,vh_2018"
#,bbh_4FS_yb2_2018,bbh_4FS_ybyt_2018"  #2016+2017+2018 only


CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"
#,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11"

SYSINPUTFILE="CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}.root"

##if running with no systematcis use any file with ws

SIGNALFILE="CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}.root"
DATAFILE="CMS-HGG_multipdf2D_DoubleEG_cats70GeV_ftest_HHbbgg_${YEAR}_${DATE}.root"
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

nodename="Radionhh300_2016,Radionhh300_2017,Radionhh300_2018"
outname="outputs/cms_HHbbgg_datacard_RD300_${DATE}_${YEAR}.txt"
if [ $DO_SYSTEMATIC -gt 0 ] 
then
   outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}_systematics_upd.txt"
fi

./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --btagReshapeFalse $btagReshapeFalse --do2D
