flashggFinalFit for ResHHbbgg
=======
Instuctions how to run FinalFit specifically for HHbbgg code. I am still running CMSSW_7_4_7. Eventually we will have to move to the newest combine. 

Main readme for flashggFinalFits can be found here : flashggFinalFit/README.md.

#### The most recent branch : setup_ResHH

For 7_4_7 CMSSW, starting from a clean area and checking out Nadya's branch :
```
cmsrel CMSSW_7_4_7
cd CMSSW_7_4_7/src
cmsenv
git cms-init
# Install Combine as per Twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHiggsAnalysisCombinedLimit#ROOT6_SLC6_release_CMSSW_7_4_X
# They recently migrated to 81X; we will follow shortly, but checkout 74X branch for now
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd ${CMSSW_BASE}/src/HiggsAnalysis/CombinedLimit
git fetch origin
git checkout origin/74x-root6
git checkout -b mybranch
cd ${CMSSW_BASE}/src
# Install the GBRLikelihood package which contains the RooDoubleCBFast implementation
git clone git@github.com:bendavid/GBRLikelihood.git HiggsAnalysis/GBRLikelihood
# Compile external libraries
cd ${CMSSW_BASE}/src/HiggsAnalysis
cmsenv
scram b -j9
# Install Flashgg Final Fit packages
cd ${CMSSW_BASE}/src/
#Git checkout Nadya's branch 
git clone -b setup_ResHH git@github.com:panwarlsweet/flashggFinalFit.git flashggFinalFit
cd ${CMSSW_BASE}/src/flashggFinalFit/
```
Two packages need to be built with their own makefiles, if needed. 
Please note that there will be verbose warnings from BOOST etc, which can be ignored. 
So long as the make commands finish without error, then the compilation happened fine.:
```
cd ${CMSSW_BASE}/src/flashggFinalFit/Background
make
cd ${CMSSW_BASE}/src/flashggFinalFit/Signal
make
```
## Contents
The FLASHgg Finals Fits package contains several subfolders which are used for the following steps:

* Create the Signal Model (see `Signal` dir)
* Create the Background Model (see `Background` dir)
* Generate a Datacard (see `Datacard` dir)
* Run `combine` and generate statistical interpretation plots. (see `Plots/FinalResults` dir)

### Each of the relevant folders are documented with specific `README_ResHHbbgg.md` files. ###

### Signal Model
__All scipts for Signal and resonant bkg (single Higgs) models are in flashggFinalFit/Signal folder__.

* By construction FinalFit requires several mass points to build a signal model, as it does extrapolation between the mass points.
We do not need this, but since the code relies on it and it is very hardcoded and difficult to change, we create these mass points 
simply by copying the workspaces and renaming them. 
* 2016, 2017, 2018 are treated as independent signals and resonant bkgs due to the difference in the resolution in 3 years. In the final fit we will only have one signal strength of course. 




### Background Model 
__All scipts for non-resonant background model are in flashggFinalFit/Background folder__.

Background model is taken from data. Discrete profiling method (envelope method) is used for the BG modeling.


### Datacards
__Datacards commands are in folder flashggFinalFit/Datacard.__


### Limits
__The scripts for final results are given in flashggFinalFit/Plots/FinalResults.__


### Yields table
For the moment, I am using a very simple script to get yields. The luminosities, SM singal xsec x BR, as well as pathes to files are hardcoded. Can be easily modified in options. 
```
python Signal/test/yields.py
```

