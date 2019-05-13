### Running Signal and Single Higgs bkg models : 

First the F-test is run, once this is done you can run the signal model. If you want to include the shape systematics, you first have to run calcPhotonSystematics before going to the signal model.

Then to create a signal model it is better to submit jobs since it takes a very long times. With the one job per process per category it takes about 5 minutes on the other hand.

To run jobs, modify the bash files with the processes you want to run and run it. __Important :__  Do not run the PackageOutput for everything because it is messed up and will not lead to correct results. You can simply merge workspaces using mergeWorkspaces.py. However, packageOutput is needed to merge properly the files if you want to plot the pretty signalModel plot afterwards. Right now in the runSignalScripts_bbgg.sh script the PackageOutput is only used for SM point (taken from nodes). 
```
source runSignalScripts_bbgg.sh
```
After the jobs are done, add them together using the following scipt : 
```
python mergeWorkspaces.py output.root input_*.root
```



