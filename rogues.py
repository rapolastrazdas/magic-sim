from actions import *

class Island(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Island.jpg'
        
    def generate_mana(self):
        return 'blue'

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana()] += 1

class Swamp(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Swamp.jpg'
        self.types = ['Swamp']

    def generate_mana(self):
        return 'black'

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana()] += 1

class Watery_Grave(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = "Watery_Grave.jpg"
        self.tapped = True
        self.types = ['Island', 'Swamp']

    def enter(self, player, opponent, ORDER):
        render_message('Pay 2 life? Y/N')
        pygame.display.update()
        loop = True
        while loop:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_y:
                        self.tapped = False
                        player.take_damage(2)
                        loop = False
                    elif event.key == pygame.K_n:
                        loop = False
        render(player, opponent, None, None, ORDER)

    def generate_mana(self, player):
        x = PLAYER_BATTLEFIELD_X
        y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
        mouse_pos = pygame.mouse.get_pos()
        for land in player.battlefield.lands:
            if land is self:
                left_rect = pygame.Rect(x, y, PERMANENT_WIDTH/2, PERMANENT_HEIGHT)
                right_rect = pygame.Rect(x+PERMANENT_WIDTH/2, y, PERMANENT_WIDTH/2, PERMANENT_HEIGHT)
                if left_rect.collidepoint(mouse_pos):
                    return 'blue'
                elif right_rect.collidepoint(mouse_pos):
                    return 'black'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Darkslick_Shores(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = "Darkslick_Shores.jpg"

    def enter(self, player, opponent, ORDER):
        if len(player.battlefield.lands) > 3:
            self.tapped = True

    def generate_mana(self, player):
        x = PLAYER_BATTLEFIELD_X
        y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
        mouse_pos = pygame.mouse.get_pos()
        for land in player.battlefield.lands:
            if land is self:
                left_rect = pygame.Rect(x, y, PERMANENT_WIDTH/2, PERMANENT_HEIGHT)
                right_rect = pygame.Rect(x+PERMANENT_WIDTH/2, y, PERMANENT_WIDTH/2, PERMANENT_HEIGHT)
                if left_rect.collidepoint(mouse_pos):
                    return 'blue'
                elif right_rect.collidepoint(mouse_pos):
                    return 'black'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Shipwreck_Marsh(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = "Shipwreck_Marsh.jpg"

    def enter(self, player, opponent, ORDER):
        if len(player.battlefield.lands) < 2:
            self.tapped = True

    def generate_mana(self, player):
        x = PLAYER_BATTLEFIELD_X
        y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
        mouse_pos = pygame.mouse.get_pos()
        for land in player.battlefield.lands:
            if land is self:
                left_rect = pygame.Rect(x, y, PERMANENT_WIDTH/2, PERMANENT_HEIGHT)
                right_rect = pygame.Rect(x+PERMANENT_WIDTH/2, y, PERMANENT_WIDTH/2, PERMANENT_HEIGHT)
                if left_rect.collidepoint(mouse_pos):
                    return 'blue'
                elif right_rect.collidepoint(mouse_pos):
                    return 'black'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Underground_River(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = "Underground_River.jpg"

    def generate_mana(self, player):
        x = PLAYER_BATTLEFIELD_X
        y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
        mouse_pos = pygame.mouse.get_pos()
        for land in player.battlefield.lands:
            if land is self:
                top_rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT/2)
                left_rect = pygame.Rect(x, y+PERMANENT_HEIGHT/2, PERMANENT_WIDTH/2, PERMANENT_HEIGHT/2)
                right_rect = pygame.Rect(x+PERMANENT_WIDTH/2, y+PERMANENT_HEIGHT/2, PERMANENT_WIDTH/2, PERMANENT_HEIGHT/2)
                if top_rect.collidepoint(mouse_pos):
                    return 'generic'
                elif left_rect.collidepoint(mouse_pos):
                    player.take_damage(1)
                    return 'blue'
                elif right_rect.collidepoint(mouse_pos):
                    player.take_damage(1)
                    return 'black'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Landfall(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Ruin_Crab.jpg'

    def effect(self, player, opponent, ORDER):
        for i in range(3):
            card = opponent.library[0]
            opponent.graveyard.insert(0, card)
            opponent.library.pop(0)
        check_graveyards(player, opponent)

class Ruin_Crab(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Ruin_Crab.jpg'
        self.power = 0
        self.toughness = 3
        self.types = ['Crab']
        self.color = ['blue']
        self.mana_cost = Counter({'blue': 1})
        self.mana_value = 1
        
        self.landfall = Landfall(self.controller)

class Enforcer_Mill(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Thieves_Guild_Enforcer.jpg'

    def effect(self, player, opponent, ORDER):
        for i in range(2):
            card = opponent.library[0]
            opponent.graveyard.insert(0, card)
            opponent.library.pop(0)
        check_graveyards(player, opponent)

class Thieves_Guild_Enforcer(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Thieves_Guild_Enforcer.jpg'
        self.power = 1
        self.toughness = 1
        self.types = ['Human', 'Rogue']
        self.color = ['black']
        self.mana_cost = Counter({'black': 1})
        self.mana_value = 1

        self.flash = True
        self.mill = Enforcer_Mill(self.controller)

    def enforce(self, opponent):
        if len(opponent.graveyard) >= 8:
            self.powerup += 2
            self.toughnessup = +1
            self.deathtouch = True
 
class Thief_Mill(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Soaring_Thought-Thief.jpg'

    def effect(self, player, opponent, ORDER):
        for i in range(2):
            card = opponent.library[0]
            opponent.graveyard.insert(0, card)
            opponent.library.pop(0)
        check_graveyards(player, opponent)

class Soaring_Thought_Thief(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Soaring_Thought-Thief.jpg'
        self.power = 1
        self.toughness = 3
        self.types = ['Human', 'Rogue']
        self.color = ['blue', 'black']
        self.mana_cost = Counter({'blue': 1, 'black': 1})
        self.mana_value = 2

        self.flash = True
        self.flying = True
        self.mill = Thief_Mill(self.controller)
        
    def steal_thoughts(self, player, opponent):
        if len(opponent.graveyard) >= 8:
            for creature in player.battlefield.creatures:
                for type in creature.types:
                    if type == 'Rogue':
                        creature.powerup += 1
                        
class Draw(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Faerie_Mastermind.jpg'

    def effect(self, player, opponent, ORDER):
        draw(player, opponent, ORDER)

class Activate_Faerie(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Faerie_Mastermind.jpg'
        self.mana_cost = Counter({'blue': 1, 'generic': 3})

    def effect(self, player, opponent, ORDER):
        draw(player, opponent, ORDER)
        draw(opponent, player, ORDER)

class Faerie_Mastermind(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Faerie_Mastermind.jpg'
        self.power = 2
        self.toughness = 1
        self.types = ['Faerie', 'Rogue']
        self.color = ['blue']
        self.mana_cost = Counter({'blue': 1, 'generic': 1})
        self.mana_value = 2

        self.flash = True
        self.flying = True
        self.draw = Draw(self.controller)
        self.ability = Activate_Faerie(self.controller)

    def activate(self, player, opponent, ORDER):
        self.ability.activate(player, opponent, ORDER)
        
class Nighthawk_Scavenger(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Nighthawk_Scavenger.jpg'
        self.power = 1
        self.toughness = 3
        self.types = ['Vampire', 'Rogue']
        self.color = ['black']
        self.mana_cost = Counter({'black': 2, 'generic': 1})
        self.mana_value = 3

        self.flying = True
        self.deathtouch = True
        
    def scavenge(self, opponent):
        for card in opponent.graveyard:
            if issubclass(card.__class__, Land):
                self.powerup += 1
                break
        for card in opponent.graveyard:
            if issubclass(card.__class__, Creature):
                self.powerup += 1
                break
        for card in opponent.graveyard:
            if issubclass(card.__class__, Instant):
                self.powerup += 1
                break
        for card in opponent.graveyard:
            if issubclass(card.__class__, Sorcery):
                self.powerup += 1
                break
        for card in opponent.graveyard:
            if issubclass(card.__class__, Planeswalker):
                self.powerup += 1
                break
        for card in opponent.graveyard:
            if issubclass(card.__class__, Artifact):
                self.powerup += 1
                break
        for card in opponent.graveyard:
            if issubclass(card.__class__, Enchantment):
                self.powerup += 1
                break
    
class Thought_Seize(Sorcery):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Thought_Seize.jpg'
        self.color = ['black']
        self.mana_cost = Counter({'black': 1})
        self.mana_value = 1

    def effect(self, player, opponent, ORDER):
        loop = True
        selected = None
        while loop:
            selected = select_card(opponent)
            render(opponent, player, selected, None, ORDER)
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                    if selected is not None:
                        if not issubclass(selected.__class__, Land):
                            opponent.hand.cards.remove(selected)
                            opponent.graveyard.insert(0, selected)
                            loop = False
        player.take_damage(2)

class Of_One_Mind(Sorcery):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Of_One_Mind.jpg'
        self.color = ['blue']
        self.mana_cost = Counter({'blue': 1, 'generic': 2})
        self.mana_value = 3

    def cost_reduction(self, player):
        human = False
        nonhuman = False
        for creature in player.battlefield.creatures:
            same_creature = False
            for type in creature.types:
                if type == 'Human' and not same_creature:
                    human = True
                    same_creature = True
                elif not same_creature:
                    nonhuman = True
                    same_creature = True
        if human and nonhuman:
            self.mana_cost = Counter({'blue': 1})
        else:
            self.mana_cost = Counter({'blue': 1, 'generic': 2})

    def effect(self, player, opponent, ORDER):
        draw(player, opponent, ORDER, 2)

class Drown_in_the_Loch(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Drown_in_the_Loch.jpg'
        self.color = ['blue', 'black']
        self.mana_cost = Counter({'blue': 1, 'black': 1})
        self.mana_value = 2

        self.targeted = True
        self.Target = None

        self.choice = ''

    def select_target(self, player, opponent, ORDER):
        render_message('Choose one: 1/2')
        pygame.display.update()
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        self.target = select_spell(player, opponent, ORDER)
                        self.choice = '1'
                        loop = False
                    elif event.key == pygame.K_2:
                        self.target = select_creature(player, opponent, ORDER) 
                        self.choice = '2'
                        loop = False
        if self.target is not None:
            if self.target.mana_value <= len(opponent.graveyard):
                return self.target
        
    def effect(self, player, opponent, ORDER):
        if self.choice == '1':
            for object in ORDER.STACK:
                if object is self.target:
                    if not object.cant_be_countered:
                        ORDER.STACK.remove(object)
                        if player.player == object.controller:
                            player.graveyard.append(object)
                        elif opponent.player == object.controller:
                            opponent.graveyard.append(object)
        elif self.choice == '2':
            for creature in player.battlefield.creatures:
                if creature is self.target:
                    creature.die(player)
            for creature in opponent.battlefield.creatures:
                if creature is self.target:
                    creature.die(opponent)

class Into_the_Story(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = 'Into_the_Story.jpg'
        self.color = ['blue']
        self.mana_cost = Counter({'blue': 2, 'generic': 5})
        self.mana_value = 7

    def cost_reduction(self, opponent):
        if len(opponent.graveyard) >= 7:
            self.mana_cost = Counter({'blue': 2, 'generic': 2}) 
        else:
            self.mana_cost = Counter({'blue': 2, 'generic': 5})

    def effect(player, opponent, ORDER):
        draw(player, opponent, ORDER, 4)

def dimir_decklist(player):
    decklist = []
    for i in range(4):
        card = Island(player.player)
        decklist.append(card)
        card = Swamp(player.player)
        decklist.append(card)
        card = Into_the_Story(player.player)
        decklist.append(card)
        card = Of_One_Mind(player.player)
        decklist.append(card)
        card = Thought_Seize(player.player)
        decklist.append(card)
        card = Drown_in_the_Loch(player.player)
        decklist.append(card)
        card = Faerie_Mastermind(player.player)
        decklist.append(card)
        card = Soaring_Thought_Thief(player.player)
        decklist.append(card)
        card = Thieves_Guild_Enforcer(player.player)
        decklist.append(card)
        card = Ruin_Crab(player.player)
        decklist.append(card)
        card = Nighthawk_Scavenger(player.player)
        decklist.append(card)
        card = Watery_Grave(player.player)
        decklist.append(card)
        card = Darkslick_Shores(player.player)
        decklist.append(card)
        card = Shipwreck_Marsh(player.player)
        decklist.append(card)
        card = Underground_River(player.player)
        decklist.append(card)

    player.library = decklist

