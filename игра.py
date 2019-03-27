import random
import pygame
import os

pygame.init()
size = w, h = 520, 570
screen = pygame.display.set_mode(size)
sp_z = [x for x in range(1, 26)]
random.shuffle(sp_z)
cell_size = 100
left = 10
top = 60
font = pygame.font.Font(None, 36)
textrules=font.render('ПРАВИЛА', 1, (255, 255, 255))
textchoise = font.render('ВЫБЕРИТЕ СЛОЖНОСТЬ', 1, (255, 255, 255))
texteasy = font.render('EASY', 1, (34, 177, 76))
textmedium = font.render('MEDIUM', 1, (255, 242, 0))
texthight = font.render('HARD', 1, (237, 28, 36))
textnightmare = font.render('NIGHTMARE', 1, (255, 0, 0))
textwin = font.render('YOU WIN', 1, (34, 177, 76))
textwin_x = w // 2 - textwin.get_width() // 2
textwin_y = h // 2 - textwin.get_height() // 2
textlose = font.render('YOU LOSE', 1, (237, 28, 36))
textlose_x = w // 2 - textlose.get_width() // 2
textlose_y = h // 2 - textlose.get_height() // 2
runstart = True
fl_sl=False
count_errors = 0
ce2=0


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 60
        self.cell_size = 100
        self.m_sh = self.board

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def start_game(self):
        z = 0
        for y in range(self.height):
            for x in range(self.width):
                im = pygame.image.load(str(sp_z[z]) + '.png')
                screen.blit(im, (x * self.cell_size + self.left, y * self.cell_size + self.top))
                self.m_sh[y][x] = sp_z[z]
                z += 1

    def get_restart(self, mous_pos):
        p_x = mous_pos[0]
        p_y = mous_pos[1]
        if p_x >= 220 and p_x <= 320 and p_y >= textwin_y + 50 and p_y <= textwin_y + 150:
            return True
        return False

    def matrix(self):
        return self.m_sh


while runstart:
    screen.fill((0, 0, 0))
    count_time = 0
    board = Board(5, 5)
    kletka = None
    m_pos = None
    fl = False
    matr = board.matrix()
    im2 = None
    x = 0
    count = 1
    y = 0
    imr = pygame.image.load('restart.png')
    running = True
    runwin = False
    runlose = False
    flf = False
    run_sl = True
    time_lose = 0
    count_errors=0
    if fl_sl:
        run_sl=False
        time_lose=20
        count_errors=ce2
    while run_sl:
        screen.blit(textrules, (10, 10))        
        screen.blit(textchoise, (
        w // 2 - textchoise.get_width() // 2, h // 2 - textchoise.get_height() // 2 - 100))
        screen.blit(texteasy,
                    (w // 2 - texteasy.get_width() // 2, h // 2 - texteasy.get_height() // 2 - 50))
        screen.blit(textmedium,
                    (w // 2 - textmedium.get_width() // 2, h // 2 - textmedium.get_height() // 2))
        screen.blit(texthight, (
        w // 2 - texthight.get_width() // 2, h // 2 - texthight.get_height() // 2 + 50))
        screen.blit(textnightmare, (
        w // 2 - textnightmare.get_width() // 2, h // 2 - textnightmare.get_height() // 2 + 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                runstart = False
                run_sl = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = event.pos
                if h // 2 - texteasy.get_height() // 2 - 50 < m_pos[1] < h // 2 - texteasy.get_height() // 2:
                    time_lose = 120
                    run_sl=False
                elif h // 2 - textmedium.get_height() // 2 < m_pos[1] < h // 2 - textmedium.get_height() // 2 +50:
                    time_lose = 60
                    run_sl=False
                elif h // 2 - texthight.get_height() // 2 +50< m_pos[1] < h // 2 - texthight.get_height() //2 +100  :
                    time_lose = 30
                    run_sl=False
                elif h // 2 - textnightmare.get_height() // 2 +100 < m_pos[1] < h // 2 - textnightmare.get_height() // 2 +150:
                    time_lose = 20
                    run_sl=False
                    fl_sl=True
                elif 10<m_pos[0]<10+textrules.get_width() and 10<m_pos[1]<10+textrules.get_height():
                    os.system('start правила.txt')
    clock = pygame.time.Clock()
    while running:
        count_time += clock.tick()
        screen.fill((0, 0, 0))
        imh = pygame.image.load('health.png')
        if count_errors == 0:
            screen.blit(imh, (460, 10))
            screen.blit(imh, (410, 10))
            screen.blit(imh, (360, 10))
        if count_errors == 1:
            screen.blit(imh, (460, 10))
            screen.blit(imh, (410, 10))
        if count_errors == 2:
            screen.blit(imh, (460, 10))
        board.render()
        board.start_game()
        if count_time/1000>time_lose:
            running=False
            runlose=True
        if count == 26:
            runwin = True
            running = False
        if count_errors == 4:
            running = False
            runlose = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                runstart = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = event.pos
                kletka = board.get_cell(m_pos)
                if m_pos[1]>50:
                    if matr[kletka[1]][kletka[0]] == count:
                        fl = True
                    elif m_pos[1]>50:
                        flf = True
                    m_pos = event.pos
        if fl:
            imw = pygame.image.load(str(matr[kletka[1]][kletka[0]]) + '.png')
            screen.blit(imw, (kletka[0] * cell_size + left, kletka[1] * cell_size + top))
            count += 1
            fl = False

        if flf:
            iml = pygame.image.load(str(matr[kletka[1]][kletka[0]]) + '.png')
            screen.blit(iml, (kletka[0] * cell_size + left, kletka[1] * cell_size + top))
            count_errors += 1
            flf = False
        text_time = font.render(str(count_time / 1000), 1, (255, 255, 255))
        screen.blit(text_time, (10, 10))
        pygame.display.flip()
    if fl_sl:
        runwin=False
        ce2=count_errors

    while runwin:
        count_time=0
        screen.fill((0, 0, 0))
        screen.blit(textwin, (textwin_x, textwin_y))
        screen.blit(text_time, (
            w // 2 - text_time.get_width() // 2, h // 2 - text_time.get_height() // 2 - 50))
        screen.blit(imr, (220, textwin_y + 50))
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                runwin = False
                runstart = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                m_poswin = i.pos
                if board.get_restart(m_poswin):
                    runwin = False
                    run_sl=True

    while runlose:
        screen.fill((0, 0, 0))
        count_time=0
        screen.blit(textlose, (textlose_x, textlose_y))
        screen.blit(imr, (220, textlose_y + 50))
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                runlose = False
                runstart = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                m_poslose = i.pos
                if board.get_restart(m_poslose):
                    runlose = False
                    run_sl=True
                    fl_sl=False

pygame.quit()
