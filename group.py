class Group(object):

    def __init__(self, theme):
        self.theme = theme
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def all_people(self):
        result = []
        for person in self.people:
            result.append(person.name)
        return result

    def __str__(self):
        return "Grupo: {}, pessoas {}".format(self.theme, self.people)
