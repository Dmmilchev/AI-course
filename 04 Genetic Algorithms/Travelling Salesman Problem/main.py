from population import Population
from load_data import load_data

RANDOM_POPULATION = True
NUMBER_OF_CITIES = 10

def main() -> None:
    
    if RANDOM_POPULATION:
        p = Population(NUMBER_OF_CITIES)

        for _ in range(NUMBER_OF_CITIES):
            parents = p.select_parents()
            next_generation = p.create_next_generation(parents)
            p.population = next_generation
            p.mutate()
            print(p.get_the_best_of_current_population().distance)
            
            
    else:
        p = Population(12, random=False, cities=load_data())

        for _ in range(12):
            parents = p.select_parents()
            next_generation = p.create_next_generation(parents)
            p.population = next_generation
            p.mutate()
            
            print(p.get_the_best_of_current_population().distance)
            
        print('The path that the algorithm found is:')
        for city in p.get_the_best_of_current_population().path:
            print(city.name)


if __name__ == '__main__':
    main()
    