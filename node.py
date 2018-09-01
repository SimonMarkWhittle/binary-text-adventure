from util import GoodInput
from gameManager import GameManager

class Node(object):

    def __init__(self, choice="", text="", branch1=None, branch2=None, isRoot=False):
        self.choice = choice
        self.text = text
        self.key = None
        self.parent = None

        if (branch1 is None and branch2 is None):
            self.isEnding = True
            self.branch1 = None
            self.branch2 = None
        else:
            self.isEnding = False
            self.branch1 = branch1
            self.branch2 = branch2
            self.branch1.parent = self
            self.branch2.parent = self
            ...
        
        if (isRoot):
            self.key = ""
            GameManager.instance.RegisterNode(self, self.key)
            branch1.MakeKeys(self.key + "1")
            branch2.MakeKeys(self.key + "2")
        ...
    ...

    def display(self):
        print(self.text)

    def MakeKeys(self, key):
        self.key = key
        GameManager.instance.RegisterNode(self, self.key)

        if self.branch1:
            self.branch1.MakeKeys(self.key + "1")
        if self.branch2:
            self.branch2.MakeKeys(self.key + "2")

    def choose(self):

        nextBranch = None

        done = False
        while not done:

            print("What do you do?")
            print("(1) %s" % (self.branch1.choice))
            print("(2) %s" % (self.branch2.choice))

            answer = GoodInput("", ['1', '2', 'save', 'load', 'quit'])

            if (answer == '1'):
                nextBranch = self.branch1
            elif (answer == '2'):
                nextBranch = self.branch2
            elif (answer == 'save'):
                GameManager.instance.Save(self.key)
            elif (answer == 'load'):
                nextBranch = GameManager.instance.Load(self.key)
            elif (answer == 'quit'):
                quit()

            if nextBranch is not None:
                done = True
        
        return nextBranch
