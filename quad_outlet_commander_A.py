import pygame, os, serial, struct

WIDTH=400
HEIGHT=400
SCRNSZ=(WIDTH,HEIGHT)
WHT=(255,255,255)
BLK=(0,0,0)
RED=(255,0,0)
BLU=(0,0,255)
GRN=(0,255,0)
COLORLIST=(BLK,RED,BLU,GRN)
CLOCK=pygame.time.Clock()
##SER=serial.Serial("/dev/zero",9600)

os.environ['SDL_VIDEO_WINDOW_POS'] =("100,100")

def text(screen,words='Test'):
    background=pygame.Surface((100,20))
    background=background.convert()
    background.fill(BLU)

    font=pygame.font.Font(None,18)
    text=font.render(words,1,(WHT))
    textpos=text.get_rect()
    textpos.centerx=background.get_rect().centerx
    background.blit(text,textpos)
    screen.blit(background,(0,0))


class Outlet(pygame.sprite.Sprite):
    def __init__(self,color,xstart,ystart,xsize=30,ysize=30):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([xsize,ysize])
        self.rect=self.image.get_rect()
        self.rect.x=xstart
        self.rect.y=ystart
        self.image.fill(color)
        

def check_state_on(plug,state,current_state):
    if state==current_state:
        return state
    elif state!=current_state and (state==1 or state==2 or state==3 or state==4):
        plug.image.fill(GRN)
        print(state)
##        SER.write(struct.pack('>B',state))
        return state
    elif state!=current_state and (state==21 or state==22 or state==23 or state==24):
        plug.image.fill(BLK)
        print(state)
##        SER.write(struct.pack('>B',state))
        return state

        

    
def main():
##    SER.open()
    pygame.init()

    win_icon=pygame.Surface([10,10])
    win_icon.fill(BLU)
    pygame.display.set_caption('quad outlet')
    pygame.display.set_icon(win_icon)
    screen=pygame.display.set_mode(SCRNSZ)
    led0=Outlet(RED,195,10,5,5)
    state1=21
    state2=22
    state3=23
    state4=24
    plug1=Outlet(BLK,165,165)
    plug2=Outlet(BLK,165,205)
    plug3=Outlet(BLK,205,165)
    plug4=Outlet(BLK,205,205)
    mover=Outlet(WHT,100,45)
    mover2=Outlet(RED,100,45)
    plug_list=(led0,plug1,plug2,plug3,plug4)
    all_sprites=pygame.sprite.Group()
    moving_sprites=pygame.sprite.Group()
    plug_sprites=pygame.sprite.Group()
    for i in plug_list:
        plug_sprites.add(i)
        all_sprites.add(i)
    all_sprites.add(mover)
    all_sprites.add(mover2)
    moving_sprites.add(mover)
    moving_sprites.add(mover2)
        
    running=True
    while running:
        for event in pygame.event.get():
            if event==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                state=led0.update()
            mouse_but=pygame.mouse.get_pressed()
            if mouse_but[0]==1:
                pos=pygame.mouse.get_pos()
                mover.rect.x=pos[0]
                mover.rect.y=pos[1]
            elif mouse_but[2]==1:
                pos=pygame.mouse.get_pos()
                mover2.rect.x=pos[0]
                mover2.rect.y=pos[1]
        hit_one=pygame.sprite.spritecollide(plug1,moving_sprites,False)
        hit_two=pygame.sprite.spritecollide(plug2,moving_sprites,False)
        hit_three=pygame.sprite.spritecollide(plug3,moving_sprites,False)
        hit_four=pygame.sprite.spritecollide(plug4,moving_sprites,False)
        
        if hit_one:
            
            state1=check_state_on(plug1,1,state1)
        else:
          
            state1=check_state_on(plug1,21,state1)


        if hit_two:
            state2=check_state_on(plug2,2,state2)

        else:
            state2=check_state_on(plug2,22,state2)
            
        if hit_three:
            state3=check_state_on(plug3,3,state3)
        else:
            state3=check_state_on(plug3,23,state3)
        if hit_four:
            state4=check_state_on(plug4,4,state4)
        else:
            state4=check_state_on(plug4,24,state4)
                    
        screen.fill(BLU)
        text(screen,'from main')
        all_sprites.draw(screen)
    
        pygame.display.flip()
        CLOCK.tick(60)

pygame.quit()

if __name__=='__main__': main()
