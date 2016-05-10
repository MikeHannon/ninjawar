# Phase 1: Comment this code!
# Phase 2: Build out the game further, make the armies attack one another!
# Phase 3: Set it up some that if a member of an army has less than 0 health remove it from the army
# Phase 4: Set up the battles so that different army types fight differently!
import random
class Human(object):
    def __init__(self, clan = None):
        super(Human, self).__init__()
        print 'New Human!!!'
        self.health = 100
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3
        self.clan = clan
    def taunt(self):
        print "You want a piece of me?"
        return self
    def attack(self,target):
        self.taunt()
        luck = round(random.random() * 100)
        attack = self.strength
        if (self.clan):
            pass
        if(luck > 50):
            if(luck * self.stealth > 150):
                print 'attacking!'
                target.health -= attack
                target.reporthealth()
                return True
            else:
                print 'attack failed'
                return False
        else:
            self.health -= self.strength
            print "attack failed"
        return False
    def reporthealth(self):
        if self.health > 0:
            print "I am not dead yet!"
        else:
            print "AAAaah you've killed me"


class Ninja(Human):
    def __init__(self, clan = 'Ninja'):
        super(Ninja, self).__init__(clan)
        self.health = 70
        self.steath = 30

class Warrior(Human):
    def __init__(self, clan = 'Ninja'):
        super(Warrior, self).__init__()
        self.health = 130
        self.strength = 30

class Wizard(Human):
    """docstring for Warrior"""
    def __init__(self, clan = 'Ninja'):
        super(Warrior, self).__init__()
        self.health = 50
        self.intelligence = 3


class Game(object):
    """docstring for Game"""
    def __init__(self):
        super(Game, self).__init__()
        self.armies = []

    def buildArmy(self, clan = None):
        clanMap = {"Wizard": Wizard, "Ninja": Ninja, "Warrior": Warrior}
        army = []
        if clanMap[clan]:
            for human in range(random.randint(10,100)):
                army.append(clanMap[clan]())
        else:
            for human in range(random.randint(10,100)):
                army.append(Human())
        self.armies.append(army)

game = Game()
game.buildArmy('Ninja')
