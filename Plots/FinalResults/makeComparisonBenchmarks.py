from ROOT import *
import collections 
from optparse import OptionParser

gROOT.SetBatch(kTRUE)

def setBarWidth(gr, bw, isX = True):
    for ipt in range(0, gr.GetN()):
        if isX:
            gr.SetPointEXhigh(ipt, bw)
            gr.SetPointEXlow(ipt, bw)
        else:
            gr.SetPointEYhigh(ipt, bw)
            gr.SetPointEYlow(ipt, bw)


def parseFile(filename):
    f = open(filename)
    res = collections.OrderedDict()
    for l in f:
        l = l.strip()
        if not l: continue
        if 'BENCH' in l: continue
        ## BENCH                  EXP                  OBS,              +2sigma,              +1sigma,              -1sigma,           -2sigma
        tokens = l.split()
        bn  = int(tokens[0])
        print '... parsing benchmark', bn
        exp = float(tokens[1])
        obs = float(tokens[2])
        p2s = float(tokens[3])
        p1s = float(tokens[4])
        m1s = float(tokens[5])
        m2s = float(tokens[6])

        res[bn] = (exp, obs, p2s, p1s, m1s, m2s)
    f.close()
    return res


parser = OptionParser()
parser.add_option("--indir", help="Input directory ")
parser.add_option("--outdir", help="Output directory ")
parser.add_option("--outtag", help="Output tag ")
parser.add_option("--labels", help="Labels ")
parser.add_option("--blind", help="Observed is present or not ",default=True)

(options,args)=parser.parse_args()
outtags = options.outtag.split(',')
labels = options.labels.split(',')
indirs = options.indir.split(',')

thelabsize = 0.045
## make the plot
c1 = TCanvas("cc", "cc", 650, 500)
#c1.SetLogy()
c1.cd()
c1.SetFrameLineWidth(3)
c1.SetBottomMargin (0.15)
c1.SetRightMargin (0.05)
c1.SetLeftMargin (0.15)
####### the frame
hframe = TH1F("hframe", ";Shape benchmark;95% CL on #sigma (gg#rightarrowHH) #times BR(HH#rightarrow#gamma#gammab#bar{b})  [fb]", 15, 0.01, 14.99)
hframe.SetStats(0)
# hframe.SetMinimum(1.0)
# hframe.SetMaximum(5000)
#hframe.SetMinimum(0.01)
#hframe.SetMaximum(30)
hframe.SetMinimum(0.12)
#hframe.SetMinimum(0.0)
#hframe.SetMaximum(2.6)
hframe.SetMaximum(3.6)
#hframe.GetYaxis().SetTitleSize(0.047)
hframe.GetYaxis().SetTitleSize(0.045)
hframe.GetXaxis().SetTitleSize(0.055)
hframe.GetYaxis().SetLabelSize(thelabsize)
# hframe.GetXaxis().SetLabelSize(0.045)
hframe.GetXaxis().SetLabelSize(0.00) # do by hand
hframe.GetXaxis().SetLabelOffset(0.012)
#hframe.GetYaxis().SetTitleOffset(1.15)
hframe.GetYaxis().SetTitleOffset(1.3)
hframe.GetXaxis().SetTitleOffset(1.1)

# hframe.GetXaxis().SetBinLabel(13, "a")
ttext_label = TLatex()
ttext_label.SetTextFont(42)
ttext_label.SetTextSize(thelabsize)
ttext_label.SetNDC(False)
# ttext_label.SetFillColor(kWhite)
hframe.GetYaxis().SetNdivisions(20)
hframe.GetXaxis().SetNdivisions(20)
hframe.Draw()
legend = TLegend()# cNice[ic].BuildLegend()
legend.SetLineColor(kWhite)
legend.SetBorderSize(0)
#legend.SetFillStyle(-1)

legend.SetX1(0.179012)
legend.SetY1(0.187368)
legend.SetX2(0.689815)
legend.SetY2(0.334737)

legend.SetNColumns(2)
legend.SetHeader('95% CL upper limits')
c1.SetLogy()
c1.SetGridy(1)
c1.SetGridx(1)
# pt = TPaveText(0.1663218,0.7966102,0.3045977,0.8898305,"brNDC")
pt = TPaveText(0.1663218-0.02,0.886316,0.3045977-0.02,0.978947,"brNDC")
pt.SetBorderSize(0)
pt.SetTextAlign(12)
pt.SetTextFont(62)
pt.SetTextSize(0.05)
pt.SetFillColor(0)
pt.SetFillStyle(0)
#pt.AddText("CMS #font[52]{Supplementary}" )
pt.AddText("CMS #font[52]{Preliminary}" )

off1bis = 0.065
off1bisx = 0.015
pt1Bis = TPaveText(0.1663218-0.02+off1bisx,0.886316-off1bis,0.3045977-0.02+off1bisx,0.978947-off1bis,"brNDC")
pt1Bis.SetBorderSize(0)
pt1Bis.SetTextAlign(12)
pt1Bis.SetTextFont(42)
pt1Bis.SetTextSize(0.04)
pt1Bis.SetFillColor(kWhite)
pt1Bis.SetFillStyle(0)
#pt1Bis.AddText("arXiv:XXXX.XXXXX" )


# boxBand = TLegend(0.17284, 0.791579, 0.929012, 0.894737)
boxBand = TLegend(0.17284, 0.790, 0.929012, 0.894737)
#boxBand.SetFillColor(kWhite)
boxBand.SetBorderSize(0)

# pt.AddText("#font[52]{preliminary}")
pt2 = TPaveText(0.79,0.9066667,0.8997773,0.957037,"brNDC")
pt2.SetBorderSize(0)
pt2.SetFillColor(0)
pt2.SetTextSize(0.040)
pt2.SetTextFont(42)
pt2.SetFillStyle(0)
#pt2.AddText("35.9 fb^{-1} (13 TeV)")
pt2.AddText("77.4 fb^{-1} (13 TeV)")

# pt4 = TPaveText(0.4819196,0.7780357+0.012,0.9008929,0.8675595+0.01+0.012,"brNDC")
# pt4 = TPaveText(0.4819196,0.67,0.9008929,0.77,"brNDC")
pt4 = TPaveText(0.534,0.79,0.93,0.88,"brNDC")
pt4.SetTextAlign(12)
pt4.SetFillColor(kWhite)
pt4.SetFillStyle(1001)
pt4.SetTextFont(42)
pt4.SetTextSize(0.05)
pt4.SetBorderSize(0)
pt4.SetTextAlign(32)
# pt4.AddText(channelsName[ic]) 
#pt4.AddText("HH combination") 
pt4.AddText("HH#rightarrow#gamma#gammab#bar{b}") 
# if ic == 3 : pt4.AddText("#scale[0.8]{Combined channels}")
pt.Draw()
pt2.Draw()
# pt4.Draw()
agrExp_array=[]
difference=[]
values_array = [[],[],[],[]]
for num,outtag in enumerate(outtags):

   values = parseFile('%s/benchmarks_limits_%s.txt'%(indirs[num],outtag))

   agrExp_array.append(TGraphAsymmErrors())
   agrExp = agrExp_array[num]

   for ipt in range(0, 13):  #13 = 12 nodes + 13th SM point
      bn = ipt + 1
      agrExp.SetPoint(agrExp.GetN(),    bn, values[bn][0])
      values_array[num].append(values[bn][0])

   legend.AddEntry(agrExp, "Median expected %s"%labels[num], "p")


   #setBarWidth(agr1sigma, 0.3)
   #setBarWidth(agr2sigma, 0.3)
   #setBarWidth(agrExp, 0.0)
   #setBarWidth(agrExp, 0.0, isX=False)


   agrExp.SetTitle("Expected CLs")
   if num==0 : 
     agrExp.SetMarkerStyle(20)
     agrExp.SetMarkerColor(4)
   if num==1 : 
     agrExp.SetMarkerStyle(25)
     agrExp.SetMarkerColor(1)
   agrExp.SetMarkerSize(0.8)
   agrExp.SetLineColor(4)
   agrExp.SetLineStyle(2)
   agrExp.SetFillColor(0)

   agrExp.SetMarkerSize(1.3)


   agrExp.Draw("PSAME")

for point in range(0,13): 
   difference.append((values_array[0][point] -values_array[1][point] )/values_array[0][point]  )
######################



# c1.SetTickx()
c1.SetTicky()
c1.Update()
c1.RedrawAxis();
c1.Update()
c1.RedrawAxis("g");
legend.Draw()
c1.Update()
boxBand.Draw()
pt1Bis.Draw()

#ymin_labels = 0.13
#ymin_labels = 0.006
ymin_labels = 0.1
for ival in range(0, 12):
    if ival < 9: ttext_label.DrawLatex(0.85+ival, ymin_labels, str(ival+1))
    else: ttext_label.DrawLatex(0.85+ival-0.15, ymin_labels, str(ival+1))
# ttext_label.DrawLatex(0.8+12-0.3, ymin_labels, 'k_{#lambda}=0')
# ttext_label.DrawLatex(0.8+13, ymin_labels, 'SM')
ttext_label.DrawLatex(0.8+12-0.2, ymin_labels, 'SM')
ttext_label.DrawLatex(0.8+13-0.1, ymin_labels, 'k_{#lambda}=0')


pt4.Draw()
c1.Update()
raw_input()

c1.Print('%s/benchmark_plot_%s_combined.pdf'%(options.outdir,options.outtag[0]), 'pdf')

for point in range(0,13): 
	print point+1,'\t',
print 
for point in range(0,13): 
	print round(difference[point],4),'\t',
