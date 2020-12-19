YEAR="2016_2017_2018"
DATE="06_12_2020" ## change here

INDIR="/afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/"
OUTDIR="/afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/"

CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"

#Masses="260,270,280,300,320,350"

#Masses="260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000"
Masses="300,400,500,600,800,900,1000"
massY=$2
Signal=$1  ### give signal name as an arguement
set -x

for X in $(echo $Masses | sed "s/,/ /g")
    do
    PROCS=$Signal"X"$X"ToY"$massY"H125,ggh,qqh,vh,tth,bbhyb2,bbhybyt,Radionhh"$X",BulkGravitonhh"$X
    if [ $X -gt 550 ]; then
	PROCS=$Signal"X"$X"ToY"$massY"H125,Radionhh"$X",BulkGravitonhh"$X
    fi
    python test/createMjjMggModel.py --date ${DATE} --inp-procs ${PROCS} --inp-dir ${INDIR} --inp-dir-mjj ${INDIR} --inp-file CMS-HGG_sigfit_${Signal}_Y${massY}_${DATE}.root --inp-file-mjj workspace_out_mjj_${Signal}_Y${massY}_${DATE}.root --out-dir ${OUTDIR}  --cats ${CATS}

done

set +x
