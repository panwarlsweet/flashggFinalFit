DATE="27_12_2020"
YEAR="2016_2017_2018"
YEAR=2018
#YEAR=""
#YEAR2=2016
X_points="300,400,500,600,800,900,1000"
Y_points="90,100,125,150,200,250,300,400,500,600,700,800"
set -x
for X in $(echo $X_points | sed "s/,/ /g")
do
    for Y in $(echo $Y_points | sed "s/,/ /g")
    do
	check=$((${X}-$Y-125))
	echo ${check}
	if [ "${check}" -lt 0 ]; then
	    continue;
	else
	    for cat in {0..2}
	    do
	    
	    ./bin/makeParametricSignalModelPlots -i output/out_fit_${DATE}_NMSSMX${X}ToY${Y}H125_${YEAR}/CMS-HGG_sigfit_NMSSMX${X}ToY${Y}H125_${YEAR}_NMSSMX${X}ToY${Y}H125_${YEAR}_DoubleHTag_$cat.root -o plots -p NMSSMX${X}ToY${Y}H125_${YEAR} -f DoubleHTag_$cat
	    if [ $Y == 125 ]; then
		./bin/makeParametricSignalModelPlots -i output/out_fit_${DATE}_Radionhh${X}_${YEAR}/CMS-HGG_sigfit_Radionhh${X}_${YEAR}_Radionhh${X}_${YEAR}_DoubleHTag_$cat.root -o plots -p Radionhh${X}_${YEAR} -f DoubleHTag_$cat
		./bin/makeParametricSignalModelPlots -i output/out_fit_${DATE}_BulkGravitonhh${X}_${YEAR}/CMS-HGG_sigfit_BulkGravitonhh${X}_${YEAR}_BulkGravitonhh${X}_${YEAR}_DoubleHTag_$cat.root -o plots -p BulkGravitonhh${X}_${YEAR} -f DoubleHTag_$cat 
	    fi
	    done
	fi
    done
done
set +x
output/out_fit_27_12_2020_Radionhh300_2018/CMS-HGG_sigfit_Radionhh300_2018_Radionhh300_2018_DoubleHTag_0.root
