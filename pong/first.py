import pygame

p1 = 0
p2 = 0

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pong")
preto=(0,0,0)
branco=(255,255,255)
vermelho=(255,0,0)
y=210
z=210
Qx=300
Qy=230
Xy = 100

pygame.font.init()

font = pygame.font.SysFont(None,50)


block = pygame.Rect(Qx, Qy, 20, 20)

vx = 0.4
vy = 0

clock = pygame.time.Clock()

fim = False

while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    left_pad = pygame.Rect(25, y, 20, 90)
    right_pad = pygame.Rect(600, z, 20, 90)
    a = pygame.Rect(1, 0, 20, 480)
    b = pygame.Rect(625, 0, 20, 480)
    c = pygame.Rect(0, 470, 650, 20)
    d = pygame.Rect(0, -10, 650, 20)

    text = font.render(str(p1)+' - '+str(p2), 1, preto)

    pads = [left_pad, right_pad]

    def texto(msg,cor):
        texto = font.render(msg, True, cor)
        screen.blit(texto, (100, 240))

    def jogo():
        sair = True

        dt = clock.tick(60)

        block.move_ip(vx * dt, vy)

        
    if block.collidelist(pads) >= 0:
        vx = -vx
        if y < 320:
            vy = 1
        if y > 320:
            vy = -1


    if block.colliderect(b):
        p1 = p1+1
        vx = -vx
        vy = 0
        

    if block.colliderect(a):
        p2 = p2+1
        vx = -vx
        vy = 0
        

    if block.colliderect(c):
        vy = -vy

    if block.colliderect(d):
        vy = vy + 1

    screen.fill((255,255,255))

    pygame.draw.rect(screen, preto, left_pad)

    pygame.draw.rect(screen, preto, c)

    pygame.draw.rect(screen, preto, d)
        
    pygame.draw.rect(screen, preto, right_pad)
        
    pygame.draw.rect(screen, vermelho, block)


    screen.blit(text,(40,20))

    if p1==10:
        ganhador = 'Player 1'
        fim = True

    if p2==10:
        ganhador = 'Player 2'
        fim = True


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y = y-5


    if keys[pygame.K_s]:
        y = y+5

    if keys[pygame.K_UP]:
        z = z-5

    if keys[pygame.K_DOWN]:
        z = z+5

    if y == 0:
        y=y+5
        
    if z == 0:
        z=z+5

    if y == 400:
        y=y-5

    if z == 400:
        z=z-5


    jogo()

    while fim:
        
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            break
        screen.fill((255,255,255))
        texto(ganhador+' Ganhou o jogo!', preto)
        pygame.display.update()

    pygame.display.update()