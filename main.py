class Student:
    def __init__(self,imma):
        self.imma = imma
        self.progress = 0
        self.happiness = 50
        self.live = True

    def vchytysya(self):
        print("chas vchytysya")
        self.progress += 0.5
        self.happiness -= 2
    def spaty(self):
        print("chas spaty")
        self.spaty += 5

    def vidpochynock(self):
        print("chas chilyty")
        self.happiness += 5
        self.progress -= 0.2

    def is_alive(self):
        if self.progress < -0.5:
            self.live = False
        elif self.happiness <= 0:
            print("depression")
            self.live = False
    def and_of_day(self):
        print(f"schastya = {self.happiness}")
        print(f"progress = {self.progress}")