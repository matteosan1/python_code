#! /usr/bin/python
import chromo
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators

def eval_func(gen):
    pass

def run_main():
    # Genome instance
    n_gruppi = 50
    genome = chromo.Chromo(n_gruppi)

    # Check posti
    genome.c.checkPosti(n_gruppi)
    
    # The evaluator function (objective function)
    genome.evaluator.set(genome.c.eval_func)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorSwap)
    
    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    #ga.selector.set(Selectors.GTournamentSelector)
    ga.selector.set(Selectors.GRankSelector)
    ga.setGenerations(4000)
    ga.evolve(freq_stats=50)

   # Best individual
    print ga.bestIndividual()

if __name__ == "__main__":
    run_main()
