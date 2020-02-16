#DATE="24_01_2020"
DATE="18_02_2020"
DO_SYSTEMATIC=0
btagReshapeFalse=1  #btagReshapeWeight was propagated with False in the flashgg trees

PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016,tth_2017,ggh_2017,qqh_2017,vh_2017,tth_2018,ggh_2018,qqh_2018,vh_2018"
#PROCS="tth_2016,ggh_2016,qqh_2016,vh_2016,tth_2017,ggh_2017,qqh_2017,vh_2017"  #2016.2017 only
CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11"

#SYSINPUTFILE="/work/nchernya/DiHiggs/inputs/${DATE}/systematics_merged/output_allprocs.root"
#SYSINPUTFILE="/work/nchernya/DiHiggs/inputs/${DATE}/output_vh_2016.root"
SYSINPUTFILE="/scratch/nchernya/HHbbgg/24_01_2020/workspaces_systematics/output_syst_single_higgs_24_01_2020.root,/scratch/nchernya/HHbbgg/24_01_2020/workspaces_systematics/output_hh_node_SM_2016.root,/scratch/nchernya/HHbbgg/24_01_2020/workspaces_systematics/output_hh_node_SM_2017.root,/scratch/nchernya/HHbbgg/24_01_2020/workspaces_systematics/output_hh_node_SM_2018.root" # if no systematics, then whatever file is ok

SIGNALFILE="inputs/CMS-HGG_sigfit_singleHiggs2016_${DATE}.root,inputs/CMS-HGG_sigfit_singleHiggs2017_${DATE}.root,inputs/CMS-HGG_sigfit_singleHiggs2018_${DATE}.root"
DATAFILE="inputs/CMS-HGG_multipdf_HHbbgg_2016_2017_2018_${DATE}.root"
#DATAFILE="inputs/CMS-HGG_multipdf_HHbbgg_2016_2017_${DATE}.root"  #2016.2017 only
NODESFILE="inputs/CMS-HGG_sigfit_nodes2016_${DATE}.root,inputs/CMS-HGG_sigfit_nodes2017_${DATE}.root,inputs/CMS-HGG_sigfit_nodes2018_${DATE}.root"
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

#SM generated signal. Can ignore now.
#SMSIGNAL="GluGluToHHTo2B2G_node_SM_13TeV_madgraph,GluGluToHHTo2B2G_node_SM_13TeV_madgraph_2017"
#SMSIGNAL="hh_SM_generated_2016,hh_SM_generated_2017,hh_SM_generated_2018"
#./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --signalProc $SMSIGNAL -d $DATAFILE -p $PROCS,$SMSIGNAL -c $CATS --photonCatScales $SCALES --photonCatSmears $SMEARS  --globalScales $SCALESGLOBAL --photonCatScalesCorr $SCALESCORR --isMultiPdf --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 -o outputs/cms_HHbbgg_datacard_SMgenerated_${DATE}_systematics.txt

#for node in `seq 0 -1`;
for node in SM;
#for node in `seq 0 11` SM box;
do
   nodename="hh_node_${node}_2016,hh_node_${node}_2017,hh_node_${node}_2018"
   outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}.txt"
   if [ $DO_SYSTEMATIC -gt 0 ] 
   then
      outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}_systematics_upd.txt"
   fi
   #nodename="hh_node_${node}_2016,hh_node_${node}_2017" #2016.2017 only
   #outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}_2016_2017.txt"

#  ./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --btagReshapeFalse $btagReshapeFalse
  
done


########################kl kt scan##########################
klkt_dir="/work/nchernya/DiHiggs/inputs/${DATE}/categorizedTrees/kl_kt_finebinning/"
SMcard="outputs/cms_HHbbgg_datacard_nodeSM_${DATE}.txt"
if [ $DO_SYSTEMATIC -gt 0 ] 
then
  SMcard="outputs/cms_HHbbgg_datacard_nodeSM_${DATE}_systematics_upd.txt"
fi
nodename="hh_node_SM_2016,hh_node_SM_2017,hh_node_SM_2018"
outname="outputs/tmp.txt"
#./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --hhReweightDir $klkt_dir --hhReweightSM $SMcard --do_kl_scan  


######################## BSM benchmark scan##########################
klkt_dir="/work/nchernya/DiHiggs/inputs/${DATE}/categorizedTrees/kl_kt_finebinning_test/"
SMcard="outputs/cms_HHbbgg_datacard_nodeSM_${DATE}_systematics.txt"
if [ $DO_SYSTEMATIC -gt 0 ] 
then
  SMcard="outputs/cms_HHbbgg_datacard_nodeSM_${DATE}_systematics_upd.txt"
fi
nodename="hh_node_SM_2016,hh_node_SM_2017,hh_node_SM_2018"
outname="outputs/tmp.txt"
#./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --hhReweightDir $klkt_dir --hhReweightSM $SMcard --do_benchmarks_scan  



########################kl likelihood scan##########################
kl_fit_params="/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Plots/FinalResults/plots/yeilds_ratio_kl_xsec_24_01_2020_fitparams.json"
SMcard="outputs/cms_HHbbgg_datacard_nodeSM_${DATE}.txt"
if [ $DO_SYSTEMATIC -gt 0 ] 
then
  SMcard="outputs/cms_HHbbgg_datacard_nodeSM_${DATE}_systematics_upd.txt"
fi
nodename="hh_node_SM_2016,hh_node_SM_2017,hh_node_SM_2018"
outname="outputs/tmp.txt"
#./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --kl_fit_params $kl_fit_params  --hhReweightSM $SMcard --do_kl_likelihood 


############################## MC BG #####################
for node in SM;
#for node in `seq 0 11` SM box;
do
   nodename="hh_node_${node}_2016,hh_node_${node}_2017,hh_node_${node}_2018"
   #DATAFILE="inputs/CMS-HGG_multipdf_MCbg_HHbbgg_2016_2017_2018_${DATE}.root"
   DATAFILE="inputs/CMS-HGG_multipdf_MCbgbjets_HHbbgg_2016_2017_2018_${DATE}.root"
   outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}_MCbgbjets.txt"
   if [ $DO_SYSTEMATIC -gt 0 ] 
   then
      outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}_MCbgbjets_systematics_upd.txt"
   fi
#  ./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --btagReshapeFalse $btagReshapeFalse
  
done


#######################################################################
#######################################################################
################################    2D   ##############################
#######################################################################
#######################################################################

for node in SM;
#for node in `seq 0 11` SM box;
do
   #name2D=BG_MCbgbjets
   name2D=DoubleEG
   #name2D=BG_MCbg
   outtag=ivanjson
   #outtag=high
   nodename="hh_node_${node}_2016,hh_node_${node}_2017,hh_node_${node}_2018"
   outname="outputs/cms_HHbbgg2D_${name2D}_${outtag}_datacard_node${node}_${DATE}.txt" #_ivannorm.txt"   #_mjjnorm.txt"
   if [ $DO_SYSTEMATIC -gt 0 ] 
   then
      outname="outputs/cms_HHbbgg2D_${name2D}_{$outtag}_datacard_node${node}_${DATE}_systematics.txt"
   fi
   DATAFILE="inputs/CMS-HGG_multipdf2D_${name2D}_${outtag}_HHbbgg_2016_2017_2018_${DATE}.root"
   #NODESFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root"
   #SIGNALFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root"
   #NODESFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020.root"
   #SIGNALFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020.root"
   #NODESFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020_mjjnorm.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020_mjjnorm.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020_mjjnorm.root"
   #SIGNALFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020_mjjnorm.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020_mjjnorm.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_12_02_2020_mjjnorm.root"
   NODESFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root"
   SIGNALFILE="inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root,inputs/CMS-HGG_sigfit_MggMjj_2016_2017_2018_${DATE}.root"


  ./makeParametricModelDatacardFLASHgg.py -i $SYSINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi2016 $INTLUMI2016 --intLumi2017 $INTLUMI2017 --intLumi2018 $INTLUMI2018 --do_HHbbgg_systematics $DO_SYSTEMATIC --do2D --btagReshapeFalse $btagReshapeFalse
done


