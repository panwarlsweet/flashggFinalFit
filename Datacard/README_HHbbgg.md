Datacard is created by running the scipt : *makeParametricModelDatacardFLASHgg.py*.
**Beware** for lumi there are options for each year, one for 2016, 2017 and one for 2018 :
*--intLumi2016*,*--intLumi2017*,*--intLumi2018*

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

ommands that I run can be found in *Datacard/run.sh*

