Datacard is created by running the scipt : *makeParametricModelDatacardFLASHgg.py*.

All of the commands are summarized in this bash scripts :
```
source runDatacards.sh $Signal
```

You have to specify the names of the output files with the signal model created in the 'Signal' step inside .sh file and it will pick those workspaces mass point and sigbal wise.

They will not be opened at this step of making a datacard, however the path is used in the datacard as a pointer to
the workspaces.


If btagSystematics were saved separately in flashgg with a flag 'False' passed as a third argument, care should be taken, everything is taken care of by a flag : --btagReshapeFalse.

For running the limits here is a script which makes to run for all masses very fast
```
source runLimit.sh $Signal
```
makeLimitPlot.py script can be used to make limits vs mass plot with bands.
```
python makeLimitPlot.py
```

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



