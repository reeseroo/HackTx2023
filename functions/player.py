from enum import enum

#easy bookkeeping of avatars
class character(enum):
    subuwu = 1
    kaeya = 2
    loser = 3


class player:
    def __init__(self):
        self.__userID = ""
        self.__health = 0
        self.__wealth = 0
        self.__char = ""

    def set_userID(self, userID):
        self.__userID = userID

    def set_health(self, health):
        self.__health = health

    def set_wealth(self, wealth):
        self.__wealth = wealth

    def set_char(self, char):
        self.__char = char

    def get_userID(self):
        return self.__userID

    def get_health(self):
         return self.__health

    def get_wealth(self):
        return self.__wealth

    def get_char(self):
        return self.__char