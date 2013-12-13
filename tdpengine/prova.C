prova() {

  TF2* f1 = new TF2("f", "10*exp(-x*x/32) + 10*exp(-y*y/512)", -30, 30, -30, 30);
  f1->Draw("SURF");
}
