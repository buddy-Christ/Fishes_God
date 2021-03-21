import aquarium
import fish

game = aquarium.Aquarium()

game.add(0, fish.StrongFish)
game.add(0, fish.Fish)
game.add(10, fish.GanniFish)


for day in range(0, 30):
    game.step()
    game.show()