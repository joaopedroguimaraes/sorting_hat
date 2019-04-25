class Person(object):

    def __init__(self, name):
        self.name = name
        self.preferred_groups = []

    def add_group(self, group):
        self.preferred_groups.append(group)

    def all_groups(self):
        result = []
        for group in self.preferred_groups:
            result.append(group.theme)
        return result

    def __str__(self):
        return "Pessoa: {}, grupos {}".format(self.name, self.preferred_groups)