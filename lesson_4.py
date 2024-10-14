from random import randint, choice, random


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
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

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

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage



class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')



class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero.damage > 0:
                hero.damage += 2
        print(f'Magic {self.name} boosted heroes damage on 2.')



class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value



class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points



class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'RESURRECTION')

    def apply_super_power(self, boss, heroes_list):
        dead_Hero = 0
        for hero in heroes_list:
            if hero.health == 0:
                dead_Hero = hero
                break
        if dead_Hero:
            chance_resurrection = randint(1,1)
            if chance_resurrection == 1:
                dead_Hero.health = 150
                self.health = 0
                print(f'Witcher {self.name} resurrected {dead_Hero.name} at the cost of his live ')



class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,'HACK')

    def apply_super_power(self, boss, heroes_list):
        vam = choice([10,15])
        boss.health -= vam
        one_hero = choice(heroes_list)
        if one_hero.health > 0:
            one_hero.health += vam
        print(f'Hacker {self.name} transferred {vam} health from the boss to {one_hero.name}.')



class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'FORTRESS')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if self.health > 0:
                if boss.choose_defence != self.ability:
                    if hero != self:
                        if hero.health > 0:
                            hero.health += 10
                            self.health -= 10



class King(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'SAITAMA')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(1, 20)
        if coeff == 1:
            boss.health = 0
            print(f'{self.name} was able to summon SAITAMA and killed the {boss.name} with one punch.')



round_number = 0


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)


def start_game():
    boss = Boss(name='Minotavr', health=3300, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=20)
    warrior_2 = Warrior(name='Obelix', health=280, damage=22)
    magic = Magic(name='Alice', health=270, damage=10)
    berserk = Berserk(name='Guts', health=220, damage=23)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=10)
    witcher = Witcher(name='Wirall', health=400, damage=0)
    hacker = Hacker(name='Anon', health=240, damage=10)
    golem = Golem(name='Grok', health=600, damage=1)
    king = King(name='King', health=400, damage=0)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant,witcher,hacker,golem,king]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()