import random
from render import *
from card import *

def select_card(player):
    selected_card = None
    mouse_pos = pygame.mouse.get_pos()

    if len(player.hand.cards) > 6:
        x = PLAYER_HAND_X
        spacing = (PLAYER_HAND_WIDTH - PLAYER_CARD_WIDTH * len(player.hand.cards)) / (len(player.hand.cards) - 1)
    else:
        x = SCREEN_WIDTH/2 - PLAYER_CARD_WIDTH/2 * len(player.hand.cards)
        spacing = 5
    y = PLAYER_HAND_Y
    for card in player.hand.cards:
        if len(player.hand.cards) < 7:
            card_rect = pygame.Rect(x, y, PLAYER_CARD_WIDTH, PLAYER_CARD_HEIGHT)
        else:
            card_rect = pygame.Rect(x+PLAYER_CARD_WIDTH/4, y, PLAYER_CARD_WIDTH/4*3, PLAYER_CARD_HEIGHT)

        if card_rect.collidepoint(mouse_pos):
            selected_card = card
        x += PLAYER_CARD_WIDTH + spacing
    
    return selected_card

def select_activate(player, opponent):
    selected_permanent = None
    mouse_pos = pygame.mouse.get_pos()
    x = PLAYER_BATTLEFIELD_X
    y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
    for land in player.battlefield.lands:
        land_rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
        if land_rect.collidepoint(mouse_pos):
            selected_permanent = land
        x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
    if selected_permanent is None:
        x = PLAYER_BATTLEFIELD_X
        y = PLAYER_BATTLEFIELD_Y
        for creature in player.battlefield.creatures:
            rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
            if rect.collidepoint(mouse_pos):
                selected_permanent = creature
            x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
    if selected_permanent is None:
        x = PLAYER_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH
        y = PLAYER_BATTLEFIELD_Y
        for other in player.battlefield.others:
            other_rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
            if other_rect.collidepoint(mouse_pos):
                selected_permanent = other
            x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE
    return selected_permanent

def select_creature(player, opponent):
    render_message('Select target creature!')
    pygame.display.update()
    selected = None
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x, y = PLAYER_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y
                for creature in player.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = creature
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

                x, y = OPPONENT_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                for creature in opponent.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = creature
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
                loop = False
    if selected is not None:
        return selected
    
def select_land(player, opponent):
    render_message('Select target land!')
    pygame.display.update()
    selected = None
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x, y = PLAYER_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                for land in player.battlefield.lands:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = land
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

                x, y = OPPONENT_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y
                for land in opponent.battlefield.lands:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = land
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
                loop = False
    if selected is not None:
        return selected

def select_nonland(player, opponent):
    render_message('Select target nonland permanent!')
    pygame.display.update()
    selected = None
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x, y = PLAYER_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y
                for creature in player.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = creature
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

                x, y = OPPONENT_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                for creature in opponent.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = creature
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

                x, y = PLAYER_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH, PLAYER_BATTLEFIELD_Y
                for other in player.battlefield.others:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = other
                        loop = False
                    x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE

                x, y = OPPONENT_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                for other in opponent.battlefield.others:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = other
                        loop = False
                    x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE
                loop = False
    if selected is not None:
        return selected

def select_permanent(player, opponent):
    render_message('Select target permanent!')
    pygame.display.update()
    selected = None
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                x, y = OPPONENT_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y
                for land in opponent.battlefield.lands:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = land
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

                x, y = OPPONENT_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                for creature in opponent.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = creature
                        loop = False
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

                x, y = OPPONENT_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                for other in opponent.battlefield.others:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        selected = other
                        loop = False
                    x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE
                loop = False

    if selected is not None:
        return selected
            
def select_spell(player, opponent, ORDER):
    render(player, opponent, None, None, ORDER)
    render_message('Select target spell!')
    pygame.display.update()
    selected = None
    loop = True
    x, y = STACK_X, STACK_Y
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for object in ORDER.STACK:
                    object_rect = pygame.Rect(x, y, PLAYER_CARD_WIDTH, PLAYER_CARD_HEIGHT)
                    if object_rect.collidepoint(mouse_pos):
                        if issubclass(object.__class__, Spell):
                            selected = object
                            loop = False
                            break
                    x += PLAYER_CARD_WIDTH
                loop = False
    if selected is not None:
        return selected

def pass_priority(player, opponent, ORDER):
    if len(ORDER.STACK) == 0:
        if not player.turn:
            if ORDER.PHASE == 'Untap':
                ORDER.PHASE = 'Upkeep'
            elif ORDER.PHASE == 'Upkeep':
                ORDER.PHASE = 'Draw'
            elif ORDER.PHASE == 'Draw':
                ORDER.PHASE = 'Main phase 1'
            elif ORDER.PHASE == 'Main phase 1':
                ORDER.PHASE = 'Beginning of combat'
            elif ORDER.PHASE == 'Beginning of combat':
                ORDER.PHASE = 'Declare attackers'
            elif ORDER.PHASE == 'Declare attackers':
                ORDER.PHASE = 'Declare blockers'
            elif ORDER.PHASE == 'Declare blockers':
                ORDER.PHASE = 'Combat damage'
            elif ORDER.PHASE == 'Combat damage':
                ORDER.PHASE = 'End of combat'
            elif ORDER.PHASE == 'End of combat':
                ORDER.PHASE = 'Main phase 2'
            elif ORDER.PHASE == 'Main phase 2':
                ORDER.PHASE = 'End step'
            elif ORDER.PHASE == 'End step':
                ORDER.PHASE = 'Clean up'
            player.priority = False
            opponent.priority = True
        elif player.turn:
            player.priority = False
            opponent.priority = True
    elif ORDER.STACK[0].controller == player.player:
        player.priority = False
        opponent.priority = True
    elif ORDER.STACK[0].controller != player.player:
        ORDER.STACK[0].resolve(opponent, player, ORDER)
        player.priority = False
        opponent.priority = True
    check_graveyards(player, opponent)
    for card in player.library: 
        if card.__class__.__name__ == 'Of_One_Mind':
            card.cost_reduction(player)
    for card in player.hand.cards: 
        if card.__class__.__name__ == 'Of_One_Mind':
            card.cost_reduction(player)
    for card in opponent.library: 
        if card.__class__.__name__ == 'Of_One_Mind':
            card.cost_reduction(opponent)
    for card in opponent.hand.cards: 
        if card.__class__.__name__ == 'Of_One_Mind':
            card.cost_reduction(opponent)

def draw(player, opponent, ORDER, amount=1):
    if len(player.library) > 0 and len(player.library) >= amount:
        for i in range(amount):
            card = player.library.pop(0)
            player.hand.cards.append(card)
            if len(player.emblems) > 0:
                for emblem in player.emblems:
                    if emblem.__class__.__name__ == 'Teferi_Emblem':
                        render(player, opponent, None, None, ORDER)
                        if emblem.exile.select_target(opponent, player) is not None:
                            emblem.exile.activate(opponent, player, ORDER)
            player.cards_drawn += 1
            if player.cards_drawn == 2:
                for creature in opponent.battlefield.creatures:
                    if creature.__class__.__name__ == 'Faerie_Mastermind':
                        creature.draw.activate(opponent, player, ORDER)
    else:
        player.lose_game()

def discard(player, opponent, ORDER):
    loop = True
    selected = None
    while loop:
        selected = select_card(player)
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                if selected is not None:
                    player.hand.cards.remove(selected)
                    player.graveyard.insert(0, selected)
                    loop = False
        render(player, opponent, selected, None, ORDER)
        check_graveyards(player, opponent)

def shuffle_library(player):
        random.shuffle(player.library)

def untap(player):
    player.land_counter = 1
    for land in player.battlefield.lands:
        land.untap()
    for creature in player.battlefield.creatures:
        creature.untap()
        creature.sickness = False
    for other in player.battlefield.others:
        other.untap()

def declare_attackers(player, opponent, ORDER):
    ORDER.PRIORITY = ''
    render(player, opponent, None, None, ORDER)
    render_message('Press return to declare an attacker!')
    pygame.display.update()
    loop1 = True
    while loop1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                attacker = None
                mouse_pos = pygame.mouse.get_pos()
                x, y = PLAYER_BATTLEFIELD_X, PLAYER_BATTLEFIELD_Y
                for creature in player.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        attacker = creature
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
                if attacker is not None:
                    if not attacker.tapped and not attacker.sickness:
                        render_message('Press return to select attackee!')
                        pygame.display.update()
                        loop2 = True
                        while loop2:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                                elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                                    mouse_pos = pygame.mouse.get_pos()
                                    x, y = OPPONENT_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                                    for other in opponent.battlefield.others:
                                        rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                                        if rect.collidepoint(mouse_pos):
                                            attacker.target = other
                                        x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE
                                    if attacker.target is None:
                                        attacker.target = opponent
                                    attacker.attack()
                                    loop2 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                loop1 = False
                    
        render(player, opponent, None, None, ORDER)
    ORDER.PRIORITY = player.player

    for thief in player.battlefield.creatures:
        if thief.__class__.__name__ == 'Soaring_Thought_Thief':
            rogue_attacks = False
            for creature in player.battlefield.creatures:
                if not rogue_attacks:
                    if creature.attacking:
                        for type in creature.types:
                            if type == 'Rogue':
                                thief.mill.activate(player, opponent, ORDER)
                                rogue_attacks = True
                else:
                    break
                            
def declare_blockers(player, opponent, ORDER):
    ORDER.PRIORITY = ''
    loop1 = True
    while loop1:
        render(player, opponent, None, None, ORDER)
        render_message('Press enter to declare a blocker!')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                blocker = None
                mouse_pos = pygame.mouse.get_pos()
                x, y = PLAYER_BATTLEFIELD_X, PLAYER_BATTLEFIELD_Y
                for creature in player.battlefield.creatures:
                    rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                    if rect.collidepoint(mouse_pos):
                        blocker = creature
                    x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
                if blocker is not None:
                    if not blocker.tapped:
                        loop2 = True
                        while loop2:
                            render(player, opponent, None, None, ORDER)
                            render_message('Press return to select an attacker!')
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                                elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                                    attacker = None
                                    mouse_pos = pygame.mouse.get_pos()
                                    x, y = OPPONENT_BATTLEFIELD_X, OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
                                    for creature in opponent.battlefield.creatures:
                                        rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
                                        if rect.collidepoint(mouse_pos) and ((creature.flying ^ blocker.flying) or (not creature.flying and blocker.flying)):
                                            attacker = creature
                                        x += PERMANENT_WIDTH + BATTLEFIELD_SPACE
                                    if attacker is not None:
                                        blocker.block(attacker)
                                    loop2 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                loop1 = False

        render(player, opponent, None, None, ORDER)
    ORDER.PRIORITY = opponent.player

def combat_damage(player, opponent):
    for creature in player.battlefield.creatures:
        if creature.target is not None:
            creature.deal_damage(creature.target)
    for creature in opponent.battlefield.creatures:
        if creature.target is not None:
            creature.deal_damage(creature.target)
    
def end_combat(player):
    for creature in player.battlefield.creatures:
        creature.attacking = False
        creature.target = None
        creature.blocked = None
        creature.blocking = False  
        creature.is_blocked = False

def clean_up(player, opponent, ORDER):
    player.cards_drawn = 0
    for creature in player.battlefield.creatures:
        creature.heal()
    for other in player.battlefield.others:
        if issubclass(other.__class__, Planeswalker):
            other.activated = False
    if player.turn:
        while len(player.hand.cards) > 7:
            discard(player, opponent, ORDER)

def play_card(player, opponent, selected, ORDER):
    if issubclass(selected.__class__, Land):
        try:
            if ((ORDER.PHASE != 'Main phase 1') and (ORDER.PHASE != 'Main phase 2')) or (not player.turn) or len(ORDER.STACK) != 0:
                raise ValueError('WAIT FOR YOUR MAIN PHASE!')
            elif player.land_counter == 0:
                raise ValueError("YOU'VE ALREADY PLAYED YOUR LAND FOR THE TURN!")
            player.land_counter -= 1
            player.battlefield.lands.append(selected)
            player.hand.cards.remove(selected)
            selected.enter(player, opponent, ORDER)
            for crab in player.battlefield.creatures:
                if crab.__class__.__name__ == 'Ruin_Crab':
                    crab.landfall.activate(player, opponent, ORDER)

        except ValueError as error:
            render_message(str(error))
            pygame.display.update()
            time.sleep(1)
            
def cast_card(player, opponent, selected, ORDER):
    try:
        if ((not selected.flash) and (ORDER.PHASE != 'Main phase 1' and ORDER.PHASE != 'Main phase 2')):
            raise ValueError('WAIT FOR YOUR MAIN PHASE!')
        elif selected.targeted:
            if selected.select_target(player, opponent, ORDER) is None:
                raise ValueError('Select a valid target!')
            
        if player.mana_pool.spend_mana(selected.mana_cost):
            ORDER.STACK.insert(0, selected)
            player.hand.cards.remove(selected)
    
    except ValueError as error:
        render(player, opponent, selected, None, ORDER)
        render_message(str(error))
        pygame.display.update()
        time.sleep(1)

def win_game(player, opponent):
    pass

def lose_game(player, opponent):
    pass

def check_graveyards(player, opponent):
    for creature in player.battlefield.creatures:
            creature.powerup = 0
            creature.toughnessup = 0
            if creature.__class__.__name__ == 'Thieves_Guild_Enforcer':
                creature.deathtouch = False
    for creature in player.battlefield.creatures:
        if creature.__class__.__name__ == 'Thieves_Guild_Enforcer':
            creature.enforce(opponent)
        elif creature.__class__.__name__ == 'Nighthawk_Scavenger':
            creature.scavenge(opponent)
        elif creature.__class__.__name__ == 'Soaring_Thought_Thief':
            creature.steal_thoughts(player, opponent)
    for card in player.hand.cards:
        if card.__class__.__name__ == 'Into_the_Story':
            card.cost_reduction(opponent)
    for card in player.library:
        if card.__class__.__name__ == 'Into_the_Story':
            card.cost_reduction(opponent)

    for creature in opponent.battlefield.creatures:
        creature.powerup = 0
        creature.toughnessup = 0
        if creature.__class__.__name__ == 'Thieves_Guild_Enforcer':
            creature.deathtouch = False
    for creature in opponent.battlefield.creatures:
        if creature.__class__.__name__ == 'Thieves_Guild_Enforcer':
            creature.enforce(player)
        elif creature.__class__.__name__ == 'Nighthawk_Scavenger':
            creature.scavenge(player)
        elif creature.__class__.__name__ == 'Soaring_Thought_Thief':
            creature.steal_thoughts(opponent, player)
    for card in opponent.hand.cards:
        if card.__class__.__name__ == 'Into_the_Story':
            card.cost_reduction(player)
    for card in opponent.library:
        if card.__class__.__name__ == 'Into_the_Story':
            card.cost_reduction(player)