import math
import random
from Game_Mechanics import Adverseries
from selenium import webdriver


class CopyCat:
    def init(self):
        self.ai = 0
        self.human = 0
        self.url = "https://connect4.gamesolver.org/"
        pass

    def get_move(self, board, player):
        self.ai = player
        self.human = 3 - player
        col = self.site_watcher()
        return col

    def site_watcher(self):
        browser = webdriver.Chrome('E:/4inarow/chromedriver.exe')
        browser.get(self.url)
        if self.ai == 1:
            temp = browser.find_element_by_id("player1")
            temp.click()
        else:
            temp = browser.find_element_by_id("player2")
            temp.click()
