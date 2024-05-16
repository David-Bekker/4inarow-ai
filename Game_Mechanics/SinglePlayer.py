import pygame
from Basic_Things import Basic_Game_Functions

def run_single_player_game(screen, colors, FRAME_RATE, clock, player1, player2):
    # Initiate fonts
    pygame.font.init()
    GAMEOVERfont = pygame.font.SysFont('Geisha', 80)
    CreditFont = pygame.font.SysFont('Geisha', 35)


    # Initiate Parameters
    game_board = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]

    player = 1
    winner = 0

    # GAME_LOOP
    finish = False
    end_game = False
    while not finish:
        # CHANGE_BOARD
        if not end_game:
            curr_player = player1 if player == 1 else player2
            move = curr_player.get_move(game_board, player)
            if move != -1:
                if move != 8:
                    game_board = Basic_Game_Functions.apply_move(game_board, move, player)
                winner = Basic_Game_Functions.Winner_check(game_board, player)
                tie = Basic_Game_Functions.tie_check(game_board)
                if winner > 0:
                    end_game = True
                elif tie == 1:
                    end_game = True
                player = Basic_Game_Functions.switch_player(player)


        # DRAW_EVERYTHING
        pos = pygame.mouse.get_pos()
        screen.fill(colors.DARK_GREY)
        Basic_Game_Functions.draw_gameboard(game_board, screen, colors)
        # MENU
        pygame.draw.rect(screen, colors.DARK_GREY, pygame.Rect(0, 500, 580, 50))
        Credit = CreditFont.render('@SBD GAMES', False, colors.BLACK)
        screen.blit(Credit, (10, 515))


        if end_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
            str_winner = str(winner)
            if winner == 1:
                Game_over = GAMEOVERfont.render('Player ' + str_winner + ' Won!', False, colors.BLACK)
            elif winner == 2:
                Game_over = GAMEOVERfont.render('Player ' + str_winner + ' Won!', False, colors.BLACK)
            elif winner == 0:
                Game_over = GAMEOVERfont.render('        Tie!        ', False, colors.BLACK)
            screen.blit(Game_over, (110, 185))

        pygame.display.flip()
        clock.tick(FRAME_RATE)

pygame.quit()