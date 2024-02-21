import pygame
from pygame.locals import *
import sys
import time
import random
import pyjokes

class Game:
    def __init__(self):
        self.w = 750
        self.h = 500
        self.rest = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accurcy:0 WPM:0'
        self.WPM = 0
        self.end = False
        self.HEAD_C = (225,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)

        pygame.init()
        self.open_img = pygame.image.load('src')
        self.open_img = pygame.transform.scale(scale(self.bg,(700,500)))

        self.screen = pygame.display.set_mode(self.w/self.h)
        pygame.display.set_caption('CheetaToise')

        def draw_text(self, screen,msg,y,fsize,color):
            font = pygame.font.Font(None,fsize)
            text = font.render(msg,1,color)
            text_rect = text.get_rect(center=(self.w/2,y))
            screen.blit(text,text_rect)
            pygame.display.update()

        def get_sentence(self):
            sentence = pyjokes.get_jokes()
            return sentence
        
        def show_result(self,screen):
            if(not self.end):
                #calculate time
                self.total_time = time.time() - self.time_start

                #calculate accurace
                count = 0
                for i,c in enumerate(self.word):
                    try:
                        if self.input_text[i] == c:
                            count += 1
                    except:
                        pass
                self.accuracy = count/len(self.word)*100

                #calculaet wpm

                self.wpm = len(self.input_text) * 60 / (5*self.total_time)
                self.end = True
                print(self.total_time)

                self.result = 'Time' + str(round(self.total_time)) + "secs Accuracy :"  + str(round(self.accuracy))
                





