from ROOT import * 

f = TFile("../zee_barrel.root")


h = f.Get("eta_reco_cat0_0")
h1 = f.Get("pt_reco_cat0_0")

h.Draw()

h1.Draw()

