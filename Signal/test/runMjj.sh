# compile
#check boost path
#export BOOST_PATH=$(scram tool info boost | awk '{  print $$2  }')

#c++ -lm -o mjj MjjSignalFit.cpp `root-config --glibs --cflags` -lRooFit -lRooFitCore -lRooStats -I /cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/boost/1.57.0-jlbgio/include/ -L/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/boost/1.57.0-jlbgio/lib/ -lboost_regex -lboost_program_options


./mjj -t models_2D_higgs_mjj70_adjusted.rs -y 2016 -d /work/nchernya/DiHiggs/inputs/04_02_2020/ 
