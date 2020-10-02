### Prepare data workspace ###

If you ran flashgg with dumpWorkspaces = True, you already have the workspaces in the proper form. However if you had to create trees first, you need to first convert these trees to the workspaces. For this one needs to use the following instructions from Signal folder ResHH readme file. 

### Envelope method ###
Now when you have both Data and MC workspaces ready, one can create the BG model

BG model can be obtained using envelope method. Run :
```
cd flashggFinalFit/Background
./bin/fTest -i options...
```
Plots with signal model can be created using the script *scripts/subBkgPlots.py*

To make it easier I have prepared run.sh script in Bakcground folder with the exact commands written.
Folders, names of the files, processes you want to run on have to be modified.
```
cd flashggFinalFit/Background
source run.sh $Signal ## before running adust the masses in .sh file
```
Thus it will perform bkg modeling for all masses of together in one go.
