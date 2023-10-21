import pygame

class Flashcards:
    cards = dict()

    def __init__(self) -> None:
        pass

    def add(self, question, answer):
        self.cards.update({question : answer})
        print("added question") #for debugging
        return
    
    def remove(self, question):
       print("removed question") #for debugging
       self.cards.pop(question)
       return

