from util import GoodInput
from gameManager import GameManager

class Node(object):

    def __init__(self, choice="", text="", branches=None, isRoot=False):
        self.choice = choice
        self.text = text
        self.key = None
        self.parent = None
        self.taken = []

        if (branches is None):
            self.isEnding = True
            self.branches = None
        else:
            self.isEnding = False
            self.branches = branches
            self.SetBranchParents()
            ...
        
        if (isRoot):
            self.key = ""
            GameManager.instance.RegisterNode(self, self.key)
            self.MakeKeys(self.key)
        ...
    ...

    def display(self):
        print(self.text)

    def SetBranchParents(self):
        for branch in self.branches:
            branch.parent = self

    def MakeKeys(self, key):
        self.key = key
        GameManager.instance.RegisterNode(self, self.key)

        if self.branches is None:
            return

        count = 0
        for branch in self.branches:
            branch.MakeKeys(self.key + str(count))
            count += 1
            if count >= 10:
                break

    def choose(self):

        nextBranch = None

        done = False
        while not done:

            print("What do you do?")

            inputList = []

            optionBranches = self.branches.copy()

            for takenBranch in self.taken:
                optionBranches.remove(takenBranch)

            count=1
            for branch in optionBranches:
                print("(" + str(count) + ") %s" % (branch.choice))
                inputList.append(str(count))
                count += 1

            otherOpts = ['save', 'load', 'quit', 'back']
            answer = GoodInput("", inputList + otherOpts)

            if (answer == 'save'):
                GameManager.instance.Save(self.key)
            elif (answer == 'load'):
                nextBranch = GameManager.instance.Load(self.key)
            elif (answer == 'quit'):
                quit()
            elif answer == 'back':
                nextBranch = self.parent

            try:
                num = int(answer) - 1
                nextBranch = optionBranches[num]
                self.taken.append(nextBranch)        
            except:
                nextBranch = None

            if nextBranch is not None:
                done = True

        return nextBranch
