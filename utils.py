from collections import OrderedDict


def most_desired_preferred_groups(people, capacity_mod):
    groups = {}
    for person in people:
        if (theme := person.preferred_group().theme) not in groups:
            groups[theme] = 1
        else:
            groups[theme] = groups[theme] + 1
    desired_by_group = OrderedDict(sorted({group: groups.get(group) for group in groups}.items(),
                                          reverse=True, key=lambda t: t[1]))
    return [group for group in desired_by_group][:capacity_mod]
