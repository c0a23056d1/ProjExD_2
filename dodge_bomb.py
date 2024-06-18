import os
import random
import sys
import pygame as pg
import time


WIDTH, HEIGHT = 1600, 900

#こうかとんを動かすための辞書
DELTA = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    bomb = pg.Surface((20, 20))        #一辺が20の正方形Surface
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)     #中心に半径10の赤い円を描画
    bomb.set_colorkey((0, 0, 0))         #四隅の黒を透過させる
    x_bomb = random.randint(0,1600)
    y_bomb = random.randint(0,900)
    bomb_rect = bomb.get_rect()
    bomb_rect.center = x_bomb, y_bomb
    vx, vy = +5, +5
    
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        tmr += 1
        clock.tick(50)


        screen.blit(bomb, bomb_rect)
        bomb_rect.move_ip(vx, vy)
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct) 
        pg.display.update()

        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()



# key_lst = pg.key.get_pressed()
        # sum_mv = [0, 0]
        # if key_lst[pg.K_UP]:
            # sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
            # sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
            # sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
            # sum_mv[0] += 5
        # kk_rct.move_ip(sum_mv)
        # screen.blit(kk_img, kk_rct)

        