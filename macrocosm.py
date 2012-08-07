import sys, pygame
from pygame.locals import *

CharPos = [0, 0]
Warps = []
Paths = []
Walls = []
#try:
#    save = f.open('~/Macrocosm/save', 'rw')
#except:
#    try:

def MoveCharacter(direction):
    if direction == 'up':
        pass
    if direction == 'down':
        pass
    if direction == 'left':
        pass
    if direction == 'right':
        pass

def main():
    dimensions = 800, 600

    #color definitions
    white = 255, 255, 255
    slategray = 112, 128, 144

    pygame.init()

    #menu properties
    menuitems = ['option1', 'option2', 'option3', 'option4', 'option5']
    height, width = 80, ((len(menuitems) * 20) + 30)
    menu = 0
    menurect = pygame.rect.Rect(0, 0, height, width)
    menuoption = 1

    print 'Menu configured.'

    fps = pygame.time.Clock()
    screen = pygame.display.set_mode(dimensions)
    menutext = pygame.display.get_surface()
    textfont = pygame.font.Font('FreeSans.ttf', 16)
    background = pygame.image.load('Grassyfield2.png').convert()
    pygame.display.update()

    print "We're at the loop."

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print "We're done."
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if menu == 0:
                        MoveCharacter('up')
                    else:
                        menuoption = menuoption - 1
                        if menuoption < 1:
                            menuoption = 1
                elif event.key == K_DOWN:
                    if menu == 0:
                        MoveCharacter('down')
                    else:
                        menuoption = menuoption + 1
                        if menuoption > len(menuitems):
                            menuoption = len(menuitems)
                elif event.key == K_LEFT:
                    MoveCharacter('left')
                elif event.key == K_RIGHT:
                    MoveCharacter('right')
                elif event.key == K_ESCAPE:
                    if menu == 0:
                        menu = 1
                        print 'Menu opened.'
                    else:
                        menu = 0
                        print 'Closed the menu.'
        screen.blit(background, (0, 0))
        if menu == 1:
            #draw a menu
            screen.fill(slategray, menurect)
            foo = 0
            for option in menuitems:
                menutext = textfont.render(option, 1, white)
                screen.blit(menutext, (5, (15 + (foo * 20))))
                foo = foo + 1
            foo = 0
        pygame.display.update()
        fps.tick(26)

if __name__ == '__main__':
    main()
