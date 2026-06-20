from actions import *
from collections import Counter

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_size = 7

class Battlefield:
    def __init__(self):
        self.creatures = []
        self.lands = []
        self.others = []

class ManaPool:
    def __init__(self):
        self.pool = Counter({'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'green': 0, 'generic': 0})

    def add_mana(self, mana):
        self.pool += mana

    def spend_mana(self, mana_cost):
        try:
            remaining_pool = self.pool.copy()
            generic_cost = mana_cost['generic']
            if(sum(mana_cost.values()) > sum(remaining_pool.values())):
                raise ValueError(f'NOT ENOUGH MANA!')

            for color, amount in mana_cost.items():
                if color != 'generic':
                    if remaining_pool[color] >= amount:
                        remaining_pool[color] -= amount
                    else:
                        raise ValueError(f'NOT ENOUGH COLORED MANA!')

            for color in remaining_pool.keys():
                while remaining_pool[color] > 0 and generic_cost > 0:
                    remaining_pool[color] -= 1
                    generic_cost -= 1
            self.pool = remaining_pool
            return True

        except ValueError as error:
            render_message(str(error))
            pygame.display.update()
            time.sleep(1)
            return False
    
class Player:
    def __init__(self, player):
        self.player = player
        self.turn = False
        self.priority = False

        self.life_total = 20
        self.hand = Hand()
        self.cards_drawn = 0
        self.library = []
        self.graveyard = []
        self.battlefield = Battlefield()
        self.emblems = []
        self.land_counter = 1
        self.mana_pool = ManaPool()

        self.teferi_untap = False

    def take_damage(self, source):
        if issubclass(source.__class__, Creature):
            amount = source.power + source.powerup + source.counters
        else:
            amount = source
        self.life_total -= amount
        if self.life_total <= 0:
            self.lose_game()
    
    def reset(self):
        self.life_total = 20
        self.hand = Hand()
        self.library = []
        self.graveyard = []
        self.battlefield = Battlefield()
        self.land_counter = 1
        self.mana_pool = ManaPool()

    def lose_game(self):
        loop = True
        while loop:
            arena = pygame.image.load('Battlefield.jpg').convert()
            arena = pygame.transform.smoothscale(arena, (SCREEN_WIDTH, SCREEN_HEIGHT))
            SCREEN.blit(arena, (0, 0))
            surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(surface, (0, 0, 0, 64), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            SCREEN.blit(surface, (0, 0))

            if self.player == 'Player 1':
                color = 'Red'
            else:
                color = 'Blue'
            font = font = pygame.font.Font('Beleren2016-Bold.ttf', 80)
            text = font.render('VICTORY!', True, color) 
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            SCREEN.blit(text, rect)
            pygame.display.update()

            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        exit()
            


        