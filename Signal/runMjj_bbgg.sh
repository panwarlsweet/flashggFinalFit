#YEAR=$3
Signal=$1
X_points="300,400,500,600,800,900,1000"
Run2_YEAR="2016,2017,2018"
#YEAR="2018"
mergeYears=0  #used for all procs
mergeCats=0 #used for single Higgs and 12 DoubleHTag cats only, not for VBF
PAPER=0
massY=$2

DATE="06_12_2020"

#EXT="singleHiggs"$YEAR

#EXT=$1"hh"$2"_"$YEAR
set -x
for X in $(echo $X_points | sed "s/,/ /g")
do

INDIR="/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/hadd_files/Run2_WS/"$Signal"/"$X"/"$massY"/"
OUTDIR="./output/out_fit_"${DATE}"_"$Signal$X"Y"$massY"/"
PLOTDIR="plot_dir_"$Signal$X"Y"$massY"/"
TEMPLATE="../MetaData_HHbbgg/models_2D_higgs_mjj"$massY".rs"  #working rather well for all qqHH and ggHH


CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"


#############SINGLE HIGGS ############
PROCS="ggh,tth,qqh,vh,bbhyb2,bbhybyt,"$Signal"X"$X"ToY"$massY"H125,Radionhh"$X",BulkGravitonhh"$X
#PROCS=$Signal"X"$X"ToY"$massY"H125,Radionhh"$X",BulkGravitonhh"$X
#PROCS="bbhyb2"
SIG_PROCS=$Signal"X"$X"ToY"$massY"H125,Radionhh"$X",BulkGravitonhh"$X 
################################


for YEAR in $(echo $Run2_YEAR | sed "s/,/ /g")
do
for PROC in $(echo $PROCS | sed "s/,/ /g")
	do
   
		INFILEWITHYEARS=${INDIR}${PROC}'_2016.root,'${INDIR}${PROC}'_2017.root,'${INDIR}${PROC}'_2018.root'  #example if you are using merged years
		if [ $mergeCats == 1 ]; then
			if [[ $PROC == *"ggh"* ]] || [[ $PROC == *"vh"* ]] || [[ $PROC == *"tth"* ]]  || [[ $PROC == *"qqh"* ]]  ; then
				if [ $mergeYears == 1 ]; then
					./bin/MjjSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} --mergeYears 2016,2017,2018 --infileWithAllYears ${INFILEWITHYEARS} -m 1 -f ${CATS} --paper ${PAPER}
				else
					./bin/MjjSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} -m 1 -f ${CATS} --paper ${PAPER}
				fi
			else 
				echo "You are trying to merge categories for a single Higgs process, are you sure you want to do this??"		
			fi	
		else
			if [ $mergeYears == 1 ]; then
				./bin/MjjSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} --mergeYears 2016,2017,2018 --infileWithAllYears ${INFILEWITHYEARS} -f ${CATS} --paper ${PAPER} -s ${SIG_PROCS}
			else
				./bin/MjjSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} -f ${CATS}  --paper ${PAPER} -s ${SIG_PROCS}  --massY $massY
			fi
		fi	
done
done
done
set +x
