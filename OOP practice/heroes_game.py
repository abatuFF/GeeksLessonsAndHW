import random

class Boss:
    def __init__(self, health):
        self.__health = health

    def get_health(self):
        return self.__health

    def attack(self, target):
        damage = random.randint(10, 20)  # Random damage between 10 and 20
        target.take_damage(damage)

    def take_damage(self, damage):
        self.__health -= damage

    def choose_perk(self):
        perks = [
            "Forbids all medics from healing allies for this round.",
            "Prevents mages from boosting their allies' damage for this round.",
            "Absorbs critical damage from warriors and increases own damage by a percentage of the absorbed damage.",
            "Removes the armor granted by berserk for one round."
        ]
        return random.choice(perks)


class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        self.__is_alive = True

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def is_alive(self):
        return self.__is_alive

    def attack(self, boss):
        pass

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.__is_alive = False

    def special_ability(self):
        pass

class Warrior(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, boss):
        damage = random.randint(15, 25)  # Random damage between 15 and 25
        boss.take_damage(damage)

    def special_ability(self):
        critical_damage = random.randint(30, 40)  # Random critical damage between 30 and 40
        return critical_damage

class Mage(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, boss):
        damage = random.randint(10, 20)  # Random damage between 10 and 20
        boss.take_damage(damage)

    def special_ability(self):
        boost_percentage = random.randint(10, 20)  # Random boost percentage between 10% and 20%
        return boost_percentage

class Berserk(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.__armor = True

    def attack(self, boss):
        damage = random.randint(12, 22)  # Random damage between 12 and 22
        boss.take_damage(damage)

    def special_ability(self):
        self.__armor = False  # Removes armor
        return None

class Medic(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, boss):
        damage = random.randint(5, 15)  # Random damage between 5 and 15
        boss.take_damage(damage)

    def special_ability(self):
        Hero.get_health += random.randint(20, 30)
        return warrior.get_health

class Second_Medic(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)


    def attack(self, boss):
        damage = random.randint(5, 15)
        boss.take_damage(damage)

    def special_ability(self):
        Hero.get_health += random.randint(20, 30)
        return Hero.get_health

# Game simulation
boss = Boss(100)
warrior = Warrior("Warrior", 50)
mage = Mage("Mage", 40)
berserk = Berserk("Berserk", 60)
medic = Medic("Medic", 30)

heroes = [warrior, mage, berserk, medic]

rounds = 1
while boss.get_health() > 0 and any(hero.is_alive() for hero in heroes):
    print(f"Round {rounds}:")
    boss_perk = boss.choose_perk()
    print(f"Boss chose the following perk for this round: {boss_perk}")

    for hero in heroes:
        if hero.is_alive():
            hero.attack(boss)

    boss.attack(random.choice(heroes))

    for hero in heroes:
        if hero.is_alive():
            print(f"{hero.get_name()} - Health: {hero.get_health()}")

    print(f"Boss - Health: {boss.get_health()}\n")
    rounds += 1

if boss.get_health() <= 0:
    print("Boss defeated! Heroes win!")
else:
    print("All heroes defeated! Boss wins!")
