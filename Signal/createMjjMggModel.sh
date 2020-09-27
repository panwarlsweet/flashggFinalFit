YEAR="2016_2017_2018"
DATE="25_09_2020" ## change here

INDIR="/afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/MggMjjworkspaces/"
OUTDIR="/afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/MggMjjworkspaces/"



CATS="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2"

#Masses="260,270,280,300,320,350"

Masses="400,450,500,550,600,650,700,800,900,1000"
Signal=$1  ### give signal name as an arguement
set -x
for mass in $(echo $Masses | sed "s/,/ /g")
    do
    PROCS=${Signal}hh${mass},ggh,qqh,vh,tth,bbhyb2,bbhybyt
    if [ $mass -gt 550 ]; then
	PROCS=${Signal}hh${mass}
    fi
    python test/createMjjMggModel.py --date ${DATE} --inp-procs ${PROCS} --inp-dir ${INDIR} --inp-dir-mjj ${INDIR} --inp-file CMS-HGG_sigfit_Mgg_SingleH_${Signal}${mass}_${YEAR}_${DATE}.root --inp-file-mjj workspace_out_mjj_${Signal}${mass}_${YEAR}_${DATE}.root --out-dir ${OUTDIR}  --cats ${CATS}

done

set +x
