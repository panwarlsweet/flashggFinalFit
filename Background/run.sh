DATE=02_09_2020
#DATE=22_04_2020_2

YEAR=2016_2017_2018
#YEAR=2018

############# 2D ################
addition=''
#addition=_cats90GeV
name2D=DoubleEG
#name2D=BG_MCbgbjets

name2D=${name2D}${addition}
outtag=ftest
json2D=Env_json_high.dat
input2D=output_${name2D}_${YEAR}_${DATE}.root

outputdir=plots/plots2D/${name2D}_${DATE}_${outtag}


#./bin/fTest2D -i /work/nchernya/DiHiggs/inputs/${DATE}/${input2D} --saveMultiPdf  CMS-HGG_multipdf2D_${name2D}_${outtag}_HHbbgg_${YEAR}_${DATE}.root --isData 1 -f DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11 --isFlashgg 1  -c 12 -D ${outputdir} -d ${outputdir}/res.dat --jsonForEnvelope $json2D

#./bin/fTest2D -i /work/nchernya/DiHiggs/inputs/${DATE}/Data_90GeV_Mgg_blind/${input2D} --saveMultiPdf  CMS-HGG_multipdf2D_${name2D}_${outtag}_HHbbgg_${YEAR}_${DATE}.root --isData 1 -f DoubleHTag_10,DoubleHTag_11 --isFlashgg 1  -c 1 -D ${outputdir} -d ${outputdir}/res.dat 


./bin/fTest2D -i /eos/user/l/lata/Resonant_bbgg/flattrees_L2Regression_resonant_PR1217_PR1220_16Jul2020/WED/Run2_ws_trees_PR1217_1220/Radion/RD300/DoubleEG_Run2_RD300.root  --saveMultiPdf  CMS-HGG_multipdf2D_${name2D}_${outtag}_HHbbgg_${YEAR}_${DATE}.root --isData 1 -f DoubleHTag_0,DoubleHTag_1,DoubleHTag_2 --isFlashgg 1  -c 3 -D ${outputdir} -d ${outputdir}/res.dat --jsonForEnvelope ../MetaData_HHbbgg/Env_json_02_09_2020.dat


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
plotdir='plots/plots2D/Mgg_18_02_2020/'

#./scripts/subBkgPlots2D.py -b CMS-HGG_multipdf2D_DoubleEG_cats70GeV_ftest_HHbbgg_2016_2017_2018_22_04_2020_2.root  -d ${plotdir} -S 13 --isMultiPdf   --massStep 5 -s /afs/cern.ch/work/l/lata/2Denvelop/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/out_fit_24_08_2020_2_qqHH2018/CMS-HGG_sigfit_MggMjj_2018_24_08_2020_2.root   --variableName  ${variable}   -L $low -H $high  --lowblind ${lowblind} --highblind ${highblind}   -f DoubleHTag_0,DoubleHTag_1 -l  CAT_0,CAT_1 --intLumi 136.8 --runLocal
