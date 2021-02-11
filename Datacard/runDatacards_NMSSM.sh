YEAR="2016_2017_2018"
DATE="18_01_2021_SYS"
DO_SYSTEMATIC=1
btagReshapeFalse=1  #btagReshapeWeight was propagated with False in the flashgg trees
signal=$1
massY=$2

PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016,bbhyb2_2016,bbhybyt_2016,tth_2017,ggh_2017,qqh_2017,vh_2017,bbhyb2_2017,bbhybyt_2017,tth_2018,ggh_2018,qqh_2018,vh_2018,bbhyb2_2018,bbhybyt_2018"

CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"

Masses="300,400,500,600,800,900,1000"
#Masses="400"
## low Y systematics
#Masses="400,500,800" 
## mid Y systematics 
#Masses="600,900"
## high Y systematics                                                                         
#Masses="1000"

set -x
for mass in $(echo $Masses | sed "s/,/ /g")
    do
    check=$((${mass}-$massY-125))
    echo ${check}
    if [ "${check}" -lt 0 ]; then
	continue;
    else
    SYSINPUTFILE="/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/1000/700/NMSSMX1000ToY700H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/1000/700/NMSSMX1000ToY700H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/1000/700/NMSSMX1000ToY700H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/NMSSMX400ToY100H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/NMSSMX400ToY100H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/NMSSMX400ToY100H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/bbhyb2_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/bbhyb2_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/bbhyb2_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/bbhybyt_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/bbhybyt_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/bbhybyt_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/ggh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/ggh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/ggh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/qqh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/qqh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/qqh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/tth_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/tth_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/tth_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/vh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/vh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/100/vh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/NMSSMX400ToY125H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/NMSSMX400ToY125H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/NMSSMX400ToY125H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/bbhyb2_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/bbhyb2_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/bbhyb2_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/bbhybyt_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/bbhybyt_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/bbhybyt_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/ggh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/ggh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/ggh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/qqh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/qqh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/qqh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/tth_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/tth_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/tth_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/vh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/vh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/125/vh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/NMSSMX400ToY200H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/NMSSMX400ToY200H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/NMSSMX400ToY200H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/bbhyb2_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/bbhyb2_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/bbhyb2_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/bbhybyt_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/bbhybyt_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/bbhybyt_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/ggh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/ggh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/ggh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/qqh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/qqh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/qqh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/tth_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/tth_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/tth_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/vh_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/vh_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/400/200/vh_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/100/NMSSMX500ToY100H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/100/NMSSMX500ToY100H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/100/NMSSMX500ToY100H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/125/NMSSMX500ToY125H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/125/NMSSMX500ToY125H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/125/NMSSMX500ToY125H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/200/NMSSMX500ToY200H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/200/NMSSMX500ToY200H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/500/200/NMSSMX500ToY200H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/600/300/NMSSMX600ToY300H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/600/300/NMSSMX600ToY300H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/600/300/NMSSMX600ToY300H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/100/NMSSMX800ToY100H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/100/NMSSMX800ToY100H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/100/NMSSMX800ToY100H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/125/NMSSMX800ToY125H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/125/NMSSMX800ToY125H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/125/NMSSMX800ToY125H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/200/NMSSMX800ToY200H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/200/NMSSMX800ToY200H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/800/200/NMSSMX800ToY200H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/900/300/NMSSMX900ToY300H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/900/300/NMSSMX900ToY300H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/900/300/NMSSMX900ToY300H125_2018.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/900/500/NMSSMX900ToY500H125_2016.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/900/500/NMSSMX900ToY500H125_2017.root,/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/SYS/WS/NMSSM/900/500/NMSSMX900ToY500H125_2018.root"

    #SYSINPUTFILE="final_workspaces/${signal}/CMS-HGG_sigfit_MggMjj_${YEAR}_${DATE}_${signal}X${mass}ToY${massY}H125.root"

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
    
    nodename="${signal}X${mass}ToY${massY}H125_2016,${signal}X${mass}ToY${massY}H125_2017,${signal}X${mass}ToY${massY}H125_2018"
    #nodename="Radionhh"${mass}"_2016,Radionhh"${mass}"_2017,Radionhh"${mass}"_2018"
    #nodename="BulkGravitonhh"${mass}"_2016,BulkGravitonhh"${mass}"_2017,BulkGravitonhh"${mass}"_2018"
    outname="outputs/cms_HHbbgg_datacard_${signal}_X${mass}_Y${massY}_${DATE}_${YEAR}.txt"
    #outname="outputs/cms_HHbbgg_datacard_Radionhh_X${mass}_${DATE}_${YEAR}.txt"
    #outname="outputs/cms_HHbbgg_datacard_BulkGravitonhh_X${mass}_${DATE}_${YEAR}.txt"
    if [ $DO_SYSTEMATIC -gt 0 ] 
    then
	outname="outputs/cms_HHbbgg_datacard_node${node}_"${signal}${mass}"Y${massY}_${DATE}_systematics_upd.txt"
    fi
    P=$nodename,$PROCS
    if [ $mass -gt 550 ] || [ $massY -gt 250 ]; then
	P=$nodename
    fi
    ./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --signalProc $nodename -d $DATAFILE -p $P -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --btagReshapeFalse $btagReshapeFalse --do2D
    fi
    done
set +x
