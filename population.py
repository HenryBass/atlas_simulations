import matplotlib.pyplot as plt

population = 4432266
unlimited_population = 4432266

tool_human_equivilance = 101_000

simulation_years = 10000
max_growth = 0.016
max_usable_population = 10_000_000
innovation_per_person = 0.00000000002
tool_self_improvement = 0.0000000005

unlimited_population_over_time = []
population_over_time = []
tool_human_equivilance_over_time = []
net_intelligence_over_time = []

for i in range(1, simulation_years):
    tool_human_equivilance *= (1 + (tool_self_improvement * tool_human_equivilance) + (innovation_per_person * population))#(1 + min(max_growth, innovation_per_person * population))
    population *= (1 + (innovation_per_person * (min(population, max_usable_population))))#(1 + min(max_growth, innovation_per_person * population))
    unlimited_population *= (1 + innovation_per_person * population)

    print(tool_human_equivilance)

    population_over_time.append(min(population, 1e8))
    unlimited_population_over_time.append(min(unlimited_population, 1e8))
    tool_human_equivilance_over_time.append(min(tool_human_equivilance, 1e8))
    net_intelligence_over_time.append(min(tool_human_equivilance + population, 1e8))

plt.plot(population_over_time, color='red')
plt.plot(unlimited_population_over_time, color='blue')
plt.plot(tool_human_equivilance_over_time, color='green')
plt.plot(net_intelligence_over_time, color='purple')
plt.show()