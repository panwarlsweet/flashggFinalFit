## Running limits and making plots

To run Asymptotic to get upper limits for all benchmarks and SM:
```
source run.sh
```
In the future I will use combineHarverster, but for now job submission does not work out of the box. I will investigate.

To make plot with U.L. on x-sec times BR for all benchmark plus SM :
First prepare a .txt files with all limits from the combine .root files from previous step of running Asymptotic:
```
python prepareBenchmarkOutput.py --indir output/Limits_21_02_2019/ --outdir plots/ --outtag 21_02_2019
```
Then to make the plot:
```
python makePlotBenchmarks_withSMBox_2016Comb.py --indir output/Limits_21_02_2019/ --outdir plots/ --outtag 21_02_2019
```

To compare the limits (for now only 2 inputs are supported -> but very easily extendable for more):
```
python  makeComparisonBenchmarks.py --indir 'output/Limits_27_03_2019/,output/Limits_21_02_2019/' --outtag '27_03_2019,21_02_2019'  --outdir output/Limits_27_03_2019/ --labels 'with Mjj,w/o Mjj'
```
