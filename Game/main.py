import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 650
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Blocks Break")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)
gold = (255, 215, 0)

radius = 10
velocity = 8

border_d = HEIGHT - bound - radius
border_u = bound + radius + 50
border_l = bound + radius
border_r = WIDTH - bound - radius

height = 10
width = 80
vp = 8

score = 0
ball_color = (0, 255, 0)

record_score = 0

class Block:
    def __init__(self, x, y, width, height, points, color, special=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.points = points
        self.color = color
        self.special = special

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text = "?" if self.special else str(self.points)
        text_render = font.render(text, True, black)
        text_rect = text_render.get_rect(center=self.rect.center)
        win.blit(text_render, text_rect)


def create_block_row(y, row_number):
    blocks = []
    block_width = 44
    block_height = 20
    points_list = [5, 10, 15, 20, 25, 30, 35, 40]
    random.shuffle(points_list)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    special_block_position = random.randint(0, 7) if row_number % 5 == 0 else -1
    for j in range(8):
        x = bound + j * (block_width + 5)
        if j == special_block_position:
            blocks.append(Block(x, y, block_width, block_height, 0, gold, special=True))
        else:
            blocks.append(Block(x, y, block_width, block_height, points_list[j], color))
    return blocks


def draw_window(balls, xp, yp, blocks):
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))

    for ball in balls:
        pygame.draw.circle(win, ball_color, (ball['x'], ball['y']), radius)
    pygame.draw.rect(win, white, (xp, yp, width, height))

    for block in blocks:
        block.draw(win)

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, white)
    win.blit(text, (10, 10))

    record_text = font.render(f'Record: {record_score}', True, gold)
    win.blit(record_text, (250, 10))

    pygame.display.update()


def show_menu(final_score):
    global record_score

    win.fill(black)
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, white)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 100))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {final_score}', True, white)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 50))

    if final_score > record_score:
        record_score = final_score
        new_record_text = font.render('New Record!', True, gold)
        win.blit(new_record_text, (WIDTH // 2 - new_record_text.get_width() // 2, HEIGHT // 2 - 77))
    else:
        record_text = font.render(f'Record: {record_score}', True, gold)
        win.blit(record_text, (WIDTH // 2 - record_text.get_width() // 2, HEIGHT // 2 - 77))

    restart_text = font.render('Restart', True, white)
    menu_text = font.render('Menu', True, white)
    exit_text = font.render('Exit', True, white)

    restart_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 10, 200, 50)
    menu_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50)
    exit_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 130, 200, 50)

    pygame.draw.rect(win, white, restart_rect, 2)
    pygame.draw.rect(win, white, menu_rect, 2)
    pygame.draw.rect(win, white, exit_rect, 2)

    win.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
    win.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 + 80))
    win.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 140))

    pygame.display.update()

    return restart_rect, menu_rect, exit_rect


def main_menu():
    run = True
    while run:
        win.fill(black)

        font = pygame.font.Font(None, 74)
        title_text = font.render('Blocks Break', True, white)
        win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height() // 2 - 150))

        font = pygame.font.Font(None, 36)
        start_text = font.render('Start', True, white)
        color_text = font.render('Change Ball Color', True, white)
        exit_text = font.render('Exit', True, white)

        start_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 230, 50)
        color_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 230, 50)
        exit_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 90, 230, 50)

        pygame.draw.rect(win, white, start_rect, 2)
        pygame.draw.rect(win, white, color_rect, 2)
        pygame.draw.rect(win, white, exit_rect, 2)

        win.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2 + 13, HEIGHT // 2 - 40))
        win.blit(color_text, (WIDTH // 2 - color_text.get_width() // 2 + 17, HEIGHT // 2 + 33))
        win.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2 + 13, HEIGHT // 2 + 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    main()
                if color_rect.collidepoint(event.pos):
                    change_color_menu()
                if exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()


def change_color_menu():
    global ball_color
    saved_color = ball_color
    run = True
    red, green, blue = ball_color
    while run:
        win.fill(black)

        font = pygame.font.Font(None, 36)
        title_text = font.render('Change Ball Color', True, white)
        win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height() // 2 - 200))

        ball_preview = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 150, 100, 100)
        pygame.draw.circle(win, (red, green, blue), ball_preview.center, 50)

        back_text = font.render('Back', True, white)
        back_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        pygame.draw.rect(win, white, back_rect, 2)
        win.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT // 2 + 12))

        slider_length = 200
        slider_x = WIDTH // 2 - slider_length // 2

        red_slider = pygame.Rect(slider_x, 450, slider_length, 20)
        green_slider = pygame.Rect(slider_x, 500, slider_length, 20)
        blue_slider = pygame.Rect(slider_x, 550, slider_length, 20)

        red_knob = pygame.Rect(red_slider.x + (red * red_slider.width // 255) - 10, red_slider.y - 5, 20, 30)
        green_knob = pygame.Rect(green_slider.x + (green * green_slider.width // 255) - 10, green_slider.y - 5, 20, 30)
        blue_knob = pygame.Rect(blue_slider.x + (blue * blue_slider.width // 255) - 10, blue_slider.y - 5, 20, 30)

        pygame.draw.rect(win, white, red_slider, 2)
        pygame.draw.rect(win, white, green_slider, 2)
        pygame.draw.rect(win, white, blue_slider, 2)

        pygame.draw.rect(win, (red, 0, 0), red_slider)
        pygame.draw.rect(win, (0, green, 0), green_slider)
        pygame.draw.rect(win, (0, 0, blue), blue_slider)

        pygame.draw.rect(win, white, red_knob)
        pygame.draw.rect(win, white, green_knob)
        pygame.draw.rect(win, white, blue_knob)

        red_text = font.render('Red', True, white)
        green_text = font.render('Green', True, white)
        blue_text = font.render('Blue', True, white)

        win.blit(red_text, (red_slider.x - 90, red_slider.y - 5))
        win.blit(green_text, (green_slider.x - 90, green_slider.y - 5))
        win.blit(blue_text, (blue_slider.x - 90, blue_slider.y - 5))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    ball_color = saved_color
                    run = False
                if red_slider.collidepoint(event.pos):
                    red = (event.pos[0] - red_slider.x) * 255 // red_slider.width
                    red = max(0, min(255, red))
                if green_slider.collidepoint(event.pos):
                    green = (event.pos[0] - green_slider.x) * 255 // green_slider.width
                    green = max(0, min(255, green))
                if blue_slider.collidepoint(event.pos):
                    blue = (event.pos[0] - blue_slider.x) * 255 // blue_slider.width
                    blue = max(0, min(255, blue))

            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if red_knob.collidepoint(event.pos) or red_slider.collidepoint(event.pos):
                    red = (event.pos[0] - red_slider.x) * 255 // red_slider.width
                    red = max(0, min(255, red))
                if green_knob.collidepoint(event.pos) or green_slider.collidepoint(event.pos):
                    green = (event.pos[0] - green_slider.x) * 255 // green_slider.width
                    green = max(0, min(255, green))
                if blue_knob.collidepoint(event.pos) or blue_slider.collidepoint(event.pos):
                    blue = (event.pos[0] - blue_slider.x) * 255 // blue_slider.width
                    blue = max(0, min(255, blue))

        ball_color = (red, green, blue)


def main():
    global score
    score = 0
    x, y = WIDTH // 2, HEIGHT // 2
    vx = velocity * (random.uniform(0.5, 1)) * (1 if random.random() > 0.5 else -1)
    vy = velocity * (random.uniform(0.5, 1)) * (1 if random.random() > 0.5 else -1)
    xp = (WIDTH - width) // 2
    yp = HEIGHT - height - 30

    balls = [{'x': x, 'y': y, 'vx': vx, 'vy': vy}]
    blocks = create_block_row(border_u, 0)
    last_spawn_time = pygame.time.get_ticks()
    row_number = 1

    run = True
    while run:
        clock.tick(c2s)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and xp > bound:
            xp -= vp
        if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
            xp += vp

        for ball in balls:
            if ball['x'] + ball['vx'] < border_l or ball['x'] + ball['vx'] > border_r:
                ball['vx'] = -ball['vx']
            if ball['y'] + ball['vy'] < border_u:
                ball['vy'] = -ball['vy']

            if xp <= ball['x'] + ball['vx'] <= xp + width and yp - radius <= ball['y'] + ball['vy'] <= yp:
                ball['vy'] = -ball['vy']

            for block in blocks[:]:
                if block.rect.colliderect(pygame.Rect(ball['x'] - radius, ball['y'] - radius, radius * 2, radius * 2)):
                    score += block.points
                    if block.special:
                        num_new_balls = random.choice([2, 3, 4])
                        new_balls = [{'x': ball['x'], 'y': ball['y'],
                                      'vx': velocity * (random.uniform(0.5, 1)) * (1 if random.random() > 0.5 else -1),
                                      'vy': velocity * (random.uniform(0.5, 1)) * (1 if random.random() > 0.5 else -1)}
                                     for _ in range(num_new_balls - 1)]
                        balls.extend(new_balls)
                    blocks.remove(block)
                    ball['vy'] = -ball['vy']
                    break

        balls = [ball for ball in balls if ball['y'] + ball['vy'] <= border_d]

        if not balls:
            run = False
            restart_rect, menu_rect, exit_rect = show_menu(score)
            menu = True
            while menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rect.collidepoint(event.pos):
                            main()
                        if menu_rect.collidepoint(event.pos):
                            main_menu()
                        if exit_rect.collidepoint(event.pos):
                            pygame.quit()
                            exit()

        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > 15000:
            new_blocks = create_block_row(border_u, row_number)
            row_number += 1
            for block in blocks:
                block.rect.y += 20
            blocks.extend(new_blocks)
            last_spawn_time = current_time

        for ball in balls:
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']

        draw_window(balls, xp, yp, blocks)

    pygame.quit()

main_menu()