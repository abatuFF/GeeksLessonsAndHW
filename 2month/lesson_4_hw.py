from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    NO_DAMAGE_REVIVE = 5  # New ability for Witcher
    ATTACK_BOOST = 6  # New ability for Magic
    HACKER_ABILITY = 7  # New ability for Hacker
    GOLEM_ABILITY = 8  # New ability for Golem
    AVROA_ABILITY = 9  # New ability for Avrora
    DRUID_ABILITY = 10  # New ability for Druid


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT \
                        and self.__defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT:
                    coeff = randint(1, 2)  # 1, 2
                    hero.blocked_damage = int(self.damage / (5 * coeff))  # 5, 10
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 4)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically: {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        global round_number
        round_number += 1
        if round_number % 2 == 0:  # Increase attack every 2 rounds
            self.damage += 10
            print(f'Magic {self.name} boosted attack to {self.damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted: {self.blocked_damage}')


class Witcher(Hero):  # New hero class with NO_DAMAGE_REVIVE ability
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.NO_DAMAGE_REVIVE)
        self.revive_used = False  # Track if revive ability has been used

    def apply_super_power(self, boss, heroes):
        global round_number
        if not self.revive_used and round_number > 1:
            for hero in heroes:
                if hero.health <= 0:
                    hero.health = randint(50, 100)  # Revive with random health
                    self.health -= hero.health  # Sacrifice own health
                    self.revive_used = True
                    print(f'Witcher {self.name} sacrificed to revive {hero.name}')


class Hacker(Hero):  # New hero class with HACKER_ABILITY
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.HACKER_ABILITY)

    def apply_super_power(self, boss, heroes):
        global round_number
        if round_number % 2 == 0:  # Steal boss health every 2 rounds
            steal_amount = randint(50, 100)
            boss.health -= steal_amount
            target_hero = choice(heroes)
            target_hero.health += steal_amount
            print(f'Hacker {self.name} stole {steal_amount} health from boss and gave it to {target_hero.name}')


class Golem(Hero):  # New hero class with GOLEM_ABILITY
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.GOLEM_ABILITY)

    def apply_super_power(self, boss, heroes):
        boss.health -= int(boss.damage / 5)  # Golem takes 1/5th damage for other heroes
        print(f'Golem {self.name} took damage for other heroes: {int(boss.damage / 5)}')


class Avrora(Hero):  # New hero class with AVROA_ABILITY
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.AVROA_ABILITY)
        self.invisible = False  # Track if Avrora is invisible
        self.invisible_used = False  # Track if invisibility ability has been used

    def apply_super_power(self, boss, heroes):
        global round_number
        if not self.invisible_used and round_number > 1:
            self.invisible = True
            self.invisible_used = True
            print(f'Avrora {self.name} turned invisible')
        elif self.invisible and boss.health > 0:  # Return damage to boss if invisible
            boss.health -= self.damage
            print(f'Avrora {self.name} returned {self.damage} damage to boss')


class Druid(Hero):  # New hero class with DRUID_ABILITY
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.DRUID_ABILITY)
        self.helper_summoned = False  # Track if helper has been summoned

    def apply_super_power(self, boss, heroes):
        global round_number
        if not self.helper_summoned and round_number > 1:
            helper_type = choice(['Angel', 'Raven'])  # Randomly summon Angel or Raven
            if helper_type == 'Angel':
                medic_heroes = [hero for hero in heroes if isinstance(hero, Medic)]
                if medic_heroes:
                    medic_heroes[0].apply_super_power(boss, heroes)  # Increase medic healing
                    self.helper_summoned = True
                    print(f'Druid {self.name} summoned Angel to boost healing')
            elif helper_type == 'Raven':
                if boss.health < 500:
                    boss.damage *= 1.5  # Increase boss damage by 50% if health below 500
                    self.helper_summoned = True
                    print(f'Druid {self.name} summoned Raven to increase boss damage')


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = all(hero.health <= 0 for hero in heroes)
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Sauron', 1000, 50)

    warrior_1 = Warrior('Arthur', 280, 10)
    warrior_2 = Warrior('Ahiles', 270, 15)
    magic = Magic('Maga', 290, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    assistant = Medic('Student', 300, 5, 5)
    berserk = Berserk('Guts', 260, 10)
    witcher = Witcher('Geralt', 300, 0)  # Witcher starts with 0 damage for no boss damage ability
    hacker = Hacker('Neo', 290, 20)
    golem = Golem('Rock', 350, 8)
    avrora = Avrora('Elsa', 280, 12)
    druid = Druid('Malfurion', 270, 15)
    heroes_list = [warrior_1, doc, warrior_2, magic, assistant, berserk, witcher, hacker, golem, avrora, druid]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
