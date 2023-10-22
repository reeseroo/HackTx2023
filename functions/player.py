from enum import enum

#easy bookkeeping of avatars
class playerType(enum):
    subuwu = 1
    kaeya = 2
    loser = 3
 
 
 #keeping track of player info(current health, amount of money, what kind of avatar they have) across users hopefully
class player:
    def __init__(h, c, type):
        health = h
        currency = c
        pType = type
    

