import pygame
import random


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
winner = None 

# Estados de animação
animating_dice = False
animation_start_time = 0
animation_duration = 800
temp_dice_value = 1

# Estado do Jogo
game_active = True

# Animação do Dado
def update_dice_animation():
    global animating_dice , temp_dice_value, dice_value , animation_start_time

    if animating_dice :
        elapsed = pygame.time.get_ticks() - animation_start_time
        
        if elapsed < animation_duration:
            temp_dice_value = random.randint(1,6)
        else:
            
            animating_dice = False

# Desenhando a Tela
def draw_ui():
    screen.fill(BACKGROUND_COLOR)

    # PLACAR
    score_text = font.render(f"Jogador 1 : {players_score[0]}", True, TEXT_COLOR)
    screen.blit(score_text, (50,30))

    score_text2 = font.render(f"Jogador 2 : {players_score[1]}", True, TEXT_COLOR)
    screen.blit(score_text2, (50,80))

    # Pontuação da Rodada
    if animating_dice is not None:
        round_text = small_font.render(f"Pontos da Rodada : {current_round_score}", True, (255,255,0))
        screen.blit(round_text, (50,140))

    # Turno do Jogador
    turn_text = small_font.render(f"Vez do Jogador {current_player}", True , (0,255,0))
    screen.blit(turn_text, (50,180))

    # Exibir valor do dado
    if animating_dice or dice_value is not None:
        value_to_show = temp_dice_value if animating_dice else dice_value 
        x = WIDTH // 2 - 50 
        y = HEIGHT //2 - 50
        screen.blit(dice_images[value_to_show - 1 ] , (x,y))

    # Exibir Vitoria 
    if not game_active and winner is not None:
        win_text = font.render(f"Jogador {winner} Venceu !! ", True, (0, 255, 0))
        screen.blit(win_text , (WIDTH // 2 -100 , HEIGHT // 2 - 30))

    # Botao "Roll"
    button_rect = pygame.Rect(50, 500, 150, 50)
    pygame.draw.rect(screen, BUTTON_HOVER_COLOR if pygame.mouse.get_pos()[0] in range(50,200) and pygame.mouse.get_pos()[1] in range (500,550) else BUTTON_COLOR, button_rect)
    roll_text = small_font.render("Rolar" , True , (0,0,0))
    screen.blit(roll_text, (95,510))

    # Botão "Parar"
    stop_button_rect = pygame.Rect(250 , 500 , 150, 50)
    stop_hover = pygame.mouse.get_pos()[0] in range(250 ,400) and pygame.mouse.get_pos()[1] in range (500,550)
    pygame.draw.rect(screen, BUTTON_HOVER_COLOR if stop_hover else BUTTON_COLOR, stop_button_rect)
    stop_text = font.render("Parar", True, (0,0,0))
    screen.blit(stop_text,  (295,510))



# Carregar imanges
dice_images = []
for i in range(1,7):
    image_path = f"assets/dice_{i}.png"
    try:
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (100,100))
        dice_images.append(image)
    except FileNotFoundError:
        print(f"Imagem não encontrada : {image_path}")
        pygame.quit()
        exit()

# LOOP Principal do Jogo

running = True
while running:
    update_dice_animation()
    draw_ui()
    pygame.display.flip() #Atualiza a Tela
    clock.tick(60) #Limita 60FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
         # verificar click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            # Verificar se clicou do "Rolar"
            if 50 < mouse_pos[0] < 200 and 500 < mouse_pos[1] < 550 :
                print("Botão 'Rolar' Clicado")

                # Rola o dado
                dice_value = random.randint(1,6) 
                animating_dice = True
                animation_start_time = pygame.time.get_ticks()
                temp_dice_value = 1 

                # Se tirar 1 Perde os pontos e muda o turno
                if dice_value == 1:
                    current_round_score = 0 
                    current_player = 2 if current_player == 1 else 1
                else:
                    current_round_score += dice_value
            elif 250 < mouse_pos[0] < 400 and 500 < mouse_pos[1] < 550 :
                print("Botar 'Parar' Clicado")

                # Soma os pontos da rodada ao jogador atual
                players_score[current_player - 1] += current_round_score
                current_round_score = 0 
                # Verifica Vitoria
                if players_score[current_player - 1] >= 50:
                    winner = current_player
                    game_active = False
                    dice_value = None

                # Troca de Jogador 
                current_player = 2 if current_player == 1 else 1