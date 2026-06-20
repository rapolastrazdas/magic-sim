from collections import Counter
class Card:
    def __init__(self, controller):
        self.controller = controller
        self.tapped = False
        self.art = ''
        self.types = []
        self.color = []
        self.mana_cost = Counter()
        self.mana_value = 0
        self.sickness = True
    def enter(self, player, opponent, STACK):
        pass

    def activate(self, player, opponent, STACK):
        pass

    def untap(self):
        if self.tapped:
            self.tapped = False

class Land(Card):
    def __init__(self, controller):
        super().__init__(controller)

    def generate_mana(self):
        pass

    def tap(self):
        if not self.tapped:
            self.tapped = True

class Spell(Card):
    def __init__(self, controller):
        super().__init__(controller)
        self.flash = False
        self.targeted = False
        self.cant_be_countered = False

    def select_target(self, player, opponent, ORDER):
        pass

    def resolve(self, player, opponent, ORDER):
        if issubclass(self.__class__, Creature):
            player.battlefield.creatures.insert(0, self)
            del ORDER.STACK[0]
            for enforcer in player.battlefield.creatures:
                if enforcer.__class__.__name__ == 'Thieves_Guild_Enforcer':
                    for type in self.types:
                        if type == 'Rogue':
                            enforcer.mill.activate(player, opponent, ORDER)

        elif issubclass(self.__class__, Instant) or issubclass(self.__class__, Sorcery):
            self.effect(player, opponent, ORDER)
            player.graveyard.insert(0, self)
            del ORDER.STACK[0]

        else:
            player.battlefield.others.insert(0, self)
            del ORDER.STACK[0]

class Creature(Spell):
    def __init__(self, controller):
        super().__init__(controller)
        self.power = 0
        self.powerup = 0
        self.total_power = 0
        self.fatigue = 0
        self.toughness = 0
        self.toughnessup = 0
        self.total_toughness = 0
        self.counters = 0
        self.damage = 0

        self.attacking = False
        self.blocking = False
        self.target = None
        
        self.flying = False
        self.deathtouch = False
        self.vigilance = False

    def attack(self):
        if not self.vigilance:
            self.tapped = True
        self.attacking = True

    def block(self, attacker):
        self.target = attacker
        attacker.target = self
        self.blocking = True

    def deal_damage(self, target):
        target.take_damage(self)

    def take_damage(self, source):
        if issubclass(source.__class__, Creature):
            if source.deathtouch:
                amount = source.power + source.powerup + source.counters - source.fatigue
                if amount > 0:
                    source.fatigue += 1
                    self.damage = self.toughness
            else:
                amount = source.power + source.powerup + source.counters - source.fatigue
                if self.toughness < amount:
                    source.fatigue += self.toughness
                    self.damage = self.toughness
                else:
                    self.damage = amount
        else:
            self.damage = 0
        if self.damage >= self.toughness:
            self.die()
    
    def heal(self):
        self.fatigue = 0
        self.damage = 0

    def die(self, player):
        player.graveyard.insert(0, self)
        player.battlefield.creatures.remove(self)

class Instant(Spell):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller
        self.flash = True

    def effect(self, player, opponent, ORDER):
        pass

class Sorcery(Spell):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

    def effect(self, player, opponent, ORDER):
        pass

class Planeswalker(Spell):
    def __init__(self, controller):
        super().__init__(controller)
        self.loyalty = 0
        self.activated = False

    def activate(self, cost):
        pass

    def take_damage(self, source):
        if issubclass(source.__class__, Creature):
            amount = source.power + source.powerup + source.counters
        self.loyalty -= amount
        if self.loyalty <= 0:
            self.die()

    def die(self, player):
        player.graveyard.insert(0, self)
        player.battlefield.others.remove(self)

class Artifact(Spell):
    def __init__(self, controller):
        super().__init__(controller)

class Enchantment(Spell):
    def __init__(self, controller):
        super().__init__(controller)

class Ability:
    def __init__(self, controller):
        self.controller = controller
        self.flash = True
        self.mana_cost = Counter()
        self.targeted = False
    
    def activate(self, player, opponent, ORDER):
        if player.mana_pool.spend_mana(self.mana_cost):
            ORDER.STACK.append(self)

    def effect(self, player, opponent, ORDER):
        pass

    def resolve(self, player, opponent, ORDER):
        self.effect(player, opponent, ORDER)
        ORDER.STACK.pop(0)

class LoyaltyAbility(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller
        self.flash = False

class Emblem():
    def __init__(self, controller):
        self.controller = controller


