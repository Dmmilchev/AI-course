import random
from point import Point
from copy import deepcopy
from path import Path

# random.seed(39)

class Population:
    LOWER_BOUND = 0
    UPPER_BOUND = 100
    FIRST_GENERATION_COUNT = 100
    MUTATION_PERCENT = 0.1
    
    def __init__(self, headcount: int, random=True, cities=None) -> None:
        self.N = headcount
        if random:
            self.cities, self.first_city = self._init_cities(self.N)
        else:
            self.cities: list[Point] = []
            for city in cities:
                self.cities.append(Point(x=city[1][0], y=city[1][1], name=city[0]))
            self.first_city = self.cities[0]
        self.population: list[Path] = self._init_population(Population.FIRST_GENERATION_COUNT)

    def _init_cities(self, n: int) -> list[Point]:
        cities: list[Point] = []
        for _ in range(n):
            p = Point(random.uniform(Population.LOWER_BOUND, Population.UPPER_BOUND), 
                      random.uniform(Population.LOWER_BOUND, Population.UPPER_BOUND))
            cities.append(p)
        return cities, random.choice(cities)
        
    def _init_population(self, gen_count: int) -> list[Path]:
        res: list[list[Point]] = []
        for _ in range(gen_count):
            s = deepcopy(self.cities)
            random.shuffle(s)
            s.remove(self.first_city)
            res.append(Path([self.first_city] + s))
        return res
        
    def select_parents(self) -> list[Path]:
        winners: list[Path] = []
        
        mid = len(self.population) // 2
        for i in range(mid):
            if self.population[i].distance > self.population[i + mid].distance:
                winners.append(self.population[i + mid])
            else:
                winners.append(self.population[i])
                
        return winners        
        
    def create_next_generation(self, parents: list[Path]) -> list[Path]:
        def create_children(p1: Path, p2: Path) -> tuple[Path, Path]:
            stopper = random.randint(1, len(p1.path))
            l1: list[Point] = p1.path[:stopper]
            l2: list[Point] = p2.path[:stopper]
            
            for p in p2.path:
                if p not in l1:
                    l1.append(p)
            for p in p1.path:
                if p not in l2:
                    l2.append(p)
                    
            return Path(l1), Path(l2)
        
        children: list[Path] = []
        mid = len(parents) // 2
        for i in range(mid):
            for _ in range(2):
                c1, c2 = create_children(parents[i], parents[i + mid])
                children.append(c1)
                children.append(c2)
                
        return children
    
    def mutate(self) -> None:
        def mutate_path(path: Path) -> None:
            i, j = random.randint(0, len(path.path) - 1), random.randint(0, len(path.path) - 1)
            i, j = sorted([i, j])
            path.path[i], path.path[j] = path.path[j], path.path[i]
            
        count_to_mutate = round(Population.MUTATION_PERCENT * len(self.population))
        indexes = random.sample(range(len(self.population)), count_to_mutate)
        
        for i in indexes:
             mutate_path(self.population[i])
             
    def get_the_best_of_current_population(self) -> Path:
        res: Path = None
        min = float('inf')
        
        for path in self.population:
            if min > path.distance:
                min = path.distance
                res = path
        
        return res
                 