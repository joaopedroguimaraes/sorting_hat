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