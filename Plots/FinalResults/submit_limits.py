#!/usr/bin/env python

import os
import numpy
import sys
import fnmatch
from copy import deepcopy as copy
import re
import json

from optparse import OptionParser
from optparse import OptionGroup


from Queue import Queue

from threading import Thread, Semaphore
from multiprocessing import cpu_count

class Wrap:
    def __init__(self, func, args, queue):
        self.queue = queue
        self.func = func
        self.args = args
        
    def __call__(self):
        ret = self.func( *self.args )
        self.queue.put( ret  )

    
class Parallel:
    def __init__(self,ncpu):
        self.running = Queue(ncpu)
        self.returned = Queue()
        self.njobs = 0
  
    def run(self,cmd,args):
        wrap = Wrap( self, (cmd,args), self.returned )
        self.njobs += 1
        thread = Thread(None,wrap)
        thread.start()
        
    def __call__(self,cmd,args):
        if type(cmd) == str:
            print cmd
            for a in args:
                cmd += " %s " % a
            args = (cmd,)
            cmd = commands.getstatusoutput
        self.running.put((cmd,args))
        ret = cmd( *args ) 
        self.running.get()
        self.running.task_done()
        return ret


parser = OptionParser()
parser.add_option("-d","--datfile",help="Pick up running options from datfile")
parser.add_option("--cats",default="DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11", help = "categories")
parser.add_option("--channels_to_run",default="all", help = "which channels to run on")
parser.add_option("--freeze_kl_fit_params",default = "--freezeNuisances param0_DoubleHTag_0,param1_DoubleHTag_0,param2_DoubleHTag_0,param0_DoubleHTag_1,param1_DoubleHTag_1,param2_DoubleHTag_1,param0_DoubleHTag_2,param1_DoubleHTag_2,param2_DoubleHTag_2,param0_DoubleHTag_3,param1_DoubleHTag_3,param2_DoubleHTag_3,param0_DoubleHTag_4,param1_DoubleHTag_4,param2_DoubleHTag_4,param0_DoubleHTag_5,param1_DoubleHTag_5,param2_DoubleHTag_5,param0_DoubleHTag_6,param1_DoubleHTag_6,param2_DoubleHTag_6,param0_DoubleHTag_7,param1_DoubleHTag_7,param2_DoubleHTag_7,param0_DoubleHTag_8,param1_DoubleHTag_8,param2_DoubleHTag_8,param0_DoubleHTag_9,param1_DoubleHTag_9,param2_DoubleHTag_9,param0_DoubleHTag_10,param1_DoubleHTag_10,param2_DoubleHTag_10,param0_DoubleHTag_11,param1_DoubleHTag_11,param2_DoubleHTag_11")
parser.add_option("--hhReweightDir",default='/work/nchernya/DiHiggs/inputs/25_10_2019/trees/kl_kt_finebinning/',help="hh reweighting directory with all txt files" )
parser.add_option("--do_kl_scan",default=False,action="store_true",help="do kl scan?" )
parser.add_option("--do_kl_likelihood",default=False,action="store_true",help="prepare datacard for kl likelihood" )
parser.add_option("--generateAsimovHHSM",default=False,action="store_true",help="generate SM S+B HH Asimov" )
parser.add_option("-q","--queue",default='short.q',help="Which batch queue")
parser.add_option("--dryRun",default=False,action="store_true",help="Dont submit")
parser.add_option("--parallel",default=False,action="store_true",help="Run local fits in multithreading")
parser.add_option("--runLocal",default=False,action="store_true",help="Run locally")
parser.add_option("--hadd",help="Trawl passed directory and hadd files. To be used when jobs are complete.")
parser.add_option("--resubmitFailures",help=" Provide directory and the script will find failed jobs and resubmit them")
parser.add_option("-v","--verbose",default=False,action="store_true")
parser.add_option("--poix",default="r")
parser.add_option("--S0",default=False,action="store_true",help="Stats only")
parser.add_option("--batch",default="T3CH",help="Which batch system to use (LSF,IC)")
parser.add_option("--prefix",default="./")
parser.add_option("--freezeAll",default=False,action="store_true",help="Freeze all nuisances")
parser.add_option("--float",default="",action="store",help="Freeze all nuisances")
parser.add_option("--postFitAll",default=False,action="store_true",help="Use post-fit nuisances for all methods")
specOpts = OptionGroup(parser,"Specific options")
specOpts.add_option("--datacard",default=None)
specOpts.add_option("--files",default=None)
specOpts.add_option("--outDir",default=None)
specOpts.add_option("--outtag",default=None)
specOpts.add_option("--justThisSyst",default=None)
specOpts.add_option("--method",default=None)
specOpts.add_option("--label",default=None)
specOpts.add_option("--expected",type="int",default=1)
specOpts.add_option("--toysFile",default=None)
specOpts.add_option("--mh",type="float",default=None)
specOpts.add_option("--expectSignal",type="float",default=None)
specOpts.add_option("--jobs",type="int",default=None)
specOpts.add_option("--pointsperjob",type="int",default=1)
parser.add_option_group(specOpts)
(opts,args) = parser.parse_args()

allowedMethods = ['Asymptotic','MultiDimFit','GenerateOnly']

defaults = copy(opts)
print "INFO - queue ", opts.queue
def system(exec_line):
  #print "[INFO] defining exec_line"
  #if opts.verbose: print '\t', exec_line
  os.system(exec_line)


def writePreamble(sub_file):
  workdir = os.getcwd()
  #print "[INFO] writing preamble"
  sub_file.write('#!/bin/bash\n')
  if (opts.batch == "T3CH"):
      sub_file.write('set -x\n')
  sub_file.write('touch %s.run\n'%os.path.abspath(sub_file.name))
  sub_file.write('cd %s\n'%os.getcwd())
  if (opts.batch == "T3CH"):
      sub_file.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n')
      sub_file.write('source /mnt/t3nfs01/data01/swshare/glite/external/etc/profile.d/grid-env.sh\n')
      sub_file.write('export SCRAM_ARCH=slc6_amd64_gcc481\n')
      sub_file.write('export LD_LIBRARY_PATH=/swshare/glite/d-cache/dcap/lib/:$LD_LIBRARY_PATH\n')
      sub_file.write('set +x\n') 
  sub_file.write('eval `scramv1 runtime -sh`\n')
  if (opts.batch == "T3CH"):
      sub_file.write('set -x\n') 
  #sub_file.write('cd -\n')
 # if (opts.batch == "T3CH" ) : sub_file.write('cd $TMPDIR\n')
 # sub_file.write('number=$RANDOM\n')
 # sub_file.write('mkdir -p scratch_$number\n')
  #sub_file.write('cd scratch_$number\n')


def writePostamble(sub_file, exec_line,outtag):

  #print "[INFO] writing to postamble"
  sub_file.write('if ( %s ) then\n'%exec_line)
  sub_file.write('\t mv higgsCombine%s*.root %s\n'%(outtag,os.path.abspath(opts.outDir)))
  sub_file.write('\t touch %s.done\n'%os.path.abspath(sub_file.name))
  sub_file.write('else\n')
  sub_file.write('\t touch %s.fail\n'%os.path.abspath(sub_file.name))
  sub_file.write('fi\n')
  sub_file.write('rm -f %s.run\n'%os.path.abspath(sub_file.name))
  sub_file.write('rm -rf scratch_$number\n')
  sub_file.close()
  system('chmod +x %s'%os.path.abspath(sub_file.name))
  if opts.runLocal:
     system('bash %s > %s.log'%(os.path.abspath(sub_file.name),os.path.abspath(sub_file.name)))
  elif opts.queue:
    system('rm -f %s.done'%os.path.abspath(sub_file.name))
    system('rm -f %s.fail'%os.path.abspath(sub_file.name))
    system('rm -f %s.log'%os.path.abspath(sub_file.name))
    system('rm -f %s.err'%os.path.abspath(sub_file.name))
    if (opts.batch == "LSF") : system('bsub -q %s -o %s.log %s'%(opts.queue,os.path.abspath(sub_file.name),os.path.abspath(sub_file.name)))
    if (opts.batch == "IC") : system('qsub -q %s -o %s.log -e %s.err %s > out.txt'%(opts.queue,os.path.abspath(sub_file.name),os.path.abspath(sub_file.name),os.path.abspath(sub_file.name)))
    if (opts.batch == "T3CH") : 
          command = 'qsub -q %s -o %s.log -e %s.err %s > out.txt'%(opts.queue,os.path.abspath(sub_file.name),os.path.abspath(sub_file.name),os.path.abspath(sub_file.name))
          print command
          system(command)

def writeAsymptotic(jobid,card,outtag):
    print '[INFO] Writing Asymptotic'
    file = open('%s/Jobs/sub_job%d.sh'%(opts.outDir,jobid),'w')
    writePreamble(file)
    exec_line =  'combine %s/%s -n %s -M Asymptotic -m 125.00 --cminDefaultMinimizerType=Minuit2 -L $CMSSW_BASE/lib/$SCRAM_ARCH/libHiggsAnalysisGBRLikelihood.so  --rRelAcc 0.001 '%(os.getcwd(),card,outtag)
    if opts.S0: exec_line += ' -s 0 '
    if opts.expected: exec_line += ' --run=blind -t -1'
    writePostamble(file,exec_line,outtag)



def writeMultiDimFitLikelihood(card,toysFile,channels="all",kl_range="-10,15"):
    print "[INFO] writing multidim fit"
    mask_str = ""
    if channels!="all" :
       for cat in opts.cats.split(","):
         if channels != cat:
           mask_str += ",mask_%s_13TeV=1"%(cat)
    for i in range(opts.jobs):
       file = open('%s/Jobs/sub_%s_job_kl_%d.sh'%(opts.outDir,channels,i),'w')
       writePreamble(file)
       exec_line = 'combine %s/%s -M MultiDimFit --algo grid --points %s -P kl --floatOtherPOIs 0 --setPhysicsModelParameterRanges kl=%s --setPhysicsModelParameters r=1%s --firstPoint=%d --lastPoint=%d -n MultiDim_%s_%s_Job%d -L $CMSSW_BASE/lib/$SCRAM_ARCH/libHiggsAnalysisGBRLikelihood.so %s '%(os.getcwd(),card,opts.pointsperjob*opts.jobs,kl_range,mask_str,i*opts.pointsperjob,(i+1)*opts.pointsperjob-1,channels,opts.outtag,i,opts.freeze_kl_fit_params)
       if opts.S0: exec_line += ' -s 0 '
       if opts.expected: exec_line += ' -t -1 --toysFile %s'%toysFile
       writePostamble(file,exec_line,"MultiDim_%s_%s_Job%d"%(channels,opts.outtag,i))



def generateAsimovHHSM(card,channels="all"):
    print "[INFO] generating Asimov SM S+B for channels : %s"%channels
    mask_str = ""
    if channels!="all" :
       for cat in opts.cats.split(","):
         if channels != cat:
           mask_str += ",mask_%s_13TeV=1"%(cat)
    exec_line = "combine %s/%s  -M GenerateOnly -t -1 --saveToys -n SM_AsimovToy_%s_%s --setPhysicsModelParameters kl=1,r=1%s %s,kl"%(os.getcwd(),card,channels,opts.outtag,mask_str,opts.freeze_kl_fit_params)
    system(exec_line)
    system('mv higgsCombineSM_AsimovToy_*%s*.root %s\n'%(opts.outtag,os.path.abspath(opts.outDir)))
    

def checkValidMethod():
  print "[INFO] checking valid methods"
  if opts.method not in allowedMethods: sys.exit('%s is not a valid method'%opts.method)


#######################################
checkValidMethod()
system('mkdir -p %s/Jobs/'%opts.outDir)
if opts.do_kl_scan:
  counter=0
  with open(opts.hhReweightDir+"config.json","r") as rew_json:
    rew_dict = json.load(rew_json)
  for ikl in range(0,rew_dict['Nkl']):
    kl = rew_dict['klmin'] + ikl*rew_dict['klstep']
    kl_str = ("{:.6f}".format(kl)).replace('.','d').replace('-','m') 
    for ikt in range(0,rew_dict['Nkt']):
      kt = rew_dict['ktmin'] + ikt*rew_dict['ktstep']
      kt_str = ("{:.6f}".format(kt)).replace('.','d').replace('-','m') 
      hhcard_name = opts.datacard.replace('.txt','_kl_%s_kt_%s.txt'%(kl_str,kt_str))
      outtag = '_kl_%s_kt_%s'%(kl_str,kt_str)
      print "job ", counter , " , kl =  ", kl, " ,kt =  ", kt, '  outtag = ',outtag
      writeAsymptotic(counter,hhcard_name,outtag)
      counter =  counter+1
elif opts.do_kl_likelihood:
    toysFile = opts.toysFile
    kl_range = "-10,15"
    for ch in opts.channels_to_run.split(","):
       if ch!="all" : 
          toysFile = opts.toysFile.replace("all",ch)
          kl_range = "-20,20"
       writeMultiDimFitLikelihood(opts.datacard,toysFile,ch,kl_range)
elif opts.generateAsimovHHSM:
    for ch in opts.channels_to_run.split(","): 
      generateAsimovHHSM(opts.datacard,ch)
    
