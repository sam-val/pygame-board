import pygame as pg
import copy
import time
from typing import Tuple
from collections import namedtuple


class MyRect:
    def __init__(self, size: Tuple[int, int],
                 pic = None,
                 func = None, border_colour = (0,0,0),
                 line_colour = (255,255,255),
                 colour = None, rect=None,
                 active = False ):
        self.func = func
        self.pic = pic
        self.active = active
        self.border_colour = border_colour
        self.line_colour = line_colour
        self.colour = colour
        self.rect = rect
        self.size = size


class Board:
    LINE_WIDTH = 2
    def __init__(self, screen,
                 position: Tuple[int,int],
                 size: Tuple[int,int] ,
                 cube: MyRect,
                 border = True,
                 line=True):
        self.screen = screen
        self.posx, self.posy = position
        self.w, self.h = size
        self.border = border
        self.cube = cube
        self.cube_w, self.cube_h = cube.size
        self.array = self.make_new_array()
        self.line = line

    def draw(self):
        for x in range(self.w):
            for y in range(self.h):
                px = self.posx + x*self.cube_w
                py = self.posy + y*self.cube_h
                colour = self.array[x+y*self.w].colour

                # draw the cube/rectangle
                pg.draw.rect(self.screen, colour, self.array[x + y * self.w].rect)

                # check and draw its borders:
                if self.border:
                    if self.checkIfBorder(x, y):
                        border_colour =  self.array[x+y*self.w].border_colour
                        if not border_colour:
                            border_colour = (0,0,0)
                        pg.draw.rect(self.screen, border_colour, self.array[x + y * self.w].rect)
                if self.line:
                    if self.array[x+y*self.w].line_colour:
                        # horizontal lines
                        pg.draw.line(self.screen, self.array[x+y*self.w].line_colour, (px, py), (px + self.cube_w, py))
                        if y == self.h-1:
                            pg.draw.line(self.screen, self.array[x+y*self.w].line_colour, (px,py+self.cube_h), (px+self.cube_w,py+self.cube_h))
                        # vertical lines
                        pg.draw.line(self.screen, self.array[x+y*self.w].line_colour, (px, py), (px, py + self.cube_h))
                        if x == self.w-1:
                            pg.draw.line(self.screen, self.array[x+y*self.w].line_colour, (px+self.cube_w,py), (px+self.cube_w,py+self.cube_h))


    def click(self,pos):
        for x in range(self.w):
            for y in range(self.h):
                Rect = self.array[x+y*self.w]
                Rect.x = x
                Rect.y = y
                if Rect.rect.collidepoint(pos):
                    Rect.active = not Rect.active
                    if not self.checkIfBorder(x,y):
                        if Rect.func is not None:
                            for i,f in enumerate(Rect.func):
                                Rect.func[i](rect=Rect, board=self)
                    return Rect

    def checkIfBorder(self, x, y):
        if x == 0 or x == self.w - 1 or y == 0 or y == self.h - 1:
                return True
        else:
            return False

    def make_new_array(self):
        array = [ None] * self.w * self.h
        for x in range(self.w):
            for y in range(self.h):
                self.assign_rect_to_array(array, x, y, self.cube)
        return array

    def assign_rect_to_array(self, array, x,y, rect):
        px = self.posx + x * self.cube_w
        py = self.posy + y * self.cube_h
        array[x + y * self.w] = copy.copy(rect)
        array[x + y * self.w].rect = pg.Rect(px, py, self.cube_w, self.cube_h)
        if self.checkIfBorder(x, y):
            array[x + y * self.w].func = None
            array[x + y * self.w].border = True


    def init_array(self):
        self.array = self.make_new_array()

    def change_colour(self, colour):
        for x in range(self.w):
            for y in range(self.h):
                self.array[x+y*self.w].colour = colour


class TextDisplay:
    def __init__(self, surface, font=None, colour=None):
        self.surface = surface
        self.font = font
        self.colour = colour

    def display_text(self, x, y, text,
                     font=None,
                     colour=None, bg=None, centeredX = False, centeredY = False):
        if colour == None:
            colour = self.colour if self.colour != None else (0,0,0)
        if font == None:
            font = self.font if self.font != None else pg.font.SysFont("ubuntumono",20)
        text_w, text_h = font.size(text)
        text_sur = font.render(text, False, colour,bg)
        text_rect = text_sur.get_rect()

        self.display_sur(x, y, sur=text_sur, centeredY=centeredY, centeredX=centeredX)
        # self.surface.blit(text_sur,(x, y))

    def display_clock(self, x, y, secs=0, colour = None, font=None, bg = None, centeredX = False, centeredY=False):
        time = self.convert(secs=secs)

        self.display_text(x, y, text=time, colour=colour, font=font, bg=bg, centeredX=centeredX, centeredY=centeredY)

    @staticmethod
    def convert(secs = None):
        secs = int(secs)
        if secs < 0 or secs == None:
            secs = 0
        min = secs // 60
        sec = secs - min*60
        time = (str(min) if min > 9 else "0"+str(min)) + \
               ":" + \
               (str(sec) if sec > 9 else "0"+str(sec))
        return time


    def display_sur(self, x, y, sur, centeredX = False, centeredY = False):
        text_rect = sur.get_rect()
        text_w = sur.get_width()
        text_h = sur.get_height()

        if centeredX:
            x = x - text_w//2
        if centeredY:
            y = y - text_h//2

        self.surface.blit(sur, (x, y))

