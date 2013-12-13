from pyevolve import GenomeBase
from pyevolve import Consts
from random import randint as rand_randint, uniform as rand_uniform, choice as rand_choice, sample as rand_sample
from pyevolve import Util
import container

def ChromoInitializator(genome, **args):
    genome.genomeList = rand_sample(xrange(genome.getListSize()), genome.getListSize())

def G1DBinaryStringMutatorNull(genome, **args):
    return 0

def G1DBinaryStringMutatorSwap(genome, **args):
   """ The 1D Binary String Swap Mutator """

   if args["pmut"] <= 0.0: return 0
   stringLength = len(genome)
   #mutations = args["pmut"] * (stringLength)
   mutations = 0.5 * (stringLength)
   if mutations < 1.0:
      mutations = 0
      for it in xrange(stringLength):
         if Util.randomFlipCoin(args["pmut"]):
            Util.listSwapElement(genome, it, rand_randint(0, stringLength-1))
            mutations+=1

   else:
      for it in xrange(int(round(mutations))):
         Util.listSwapElement(genome, rand_randint(0, stringLength-1),
                                      rand_randint(0, stringLength-1))

   return int(mutations)

def G1DBinaryStringMutatorFlip(genome, **args):
   """ The classical flip mutator for binary strings """
   if args["pmut"] <= 0.0: return 0
   stringLength = len(genome)
   mutations = args["pmut"] * (stringLength)
   
   if mutations < 1.0:
      mutations = 0
      for it in xrange(stringLength):
         if Util.randomFlipCoin(args["pmut"]):
            if genome[it] == 0: genome[it] = 1
            else: genome[it] = 0
            mutations+=1

   else:
      for it in xrange(int(round(mutations))):
         which = rand_randint(0, stringLength-1)
         if genome[which] == 0: genome[which] = 1
         else: genome[which] = 0

   return int(mutations)

def G1DBinaryStringXSinglePoint(genome, **args):
#   """ The crossover of 1D Binary String, Single Point
#
#   .. warning:: You can't use this crossover method for binary strings with length of 1.
#
#   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   if len(gMom) == 1:
      Util.raiseException("The Binary String have one element, can't use the Single Point Crossover method !", TypeError)

   cut = rand_randint(1, len(gMom)-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.resetStats()
      sister[cut:] = gDad[cut:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.resetStats()
      brother[cut:] = gMom[cut:]

   Pruner(sister)
   Pruner(brother)
   #print "\tsister :\t\t %s\n\n" % (sister.getBinary(),)
   #print "\tbrother:\t\t %s\n\n" % (brother.getBinary(),)
   return (sister, brother)

def Pruner(genome):
    missing = []
    doubles = []
    for i in xrange(genome.getListSize()):
        c = genome.genomeList.count(i)
        if (c == 0):
            missing.append(i)
        if (c > 1):
            doubles.append(i)
    
    for d in doubles:
        indices = [i for i,j in enumerate(genome) if (j == d)]
        for i in indices[1:]:
            y = rand_choice(xrange(len(missing)))
            genome[i] = missing[y]
            missing.remove(missing[y])


def G1DBinaryStringXTwoPoint(genome, **args):
   """ The 1D Binary String crossover, Two Point

   .. warning:: You can't use this crossover method for binary strings with length of 1.

   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   
   if len(gMom) == 1:
      Util.raiseException("The Binary String have one element, can't use the Two Point Crossover method !", TypeError)

   cuts = [rand_randint(1, len(gMom)-1), rand_randint(1, len(gMom)-1)]

   if cuts[0] > cuts[1]:
      Util.listSwapElement(cuts, 0, 1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.resetStats()
      sister[cuts[0]:cuts[1]] = gDad[cuts[0]:cuts[1]]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.resetStats()
      brother[cuts[0]:cuts[1]] = gMom[cuts[0]:cuts[1]]

   return (sister, brother)

def G1DBinaryStringXUniform(genome, **args):
   """ The G1DList Uniform Crossover """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   sister = gMom.clone()
   brother = gDad.clone()
   sister.resetStats()
   brother.resetStats()

   for i in xrange(len(gMom)):
      if Util.randomFlipCoin(Consts.CDefG1DBinaryStringUniformProb):
         temp = sister[i]
         sister[i] = brother[i]
         brother[i] = temp
            
   return (sister, brother)

class Chromo(GenomeBase.GenomeBase, GenomeBase.G1DBase):
    initializator = None
    mutator = None
    crossover = None
    evaluator = None
    c = container.Container()

    def __init__(self, length=10):
        GenomeBase.GenomeBase.__init__(self)
        GenomeBase.G1DBase.__init__(self, length)
        self.genomeList = []
        self.genomeSize = length
        self.initializator.set(ChromoInitializator)
        self.mutator.set(G1DBinaryStringMutatorNull)
        self.crossover.set(G1DBinaryStringXSinglePoint)

    def __setitem__(self, key, value):
        #if value not in (0, 1):
        #    Util.raiseException("The value must be zero (0) or one (1), used (%s)" % value, ValueError)
        GenomeBase.G1DBase.__setitem__(self, key, value)

    def __repr__(self):
        ret = ""
        #ret = GenomeBase.GenomeBase.__repr__(self)
        #ret += "- Chromo\n"
        ret += "\tString length:\t %s\n" % (self.getListSize(),)
        ret += "\tIndice:\t\t %s\n\n" % (self.getBinary(),)
        ret += "\tGruppi:\t\t %s\n\n" % (self.getGruppi(),)
        ret += "\tScore : %d" % (self.c.eval_func(self))
        return ret

    def getGruppi(self):
        l = list(self)
        a = [str(self.c.mappa[i]) for i in l]
        m = self.c.matchTavGru(l)
        s = "\n"
        for i, t in enumerate(self.c.tavoli):
            s = s + "Tavolo: " + str(t) + " " 
            
            s = s + str(m[i]) + "\n"
        print s
        return ".".join(a) 

    def getDecimal(self):
        return int(self.getBinary(), 2)

    def getBinary(self):
        return ".".join(map(str, self))

    def append(self, value):
        if value not in [0, 1]:
            Util.raiseException("The value must be 0 or 1", ValueError)
        GenomeBase.G1DBase.append(self, value)

    def copy(self, g):
        GenomeBase.GenomeBase.copy(self, g)
        GenomeBase.G1DBase.copy(self, g)
   
    def clone(self):
        newcopy = Chromo(self.getListSize())
        self.copy(newcopy)
        return newcopy

