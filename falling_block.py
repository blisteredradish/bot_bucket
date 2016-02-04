import pygame, sys, random, math, random

WIDTH=180
HEIGHT=680
SCRNSZ=(WIDTH,HEIGHT)
WHT=(255,255,255)
BLK=(0,0,0)
RED=(255,0,0)
BLU=(0,0,255)
GRN=(0,255,0)
COLORLIST=(BLK,RED,BLU,GRN)
BLOCK_NUMBER=10

def ScoreBoard(screen,score):
    font=pygame.font.Font(None,36)
    if score < BLOCK_NUMBER:
        text=font.render(str(score),1,BLK)
    else:
        text=font.render("you are a loser",1,BLK)
    textpos=text.get_rect()
    screen.blit(text,(5,90))
        
class Tester(pygame.sprite.Sprite):
    def __init__(self,color,xsize=10,ysize=10,xstart=30,ystart=0):
#    def __init__(self,xstart=30,ystart=0):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([xsize,ysize])
#        self.image=pygame.image.load('guysmiley.png')
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=xstart
        self.rect.y=ystart
    def update(self,x):
        speed=5
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:      
            return x
        elif key[pygame.K_LEFT]:
            if (x-speed)<0: return WIDTH
            x-=speed
            return x
        elif key[pygame.K_RIGHT]:
            if (x+speed)>(WIDTH-10): return 0
            x+=speed
            return x
        else:
            return x  
    def fall(self,y,rest=False):
        speed=10
        key=pygame.key.get_pressed()
        while not rest:
            if key[pygame.K_DOWN]:
                y+=speed+5
                return y
            if key[pygame.K_UP]:
                y+=speed-5
                return y
            else:
                
                y+=speed
                return y
        return y
    def rest():
        pass
    
def main():
    pygame.init()
    all_sprites=pygame.sprite.Group()
    test_sprites=pygame.sprite.Group()
    blocker_sprites=pygame.sprite.Group()
    clock=pygame.time.Clock()
    screen=pygame.display.set_mode(SCRNSZ)
    screen.fill(GRN)
    faller=Tester(BLK)
    test_sprites.add(faller)
    all_sprites.add(faller)
    for i in range(BLOCK_NUMBER):
        blocker=Tester(RED)
        blocker.rect.x=random.randrange(WIDTH)
        blocker.rect.y=random.randrange(HEIGHT)
        all_sprites.add(blocker)
        blocker_sprites.add(blocker)
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: done=True
        if event.type==pygame.KEYDOWN:
                faller.rect.x=(faller.update(faller.rect.x))
        if faller.rect.y<670:
            faller.rect.y=(faller.fall(faller.rect.y))
        else:
            faller.rect.y=0
        hit_list=pygame.sprite.spritecollide(faller,blocker_sprites,True)
        score=(BLOCK_NUMBER-len(blocker_sprites))
        screen.fill(GRN)
        all_sprites.draw(screen)
        ScoreBoard(screen,score)
        pygame.display.flip()
##        print(faller.rect.y)
        
        clock.tick(60)

pygame.quit()
if __name__=='__main__': main()

