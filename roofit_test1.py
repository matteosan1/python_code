import ROOT

w = ROOT.RooWorkspace()

w.factory("PROD::model(Poisson::pois(n[61,0,100],expr::mean('a*b',a[10,0,100],b[10,0,100])),Gaussian::gaus(b_obs[5,0,100],b,3))")

w.defineSet("poi","a")
w.defineSet("np","b")
w.defineSet("obs","n,b_obs")

data = ROOT.RooDataSet("data","data",w.set("obs"))
data.add(w.set("obs"))


# Method 1. Set np to their conditional MLE values using the observed data, then calculate the expected observables
w.var("a").setVal(4)
w.var("a").setConstant(True)
w.pdf("model").fitTo(data)
w.var("a").setConstant(False)

asimov = ROOT.RooDataSet("asimov","asimov", w.set("obs"))
w.var("n").setVal(w.function("mean").getVal())
w.var("b_obs").setVal(w.function("b").getVal())
asimov.add(w.set("obs"))

# check the asimov dataset will give back a=4
w.pdf("model").fitTo(asimov)
print "Asimov designed for a=4 gave a-hat = ", w.var("a").getVal()

# Method 2. Use ExpectedData option of "generate"
w.var("a").setVal(4)

asimov2 = w.pdf("model").generate(w.set("obs"), 1, False, True, "", True)
asimov3 = w.pdf("model").generate(w.set("obs"), ROOT.RooFit.NumEvents(1), ROOT.RooFit.ExpectedData())

w.pdf("model").fitTo(asimov2)
print "Asimov2 designed for a=4 gave a-hat = ", w.var("a").getVal()

mc = ROOT.RooStats.ModelConfig(w) 
mc.SetPdf("model")
mc.SetObservables(w.set("obs"))
mc.SetParametersOfInterest(w.set("poi"))
mc.SetNuisanceParameters(w.set("np"))

asimov = ROOT.RooStats.AsymptoticCalculator.MakeAsimovData(data, mc, ROOT.RooArgSet(w.var("a"),w.var("b")), ROOT.RooArgSet())
mc.pdf("model").fitTo(asimov)
print "Asimov2 designed for a=4 gave a-hat = ", mc.var("a").getVal()
