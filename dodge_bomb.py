import os
import random
import sys
import pygame as pg
import time


WIDTH, HEIGHT = 1500, 700

#こうかとんを動かすための辞書
DELTA = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_bound(rct:pg.Rect) -> tuple[bool, bool]:
    """
    引数：こうかとんRectまたは爆弾Rect
    戻り値：真理値タプル（横方向、縦方向）
    画面内ならTrue/画面外ならFalse
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:   #横方向判定
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:  #縦方向判定
        tate = False
    return yoko, tate

def direction_kk(): #こうかとんの向きを変える関数
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0) #こうかとん左向き
    kk_img1 = pg.transform.flip(kk_img, True, False)
    return {
        (0, 0): kk_img,    #何も押していない時
        (0, -5): pg.transform.rotozoom(kk_img1, 90, 1.0), #
        (+5, -5): pg.transform.rotozoom(kk_img1, 45, 1.0),
        (+5, 0):kk_img1,
        (+5, +5): pg.transform.rotozoom(kk_img1, -45, 1.0),
        (0, +5): pg.transform.rotozoom(kk_img1, -45, 1.0),
        (-5, +5): pg.transform.rotozoom(kk_img, 45, 1.0),
        (-5,0): pg.transform.rotozoom(kk_img, 0, 1.0),
        (-5, -5): pg.transform.rotozoom(kk_img, -45, 1.0),
    }



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_imgs = direction_kk()
    kk_img = kk_imgs[(0,0)]
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
        if kk_rct.colliderect(bomb_rect):
            return
        screen.blit(bg_img, [0, 0]) 

        tmr += 1
        clock.tick(50)


        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        screen.blit(bomb, bomb_rect)
        for k, v in DELTA.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        kk_img = kk_imgs[tuple(sum_mv)]
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        bomb_rect.move_ip(vx, vy)
        yoko, tate = check_bound(bomb_rect)
        screen.blit(kk_img, kk_rct)
        if not yoko: #横方向にはみ出たら
            vx *= -1
        if not tate:
            vy *= -1
        

        
            

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

        