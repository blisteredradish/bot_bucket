import pygame, sys, random

WIDTH=800
HEIGHT=600
SCRNSZ=(WIDTH,HEIGHT)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

BLUE=(0,255,0)
GREEN=(0,0,255)

class Guy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('/home/nick/Pictures/guysmiley.png')
        self.rect=self.image.get_rect()
class Objective(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()

def main():
    clock=pygame.time.Clock()
    screen=pygame.display.set_mode(SCRNSZ)
    man=Guy()
    
#    man.rect.x=50
#    man.rect.y=50
    player_sprite_list=pygame.sprite.Group()
    player_sprite_list.add(man)
    sprite_list=pygame.sprite.Group()
#    sprite_list.add(man)
    for i in range(0,21):
        block=Objective()
        block.rect.x=random.randrange(WIDTH-20)
        block.rect.y=random.randrange(HEIGHT+20)
        sprite_list.add(block)
    done = False
    pygame.mouse.set_visible(False)
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit()
        pos=pygame.mouse.get_pos()
        man.rect.x=pos[0]
        man.rect.y=pos[1]
        screen.fill(WHITE)
        blocks_hit_list=pygame.sprite.spritecollide(man, sprite_list, True)
        sprite_list.draw(screen)
        player_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
#        print(sprite_list)

if __name__=='__main__': main()
