import random
import fish



class Aquarium:
    __day = 1
    __fishes = []

    def add(self, fishCount, fishClass):
        for i in range(0, fishCount):
            self.__fishes.append(fishClass())



    def step(self):
        newFishes = []
        for i in range(0, len(self.__fishes)):
            self.__fishes[i].step()
            first = random.randint(0,len(self.__fishes)-1)
            second = random.randint(0,len(self.__fishes)-1)
            newFishes = newFishes + fish.Fish.born(self.__fishes[first], self.__fishes[second])
        self.__fishes = self.__fishes + newFishes
        #for eat
        for i in range(0, len(self.__fishes)):
            first = random.randint(0,len(self.__fishes)-1)
            self.__fishes[i].eat(self.__fishes[first])



    def show(self):
        males = 0
        females = 0
        dead = 0
        eaten = 0
        for i in range(0, len(self.__fishes)):
            if self.__fishes[i].isAlive():
                if self.__fishes[i].sex() == "Male":
                    males = males + 1
                else:
                    females = females + 1
            else:
                dead = dead + 1
            if self.__fishes[i].isEaten():
                eaten += 1


        print("Day", self.__day, "\t   Males:", males, "\t   Females:", females, "\t   Dead:", dead, "\t Eaten", eaten)
        self.__day = self.__day + 1

