YEAR="2016_2017_2018"
DATE="27_12_2020" ## change here

INDIR="/afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/"
OUTDIR="/afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/"

CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"
Masses="260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000"
#Masses="300,400,500,600,800,900,1000"
massY=$2
Signal=$1  ### give signal name as an arguement
set -x
for X in $(echo $Masses | sed "s/,/ /g")
do
    if [ "$Signal" == "NMSSM" ]; then
	check=$((${X}-$massY-125))
	echo ${check}
	if [ "${check}" -lt 0 ]; then
	    continue;
	else
	    if [ $massY == 125 ]; then
		PROCS=$Signal"X"$X"ToY"$massY"H125,ggh,tth,qqh,vh,bbhyb2,bbhybyt"
		if [ $X -gt 550 ]; then
	            PROCS=$Signal"X"$X"ToY"$massY"H125"
		    #,Radionhh"$X",BulkGravitonhh"$X 
		fi
	    else
		PROCS=$Signal"X"$X"ToY"$massY"H125,ggh,tth,qqh,vh,bbhyb2,bbhybyt"
		if [ $X -gt 550 ] || [ $massY -gt 250 ]; then
	            PROCS=$Signal"X"$X"ToY"$massY"H125"
		fi
	    fi
	    python test/createMjjMggModel.py --date ${DATE} --inp-procs ${PROCS} --inp-dir ${INDIR} --inp-dir-mjj ${INDIR} --inp-file CMS-HGG_sigfit_${Signal}_X${X}Y${massY}_${DATE}.root --inp-file-mjj workspace_out_mjj_${Signal}_X${X}Y${massY}_${DATE}.root --out-dir ${OUTDIR}  --cats ${CATS}
	fi
    else
	DATE="18_01_2021"
	PROCS="Radionhh"$X",BulkGravitonhh"$X",ggh,tth,qqh,vh,bbhyb2,bbhybyt"
	if [ $X -gt 550 ]; then
	    PROCS="Radionhh"$X",BulkGravitonhh"$X
	fi
	python test/createMjjMggModel.py --date ${DATE} --inp-procs ${PROCS} --inp-dir ${INDIR} --inp-dir-mjj ${INDIR} --inp-file CMS-HGG_sigfit_WED_X${X}_${DATE}.root --inp-file-mjj workspace_out_mjj_WED_X${X}_${DATE}.root --out-dir ${OUTDIR}  --cats ${CATS}
	
    fi
done

set +x

