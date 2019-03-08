INDIR="/mnt/t3nfs01/data01/shome/nchernya/DiHiggs/inputs/07_03_2019/"
YEAR="_2017"  #empty for 2016 and _2017 for 2017
YEAR2="2017" 
EXT="nodes"$YEAR2

OUTDIR="output/out_27_02_2019tthKiller_set_test"$YEAR2
#PROCS="GluGluToHHTo2B2G_node_0_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_1_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_2_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_3_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_4_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_5_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_6_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_7_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_8_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_9_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_10_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_11_13TeV_madgraph$YEAR"
PROCS="GluGluToHHTo2B2G_node_0_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_2_13TeV_madgraph$YEAR"
INFILES="output_GluGluToHHTo2B2G_node_0_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_2_13TeV-madgraph$YEAR"
CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11"
REFTAG="DoubleHTag_0"
REFPROC="GluGluToHHTo2B2G_node_0_13TeV_madgraph$YEAR"
#INFILES="output_GluGluToHHTo2B2G_node_0_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_1_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_2_13TeV-madgraph,output_GluGluToHHTo2B2G_node_3_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_4_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_5_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_6_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_7_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_8_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_9_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_10_13TeV-madgraph$YEAR,output_GluGluToHHTo2B2G_node_11_13TeV-madgraph$YEAR"

INTLUMI=77.4
#CONFIGDAT="config_13_12_nodes_"$YEAR2".dat"
CONFIGDAT="config_13_12_nodes_"$YEAR2"_test.dat"



#############SINGLE HIGGS BKG plus SM signal ###############

#YEAR=""
YEAR="_2017"
YEAR2="2017"
EXT="singleHiggs"$YEAR2

PROCS="GluGluToHHTo2B2G_node_SM_13TeV_madgraph_2017,GluGluHToGG_M_125_13TeV_powheg_pythia8_2017,VBFHToGG_M125_13TeV_amcatnlo_pythia8_2017,ttHToGG_M125_13TeV_powheg_pythia8_2017,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_2017"
REFPROC="ttHToGG_M125_13TeV_powheg_pythia8_2017"
INFILES="output_GluGluToHHTo2B2G_node_SM_13TeV-madgraph_2017,output_GluGluHToGG_M-125_13TeV_powheg_pythia8_2017,output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_2017,output_ttHToGG_M125_13TeV_powheg_pythia8_2017,output_VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_2017"
INTLUMI=41.5

#REFPROC="ttHToGG_M125_13TeV_powheg_pythia8_v2"
#PROCS="GluGluToHHTo2B2G_node_SM_13TeV_madgraph,GluGluHToGG_M_125_13TeV_powheg_pythia8,VBFHToGG_M_125_13TeV_powheg_pythia8,ttHToGG_M125_13TeV_powheg_pythia8_v2,VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8"
#INFILES="output_GluGluToHHTo2B2G_node_SM_13TeV-madgraph,output_GluGluHToGG_M-125_13TeV_powheg_pythia8,output_VBFHToGG_M-125_13TeV_powheg_pythia8,output_ttHToGG_M125_13TeV_powheg_pythia8_v2,output_VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8"
#INTLUMI=35.9

CONFIGDAT="config_13_12_all.dat"
OUTDIR="output/test"$YEAR2

BATCH=T3CH
DEFAULTQUEUE=all.q


####################################################
################## SIGNAL F-TEST ###################
####################################################
INDIR="/mnt/t3nfs01/data01/shome/nchernya/DiHiggs/inputs/27_02_2019/"
MASS=_125
PROCS="GluGluToHHTo2B2G_node_SM_13TeV_madgraph_2017,GluGluHToGG_M_125_13TeV_powheg_pythia8_2017"
INFILES="output_GluGluToHHTo2B2G_node_SM_13TeV-madgraph_2017$MASS,output_GluGluHToGG_M-125_13TeV_powheg_pythia8_2017$MASS"
#ls dat/newConfig_${EXT}.dat
mkdir -p $OUTDIR/dat
if [ -e ${OUTDIR}/dat/newConfig_${EXT}.dat ]; then
  echo "[INFO] sigFTest dat file $OUTDIR/dat/newConfig_${EXT}.dat already exists, so SKIPPING SIGNAL FTEST"
else
 echo "[INFO] sigFTest dat file $OUTDIR/dat/newConfig_${EXT}.dat  DOES NOT already exist, so PERFORMING SIGNAL FTEST"
 if [ 1 > 0 ]; then
    mkdir -p $OUTDIR/fTest
    echo "=============================="
    echo "Running Signal F-Test"
    echo "-->Determine Number of gaussians"
    echo "=============================="
    echo "./python/submitSignaFTest.py --procs $PROCS --flashggCats $CATS --outDir $OUTDIR -i $INFILES  --indir $INDIR   --batch $BATCH -q '$DEFAULTQUEUE'"
    ./python/submitSignaFTest.py --procs $PROCS --flashggCats $CATS --outDir $OUTDIR -i $INFILES --indir $INDIR    --batch $BATCH -q "$DEFAULTQUEUE"

    PEND=`ls -l $OUTDIR/fTestJobs/sub*| grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" |grep -v "\.log"  |wc -l`
    TOTAL=`ls -l $OUTDIR/fTestJobs/sub*| grep "\.sh"  |wc -l`
    echo "PEND $PEND"
    while (( $PEND > 0 )) ; do
      PEND=`ls -l $OUTDIR/fTestJobs/sub* | grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" | grep -v "\.log" |wc -l`
      RUN=`ls -l $OUTDIR/fTestJobs/sub* | grep "\.run" |wc -l`
      FAIL=`ls -l $OUTDIR/fTestJobs/sub* | grep "\.fail" |wc -l`
      DONE=`ls -l $OUTDIR/fTestJobs/sub* | grep "\.done" |wc -l`
      (( PEND=$PEND-$RUN-$FAIL-$DONE ))
      echo " PEND $PEND - RUN $RUN - DONE $DONE - FAIL $FAIL"
      if (( $RUN > 0 )) ; then PEND=1 ; fi
	   if (( $DONE == $TOTAL )) ; then PEND=0; fi
      if (( $FAIL > 0 )) ; then 
          echo "ERROR at least one job failed :"
          ls -l $OUTDIR/fTestJobs/sub* | grep "\.fail"
          exit 1
      fi
      sleep 10
    done
    mkdir -p $OUTDIR/dat
    cat $OUTDIR/fTestJobs/outputs/* > dat/newConfig_${EXT}_temp.dat
    sort -u dat/newConfig_${EXT}_temp.dat  > dat/tmp_newConfig_${EXT}_temp.dat 
    mv dat/tmp_newConfig_${EXT}_temp.dat dat/newConfig_${EXT}_temp.dat
    cp dat/newConfig_${EXT}_temp.dat $OUTDIR/dat/copy_newConfig_${EXT}_temp.dat
    rm -rf $OUTDIR/sigfTest
    mv $OUTDIR/fTest $OUTDIR/sigfTest
  fi
  echo "[INFO] sigFtest completed"
  echo "[INFO] using the results of the F-test as they are and building the signal model"
  echo "If you want to amend the number of gaussians, do it in $PWD/dat/newConfig_${EXT}.dat and re-run!"
  cp dat/newConfig_${EXT}_temp.dat dat/newConfig_${EXT}.dat
  cp dat/newConfig_${EXT}_temp.dat $OUTDIR/dat/newConfig_${EXT}.dat
fi




############################################################

echo "./python/submitSignalFit.py --indir $INDIR -i $INFILES -d dat/${CONFIGDAT} --mhLow=120 --mhHigh=130 --procs $PROCS -s dat/photonCatSyst.dat --changeIntLumi ${INTLUMI} --refProc $REFPROC --refTag $REFTAG -p $OUTDIR/sigfit --batch T3CH -q all.q -f $CATS  -o ${OUTDIR}/CMS-HGG_sigfit_${EXT}.root"
#./python/submitSignalFit.py --indir $INDIR -i $INFILES -d dat/${CONFIGDAT} --mhLow=120 --mhHigh=130 --procs $PROCS -s dat/photonCatSyst.dat --changeIntLumi ${INTLUMI} --refProc $REFPROC --refTag $REFTAG -p $OUTDIR/sigfit --batch T3CH -q all.q -f $CATS  -o ${OUTDIR}/CMS-HGG_sigfit_${EXT}.root


######################Combined output for 2016+2017################
#OUTDIR="output/out_20_02_2019_set20162017"
#PROCS1="GluGluToHHTo2B2G_node_0_13TeV_madgraph,GluGluToHHTo2B2G_node_1_13TeV_madgraph,GluGluToHHTo2B2G_node_2_13TeV_madgraph,GluGluToHHTo2B2G_node_3_13TeV_madgraph,GluGluToHHTo2B2G_node_4_13TeV_madgraph,GluGluToHHTo2B2G_node_5_13TeV_madgraph,GluGluToHHTo2B2G_node_6_13TeV_madgraph,GluGluToHHTo2B2G_node_7_13TeV_madgraph,GluGluToHHTo2B2G_node_8_13TeV_madgraph,GluGluToHHTo2B2G_node_9_13TeV_madgraph,GluGluToHHTo2B2G_node_10_13TeV_madgraph,GluGluToHHTo2B2G_node_11_13TeV_madgraph"
#YEAR='_2017'
#PROCS2="GluGluToHHTo2B2G_node_0_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_1_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_2_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_3_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_4_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_5_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_6_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_7_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_8_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_9_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_10_13TeV_madgraph$YEAR,GluGluToHHTo2B2G_node_11_13TeV_madgraph$YEAR"
#PROCS="$PROCS1,$PROCS2"
#EXT="nodes2016_2017"



################################DO NOT USE PACKAGER . IT IS MESSED UP IN CURRENT MASTER BRANCH############

#ls $PWD/$OUTDIR/CMS-HGG_sigfit_*.root > out.txt
#echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root > out.txt"
###ls $PWD/$OUTDIR/CMS-HGG_sigfit_*.root > out.txt
###echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_*.root > out.txt"
#counter=0
#while read p ; do
#  if (($counter==0)); then
#    SIGFILES="$p"
#  else
#    SIGFILES="$SIGFILES,$p"
#  fi
#  ((counter=$counter+1))
#done < out.txt
#echo "SIGFILES $SIGFILES"

#echo "./bin/PackageOutput -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_$EXT.root"
#./bin/PackageOutput  --skipMasses 120,130 -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_${EXT}_test.root > package.out
#./bin/PackageOutput -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_${EXT}_test.root > package.out
