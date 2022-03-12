################### 8.  PROGRAM BERORIENTASI OBJEK ##########
class Hero:
    def __init__(self):
        self.name = 'Meepo'
        self.strength = 300
        self.agility = 400
        self.inteligent = 200
        self.level = 1

    def attack(self):  # Method
        print('Smash!!!')


hero1 = Hero()
hero1.attack()
print(hero1.name)

# ############## coba

print(hero1.strength)
print(hero1.level)