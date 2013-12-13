import chromo
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators

def eval_func(chromosome):
    score = 0.0

    # iterate over the chromosome
    for i, value in enumerate(chromosome):
        if (value == 10 and i > 5):
            score += 0.5
        elif (value == 1 and i < 6):
            score += 0.5
        else:
            score += 0
      
    return score

def run_main():
    # Genome instance
    genome = chromo.Chromo(12)

   # The evaluator function (objective function)
    genome.evaluator.set(eval_func)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)
    
   # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    ga.selector.set(Selectors.GTournamentSelector)
    ga.setGenerations(70)
    
    # Do the evolution, with stats dump
    # frequency of 10 generations
    ga.evolve(freq_stats=20)

   # Best individual
    print ga.bestIndividual()

if __name__ == "__main__":
    run_main()