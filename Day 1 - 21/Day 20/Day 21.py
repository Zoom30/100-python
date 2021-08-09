class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super(Fish, self).breathe()
        print("We're doing this underwater")

    def swim(self):
        print("swim")


nemo = Fish()
nemo.swim()
nemo.breathe()
