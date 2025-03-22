# Algo2. Home work 9
## "Local Search, Heuristics, and Simulated Annealing"

### Task 

Implement a program for minimizing the [Sphere function](https://uk.m.wikipedia.org/wiki/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D1%96_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97_%D0%B4%D0%BB%D1%8F_%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%97) $f(x) = \sum^{n}_{i=1} x^{2}_{i}$ , using three different approaches to local optimization:

 - "Hill Climbing"
 - "Random Local Search"
 - "Simulated Annealing"


#### Technical Requirements

1. Function boundaries are defined as $x_i \in [-5, 5]$ for every parameter $x_i$. 

2. Algorithms must return the optimal point (list of x coordinates) and the function value at that point.

3. Implement three optimization methods:

    - `hill_climbing`
    - `random_local_search`
    - `simulated_annealing`

4. Each algorithm must accept an `iterations` parameter that defines the maximum number of iterations for algorithm execution.

5. Algorithms must terminate execution under one of the following conditions:

    - The change in the objective function value or point position in the solution space between two consecutive iterations becomes less than `epsilon`, where `epsilon` is a precision parameter that determines the algorithm's sensitivity to minor improvements.
    - For the simulated annealing algorithm, temperature is considered: if the temperature decreases to a value less than `epsilon`, the algorithm terminates, as this indicates the exhaustion of the algorithm's search capability.

#### Acceptance Criteria

 1. Algorithms operate within the specified range $x_i \in [-5, 5]$.
 2. The program finds an approximation to the global minimum of the function.
 3. Results of all three algorithms are presented in text form in a clear format.

#### Solution

The taks is implemented in file taks.py

#### Output
```
Hill Climbing:
Розв'язок: (-0.029386365795608743, -0.0187785645112363) Значення: 0.001216192979775987

Random Local Search:
Розв'язок: (0.01616362229413998, 0.08584266097355324) Значення: 0.0076302251286880195

Simulated Annealing:
Розв'язок: (0.015306282497692225, 0.0016790777365676135) Значення: 0.00023710158594459637
```