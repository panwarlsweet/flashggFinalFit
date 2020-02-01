### Prepare data workspace ###

If you ran flashgg with dumpWorkspaces = True, you already have the workspaces in the proper form. However if you had to create trees first, you need to first convert these trees to the workspaces. For this one needs to use the following script : 

https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2ws_data.py
```
cd flashggFinalFit/Signal/
python trees2ws_data.py 
```
Specify input files, input dir, output dir :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2ws_data.py#L79-L82

This script relies on the fact that you start from the trees that have events already categories (DoubleHTag_0, DoubleHTag_1, DoubleHTag_2 ... DoubleHTag_11). However if you did not run the categorization, you can use this script that will perform categorization and then create a workspace. 

https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2ws_data_incl.py

Both of these scripts are basically the same,  they can be very easily merged in one by adding an option 'doCategorization' in the first one, but I have not done it yet : 
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2ws_data_incl.py#L86-L88

### Prepare MC BG workspace ###
If you wish to extract the expected limit using MC instead of data as bkg, you also need to prepare a workspace that looks like Data workspace from the MC files. We consider DiPhoton and GJets with a SF = 2.9, eachb year has to be weighted with respective lumi. weight *= lumi * SF
```
cd flashggFinalFit/Signal/
python trees2ws_data.py 
```
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2ws_mcbg_incl.py

This script relies that you start from non-categorized trees, however you can easily modify it by setting categories to something that will include everything and to make sure you look over cat names and not only start from DoubleHTag_0 tree :
By using finalname instead of initial name :
https://github.com/chernyavskaya/flashggFinalFit/blob/fullRunII_Oct2019/Signal/trees2ws_mcbg_incl.py#L147


### Envelope method ###
Now when you have both Data and MC workspaces ready, one can create the BG model

BG model can be obtained using envelope method. Run :
```
cd flashggFinalFit/Background
./bin/fTest -i options...
```
Plots with signal model can be created using the script *scripts/subBkgPlots.py*

To make life easier I have prepared run.sh script in Bakcground folder with the exact commands written.
Folders, names of the files, processes you want to run on have to be modified.
```
cd flashggFinalFit/Background
source run.sh
```
