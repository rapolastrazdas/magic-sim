import pygame
from pygame.locals import *
from grobal import *
from card import *

def render(player, opponent, card, Nothing, ORDER):
    global SCREEN

    arena = pygame.image.load('Battlefield.jpg').convert()
    arena = pygame.transform.smoothscale(arena, (SCREEN_WIDTH, SCREEN_HEIGHT))
    SCREEN.blit(arena, (0, 0))
    render_libraries(player, opponent)
    render_battlefields(player, opponent)
    render_hands(player, opponent, card)
    render_graveyards(player, opponent)
    render_lives(player, opponent)
    render_mana_pools(player, opponent)
    render_phase(ORDER.PRIORITY, ORDER.TURN, ORDER.PHASE)
    render_stack(ORDER.STACK)
    pygame.display.update()

def render_hands(player, opponent, selected): 
    global SCREEN

    if len(player.hand.cards) > 6:
        x = PLAYER_HAND_X
        spacing = (PLAYER_HAND_WIDTH - PLAYER_CARD_WIDTH * len(player.hand.cards)) / (len(player.hand.cards) - 1)
    else:
        x = SCREEN_WIDTH/2 - PLAYER_CARD_WIDTH/2 * len(player.hand.cards)
        spacing = 5
    y = PLAYER_HAND_Y
    for card in player.hand.cards:
        art = pygame.image.load(card.art).convert()
        art = pygame.transform.smoothscale(art, (PLAYER_CARD_WIDTH, PLAYER_CARD_HEIGHT))
        
        if card is selected:
            SCREEN.blit(art, (x, y - PLAYER_CARD_HEIGHT / 4))
        else:
            SCREEN.blit(art, (x, y))
        x += PLAYER_CARD_WIDTH + spacing

    if len(opponent.hand.cards) > 6:
        x = OPPONENT_HAND_X
        spacing = (OPPONENT_HAND_WIDTH - OPPONENT_CARD_WIDTH * len(opponent.hand.cards)) / (len(opponent.hand.cards) - 1)
    else:
        x = SCREEN_WIDTH/2 - OPPONENT_HAND_WIDTH/2 - OPPONENT_CARD_WIDTH/2 * (len(opponent.hand.cards) - 1)
        spacing = 5
    y = OPPONENT_HAND_Y
    for card in opponent.hand.cards:
        art = pygame.image.load('Card_Back.jpg').convert()
        art = pygame.transform.rotate(art, 180)
        art = pygame.transform.smoothscale(art, (OPPONENT_CARD_WIDTH, OPPONENT_CARD_HEIGHT))
        SCREEN.blit(art, (x, y))
        x += OPPONENT_CARD_WIDTH + spacing

def render_stack(STACK):
    global SCREEN

    if len(STACK) > 0:
        surface = pygame.Surface((SCREEN_WIDTH, PLAYER_CARD_HEIGHT+40), pygame.SRCALPHA)
        pygame.draw.rect(surface, (0, 0, 0, 128), (0, 0, SCREEN_WIDTH, PLAYER_CARD_HEIGHT+40))
        SCREEN.blit(surface, (0, STACK_Y-20))

    x, y = STACK_X, STACK_Y
    for object in STACK:
        art = pygame.image.load(object.art).convert()
        art = pygame.transform.smoothscale(art, (PLAYER_CARD_WIDTH, PLAYER_CARD_HEIGHT))
        x += PLAYER_CARD_WIDTH

        SCREEN.blit(art, (x, y))

def render_libraries(player, opponent):
    global SCREEN

    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.Font('Beleren2016-Bold.ttf', 30)

    player_library = pygame.image.load('Card_Back.jpg').convert()
    player_library = pygame.transform.smoothscale(player_library, (PLAYER_DECK_WIDTH, PLAYER_DECK_HEIGHT))

    if len(player.library) > 0:
        SCREEN.blit(player_library, (PLAYER_DECK_X, PLAYER_DECK_Y))

    player_rect = pygame.Rect(PLAYER_DECK_X, PLAYER_DECK_Y, PLAYER_DECK_WIDTH, PLAYER_DECK_HEIGHT)
    if player_rect.collidepoint(mouse_pos):
        player_text = font.render(str(len(player.library)), True, (255, 255, 255))
        SCREEN.blit(player_text, (PLAYER_DECK_X, PLAYER_DECK_Y))

    opponent_library = pygame.image.load('Card_Back.jpg').convert()
    opponent_library = pygame.transform.smoothscale(opponent_library, (OPPONENT_DECK_WIDTH, OPPONENT_DECK_HEIGHT))

    if len(opponent.library) > 0:
        SCREEN.blit(opponent_library, (OPPONENT_DECK_X, OPPONENT_DECK_Y))

    opponent_rect = pygame.Rect(OPPONENT_DECK_X, OPPONENT_DECK_Y, OPPONENT_DECK_WIDTH, OPPONENT_DECK_HEIGHT)
    if opponent_rect.collidepoint(mouse_pos):
        opponent_text = font.render(str(len(opponent.library)), True, (255, 255, 255))
        SCREEN.blit(opponent_text, (OPPONENT_DECK_X, OPPONENT_DECK_Y))

def render_graveyards(player, opponent):
    global SCREEN

    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.Font('Beleren2016-Bold.ttf', 30)

    if len(player.graveyard) > 0:
        player_graveyard = pygame.image.load(player.graveyard[0].art).convert()
        player_graveyard = pygame.transform.smoothscale(player_graveyard, (PLAYER_GRAVE_WIDTH, PLAYER_GRAVE_HEIGHT))
        SCREEN.blit(player_graveyard, (PLAYER_GRAVE_X, PLAYER_GRAVE_Y))

    player_rect = pygame.Rect(PLAYER_GRAVE_X, PLAYER_GRAVE_Y, PLAYER_GRAVE_WIDTH, PLAYER_GRAVE_HEIGHT)
    if player_rect.collidepoint(mouse_pos):
        player_text = font.render(str(len(player.graveyard)), True, (255, 255, 255))
        SCREEN.blit(player_text, (PLAYER_GRAVE_X, PLAYER_GRAVE_Y))

    
    if len(opponent.graveyard) > 0:
        opponent_graveyard = pygame.image.load(opponent.graveyard[0].art).convert()
        opponent_graveyard = pygame.transform.smoothscale(opponent_graveyard, (OPPONENT_GRAVE_WIDTH, OPPONENT_GRAVE_HEIGHT))
        SCREEN.blit(opponent_graveyard, (OPPONENT_GRAVE_X, OPPONENT_GRAVE_Y))

    opponent_rect = pygame.Rect(OPPONENT_GRAVE_X, OPPONENT_GRAVE_Y, OPPONENT_GRAVE_WIDTH, OPPONENT_GRAVE_HEIGHT)
    if opponent_rect.collidepoint(mouse_pos):
        opponent_text = font.render(str(len(opponent.graveyard)), True, (255, 255, 255))
        SCREEN.blit(opponent_text, (OPPONENT_GRAVE_X, OPPONENT_GRAVE_Y))

def render_battlefields(player, opponent):
    global SCREEN

    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.Font('Beleren2016-Bold.ttf', 30)

    # Render my battlefield
    x = PLAYER_BATTLEFIELD_X
    y = PLAYER_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
    for land in player.battlefield.lands:
        art = pygame.image.load(land.art).convert()
        if land.tapped:
            art = pygame.transform.rotate(art, -10)
        art = pygame.transform.smoothscale(art, (PERMANENT_WIDTH, PERMANENT_HEIGHT))
        SCREEN.blit(art, (x, y))
        x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    x = PLAYER_BATTLEFIELD_X
    y = PLAYER_BATTLEFIELD_Y
    for creature in player.battlefield.creatures:
        art = pygame.image.load(creature.art).convert()
        if creature.tapped:
            art = pygame.transform.rotate(art, -10)
        art = pygame.transform.smoothscale(art, (PERMANENT_WIDTH, PERMANENT_HEIGHT))
        if creature.attacking:
            SCREEN.blit(art, (x, y - PERMANENT_HEIGHT / 6))
        elif creature.blocking:
            SCREEN.blit(art, (x, y + PERMANENT_HEIGHT / 6))
        else:
            SCREEN.blit(art, (x, y))
        rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
        if rect.collidepoint(mouse_pos):
            font = pygame.font.Font('Beleren2016-Bold.ttf', 20)
            text = font.render(f'{creature.power + creature.powerup + creature.counters}/{creature.toughness + creature.toughnessup + creature.counters}', True, 'White')
            SCREEN.blit(text, (PERMANENT_WIDTH+x - 25, PERMANENT_HEIGHT+y))
        x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    x = PLAYER_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH
    y = PLAYER_BATTLEFIELD_Y
    for other in player.battlefield.others:
        art = pygame.image.load(other.art).convert()
        if other.tapped:
            art = pygame.transform.rotate(art, -10)
        art = pygame.transform.smoothscale(art, (PERMANENT_WIDTH, PERMANENT_HEIGHT))
        SCREEN.blit(art, (x, y))
        if issubclass(other.__class__, Planeswalker):
            rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
            font = pygame.font.Font('Beleren2016-Bold.ttf', 30)
            if rect.collidepoint(mouse_pos):
                text = font.render(str(other.loyalty), True, 'White')
                SCREEN.blit(text, (PERMANENT_WIDTH+x - 25, PERMANENT_HEIGHT+y))
        x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE

    # Render opponents battlefield
    x = OPPONENT_BATTLEFIELD_X
    y = OPPONENT_BATTLEFIELD_Y 
    for land in opponent.battlefield.lands:
        art = pygame.image.load(land.art).convert()
        if land.tapped:
            art = pygame.transform.rotate(art, -10)
        art = pygame.transform.smoothscale(art, (PERMANENT_WIDTH, PERMANENT_HEIGHT))
        SCREEN.blit(art, (x, y))
        x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    x = OPPONENT_BATTLEFIELD_X
    y = OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
    for creature in opponent.battlefield.creatures:
        art = pygame.image.load(creature.art).convert()
        if creature.tapped:
            art = pygame.transform.rotate(art, -10)
        art = pygame.transform.smoothscale(art, (PERMANENT_WIDTH, PERMANENT_HEIGHT))
        if creature.attacking:
            SCREEN.blit(art, (x, y + PERMANENT_HEIGHT / 6))
        elif creature.blocking:
            SCREEN.blit(art, (x, y - PERMANENT_HEIGHT / 6))
        else:
            SCREEN.blit(art, (x, y))
        rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
        if rect.collidepoint(mouse_pos):
            font = pygame.font.Font('Beleren2016-Bold.ttf', 20)
            text = font.render(f'{creature.power + creature.powerup + creature.counters}/{creature.toughness + creature.toughnessup + creature.counters}', True, 'White')
            SCREEN.blit(text, (PERMANENT_WIDTH+x - 25, PERMANENT_HEIGHT+y))
        x += PERMANENT_WIDTH + BATTLEFIELD_SPACE

    x = OPPONENT_BATTLEFIELD_X + BATTLEFIELD_WIDTH - PERMANENT_WIDTH
    y = OPPONENT_BATTLEFIELD_Y + PERMANENT_HEIGHT + 20
    for other in opponent.battlefield.others:
        art = pygame.image.load(other.art).convert()
        art = pygame.transform.smoothscale(art, (PERMANENT_WIDTH, PERMANENT_HEIGHT))
        SCREEN.blit(art, (x, y))
        if issubclass(other.__class__, Planeswalker):
            rect = pygame.Rect(x, y, PERMANENT_WIDTH, PERMANENT_HEIGHT)
            font = pygame.font.Font('Beleren2016-Bold.ttf', 30)
            if rect.collidepoint(mouse_pos):
                text = font.render(str(other.loyalty), True, 'White')
                SCREEN.blit(text, (PERMANENT_WIDTH+x - 25, PERMANENT_HEIGHT+y))
        x -= PERMANENT_WIDTH - BATTLEFIELD_SPACE

def render_lives(player, opponent):
    global SCREEN

    font = pygame.font.Font('Beleren2016-Bold.ttf', 60)

    player_life_total = font.render(str(player.life_total), True, 'Green')
    SCREEN.blit(player_life_total, (PLAYER_LIFE_X, PLAYER_LIFE_Y))

    opponent_life_total = font.render(str(opponent.life_total), True, 'Red')
    SCREEN.blit(opponent_life_total, (OPPONENT_LIFE_X, OPPONENT_LIFE_Y))

def render_mana_pools(player, opponent):
    global SCREEN

    font = pygame.font.Font('Beleren2016-Bold.ttf', 20)

    white = font.render(str(player.mana_pool.pool['white']), True, 'White')
    blue = font.render(str(player.mana_pool.pool['blue']), True, 'Blue')
    black = font.render(str(player.mana_pool.pool['black']), True, 'Black')
    red = font.render(str(player.mana_pool.pool['red']), True, 'Red')
    green = font.render(str(player.mana_pool.pool['green']), True, 'Green')
    generic = font.render(str(player.mana_pool.pool['generic']), True, 'Gray')

    x, y = PLAYER_MANA_POOL_X, PLAYER_MANA_POOL_Y
    if player.mana_pool.pool['white'] > 0:
        SCREEN.blit(white, (x, y))
        y += 15
    if player.mana_pool.pool['blue'] > 0:
        SCREEN.blit(blue, (x, y))
        y += 15
    if player.mana_pool.pool['black'] > 0:
        SCREEN.blit(black, (x, y))
        y += 15
    if player.mana_pool.pool['red'] > 0:
        SCREEN.blit(red, (x, y))
        y += 15
    if player.mana_pool.pool['green'] > 0:
        SCREEN.blit(green, (x, y))
        y += 15
    if player.mana_pool.pool['generic'] > 0:
        SCREEN.blit(generic, (x, y))
        y += 15

    white = font.render(str(opponent.mana_pool.pool['white']), True, 'White')
    blue = font.render(str(opponent.mana_pool.pool['blue']), True, 'Blue')
    black = font.render(str(opponent.mana_pool.pool['black']), True, 'Black')
    red = font.render(str(opponent.mana_pool.pool['red']), True, 'Red')
    green = font.render(str(opponent.mana_pool.pool['green']), True, 'Green')
    generic = font.render(str(opponent.mana_pool.pool['generic']), True, 'Gray')
    
    x, y = OPPONENT_MANA_POOL_X, OPPONENT_MANA_POOL_Y
    if opponent.mana_pool.pool['white'] > 0:
        SCREEN.blit(white, (x, y))
        y += 15
    if opponent.mana_pool.pool['blue'] > 0:
        SCREEN.blit(blue, (x, y))
        y += 15
    if opponent.mana_pool.pool['black'] > 0:
        SCREEN.blit(black, (x, y))
        y += 15
    if opponent.mana_pool.pool['red'] > 0:
        SCREEN.blit(red, (x, y))
        y += 15
    if opponent.mana_pool.pool['green'] > 0:
        SCREEN.blit(green, (x, y))
        y += 15
    if opponent.mana_pool.pool['generic'] > 0:
            SCREEN.blit(generic, (x, y))
            y += 15

def render_phase(PRIORITY, TURN, PHASE):
    global SCREEN

    font = pygame.font.Font('Beleren2016-Bold.ttf', 35)
    if PRIORITY == 'Player 1':
        color = 'Blue'
    elif PRIORITY == 'Player 2':
        color = 'Red'
    else:
        color = 'White'
    phase_text = font.render(f'{TURN} {PHASE}', True, color)
    SCREEN.blit(phase_text, (PHASE_X, PHASE_Y))

def render_message(message):
    global SCREEN
    font = font = pygame.font.Font('Beleren2016-Bold.ttf', 24)
    text = font.render(message, True, 'White') 
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT / 3))
    SCREEN.blit(text, rect)