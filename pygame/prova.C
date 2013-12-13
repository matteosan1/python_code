prova() {
  TH2F* h2 = new TH2F("h", "h", 200, 0, 200, 300, 100, 400);
  TLine* line = new TLine(148, 199, 127, 154);
  TLine* line2 = new TLine(43, 356, 103, 350);
  h2->Draw();
  line->Draw("SAME");
  line2->Draw("SAME");
}
