#include <fstream>
#include <iostream>

#include "TGraph.h"
#include "TH2D.h"
#include "TLegend.h"

void vel() {

  TH2D* h = new TH2D("h2", "h2", 100, 0, 400, 100, 0, 9000);
  TLegend* l = new TLegend(0.4,0.6,0.89,0.89);
  h->Draw();
  const char* name[6] = {"vmax_50", "vmax_50_1", "vmax_50_10", 
			 "vmax_40", "vmax_40_r1", "vmax_40_r10"};

  TGraph* graph[6];

  for(int i=0; i<6; i++) {
    int n = 0;
    float x[500], y[500], dummy;
    ifstream* fi = new ifstream(name[i]);
    
    while(!fi->eof()) {
      (*fi) >> y[n] >> dummy;
      //std::cout << x << " " << dummy << std::endl;
      n++;
      x[n] = n;
    }
    graph[i] = new TGraph(n, x, y);
    graph[i]->SetLineColor(i+2);
    graph[i]->SetLineWidth(2);
    graph[i]->Draw("SAME");
    std::cout << n << std::endl;
    l->AddEntry(graph[i], name[i], "l"); 
  }

  l->Draw("SAME");
 
}
