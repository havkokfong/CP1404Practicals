

class Guitar:
    def __init__(self, name="", year=0, cost=0, age=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = age

    def get_age(self):
        age = 2017 - self.year
        self.age = age
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            return True
        else:
            return False

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)
