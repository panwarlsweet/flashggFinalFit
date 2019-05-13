DATE="06_05_2019"

PROCS="GluGluHToGG_M_125_13TeV_powheg_pythia8,VBFHToGG_M_125_13TeV_powheg_pythia8,ttHToGG_M125_13TeV_powheg_pythia8_v2,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8,GluGluHToGG_M_125_13TeV_powheg_pythia8_2017,VBFHToGG_M_125_13TeV_powheg_pythia8_2017,ttHToGG_M125_13TeV_powheg_pythia8_2017,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_2017"
CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11"

#tests : 
#PROCS="GluGluHToGG_M_125_13TeV_powheg_pythia8,GluGluHToGG_M_125_13TeV_powheg_pythia8_2017"
#CATS="DoubleHTag_0"

#SOMEINPUTFILE="/work/nchernya/DiHiggs/inputs/${DATE}//output_GluGluToHHTo2B2G_node_SM_13TeV-madgraph_generated_125.root"
#SOMEINPUTFILE="/work/nchernya/DiHiggs/inputs/${DATE}//output_GluGluToHHTo2B2G_node_SM_13TeV-madgraph_generated.root"
SOMEINPUTFILE="/work/nchernya/DiHiggs/inputs/${DATE}/systematics_merged/output_allprocs.root"

SIGNALFILE="inputs/CMS-HGG_sigfit_singleHiggs2016_${DATE}.root,inputs/CMS-HGG_sigfit_singleHiggs2017_${DATE}.root"
DATAFILE="inputs/CMS-HGG_multipdf_HHbbgg_2016_2017_${DATE}.root"
NODESFILE="inputs/CMS-HGG_sigfit_nodes2016_${DATE}.root,inputs/CMS-HGG_sigfit_nodes2017_${DATE}.root"
INTLUMI2016=35.9
INTLUMI2017=41.5

SCALES="HighR9EE,LowR9EE,HighR9EB,LowR9EB"
SMEARS="HighR9EERho,LowR9EERho,HighR9EEPhi,LowR9EEPhi,HighR9EBPhi,LowR9EBPhi,HighR9EBRho,LowR9EBRho"
SCALESCORR="MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward"
SCALESGLOBAL="NonLinearity,Geant4,LightYield,Absolute"

SCALES=""
SMEARS=""
SCALESCORR=""
SCALESGLOBAL=""

#SMSIGNAL="GluGluToHHTo2B2G_node_SM_13TeV_madgraph,GluGluToHHTo2B2G_node_SM_13TeV_madgraph_2017"
SMSIGNAL="GluGluToHHTo2B2G_node_SM_13TeV_madgraph_generated,GluGluToHHTo2B2G_node_SM_13TeV_madgraph_generated_2017"
./makeParametricModelDatacardFLASHgg.py -i $SOMEINPUTFILE -s $SIGNALFILE --signalProc $SMSIGNAL -d $DATAFILE -p $PROCS,$SMSIGNAL -c $CATS --photonCatScales $SCALES --photonCatSmears $SMEARS  --globalScales $SCALESGLOBAL --photonCatScalesCorr $SCALESCORR --isMultiPdf --intLumi $INTLUMI2016 --intLumi2017 $INTLUMI2017 -o outputs/cms_HHbbgg_datacard_SMgenerated_${DATE}_systematics.txt

for node in `seq 0 -1`;
#for node in `seq 0 11` SM box;
do
   nodename="GluGluToHHTo2B2G_node_${node}_13TeV_madgraph,GluGluToHHTo2B2G_node_${node}_13TeV_madgraph_2017"
   outname="outputs/cms_HHbbgg_datacard_node${node}_${DATE}_systematics.txt"
   SOMEINPUTFILE="/work/nchernya/DiHiggs/inputs/${DATE}/systematics_merged/output_allprocs.root,/work/nchernya/DiHiggs/inputs/${DATE}/systematics_merged/output_GluGluToHHTo2B2G_node_${node}_13TeV-madgraph_all.root"
  #./makeParametricModelDatacardFLASHgg.py -i $SOMEINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi $INTLUMI2016 --intLumi2017 $INTLUMI2017
  echo ./makeParametricModelDatacardFLASHgg.py -i $SOMEINPUTFILE -s $SIGNALFILE --nodesFile $NODESFILE --signalProc $nodename -d $DATAFILE -p $PROCS,$nodename -c $CATS --photonCatScales ../Signal/dat/photonCatSyst.dat --photonCatSmears ../Signal/dat/photonCatSyst.dat --isMultiPdf  -o ${outname} --intLumi $INTLUMI2016 --intLumi2017 $INTLUMI2017
done
