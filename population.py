import matplotlib.pyplot as plt

population = 4432266
unlimited_population = population

tool_human_equivilance = 101_000

simulation_years = 17000
max_growth = 0.016
max_usable_population = 10_000_000
innovation_per_person = 0.00000000002
net_intelligence = tool_human_equivilance + population

unlimited_population_over_time = []
population_over_time = []
tool_human_equivilance_over_time = []
net_intelligence_over_time = []

for i in range(1, simulation_years):
    tool_human_equivilance *= (1 + innovation_per_person * net_intelligence)
    population *= (1 + (innovation_per_person * (min(population, max_usable_population))))
    unlimited_population *= (1 + innovation_per_person * population)
    net_intelligence = tool_human_equivilance + population

    print(tool_human_equivilance)

    population_over_time.append(min(population, 1e8))
    unlimited_population_over_time.append(min(unlimited_population, 1e8))
    tool_human_equivilance_over_time.append(min(tool_human_equivilance, 1e8))
    net_intelligence_over_time.append(min(net_intelligence, 1e8))

plt.plot(population_over_time, color='red')
plt.plot(unlimited_population_over_time, color='lightgray')
plt.plot(tool_human_equivilance_over_time, color='green')
plt.plot(net_intelligence_over_time, color='purple')
plt.show()