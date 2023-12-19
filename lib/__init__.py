import pygame
from entity import Tetris
from enums import BLUE, WHITE, colors
from utils import create_rect

def handle_input(event, game, pressing_down):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            game.rotate()
        elif event.key == pygame.K_DOWN:
            pressing_down = True
        elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            game.go_side(1 if event.key == pygame.K_RIGHT else -1)
        elif event.key == pygame.K_SPACE:
            game.go_space()
        elif event.key == pygame.K_ESCAPE:
            game.__init__(20, 10)
    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        pressing_down = False

    return pressing_down

def draw_grid_and_blocks(screen, game):
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, BLUE, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1, 0, 2)
            if game.grid[i][j] > 0:
                pygame.draw.rect(screen, colors[game.grid[i][j]],
                                [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1], 0, 2)

def draw_current_shape(screen, game):
    if game.shape is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.shape.block():
                    pygame.draw.rect(screen, colors[game.shape.color],
                                    [game.x + game.zoom * (j + game.shape.x) + 1,
                                      game.y + game.zoom * (i + game.shape.y) + 1,
                                      game.zoom - 2, game.zoom - 2], 0, 2)

def main():
    pygame.init()

    size = (600, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Py Tetris")

    done = False
    clock = pygame.time.Clock()
    fps = 30
    game = Tetris(20, 18)
    counter = 0
    pressing_down = False

    while not done:
        if game.shape is None:
            game.new_shape()

        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "play":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                pressing_down = handle_input(event, game, pressing_down)

        screen.fill(WHITE)
        screen.blit(create_rect(360, 400, 5, BLUE, (0, 0, 0)), (95, 55))
        font = pygame.font.SysFont('Calibri', 25, True, False)
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        font2 = pygame.font.SysFont('Calibri', 20, True, False)
        font3 = pygame.font.SysFont('Calibri', 23, True, False)
        font5 = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("Score: " + str(game.score), True, BLUE)
        text2 = font2.render("Rotate ↑", True, BLUE)
        text3 = font2.render("Move ←→", True, BLUE)
        text4 = f™ont3.render("Controls:", True, BLUE)
        sig = font.render("@HaevenDevs", True, BLUE)
        text_game_over = font1.render("Game Over", True, (193, 5, 5))
        text_game_over1 = font5.render("Press ESC", True, (0, 5, 5))

        screen.blit(text, [95, 30])
        screen.blit(text4, [470, 35])
        screen.blit(text3, [475, 60])
        screen.blit(text2, [475, 85])
        screen.blit(sig, [5, 470])
        if game.state == "complete":
            screen.blit(text_game_over, [105, 200])
            screen.blit(text_game_over1, [145, 265])

        
        draw_grid_and_blocks(screen, game)
        draw_current_shape(screen, game)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
