Datacard is created by running the scipt : *makeParametricModelDatacardFLASHgg.py*.

All of the commands are summarized in this bash scripts :
```
source runDatacards.sh
```
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh

You have to specify the names of the output files with the signal model created in the 'Signal' step :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L12

They will not be opened at this step of making a datacard, however the path is used in the datacard as a pointer to
the workspaces.

With systematics or without ?
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L2

If btagSystematics were saved separately in flashgg with a flag 'False' passed as a third argument, care should be taken, everything is taken care of by a flag : --btagReshapeFalse.

If runnning with systematics you need to put a file with all workspaces (for HH and single H processes and all systematics,
either you have it from flashgg ntuples (workspaces) and you just need to merge it using a flashgg command :
```
hadd_workspaces final_output.root *.root 
```
Or you created this file in the 'Signal' Model step. You probably also need to merge all the relevant created files into one :
```
hadd_workspaces final_output.root output_hh*.root output_qqh*.root output_ggh*.root output_vh*.root output_tth*.root
```

One can prepare several different datacards :

- 2D or 1D fit, default is 1D, if want 2D do : --do2D 
- SM datacard
  https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L36
- datacards for kl scan :
  https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L49-L55
  However for this step you need to prepare the reweighting SF. This will be elaborated upon further down.
- datacards for BSM benchmarks :  
  However for this step you need to prepare the reweighting SF. This will be elaborated upon further down.
  https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L58-L64
- datacards for kl likelihood extraction  :  
  https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L68-L74
   This will be elaborated upon further down.
- datacards to run expected with BG MC instead of data
  https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L77-L86
  Using the bkg model created for BG in the 'Background' step


###  kl scan, BSM benchmarks, likelihood ###

## kl scan and limits on the BSM benchmarks ##

We have already prepared a SM datacard. Now in order to be able to run a kl scan (set upper limits for different values of kappa lambda), one has to reweight event yield in each category (DoubleHTag_0,..., DoubleHTag_11) to the event yields that are expected for a given value of kl or for a given BSM benchmark (12 benchmarks + box diagram whn kl = 0).

To do so we have a simple and a very fast script : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/HHreweighter/runHHReweighterNodes.cpp

This script will be eventually substituted by a better one (we already have it written by Fabio Monti, but we still need to test it for certain scenarios).

This script will take the doubleH ntuple (already categoriezed tree with both gen and reco information. In flashgg terms both reco and gren trees have to be present : tagsDumper/trees and genDiphotonDumper/trees). To be able to get the gen info in the trees one has to run flashgg ntuples with these commands :
```
doDoubleHGenAnalysis=True doubleHReweight=1 ForceGenDiphotonProduction=True
```
If you do have both gen and reco trees present, but without categorization, it is not a problem, you can categorize them first using this script : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2cats.py
```
cd flashggFinalFit/Signal/
python trees2cats.py --doCategorization=True --add_gen = True --year = 2016/7/8
```
Now run the reweighting script with the grid of kl that you would like to see :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/HHreweighter/runHHReweighterNodes.cpp#L23-L30
```
c++ -lm -o runNodes runHHReweighterNodes.cpp HHReweight5D.cpp `root-config --glibs --cflags`
./runNodes
```
This script has all input files, kl grid hardcoded, which is very suboptimal, however, since we will substitute this script with a better one in a very near future, for now one can use this one. kt = 1 should be always 1, because to do a 2D kl-kt scan we will use the other script (Fabio).

Specify the same maps as specified in the flashgg : 
https://github.com/cms-analysis/flashgg/blob/dev_legacy_runII/MetaData/data/MetaConditions/Era2016_RR-17Jul2018_v1.json#L190

https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/HHreweighter/runHHReweighterNodes.cpp#L34-L36

This coefficient file is needed for the reweighting :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/HHreweighter/runHHReweighterNodes.cpp#L43
 and can be found here : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/MetaData_HHbbgg/coefficientsByBin_extended_3M_costHHSim_19-4.txt

This script will create .txt files with the reweighting needed per category for each kl point and for 15 BSM points (12 nodes + SM + box + fake2017 (not needed, should be ignored)).

Now you should create a short config with the kl grid info, example : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/MetaData_HHbbgg/config.json

__Now you are ready to create datacards for the kl points and for BSM benchmarks__ 
Specify the directory with the .txt files and the config :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L50
Use these options to specify the name of SM datacard to start from, the config for the reweighting files and the directory where they are :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/makeParametricModelDatacardFLASHgg.py#L137-L140


## kl likelihood ##
For the kl likelihood one needs to use the reweighting files created in the previous step for different values of kl. Then preform a parabolic fit in each category :

```
cd flashggFinalFit/Plots/FinalResults
python extract_kl_param.py --outdir plots --outtag 25_10_2019_fineklbinning
```
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Plots/FinalResults/extract_kl_param.py

Specify the directory where the reweighting .txt files are located (kl reweighting from the previous step) :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Plots/FinalResults/extract_kl_param.py#L31

This script will produce a fit, save a plot and results as config file with a name : out_name+"_fitparams.json"

We need this output file to create datacard to be able to get a kl likelihood : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/makeParametricModelDatacardFLASHgg.py#L141-L142
Run : https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Datacard/runDatacards.sh#L68-L74




