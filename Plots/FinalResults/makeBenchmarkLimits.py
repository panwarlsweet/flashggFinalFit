import ROOT
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend,TH1F
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
from optparse import OptionParser

import CMSlumi as CMS_lumi
import tdrstyle

# CMS style
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = True
tdrstyle.setTDRStyle()



# GET limits from root file
def getLimits(file_name):

    file = TFile(file_name)
    tree = file.Get("limit")

    limits = [ ]
    for quantile in tree:
        limits.append(tree.limit)
        print ">>>   %.2f" % limits[-1]

    return limits[:6]


# PLOT upper limits
def plotUpperLimits(labels,values,axis_labels):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    
    N = len(labels)
    yellow = TGraph(2*N)    # yellow band
    green = TGraph(2*N)     # green band
    median = TGraph(N)      # median line

    up2s = [ ]
    for i in range(N):
        file_name = options.indir+"/higgsCombine_"+labels[i]+"_"+options.outtag+".Asymptotic.mH125.root"
        limit = getLimits(file_name)
        up2s.append(limit[4])
        yellow.SetPoint(    i,    values[i], limit[4] ) # + 2 sigma
        green.SetPoint(     i,    values[i], limit[3] ) # + 1 sigma
        median.SetPoint(    i,    values[i], limit[2] ) # median
        green.SetPoint(  2*N-1-i, values[i], limit[1] ) # - 1 sigma
        yellow.SetPoint( 2*N-1-i, values[i], limit[0] ) # - 2 sigma

    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.04*W
    c = TCanvas("c","c",100,100,W,H)
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetGrid()
    c.cd()
    frame = c.DrawFrame(1.4,0.001, 4.1, 10)
   # frame = TH1F("frame","frame",1,0,14)
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.04)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetTitleOffset(0.9)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetTitle("95% CL on #sigma (pp #rightarrow HH) #times BR(HH #rightarrow #gamma#gamma b#bar{b}) [fb]")
    frame.GetXaxis().SetTitle("Shape benchmark")
    frame.SetMinimum(0)
    frame.SetMaximum(max(up2s)*1.05)
    frame.GetXaxis().SetLimits(min(values),max(values))
    for i in range(0,len(axis_labels)):
        frame.GetXaxis().SetBinLabel(i+1,axis_labels[i])

    yellow.SetFillColor(ROOT.kOrange)
    yellow.SetLineColor(ROOT.kOrange)
    yellow.SetFillStyle(1001)
    yellow.Draw('F')
    
    green.SetFillColor(ROOT.kGreen+1)
    green.SetLineColor(ROOT.kGreen+1)
    green.SetFillStyle(1001)
    green.Draw('Fsame')

    median.SetLineColor(1)
    median.SetLineWidth(2)
    median.SetLineStyle(2)
    median.SetMarkerStyle(24)
    median.Draw('Psame')

    CMS_lumi.CMS_lumi(c,14,11)
    ROOT.gPad.SetTicks(1,1)
    frame.Draw('sameaxis')

    x1 = 0.15
    x2 = x1 + 0.24
    y2 = 0.76
    y1 = 0.60
    legend = TLegend(x1,y1,x2,y2)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.041)
    legend.SetTextFont(42)
    legend.AddEntry(median, "Median expected",'L')
    legend.AddEntry(green, "#pm 1 std. deviation",'f')
    legend.AddEntry(yellow,"#pm 2 std. deviation",'f')
    legend.Draw()

    print " "
    c.SaveAs(options.outdir+"/UpperLimitBenchmarks_%s.png"%options.outtag)
    c.SaveAs(options.outdir+"/UpperLimitBenchmarks_%s.pdf"%options.outtag)
    c.Close()

def frange(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step


# MAIN
parser = OptionParser()
parser.add_option("--indir", help="Input directory ")
parser.add_option("--outdir", help="Output directory ")
parser.add_option("--outtag", help="Output tag ")

(options,args)=parser.parse_args()


labels = [] 
axis_labels = [] 
values = [ ]
for node in range(0,12):
   values.append(node+1)
   label = "node%d"%node
   labels.append(label)
   axis_labels.append("%d"%node)
values.append(13)
labels.append("SM")
axis_labels.append("SM")

plotUpperLimits(labels,values,axis_labels)

