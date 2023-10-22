import pygame

class Flashcards:
    cards = dict()

    def __init__(self) -> None:
        pass

    def add(self, question, answer):

        self.cards.append({question : answer})
        print("added question") #for debugging
        return
    
    def remove(self, question):
       print("removed question") #for debugging
       self.cards.remove(question)
       return
