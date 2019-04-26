DATE="25_04_2019"
OUTPUTDIR="output/"
OUTTAG="_SMgenerated_"$DATE
DATACARD="Datacards/cms_HHbbgg_datacard_SMgenerated_${DATE}.txt"

#combine $DATACARD -n $OUTTAG -M Asymptotic -m 125.00 --cminDefaultMinimizerType=Minuit2 -L $CMSSW_BASE/lib/$SCRAM_ARCH/libHiggsAnalysisGBRLikelihood.so   --run=expected
#mv file $OUTPUTDIR

#for node in `seq 0 -1`;
for node in SM box `seq 0 11`;
do
   datacard="Datacards/cms_HHbbgg_datacard_node${node}_${DATE}.txt"
   outtag="_node${node}_${DATE}"
	combine $datacard -n $outtag   -M Asymptotic -m 125.00 --cminDefaultMinimizerType=Minuit2 -L $CMSSW_BASE/lib/$SCRAM_ARCH/libHiggsAnalysisGBRLikelihood.so   --run=expected
   #mv file $OUTPUTDIR
done
