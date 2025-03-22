import random
import math
import numpy as np

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):

    def get_neighbors(x1, x2, step=0.1):
        return [(x1+step, x2), (x1-step, x2), (x1, x2+step), (x1, x2-step)]

    cur_p = random.uniform(bounds[0][0], bounds[0][1]), random.uniform(bounds[1][0], bounds[1][1])
    cur_v = func(cur_p)

    for _ in range(iterations):
        neighbors = get_neighbors(*cur_p, step=0.1)

        # Пошук найкращого сусіда
        next_p = None
        next_v = np.inf

        for neighbor in neighbors:
            if not all(bound[0] <= x <= bound[1] for x, bound in zip(neighbor, bounds)):
                continue

            value = func(neighbor)
            if value < next_v:
                next_p = neighbor
                next_v = value

        # Якщо не вдається знайти кращого сусіда — зупиняємось
        if abs(cur_v - next_v) < epsilon: break

        # Переходимо до кращого сусіда
        cur_p, cur_v = next_p, next_v

    return cur_p, cur_v


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6, probability=0.1):
    def get_neighbor(p, step=0.1):
        return (
            p[0] + random.uniform(-step, step),
            p[1] + random.uniform(-step, step)
        )       
    
    # Initialize random starting point
    cur_p = (random.uniform(bounds[0][0], bounds[0][1]), random.uniform(bounds[1][0], bounds[1][1]))
    cur_v = func(cur_p)

    for _ in range(iterations):
        neighbor = get_neighbor(cur_p)
        
        # Check if neighbor is within bounds
        if not all(bound[0] <= x <= bound[1] for x, bound in zip(neighbor, bounds)):
            continue
            
        value = func(neighbor)
        
        # If improvement is too small, stop
        if abs(cur_v - value) < epsilon: break
        
        # If neighbor is better, move to it
        if value < cur_v or random.random() < probability:
            cur_p = neighbor
            cur_v = value 
            
    return cur_p, cur_v


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    def get_neighbor(p, step=0.1):
        return (
            p[0] + random.uniform(-step, step),
            p[1] + random.uniform(-step, step)
        )
    
    # Initialize random starting point
    cur_p = (random.uniform(bounds[0][0], bounds[0][1]), 
             random.uniform(bounds[1][0], bounds[1][1]))
    cur_v = func(cur_p)
    best_p, best_v = cur_p, cur_v
    
    for _ in range(iterations):
        # Generate random neighbor
        neighbor = get_neighbor(cur_p)
        
        # Check if neighbor is within bounds
        if not all(bound[0] <= x <= bound[1] for x, bound in zip(neighbor, bounds)):
            continue
            
        value = func(neighbor)
        
        # Calculate acceptance probability
        delta = value - cur_v
        if delta < 0 or random.random() < math.exp(-delta / temp):
            cur_p = neighbor
            cur_v = value
            
            # Update best solution if current is better
            if cur_v < best_v:
                best_p, best_v = cur_p, cur_v
        
        # Cool down temperature
        temp *= cooling_rate
        
        # Stop if temperature is too low or improvement is too small
        if temp < epsilon or abs(delta) < epsilon:
            break
            
    return best_p, best_v


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
