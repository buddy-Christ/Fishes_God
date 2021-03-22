import random

class Fish:
    __age = 0
    __sex = "Unknown"
    __color = ""

    def color(self):
        return self.__color

    def sex(self):
        return self.__sex

    def __init__(self):
        if random.randint(1, 10) > 5:
            self.__sex = "Male"
        else:
            self.__sex = "Female"
        self.__age = random.randint(10,15)


    def step(self):
        if self.__age > 0:
            self.__age = self.__age - 1

    def isAlive(self):
        if self.__age > 0:
            return True
        else:
            return False

    def isEaten(self):
        if self.__age == -1:
            return True
        else:
            return False

    def canMakeNewFish(self):
        if self.__age > 9:
            return True
        else:
            return False


    def canBeEaten(self):
        if self.__age < 3:
            return True
        else:
            return False
    
    def canEat(self):
        return False

    def youAreEaten(self):
        self.__age = -1

    def eat(self, firstFish):
        if self.canEat() == True:
            if firstFish.canBeEaten() == True:
                if not (self is firstFish):
                    if firstFish.isAlive() == True:
                        firstFish.youAreEaten()

    @classmethod
    def born(cls, dad, mom):
        children = []
        if dad.canMakeNewFish() and mom.canMakeNewFish() and dad.sex() != mom.sex() and dad.__class__ == mom.__class__:
            for i in range(0, random.randint(0, 4)):
                children.append(mom.__class__())
        return children
          


class StrongFish(Fish):
    color = "Red"
    def canMakeNewFish(self):
        return True

class GanniFish(Fish):
    color = "Black"
    def canEat(self):
        return True
    def canBeEaten(self):
        return False

class SimpleFish(Fish):
    color = "Green"
    def canEat(self):
        return False

class ProggresiveFish(Fish):
    color = "Afro-American"
    def canBeEaten(self):
        return True

class SubmarineFish(Fish):
    color = "Yellow"