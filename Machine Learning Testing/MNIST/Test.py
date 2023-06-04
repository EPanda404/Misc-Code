import pygame, sys
from pygame.locals import *
import numpy
from keras.models import load_model
import cv2

WIN_X, WIN_Y = 640, 480

BOUNDRYSIZE = 5
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

IMAGESAVE = True
imag_cnt = 0

PREDICT = True

Model = load_model("bestmodel.h5")

LABELS = {0:'Zero',1:'One',
            2:'Two',3:'Three',
            4:'Four',5:'Five',
            6:'Six',7:'Seven',
            8:'Eight',9:'Nine'}


pygame.init()

FONT = pygame.font.SysFont(pygame.font.get_fonts()[0], 18)
DISPLAY = pygame.display.set_mode((WIN_X, WIN_Y))

pygame.display.set_caption('Digit Board')


iswriting = False
num_x = []
num_y = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            iswriting = True

        if event.type == MOUSEMOTION and iswriting:
            x, y = event.pos
            pygame.draw.circle(DISPLAY, WHITE, (x,y), 3, 0)

            num_x.append(x)
            num_y.append(y)
        
        if event.type == MOUSEBUTTONUP:
            iswriting = False
            num_x = sorted(num_x)
            num_y = sorted(num_y)

            min_x = max(num_x[0] - BOUNDRYSIZE, 0)
            max_x = min(num_x[-1] + BOUNDRYSIZE, WIN_X)

            min_y = max(num_y[0] - BOUNDRYSIZE, 0)
            max_y = min(num_y[-1] + BOUNDRYSIZE, WIN_Y)
            print((min_x,max_x,min_y,max_y))
            img_arr = numpy.array(pygame.PixelArray(DISPLAY))[min_x:max_x, min_y:max_y].T.astype(numpy.float32)

            if PREDICT:
                image = cv2.resize(img_arr, (28,28))
                image = numpy.pad(image, (5,5), 'constant', constant_values=0)
                image = cv2.resize(image, (28,28))/255

                if IMAGESAVE:
                    cv2.imwrite('image.png', image)
                    imag_cnt += 1

                label = str(LABELS[numpy.argmax(Model.predict(image.reshape(1,28,28,1)))])

                textSurface = FONT.render(label, True, BLUE, WHITE)
                textRecObj = DISPLAY.get_rect()
                textRecObj.left, textRecObj.right, textRecObj.top, textRecObj.bottom = min_x, max_x, min_y, max_y

                print(textRecObj)

                DISPLAY.blit(textSurface, (min_x,min_y))

        if event.type == KEYDOWN:
            if event.unicode == 'n':
                DISPLAY.fill(BLACK)
                num_x = []
                num_y = []

    pygame.display.update()