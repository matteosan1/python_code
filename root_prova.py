Event loop in Python
You could use a similar syntax as above for a Python event loop. But there is a much smarter way. First you create an EventTree and then access the products inside the event by EventTree.branch. Inside the loop there is no GetEntry necessary. The point here is that you don't need to define the variable beforehand and thus you don't have to know the type of the object you want to access. This makes the coding much faster. Here an example showing how it works:

from ROOT import * 
from PhysicsTools.PythonAnalysis.cmstools import *

### prepare the FWLite autoloading mechanism 
gSystem.Load("libFWCoreFWLite.so") 
AutoLibraryLoader.enable() 

# open the file and access the event tree 
events = EventTree("reco.root") 

# loop over the events 
for event in events: 
    prod = event.getProduct(productName)
    source = event.source 
    ... 
