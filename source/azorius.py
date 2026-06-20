from actions import *

SPRITES_PATH = os.path.join(os.path.dirname(__file__), "..", "sprites")


class Island(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, "Island.jpg")
        
    def generate_mana(self):
        return 'blue'

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana()] += 1

class Plains(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Plains.jpg')
        self.types = ['Plains']

    def generate_mana(self):
        return 'white'

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana()] += 1

class Hallowed_Fountain(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, "Hallowed_Fountain.jpg")
        self.tapped = True
        self.types = ['Plains', 'Island']

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
                    return 'white'
                elif right_rect.collidepoint(mouse_pos):
                    return 'blue'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Seachrome_Coast(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, "Seachrome_Coast.jpg")

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
                    return 'white'
                elif right_rect.collidepoint(mouse_pos):
                    return 'blue'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Deserted_Beach(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, "Deserted_Beach.jpg")

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
                    return 'white'
                elif right_rect.collidepoint(mouse_pos):
                    return 'blue'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Adarkar_Wastes(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, "Adarkar_Wastes.jpg")

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
                    return 'white'
                elif right_rect.collidepoint(mouse_pos):
                    player.take_damage(1)
                    return 'blue'
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, STACK):
        if not self.tapped:
            self.tap()
            player.mana_pool.pool[self.generate_mana(player)] += 1

class Human_Token(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Human.jpg')
        self.power = 1
        self.toughness = 1
        self.types = ['Human']
        self.color = ['white']

        def die(self, player):
            player.battlefield.remove(self)

class Create_Human(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Castle_Ardenvale.jpg')
        self.mana_cost = Counter({'white': 2, 'generic': 2})

    def activate(self, player, opponent, ORDER):
        if player.mana_pool.spend_mana(self.mana_cost):
            ORDER.STACK.append(self)
            return True
        return False

    def effect(self, player, opponent, ORDER):
        human = Human_Token(player.player)
        player.battlefield.creatures.append(human)

class Castle_Ardenvale(Land):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, "Castle_Ardenvale.jpg")
        self.tapped = False

        self.create = Create_Human(self.controller)

    def enter_trigger(self, player, opponent, ORDER):
        for land in player.battlefield.lands:
            for type in land.types:
                if type == 'Plains':
                    self.tapped = False
            
    def generate_mana(self, player):
        return 'white'

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def activate(self, player, opponent, ORDER):
        if not self.tapped:
            x = PLAYER_BATTLEFIELD_X
            y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
            mouse_pos = pygame.mouse.get_pos()
            for land in player.battlefield.lands:
                if land is self:
                    top_rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT/2)
                    bot_rect = pygame.Rect(x, y+PERMANENT_HEIGHT/2, PERMANENT_WIDTH, PERMANENT_HEIGHT/2)
                    if top_rect.collidepoint(mouse_pos):
                        self.tap()
                        player.mana_pool.pool[self.generate_mana(player)] += 1
                        return
                    elif bot_rect.collidepoint(mouse_pos):
                        if not self.create.activate(player, opponent, ORDER):
                            self.tapped = False
                x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

class Revitalize(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Revitalize.jpg')
        self.color = ['white']
        self.mana_cost = Counter({'white': 1, 'generic': 1})
        self.mana_value = 2

    def effect(self, player, opponent, ORDER):
        player.take_damage(-3)
        draw(player, opponent, ORDER)

class Union_of_the_Third_Path(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Union_of_the_Third_Path.jpg')
        self.color = ['white']
        self.mana_cost = Counter({'white': 1, 'generic': 2})
        self.mana_value = 3

    def effect(self, player, opponent, ORDER):
        draw(player, opponent, ORDER)
        player.take_damage(-len(player.hand.cards))

class Frantic_Inventory(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Frantic_Inventory.jpg')
        self.color = ['blue']
        self.mana_cost = Counter({'blue': 1, 'generic': 1})
        self.mana_value = 2

    def effect(self, player, opponent, ORDER):
        for card in player.graveyard:
            if isinstance(card, Frantic_Inventory):
                draw(player, opponent, ORDER)
        draw(player, opponent, ORDER)

class Absorb(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Absorb.jpg')
        self.color = ['white', 'blue']
        self.mana_cost = Counter({'white': 1, 'blue': 2})
        self.mana_value = 3

        self.targeted = True
        self.target = None

    def select_target(self, player, opponent, ORDER):
        self.target = select_spell(player, opponent, ORDER) 
        return self.target

    def effect(self, player, opponent, ORDER):
        player.take_damage(-3)
        for object in ORDER.STACK:
            if object is self.target:
                if not object.cant_be_countered:
                    ORDER.STACK.remove(object)
                    if player.player == object.controller:
                        player.graveyard.append(object)
                    elif opponent.player == object.controller:
                        opponent.graveyard.append(object)
        
class Dovins_Veto(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Dovins_Veto.jpg')
        self.color = ['white', 'blue']
        self.mana_cost = Counter({'white': 1, 'blue': 1})
        self.mana_value = 2

        self.cant_be_countered = True

        self.targeted = True
        self.target = None

    def select_target(self, player, opponent, ORDER):
        self.target = select_spell(player, opponent, ORDER) 
        if not issubclass(self.target.__class__, Creature) and self.target is not None: 
            return self.target

    def effect(self, player, opponent, ORDER):
        for object in ORDER.STACK:
            if object is self.target:
                if not object.cant_be_countered:
                    ORDER.STACK.remove(object)
                    if player.player == object.controller:
                        player.graveyard.append(object)
                    elif opponent.player == object.controller:
                        opponent.graveyard.append(object)

class Change_the_Equation(Instant):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Change_the_Equation.jpg')
        self.color = ['blue']
        self.mana_cost = Counter({'blue': 1, 'generic': 1})
        self.mana_value = 2

        self.targeted = True
        self.target = None

    def select_target(self, player, opponent, ORDER):
        self.target = select_spell(player, opponent, ORDER) 
        if self.target.mana_value <= 2:
            return self.target

    def effect(self, player, opponent, ORDER):
        for object in ORDER.STACK:
            if object is self.target:
                if not object.cant_be_countered:
                    ORDER.STACK.remove(object)
                    if player.player == object.controller:
                        player.graveyard.append(object)
                    elif opponent.player == object.controller:
                        opponent.graveyard.append(object)

class Phyrexian_Token(Creature):
    def __init__(self, controller, x):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Phyrexian.jpg')
        self.power = x
        self.toughness = x
        self.types = ['Phyrexian']

class Transform(Ability):
    def __init__(self, controller, token, x):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Incubator.jpg')
        self.mana_cost = Counter({'generic': 2})

        self.token = token
        self.phyrexian = Phyrexian_Token(self.controller, x)
    
    def activate(self, player, opponent, ORDER):
        if player.mana_pool.spend_mana(self.mana_cost):
            ORDER.STACK.append(self)

    def effect(self, player, opponent, ORDER):
        player.battlefield.creatures.append(self.phyrexian)
        player.battlefield.others.remove(self.token)

class Incubator_Token(Artifact):
    def __init__(self, controller, x):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Incubator.jpg')

        self.transform = Transform(self.controller, self, x)

    def activate(self, player, opponent, ORDER):
        self.transform.activate(player, opponent, ORDER)

class Sunfall(Sorcery):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Sunfall.jpg')
        self.color = ['white']
        self.mana_cost = Counter({'white': 2, 'generic': 3})
        self.mana_value = 5

    def effect(self, player, opponent, STACK):
        x = 0
        for creature in player.battlefield.creatures.copy():
            player.battlefield.creatures.remove(creature)
            x += 1
        for creature in opponent.battlefield.creatures.copy():
            opponent.battlefield.creatures.remove(creature)
            x += 1
        incubator = Incubator_Token(self.controller, x)
    
        player.battlefield.others.append(incubator)

class Teferi_Untap(Ability):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Teferi_Hero_of_Dominaria.jpg')
    
    def effect(self, player, opponent, ORDER):
        for i in range(2):
            land = select_land(player, opponent)
            if land is not None:
                land.tapped = False

class Teferi_Draw(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Teferi_Hero_of_Dominaria.jpg')
        self.loyalty_cost = 1

    def effect(self, player, opponent, ORDER):
        draw(player, opponent, ORDER)

class Teferi_Bounce(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Teferi_Hero_of_Dominaria.jpg')
        self.loyalty_cost = -3
        
        self.targeted = True
        self.target = None

    def select_target(self, player, opponent):
        self.target = select_nonland(player, opponent) 
        return self.target

    def effect(self, player, opponent, ORDER):
        for creature in player.battlefield.creatures:
            if creature is self.target:
                player.battlefield.creatures.remove(creature)
                player.library.insert(3, creature)
                return
        for other in player.battlefield.others:
            if other is self.target:
                player.battlefield.others.remove(other)
                player.library.insert(3, other)
                return
        for creature in opponent.battlefield.creatures:
            if creature is self.target:
                opponent.battlefield.creatures.remove(creature)
                opponent.library.insert(3, creature)
                return
        for other in opponent.battlefield.others:
            if other is self.target:
                opponent.battlefield.others.remove(other)
                opponent.library.insert(3, other)
                return

class Teferi_Exile(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Emblem.jpg')
        
        self.targeted = True
        self.target = None

    def select_target(self, player, opponent):
        self.target = select_permanent(player, opponent)
        return self.target

    def effect(self, player, opponent, ORDER):
        for land in opponent.battlefield.lands:
            if land is self.target:
                opponent.battlefield.lands.remove(land)
                return
        for creature in opponent.battlefield.creatures:
            if creature is self.target:
                opponent.battlefield.creatures.remove(creature)
                return
        for other in opponent.battlefield.others:
            if other is self.target:
                opponent.battlefield.others.remove(other)
                return

class Teferi_Emblem(Emblem):
    def __init__(self, controller):
        super().__init__(controller)
        self.exile = Teferi_Exile(self.controller)

class Teferi_Ult(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Teferi_Hero_of_Dominaria.jpg')
        self.loyalty_cost = -8

    def effect(self, player, opponent, STACK):
        emblem = Teferi_Emblem(player.player)
        player.emblems.append(emblem)

class Teferi_Hero_of_Dominaria(Planeswalker):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Teferi_Hero_of_Dominaria.jpg')
        self.color = ['white', 'blue']
        self.mana_cost = Counter({'white': 1, 'blue': 1, 'generic': 3})
        self.mana_value = 5
        self.loyalty = 4

        self.first_ability = Teferi_Draw(self.controller)
        self.second_ability = Teferi_Bounce(self.controller)
        self.last_ability = Teferi_Ult(self.controller)

    def activate(self, player, opponent, ORDER):
        mouse_pos = pygame.mouse.get_pos()
        x = PLAYER_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH
        y = PLAYER_BATTLEFIELD_Y
        try:
            if ORDER.PHASE != 'Main phase 1' and ORDER.PHASE != 'Main phase 2' and len(ORDER.STACK) == 0:
                raise ValueError('Wait for your main phase!')
            if self.activated:
                raise ValueError('You may only activate a planeswalker once a turn!')
            for other in player.battlefield.others:
                if other is self:
                    top_rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT/3)
                    mid_rect = pygame.Rect(x, y+PERMANENT_HEIGHT/3, PERMANENT_WIDTH, PERMANENT_HEIGHT/3)
                    bot_rect = pygame.Rect(x, y+PERMANENT_HEIGHT*2/3, PERMANENT_WIDTH, PERMANENT_HEIGHT/3)
                    if top_rect.collidepoint(mouse_pos):
                        self.loyalty += self.first_ability.loyalty_cost
                        ORDER.STACK.append(self.first_ability)
                        
                        player.teferi_untap = True
                    elif mid_rect.collidepoint(mouse_pos):
                        if self.loyalty - self.second_ability.loyalty_cost < 0:
                            raise ValueError('Not enough loyalty!')
                        else:
                            if self.second_ability.select_target(player, opponent):
                                self.loyalty += self.second_ability.loyalty_cost
                                ORDER.STACK.append(self.second_ability)
                                
                    elif bot_rect.collidepoint(mouse_pos):
                        if self.loyalty - self.last_ability.loyalty_cost < 0:
                            raise ValueError('Not enough loyalty!')
                        else:
                            self.loyalty += self.last_ability.loyalty_cost
                            ORDER.STACK.append(self.last_ability)
                            
                x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE
        except ValueError as error:
            render_message(str(error))
            pygame.display.update()
            time.sleep(1)

class Samurai_Token(Creature):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'Samurai.png')
        self.power = 2
        self.toughness = 2
        self.types = ['Samurai']
        self.color = ['white']
        self.vigilance = True

        def die(self, player):
            player.battlefield.remove(self)

class Emperor_Buff(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'The_Wandering_Emperor.png')
        self.loyalty_cost = + 1
        
        self.targeted = True
        self.target = None

    def select_target(self, player, opponent):
        self.target = select_creature(player, opponent) 
        return self.target

    def effect(self, player, opponent, ORDER):
        for creature in player.battlefield.creatures:
            if creature is self.target:
                creature.counters += 1
                return
        for creature in opponent.battlefield.creatures:
            if creature is self.target:
                creature.counters += 1
                return

class Create_Samurai(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'The_Wandering_Emperor.png')
        self.loyalty_cost = -1

    def effect(self, player, opponent, ORDER):
        samurai = Samurai_Token(player.player)
        player.battlefield.creatures.append(samurai)

class Exile(LoyaltyAbility):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'The_Wandering_Emperor.png')
        self.loyalty_cost = -2
        
        self.targeted = True
        self.target = None

    def select_target(self, player, opponent):
        self.target = select_creature(player, opponent) 
        if self.target.tapped:
            return self.target

    def effect(self, player, opponent, ORDER):
        for creature in player.battlefield.creatures:
            if creature is self.target:
                player.battlefield.creatures.remove(creature)
                player.take_damage(-2)
                return
        for creature in opponent.battlefield.creatures:
            if creature is self.target:
                opponent.battlefield.creatures.remove(creature)
                player.take_damage(-2)
                return

class The_Wandering_Emperor(Planeswalker):
    def __init__(self, controller):
        super().__init__(controller)
        self.art = os.path.join(SPRITES_PATH, 'The_Wandering_Emperor.png')
        self.color = ['white']
        self.mana_cost = Counter({'white': 2, 'generic': 2})
        self.mana_value = 4
        self.loyalty = 3

        self.flash = True
        self.entered_this_turn = True

        self.first_ability = Emperor_Buff(self.controller)
        self.second_ability = Create_Samurai(self.controller)
        self.last_ability = Exile(self.controller)

    def activate(self, player, opponent, ORDER):
        mouse_pos = pygame.mouse.get_pos()
        x = PLAYER_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH
        y = PLAYER_BATTLEFIELD_Y
        try:
            if ORDER.PHASE != 'Main phase 1' and ORDER.PHASE != 'Main phase 2' and not self.entered_this_turn and len(ORDER.STACK) == 0:
                raise ValueError('Wait for your main phase!')
            if self.activated:
                raise ValueError('You may only activate a planeswalker once a turn!')
            for other in player.battlefield.others:
                if other is self:
                    top_rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT/3)
                    mid_rect = pygame.Rect(x, y+PERMANENT_HEIGHT/3, PERMANENT_WIDTH, PERMANENT_HEIGHT/3)
                    bot_rect = pygame.Rect(x, y+PERMANENT_HEIGHT*2/3, PERMANENT_WIDTH, PERMANENT_HEIGHT/3)
                    if top_rect.collidepoint(mouse_pos):
                        self.loyalty += self.first_ability.loyalty_cost
                        ORDER.STACK.append(self.first_ability)
                        self.activated = True
                        self.entered_this_turn = False
                    elif mid_rect.collidepoint(mouse_pos):
                        if self.loyalty - self.second_ability.loyalty_cost < 0:
                            raise ValueError('Not enough loyalty!')
                        else:
                            self.loyalty += self.second_ability.loyalty_cost
                            ORDER.STACK.append(self.second_ability)
                            self.activated = True
                            self.entered_this_turn = False
                    elif bot_rect.collidepoint(mouse_pos):
                        if self.loyalty - self.last_ability.loyalty_cost < 0:
                            raise ValueError('Not enough loyalty!')
                        else:
                            if self.last_ability.select_target(player, opponent):
                                self.loyalty += self.last_ability.loyalty_cost
                                ORDER.STACK.append(self.last_ability)
                                self.activated = True
                                self.entered_this_turn = False
                x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE
        except ValueError as error:
            render_message(str(error))
            pygame.display.update()
            time.sleep(1)

def azorius_decklist(player):
    decklist = []
    for i in range(5):
        island = Island(player.player)
        decklist.append(island)
        plains = Plains(player.player)
        decklist.append(plains)
    for i in range(4):
        change = Change_the_Equation(player.player)
        decklist.append(change)
        absorb = Absorb(player.player)
        decklist.append(absorb)
        inventory = Frantic_Inventory(player.player)
        decklist.append(inventory)
        revitalize = Revitalize(player.player)
        decklist.append(revitalize)
        union = Union_of_the_Third_Path(player.player)
        decklist.append(union)
        emperor = The_Wandering_Emperor(player.player)
        decklist.append(emperor)
        coast = Seachrome_Coast(player.player)
        decklist.append(coast)
        fountain = Hallowed_Fountain(player.player)
        decklist.append(fountain)
        wastes = Adarkar_Wastes(player.player)
        decklist.append(wastes)
        beach = Deserted_Beach(player.player)
        decklist.append(beach)
    for i in range(3):
        sunfall = Sunfall(player.player)
        decklist.append(sunfall)
        teferi = Teferi_Hero_of_Dominaria(player.player)
        decklist.append(teferi)
    for i in range(2):
        castle = Castle_Ardenvale(player.player)
        decklist.append(castle)
        dovin = Dovins_Veto(player.player)
        decklist.append(dovin)

    player.library = decklist

