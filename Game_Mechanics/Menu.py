import pygame
from Basic_Things import Colors
from Game_Mechanics import SingleMenu

def run_game(player1, player2):
    # Screen
    Window_Width = 580
    Window_Hight = 550
    size = (Window_Width, Window_Hight)
    # #BACKGROUND_IMAGE = "Hexagon_map.png"
    # #back_img = pygame.image.load(BACKGROUND_IMAGE)

    # Colors
    colors = Colors.Colors()

    # Game Settings
    FRAME_RATE = 30
    clock = pygame.time.Clock()

    # Initiate game screen
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GraphicConnect4 - Menu")
    screen.fill(colors.LIGHT_GREY)

    ##screen.blit(back_img, (0, 0))

    # Initiate fonts
    pygame.font.init()
    GAMEOVERfont = pygame.font.SysFont('Geisha', 80)
    screen.fill(colors.LIGHT_GREY)
    Single_player = "SPRITES/SINGLE_PLAYER.png"
    Multi_player = "SPRITES/MULTI_PLAYER.png"
    Quit = "SPRITES/QUIT.png"

    Single_player_img = pygame.image.load(Single_player)
    Multi_player_img = pygame.image.load(Multi_player)
    Quit_img = pygame.image.load(Quit)

    Single_player_p = "SPRITES/SINGLE_PLAYER PRESSED.png"
    Multi_player_p = "SPRITES/MULTI_PLAYER_PRESSED.png"
    Quit_p = "SPRITES/QUIT_PRESSED.png"

    Single_player_p_img = pygame.image.load(Single_player_p)
    Multi_player_p_img = pygame.image.load(Multi_player_p)
    Quit_p_img = pygame.image.load(Quit_p)

    SingleMenu.run_single_menu(screen, colors, FRAME_RATE, clock, player1, player2)

    pygame.quit()