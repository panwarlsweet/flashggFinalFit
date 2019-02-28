### Running Signal and Single Higgs bkg models : 

First run F-test as descibed in the main readme.
Exmaples on the command can be found in run.sh

Then to create a signal model it is better to submit jobs since it takes a very long times. With the one job per process per category it takes about 5 minutes on the other hand.
To run jobs, modify the bash files with the processes you want to run and run it. __Important :__ Only run the first part - submitSignalFit.py. Do not run the PackageOutput one because it is messed up and will not lead to correct results.
```
source runSignalScripts_bbgg.sh
```
After the jobs are done, add them together using the following scipt : 
```
python mergeWorkspaces.py output.root input_*.root
```
You are done.
