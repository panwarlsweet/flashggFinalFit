YEAR=$3
#YEAR="2017"
#YEAR="2018"
mergeYears=0  #used for all procs
mergeCats=0 #used for single Higgs and 12 DoubleHTag cats only, not for VBF
PAPER=0
Signal=$1
X=$2
massY=$4
DATE="06_12_2020"

#EXT="singleHiggs"$YEAR

#EXT=$1"hh"$2"_"$YEAR

INDIR="/eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/hadd_files/Run2_WS/"$Signal"_MXMgg/"$X"/"$massY"/"
OUTDIR="./output/out_fit_"${DATE}"_"$Signal$X"Y"$massY"_"$YEAR"/"
PLOTDIR="plot_dir_"$Signal$X"Y"$massY"/"
TEMPLATE="../MetaData_HHbbgg/models_2D_higgs_mx"$X".rs"  #working rather well for all qqHH and ggHH


CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"


#############SINGLE HIGGS ############
#PROCS="ggh,tth,qqh,vh,bbhyb2,bbhybyt,"$1"X"$2"ToY"$massY"H125"
PROCS=$1"X"$2"ToY"$massY"H125" 
#PROCS=$1"hh"$2
################################

set -x
for PROC in $(echo $PROCS | sed "s/,/ /g")
	do
   
		INFILEWITHYEARS=${INDIR}${PROC}'_2016.root,'${INDIR}${PROC}'_2017.root,'${INDIR}${PROC}'_2018.root'  #example if you are using merged years
		if [ $mergeCats == 1 ]; then
			if [[ $PROC == *"ggh"* ]] || [[ $PROC == *"vh"* ]] || [[ $PROC == *"tth"* ]]  || [[ $PROC == *"qqh"* ]]  ; then
				if [ $mergeYears == 1 ]; then
					./bin/MXSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} --mergeYears 2016,2017,2018 --infileWithAllYears ${INFILEWITHYEARS} -m 1 -f ${CATS} --paper ${PAPER}
				else
					./bin/MXSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} -m 1 -f ${CATS} --paper ${PAPER}
				fi
			else 
				echo "You are trying to merge categories for a single Higgs process, are you sure you want to do this??"		
			fi	
		else
			if [ $mergeYears == 1 ]; then
				./bin/MXSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} --mergeYears 2016,2017,2018 --infileWithAllYears ${INFILEWITHYEARS} -f ${CATS} --paper ${PAPER} -s ${PROC}
			else
				./bin/MXSignalFit -t ${TEMPLATE} -d ${INDIR}  -p ${PLOTDIR} -o ${OUTDIR} --procs ${PROC}   -y ${YEAR} -f ${CATS}  --paper ${PAPER} -s ${PROC} --massY $massY --massX $X
			fi
		fi	
done

set +x
