import random

MAXIMIZE, MINIMIZE = 11, 22

class Gruppo(object):
    persone = -1
    
    def __init__(self, persone = 10):
        self.persone = persone or self._gruppocasuale()

    def _gruppocasuale(self):
        return random.uniform(1, 20)

class Tavolo(object):
    gruppi = []
    posti = -1
    score = 0

    def __init__(self, posti=10):
        self.posti = posti
        
    def riempi(self, gruppi):
        self.gruppi = gruppi

    def evaluate(self, optimum=None):
        persone = 0
        for g in gruppi:
            persone += g.persone
        self.score = (self.posti - persone)
    
    def crossover(self, other):
        g1 = self.gruppi.pop(random.choice(range(len(self.gruppi))))
        g2 = other.gruppi.pop(random.choice(range(len(other.gruppi))))
        self.gruppi.append(g2)
        other.gruppi.append(g1)
    
    def mutate(self, gene):
        "??????????????"
        pass
    
    def __repr__(self):
        return "-".join([str(i.persone) for i in self.gruppi])
        
    def __cmp__(self, other):
        return cmp(self.score, other.score)
    
class Individual(object):
    alleles = (0,1)
    length = 30
    seperator = ''
    optimization = MINIMIZE

    def __init__(self, chromosome=None):
        self.chromosome = chromosome or self._makechromosome()
        self.score = None  # set during evaluation
    
    def _makechromosome(self):
        "makes a chromosome from randomly selected alleles."
        return [random.choice(self.alleles) for gene in range(self.length)]

    def evaluate(self, optimum=None):
        "this method MUST be overridden to evaluate individual fitness score."
        pass
    
    def crossover(self, other):
        "override this method to use your preferred crossover method."
        return self._twopoint(other)
    
    def mutate(self, gene):
        "override this method to use your preferred mutation method."
        self._pick(gene) 
    
    # sample mutation method
    def _pick(self, gene):
        "chooses a random allele to replace this gene's allele."
        self.chromosome[gene] = random.choice(self.alleles)
    
    # sample crossover method
    def _twopoint(self, other):
        "creates offspring via two-point crossover between mates."
        left, right = self._pickpivots()
        def mate(p0, p1):
            chromosome = p0.chromosome[:]
            chromosome[left:right] = p1.chromosome[left:right]
            child = p0.__class__(chromosome)
            child._repair(p0, p1)
            return child
        return mate(self, other), mate(other, self)

    # some crossover helpers ...
    def _repair(self, parent1, parent2):
        "override this method, if necessary, to fix duplicated genes."
        pass

    def _pickpivots(self):
        left = random.randrange(1, self.length-2)
        right = random.randrange(left, self.length-1)
        return left, right

    #
    # other methods
    #

    def __repr__(self):
        "returns string representation of self"
        return '<%s chromosome="%s" score=%s>' % \
               (self.__class__.__name__,
                self.seperator.join(map(str,self.chromosome)), self.score)

    def __cmp__(self, other):
        if self.optimization == MINIMIZE:
            return cmp(self.score, other.score)
        else: # MAXIMIZE
            return cmp(other.score, self.score)
    
    def copy(self):
        twin = self.__class__(self.chromosome[:])
        twin.score = self.score
        return twin


class Cena(object):
    # kind tipo di poplazione
    def __init__(self, kind, population=None, size=100, maxgenerations=100, 
                 crossover_rate=0.90, mutation_rate=0.01, optimum=None):
        self.kind = kind
        self.size = size
        self.optimum = optimum
        self.population = population # or self._makepopulation()
        for individual in self.population:
            individual.evaluate(self.optimum)
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.maxgenerations = maxgenerations
        self.generation = 0
        self.report()

    #def _makepopulation(self):
    #    return [self.kind() for individual in range(self.size)]
    
    def run(self):
        while not self._goal():
            self.step()
    
    def _goal(self):
        return (self.best.score <= self.optimum) or (self.generation >= self.maxgenerations)
    
    def step(self):
        self.population.sort()
        self._crossover()
        self.generation += 1
        self.report()
    
    def _crossover(self):
        coppie = self._select() # FIXME il numero di coppie da prendere
        offsprings = []
        for i in xrange(0, len(coppie), 2):
            mate1 = coppie[i]
            mate2 = coppie[i+1]
            if random.random() < self.crossover_rate:
                offspring = mate1.crossover(mate2)  # FIXME il crossover
            else:
                offspring = mate1
                
            #if random.random() < offspring.mutation_rate:
            #    self._mutate(offspring)

            offsprings.append(offspring)
            # sostituisci N/2 tavoli a caso fra i non migliori (i migliori sono il primo 30%)

    def _select(self, size=8):
        coppie = [random.choice(self.population) for i in range(size)]
        return coppie
    
    def _mutate(self, individual):
        pass

    
    def best(): # BU FIXME
        doc = "individual with best fitness score in population."
        def fget(self):
            return self.population[0]
        return locals()
    best = property(**best())

    def report(self):
        print "="*70
        print "generation: ", self.generation
        print "best:       ", self.best




class Environment(object):
    def __init__(self, kind, population=None, size=100, maxgenerations=100, 
                 crossover_rate=0.90, mutation_rate=0.01, optimum=None):
        self.kind = kind
        self.size = size
        self.optimum = optimum
        self.population = population or self._makepopulation()
        for individual in self.population:
            individual.evaluate(self.optimum)
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.maxgenerations = maxgenerations
        self.generation = 0
        self.report()

    def _makepopulation(self):
        return [self.kind() for individual in range(self.size)]
    
    def run(self):
        while not self._goal():
            self.step()
    
    def _goal(self):
        return self.generation > self.maxgenerations or \
               self.best.score == self.optimum
    
    def step(self):
        self.population.sort()
        self._crossover()
        self.generation += 1
        self.report()
    
    def _crossover(self):
        next_population = [self.best.copy()]
        while len(next_population) < self.size:
            mate1 = self._select()
            if random.random() < self.crossover_rate:
                mate2 = self._select()
                offspring = mate1.crossover(mate2)
            else:
                offspring = [mate1.copy()]
            for individual in offspring:
                self._mutate(individual)
                individual.evaluate(self.optimum)
                next_population.append(individual)
        self.population = next_population[:self.size]

    def _select(self):
        "override this to use your preferred selection method"
        return self._tournament()
    
    def _mutate(self, individual):
        for gene in range(individual.length):
            if random.random() < self.mutation_rate:
                individual.mutate(gene)

    #
    # sample selection method
    #
    def _tournament(self, size=8, choosebest=0.90):
        competitors = [random.choice(self.population) for i in range(size)]
        competitors.sort()
        if random.random() < choosebest:
            return competitors[0]
        else:
            return random.choice(competitors[1:])
    
    def best():
        doc = "individual with best fitness score in population."
        def fget(self):
            return self.population[0]
        return locals()
    best = property(**best())

    def report(self):
        print "="*70
        print "generation: ", self.generation
        print "best:       ", self.best


