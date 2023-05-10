import matplotlib.pyplot as plt

population = 2

simulation_years = 100
max_productivity = 0.5
innovation_per_person = 0.01

population_over_time = []

for i in range(1, simulation_years):
    population = population * (1 + min(max_productivity, innovation_per_person * population))
    population_over_time.append(population)

plt.plot(population_over_time)
plt.show()