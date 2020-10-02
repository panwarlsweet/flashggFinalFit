### Running Signal and Single Higgs bkg models for Mgg: 

### First, one has to prepare a workspaces from the flashgg ntuples (trees). ### 

When running flashgg workspaces with systematics, too much memory is taken and jobs do not finish. For this reason we create flashgg trees (dumpTrees = True , dumpWorkspaces = False) and then convert them to the workspaces. If you alreeady have workspaces (dumpWorkspaces = True), then you can move on to the next step (running f-test and fit). 

In flashgg one can specify the name of the output trees. Since different years of data taking are treated differently, we need to rename the workspaces to have a year in the name. My convention names is the following : Radionhh{Mass}_2016/2017/2018 for signal (for BilkGraviton and NMSSM replace Radion) and vh2016(vh2017, vh2018), qqh(2016/2017/2018), ggh(..), tth(..), bbhyb2,bbhybyt for single higgs. Most likely you will not have the same convention in the begining, it is not a problem but you have to make sure you adjust a bit the expected names in the scripts  (will be described further).

I have updated non-res ws creating script in such a way that it will run for trees of all three years, automatically pick bTagNF from bTagSF.py file and produce ws in my eos area accoording to mass point folder (which will have MC rooworkspace files with year label)
To create workspaces from MC trees : 
```
cd flashggFinalFit/Signal/
python trees2ws_data_incl.py --inp-dir /eos/user/l/lata/Resonant_bbgg/flattrees_L2Regression_resonant_PR1217_PR1220_17Sep2020/WED/ --out-dir /eos/user/l/lata/Resonant_bbgg/flattrees_L2Regression_resonant_PR1217_PR1220_17Sep2020/WED/Run2_ws_trees_p2/ --signal Radion --doCategorization
```
note in inp-dir, I put all flashgg trees and in output dir I have mass wise signal named folder. You can change it in the script according to your convienience.
For Data use this command:
```
python data_ws.py --inp-dir /eos/user/l/lata/Resonant_bbgg/flattrees_L2Regression_resonant_PR1217_PR1220_17Sep2020/WED/Run2_Data_trees_for_ws/ --out-dir /eos/user/l/lata/Resonant_bbgg/flattrees_L2Regression_resonant_PR1217_PR1220_17Sep2020/WED/Run2_ws_trees_p2/ --signal Radion --doCategorization
```
where input directory has data root files merged for all three years according to signal and mass range. For ex. Radion low mass I have Data_Radion_lowmass.root (combining Run2 data)

You have to specify the location of the trees, the output directory, the names of the input files, etc in the . options : 
https://github.com/panwarlsweet/flashggFinalFit/blob/setup_ResHH/Signal/trees2ws_data_incl.py#L88-L100

Note that Mjj option will vary for NMSSM signal only where we have various Y mass points.

The script takes the trees with name "bbggtrees_13TeV_DoubleHTag_0" for MC and "Data_13TeV_DoubleHTag_0" for Data.

If you wish to create workspaces from the trees that are not yet categorized (doCategorization=False in flashgg), then you can use this script to create workspaces. 

Categorization should be specified here according to mass range and signal.:
https://github.com/panwarlsweet/flashggFinalFit/blob/setup_ResHH/Signal/trees2ws_data_incl.py#L126-L180
ttHKiller cut is hardcoded (0.26) for MX <550 GeV. Above 550 GeV masses SingleH backgrounds are neglected due to negligible contribution so no ttHKiller cut.

MX window cut are hardcoded here https://github.com/panwarlsweet/flashggFinalFit/blob/setup_ResHH/Signal/trees2ws_data_incl.py#L122-L123

### Now you have the workspaces ready, we can move on to the signal model. ###

First we run *signalFtest* to determine the number of gausians needed to describe signal 
(for more info see general README in Signal directory). Beware that this script is not perfect and one has to look at the plots produced.
So I have setup it like, one needs to set doFTEST=1 (other option 0) and give year, date, signal, mass point as input while running the script. 
```
source runSignalScripts_bbgg.sh 2016 $Date Radion 300
```
Once ftest is done, look at output/out_$Data_$Signal$Mass_$Year.pdf file and check all the fits. If all fits are good then we can directly go for fitting part. But if now than choose a fit to  make reftag abd refproc in the runSignalScripts_bbgg.sh and in the output/out_$Data_$Signal$Mass_$Year/dat/newConfit...dat file change number from -1 so that it could pick the fit of reftag and ref category.

We need to perform this ftest separately for Signal and Single H processes. I prefre to do it locally since it is pretty fast.

Now when FTest part is one and we have corrected all .dat file according to reference fit whereever fit is not good, our next job is to perform fit by setting the doFIT=1 and doFTest=0.

Do this fitting step very carefully, mostly be care full by adding ref proc and tag for each step. For single H process, I have updated sh script such that it takes ref process as 5th argue ment and reftag as 6th one. So I will run
```
source runSignalScripts_bbgg.sh 2016 $Date Radion 300 ttH 2
```
it takes ttH process with DoubleHTag_2 catgeory as reference fit for all other single H fits, where Ftest fails.

You do not have to use it, you can run each step one by one if you wish. I submit jobs for each process and each category, but you can run it locally by changing "--runLocal" option.

Thus Steps you need to do in order :
```
doFTEST=1
doFIT=1
merge everything in one file : python mergeWorkspaces.py final_Mgg_workspace.root all_workspaces_you_just_created.root
doPACKAGER=1 (optional, for pretty plots only)  //I don't use it for now.
```
The above script make sure you give all input properly.

Running F-test should not cause any trouble. After that you will run the fit using the optimal number of gaussians found at the previous F-test step.

if you run each category in a single job, you will have to merge the output :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/runSignalScripts_bbgg.sh#L145

It might happen that the fit fails and then the merge will fail as well. In this case, identify for which category and process it failed, check the number of gaussians from the f-test in the config, look at the plots for this category created during the f-test, and most likley you will see that it chose the wrong number of gaussians. Adjust the number of gaussian in the config, and rerun the fit.

Now if everything went well, you fill have the final workspaces(signal and single higgs) to be used for the final fit. 


### Running Signal and Single Higgs bkg models for Mjj: 
```
source runMjj_bbgg.sh Radion 300 2017
```
Theabove script performs Mjj fits for signal and singleH in one go.  
(according to year and masspoint and signal wise)

All the available options are summarized in the OptionParser : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_approval1D/Signal/test/MjjSignalFit.cpp#L70

If you want to merge datasets into 3 MVA categories to perform fits , do -m true

If you do not provide any inputs files, then the following convention will be assumed : indir_+"output_"+iproc+"_"+year_+".root";

You need to provide a template fit file :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_approval1D/Signal/test/MjjSignalFit.cpp#L75
example : https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_approval1D/MetaData_HHbbgg/models_2D_higgs_mjj70_11_02_2020.rs

Name of the input workspace is the same as for everything else in flashggFinalFits framework 'tagsDumper/cms_hgg_13TeV' : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_approval1D/Signal/test/MjjSignalFit.cpp#L141

When all fits are prepared .root files are saved. They should be merged the same way as for Mgg fits using : 
```
mergeWorkspace.py workspace_out_mjj.root *.root
```

Now we need to merge Mgg workspaces and Mjj in one final workspace file : 
```
source createMjjMggModel.sh $Signal ## Radion or BulkGraviton 
```

Done! Now you can prepare the datacards.
