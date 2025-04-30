import pygame


# Inicializa o pygame 
pygame.init()

# Configurações de tela
WIDTH , HEIGHT = 800 , 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pig Dice Game")

# Cores
BACKGROUND_COLOR = (40,40,40)
TEXT_COLOR = (255,255,255)
BUTTON_COLOR = (70,30,180)
BUTTON_HOVER_COLOR = (100,160,200)

# Fontes
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont (None, 36)

# Relogio
clock = pygame.time.Clock()

# Variaveis do jogo 
current_player = 1 
players_score = [0,0]
current_round_score = 0
dice_value = None

# Estado do Jogo
game_active = True


# Desenhando a Tela
def draw_ui():
    screen.fill(BACKGROUND_COLOR)

    # PLACAR
    score_text = font.render(f"Jogador 1 : {players_score[0]}", True, TEXT_COLOR)
    screen.blit(score_text, (50,30))

    score_text2 = font.render(f"Jogador 2 : {players_score[1]}", True, TEXT_COLOR)
    screen.blit(score_text2, (50,80))

    # Pontuação da Rodada
    round_text = small_font.render(f"Pontos da Rodada : {current_round_score}", True, (255,255,0))
    screen.blit(round_text, (50,140))

    # Turno do Jogador
    turn_text = small_font.render(f"Vez do Jogador {current_player}", True , (0,255,0))
    screen.blit(turn_text, (50,180))

    # Botao "Roll"
    button_rect = pygame.Rect(50, 500, 150, 50)
    pygame.draw.rect(screen, BUTTON_HOVER_COLOR if pygame.mouse.get_pos()[0] in range(50,200) and pygame.mouse.get_pos()[1] in range (500,550) else BUTTON_COLOR, button_rect)
    roll_text = small_font.render("Rolar" , True , (0,0,0))
    screen.blit(roll_text, (95,510))



# LOOP Principal do Jogo

running = True
while running:
    draw_ui()
    pygame.display.flip() #Atualiza a Tela
    clock.tick(60) #Limita 60FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False