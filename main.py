class Forest:
    height = 100
    weight = 5
    age = 25
    color_list = 'green'
    breed = "oak"

    def __init__(self):
        print(Forest.height)
        print(Forest.age)
        print(Forest.weight)

tree1 = Forest()
print(tree1)


class Student:
    group = "C2013"

    def __init__(self, age, height=160):
        self.height = 150
        self.weight = 60
        self.age = age
    def printer(self):
        print(self.weight)

    def grow(self, height=10):
        self.height ++ height


