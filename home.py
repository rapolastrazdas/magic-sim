import pygame
from sys import exit

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900

# Initialize Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Magic: the Gathering")
clock = pygame.time.Clock()

def menu_home(state):
    background = pygame.image.load('UI Graphics\INTROPIC.jpg').convert()
    screen.blit(background, (0, 0))

    # Define button properties
    button_width = 300
    button_height = 100
    button_margin = 20
    button_font = pygame.font.Font(None, 36)

    # Create singleplayer button
    button_singleplayer = pygame.Surface((button_width, button_height))
    button_singleplayer.fill('Blue')
    button_singleplayer_text = button_font.render("Singleplayer", True, (255, 255, 255))
    button_singleplayer_text_rect = button_singleplayer_text.get_rect(center=button_singleplayer.get_rect().center)

    # Create multiplayer button
    button_multiplayer = pygame.Surface((button_width, button_height))
    button_multiplayer.fill('Blue')
    button_multiplayer_text = button_font.render("Multiplayer", True, (255, 255, 255))
    button_multiplayer_text_rect = button_multiplayer_text.get_rect(center=button_multiplayer.get_rect().center)

    # Draw singleplayer button
    button_singleplayer_rect = button_singleplayer.get_rect(topleft=(550, 500))
    screen.blit(button_singleplayer, button_singleplayer_rect)
    screen.blit(button_singleplayer_text, button_singleplayer_text_rect.move(button_singleplayer_rect.x, button_singleplayer_rect.y))

    # Draw multiplayer button
    button_multiplayer_rect = button_multiplayer.get_rect(topleft=(550, 650))
    screen.blit(button_multiplayer, button_multiplayer_rect)
    screen.blit(button_multiplayer_text, button_multiplayer_text_rect.move(button_multiplayer_rect.x, button_multiplayer_rect.y))

    while state == 'home':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_singleplayer.get_rect(topleft=(550, 500)).collidepoint(pygame.mouse.get_pos()):
                    state = 'deck_select'
                    return state
                elif button_multiplayer.get_rect(topleft=(550, 650)).collidepoint(pygame.mouse.get_pos()):
                    exit()

        pygame.display.update()
        clock.tick(60)


def menu_deck_select(state):

    background = pygame.image.load('UI Graphics\BACKDECKSELECT.jpg').convert()
    screen.blit(background, (0, 0))

    button_red = pygame.Surface((300, 500))
    button_red.fill('Blue')

    button_dimir = pygame.Surface((300, 500))
    button_dimir.fill('Blue')

    button_azorius = pygame.Surface((300, 500))
    button_azorius.fill('Blue')

    button_red_rect = button_red.get_rect(topleft=(150, 200))
    screen.blit(button_red, button_red_rect)

    button_dimir_rect = button_dimir.get_rect(topleft=(550, 200))
    screen.blit(button_dimir, button_dimir_rect)

    button_azorius_rect = button_azorius.get_rect(topleft=(950, 200))
    screen.blit(button_azorius, button_azorius_rect)

    while state == 'deck_select':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_red_rect.get_rect(topleft=(150, 200)).collidepoint(pygame.mouse.get_pos()):
                    exit()
                elif button_dimir_rect.get_rect(topleft=(550, 200)).collidepoint(pygame.mouse.get_pos()):
                    exit()
                elif button_azorius_rect.get_rect(topleft=(950, 200)).collidepoint(pygame.mouse.get_pos()):
                    exit()

        

        pygame.display.update()
        clock.tick(60)

state = 'home'

while True:
    if state == 'home': 
        state = menu_home(state)
    elif state == 'deckselect':
        state = menu_deck_select(state)

