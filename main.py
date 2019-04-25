import networkx as nx
import sheet

people, groups = sheet.read()

dict_people = {}
for person in people:
    dict_people[person.name] = person.all_groups()

capacities = {
    'Indisciplina': 6,
    'Violência Escolar e Bullying': 6,
    'Educação Sexual na Escola': 7,
    'Medicalização (TOD/TDAH)': 7,
    'Relações Raciais na Escola': 6,
    'Relações Escola e Cultura Popular': 6
}

G = nx.DiGraph()

num_persons=len(dict_people)
G.add_node('dest', demand=num_persons)
A = []
for person, projectlist in dict_people.items():
    G.add_node(person, demand=-1)
    for i, project in enumerate(projectlist):
        if i == 0:
            cost = -10  # happy to assign first choices
        elif i == 1:
            cost = -8  # slightly unhappy to assign second choices
        G.add_edge(person, project, capacity=1, weight=cost)  # Edge taken if person does this project

for project, c in capacities.items():
    G.add_edge(project, 'dest', capacity=c, weight=0)

try:
    flowdict = nx.min_cost_flow(G)

    for person in dict_people:
        for project, flow in flowdict[person].items():
            if flow:
                print(person + ';' + project)
                # pass
except Exception as e:
    print(str(e))
