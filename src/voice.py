import os, random, time
from audioplayer import AudioPlayer

class Voice:

    def __init__(self, directory):
        self.directory = directory

    def talk(self):
        self.intro()
        self.meat()
        self.outro()

    def intro(self):
        print('INTRO (' + self.directory + ')')
        self.play('intro')
        while (self.chance(25)):
            self.play('intro')

    def meat(self):
        print('MEAT (' + self.directory + ')')
        self.play('meat')
        while (self.chance(66)):
            while (self.chance(33)): self.play('punc')
            self.play('meat')

    def outro(self):
        print('OUTRO (' + self.directory + ')')
        if (self.chance(75)):
            self.play('punc')
        while (self.chance(12)):
            self.play('punc')

    def interject(self):
        print('INTERJECT (' + self.directory + ')')
        self.play('interject')

    def play(self, subdirectory):
        target = self.directory + '/' + subdirectory
        snippet = random.choice(os.listdir(target))
        print(' ' + subdirectory + ': ' + str(snippet))
        AudioPlayer(target + '/' + snippet).play(block=True)
        while (self.chance(75)): time.sleep(.2)

    def chance(self, odds):
        roll = random.randint(1,101)
        return True if roll < odds else False