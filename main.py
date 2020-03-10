import networkx as nx
import sheet
from utils import most_desired_preferred_groups

people, groups = sheet.read()

dict_people = {}
for person in people:
    dict_people[person.name] = person.all_groups()

capacity_minimal = int(len(people)/len(groups))
capacity_mod = len(people) % len(groups)

capacities = {group.theme: capacity_minimal for group in groups}
for group_theme in most_desired_preferred_groups(people, capacity_mod):
    capacities[group_theme] = capacity_minimal + 1

G = nx.DiGraph()

num_persons = len(dict_people)
G.add_node('dest', demand=num_persons)
A = []
for person, group_themelist in dict_people.items():
    G.add_node(person, demand=-1)
    for i, group_theme in enumerate(group_themelist):
        if i == 0:
            cost = -10  # happy to assign first choices
        elif i == 1:
            cost = -8  # slightly unhappy to assign second choices
        G.add_edge(person, group_theme, capacity=1, weight=cost)  # Edge taken if person does this group_theme

for group_theme, c in capacities.items():
    G.add_edge(group_theme, 'dest', capacity=c, weight=0)

results = []
try:
    flowdict = nx.min_cost_flow(G)

    for person in dict_people:
        for group_theme, flow in flowdict[person].items():
            if flow:
                print(person + ';' + group_theme)
                results.append(f"{person};{group_theme}")

    sheet.write_results(results)
except Exception as e:
    print(str(e))
