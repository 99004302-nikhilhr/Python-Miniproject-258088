import pygame
import random
from pygame import mixer

pygame.font.init()
pygame.mixer.init()

mixer.music.load("Soundtrack.mp3")
mixer.music.play(-1)

s_w = 700
s_h = 700
p_w = 300  
p_h = 600  
b_s = 30
 
t_l_x = (s_w - p_w) // 2
t_l_y = s_h - p_h

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

ses = [S, Z, I, O, J, L, T]
s_col = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class PC(object):
    rows = 20  
    columns = 10   
 
    def __init__(self, column, row, se):
        self.x = column
        self.y = row
        self.se = se
        self.color = s_col[ses.index(se)]
        self.rot = 0  

def c_g(l_p={}):
    gd = [[(0,0,0) for m in range(10)] for m in range(20)]
 
    for m in range(len(gd)):
        for n in range(len(gd[m])):
            if (n,m) in l_p:
                c = l_p[(n,m)]
                gd[m][n] = c
    return gd

def csf(se):
    pss = []
    format = se.se[se.rot % len(se.se)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pss.append((se.x + j, se.y + i))
 
    for i, pos in enumerate(pss):
        pss[i] = (pos[0] - 2, pos[1] - 4)
 
    return pss

def v_s(se, gd):
    a_p = [[(j, i) for j in range(10) if gd[i][j] == (0,0,0)] for i in range(20)]
    a_p = [j for sub in a_p for j in sub]
    fm = csf(se)
 
    for pos in fm:
        if pos not in a_p:
            if pos[1] > -1:
                return False
    return True

def c_l(pss):
    for pos in pss:
        x, y = pos
        if y < 1:
            return True
    return False
 
 
def g_s():
    global ses, s_col
 
    return PC(5, 0, random.choice(ses))


def d_t_m(text, size, color, surface):
    font = pygame.font.SysFont('malgungothicsemilight', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (t_l_x + p_w/2 - (label.get_width() / 2), t_l_y + p_h/2 - label.get_height()/2))

def d_gr(surface, row, col):
    sx = t_l_x
    sy = t_l_y
    for i in range(row):
        pygame.draw.line(surface, (128,0,128), (sx, sy+ i*30), (sx + p_w, sy + i * 30))  
        for j in range(col):
            pygame.draw.line(surface, (128,0,128), (sx + j * 30, sy), (sx + j * 30, sy + p_h))  

def c_r(gd, lck):
 
    inc = 0
    for i in range(len(gd)-1,-1,-1):
        row = gd[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del lck[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(lck), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                lck[newKey] = lck.pop(key)

def d_n_s(se, surface):
    fff = pygame.font.SysFont('inkfree', 30)
    label = fff.render('Next Shape', 1, (169,169,169))
 
    sx = t_l_x + p_w + 50
    sy = t_l_y + p_h/2 - 100
    format = se.se[se.rot % len(se.se)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, se.color, (sx + j*30, sy + i*30, 30, 30), 0)
 
    surface.blit(label, (sx + 10, sy- 30))

def d_w(surface):
    surface.fill((0,0,32))
    ff = pygame.font.SysFont('inkfree', 80,bold=2)
    label = ff.render('TETRIS', 1, (169,169,169))
 
    surface.blit(label, (t_l_x + p_w / 2 - (label.get_width() / 2), 30))
 
    for i in range(len(gd)):
        for j in range(len(gd[i])):
            pygame.draw.rect(surface, gd[i][j], (t_l_x + j* 30, t_l_y + i * 30, 30, 30), 0)
 
    d_gr(surface, 20, 10)
    pygame.draw.rect(surface, (50, 110, 110), (t_l_x, t_l_y, p_w, p_h), 5)

def mi():
    global gd
 
    l_p = {} 
    gd = c_g(l_p)
 
    ch_p = False
    rn = True
    cu_p = g_s()
    n_p = g_s()
    clk = pygame.time.Clock()
    f_t = 0
 
    while rn:
        f_s = 0.24
 
        gd = c_g(l_p)
        f_t += clk.get_rawtime()
        clk.tick()
 
        if f_t/1000 >= f_s:
            f_t = 0
            cu_p.y += 1
            if not (v_s(cu_p, gd)) and cu_p.y > 0:
                cu_p.y -= 1
                ch_p = True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rn = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cu_p.x -= 1
                    if not v_s(cu_p, gd):
                        cu_p.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    cu_p.x += 1
                    if not v_s(cu_p, gd):
                        cu_p.x -= 1
                elif event.key == pygame.K_UP:
                    cu_p.rot = cu_p.rot + 1 % len(cu_p.se)
                    if not v_s(cu_p, gd):
                        cu_p.rot = cu_p.rot - 1 % len(cu_p.se)
 
                if event.key == pygame.K_DOWN:
                    cu_p.y += 1
                    if not v_s(cu_p, gd):
                        cu_p.y -= 1
 
                if event.key == pygame.K_SPACE:
                   while v_s(cu_p, gd):
                       cu_p.y += 1
                   cu_p.y -= 1
                   print(csf(cu_p))
 
        sh_ps = csf(cu_p)
 
        for i in range(len(sh_ps)):
            x, y = sh_ps[i]
            if y > -1:
                gd[y][x] = cu_p.color
 
        if ch_p:
            for pos in sh_ps:
                p = (pos[0], pos[1])
                l_p[p] = cu_p.color
            cu_p = n_p
            n_p = g_s()
            ch_p = False
 
            c_r(gd, l_p)
 
        d_w(wn)
        d_n_s(n_p, wn)
        pygame.display.update()
 
        if c_l(l_p):
            rn = False
 
    d_t_m("You Lost", 40, (255,0,0), wn)
    pygame.display.update()
    pygame.time.delay(1000)




def m_n():
    rn = True

    while rn:
        wn.fill((0,0,32))
        d_t_m('Press any key to begin...', 40, (169,169,169), wn)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rn = False
 
            if event.type == pygame.KEYDOWN:
                mi()
    pygame.quit()

wn = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption('GAME-2021')
 
m_n()