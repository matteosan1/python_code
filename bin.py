import sys, math
import ROOT

pdf = ROOT.TH1F("pdf", "", 100, 0, 100)

def binPDF(n, k, p):
    global pdf
    coeff = math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
    prob = coeff*math.pow(p, k)*math.pow(1-p, n-k)
    pdf.SetBinContent(k, prob)
    return prob

n = 100
p = 0.5

prob = 0
for k in xrange(60, n+1):
    prob += binPDF(n, k, p)

print prob

c = ROOT.TCanvas("c", "c")
pdf.Draw()
c.SaveAs("binomial.png")

mean = n*p
var = n*p*(1-p)
limit = (60-mean)/math.sqrt(var)

print mean, var, math.sqrt(var), limit
print 1-ROOT.Math.gaussian_cdf(limit)
