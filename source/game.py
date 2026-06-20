from sys import exit
from azorius import *
from rogues import *
from player import Player

pygame.init()
pygame.display.set_caption("Magic: the Gathering")

hero = Player('Player 1')
villain = Player('Player 2')

selected_card = None
selected_permanent = None

def take_turn(player, opponent, ORDER):
    global SCREEN
    global CLOCK

    if ORDER.PHASE == 'Untap':
        untap(player)
    elif ORDER.PHASE == 'Draw':
        draw(player, opponent, ORDER.STACK)
    elif ORDER.PHASE == 'Declare attackers' and len(player.battlefield.creatures) != 0:
        declare_attackers(player, opponent, ORDER)
    elif ORDER.PHASE == 'Declare blockers'and len(opponent.battlefield.creatures) != 0:
        declare_blockers(opponent, player, ORDER)
    elif ORDER.PHASE == 'Combat damage':
        combat_damage(player, opponent)
    elif ORDER.PHASE == 'Main phase 2':
        end_combat(player)
        end_combat(opponent)
    elif ORDER.PHASE == 'End step':
        if player.teferi_untap:
            tef_untap = Teferi_Untap(player.player)
            tef_untap.activate(player, opponent, ORDER)
            player.teferi_untap = False

    phase = ORDER.PHASE
    while phase == ORDER.PHASE:
        while player.priority:
            play(player, opponent, ORDER)
            card = select_card(player)
            permanent = select_activate(player, opponent)
            render(player, opponent, card, permanent, ORDER)
            CLOCK.tick(60)
        while opponent.priority:
            play(opponent, player, ORDER)
            card = select_card(opponent)
            permanent = select_activate(opponent, player)
            render(opponent, player, card, permanent, ORDER)
            CLOCK.tick(60)

    if ORDER.PHASE == 'Clean up':
        clean_up(player, opponent, ORDER)
        clean_up(opponent, player, ORDER)
        ORDER.PHASE = 'Untap'
        opponent.turn = True
        player.turn = False

    player.mana_pool.pool = Counter({'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'green': 0, 'generic': 0})
    opponent.mana_pool.pool = Counter({'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'green': 0, 'generic': 0})

def play(player, opponent, ORDER):
    global SCREEN
    global CLOCK

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass_priority(player, opponent, ORDER)
                if player.priority:
                    ORDER.PRIORITY = player.player
                else:
                    ORDER.PRIORITY = opponent.player
                if player.turn:
                    ORDER.TURN = player.player
                else:
                    ORDER.TURN = opponent.player
            elif event.key == pygame.K_RETURN:
                card = select_card(player)
                if card is not None:
                    if issubclass(card.__class__, Land):
                        play_card(player, opponent, card, ORDER)
                    else:
                        cast_card(player, opponent, card, ORDER)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            permanent = select_activate(player, opponent)
            if permanent is not None:
                permanent.activate(player, opponent, ORDER)

hero.reset()
dimir_decklist(hero)
shuffle_library(hero)

villain.reset()
azorius_decklist(villain)
shuffle_library(villain)

hero.turn = True
hero.priority = True
draw(hero, villain, ORDER.STACK, 7)
draw(villain, hero, ORDER.STACK, 7)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()   

    if hero.turn:
        turn = hero.player
        take_turn(hero, villain, ORDER)

    elif villain.turn:
        turn = villain.player
        take_turn(villain, hero, ORDER)

pygame.quit()