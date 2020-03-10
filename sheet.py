import pandas as pd
from person import Person
from group import Group


def read():
    data = pd.read_csv("files/arquivo.csv")
    people = []
    groups = []
    for person in data.values:
        preferred_groups = person[1:]
        new_person = Person(person[0])
        for person_group in preferred_groups:
            group_exists = False
            for group in groups:
                if group.theme == person_group:
                    group.add_person(new_person)
                    new_person.add_group(group)
                    group_exists = True
            if not group_exists:
                new_group = Group(person_group)
                new_group.add_person(new_person)
                new_person.add_group(new_group)
                groups.append(new_group)
        people.append(new_person)
    return people, groups


def write_results(results):
    column_person_name = [person_result.split(';')[0].strip() for person_result in results]
    column_group_theme = [person_result.split(';')[1].strip() for person_result in results]
    results_formatted = {
        'Nome ou apelido': column_person_name,
        'Tema': column_group_theme
    }
    df = pd.DataFrame(results_formatted, columns=['Nome ou apelido', 'Tema'])
    df.to_csv("files/arquivo_resultados.csv", sep='\t', encoding='utf-8', index=False, header=True)
