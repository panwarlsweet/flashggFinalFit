DATE=27_12_2020

#2_04_2020_2

YEAR=2016_2017_2018
#YEAR=2018

############# 2D ################
addition=''
#addition=_cats90GeV
name2D=DoubleEG
#name2D=BG_MCbgbjets

name2D=${name2D}${addition}
#outtag=ftest_$1$2
json2D=Env_json_high.dat
input2D=output_${name2D}_${YEAR}_${DATE}.root

#Masses="260,300,350"
#Masses="260,270,280,300,320,350,400,450,500,550,600,650,700,800,900,1000"
Signal=$1  ### give signal name as an arguement 
massY=$2
#if [ $Signal -eq "NMSSM" ];then
Masses="300,400,500,600,700,800,900,1000"
#fi
set -x
for mass in $(echo $Masses | sed "s/,/ /g")
    do
    check=$((${mass}-$massY-125))
    echo ${check}
    if [ "${check}" -lt 0 ]; then
        continue;
    else
	if [ "${Signal}" == "NMSSM" ]; then
	    outtag=ftest_${Signal}_X${mass}_Y$massY 
	    outputdir=plots/plots2D/${name2D}_${DATE}_${outtag}
	else
	    outtag=ftest_WED_X${mass}
	    outputdir=plots/plots2D/${name2D}_${DATE}_${outtag}
	fi
	./bin/fTest2D -i /eos/user/l/lata/Resonant_bbgg/flattrees_NMSSM_fromjobs/hadd_files/Run2_WS/$Signal/$mass/$massY/${name2D}.root  --saveMultiPdf  CMS-HGG_multipdf2D_${name2D}_${outtag}_HHbbgg_${YEAR}_${DATE}.root --isData 1 -f DoubleHTag_0,DoubleHTag_1,DoubleHTag_2 --isFlashgg 1  -c 3 -D ${outputdir} -d ${outputdir}/res.dat --massY $massY
    fi
    done
set +x

##Plots
#lowblind=105
#highblind=145
#low=70
#high=190
#variable='Mjj'
#plotdir='plots/plots2D/Mjj_18_02_2020/'

lowblind=115
highblind=135
low=100
high=180
variable='CMS_hgg_mass'
plotdir='plots/plots2D/'
DATA="../Datacard/final_worskpaces/CMS-HGG_multipdf2D_DoubleEG_ftest_Radion260_HHbbgg_2016_2017_2018_25_09_2020.root"
SIG="../Datacard/final_worskpaces/CMS-HGG_sigfit_MggMjj_2016_2017_2018_25_09_2020_Radionhh260.root"

#./scripts/subBkgPlots2D.py -b ${DATA} -d ${plotdir} -S 13 --isMultiPdf   --massStep 5 -s ${SIG}   --variableName  ${variable}   -L $low -H $high  --lowblind ${lowblind} --highblind ${highblind}   -f DoubleHTag_0 -l  CAT0 --intLumi 137 --runLocal 
