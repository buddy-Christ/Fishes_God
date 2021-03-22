import aquarium
import fish

game = aquarium.Aquarium()

game.add(0, fish.StrongFish)
game.add(0, fish.SimpleFish)
game.add(100, fish.GanniFish)
game.add(10, fish.ProggresiveFish)


for day in range(0, 30):
    game.step()
    game.show()