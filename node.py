from util import GoodInput2Opt

class Node(object):

    def __init__(self, choice="", text="", branch1=None, branch2=None):
        self.choice = choice
        self.text = text

        if (branch1 is None and branch2 is None):
            self.isEnding = True
        else:
            self.isEnding = False
            self.branch1 = branch1
            self.branch2 = branch2
            ...
        ...
    ...

    def display(self):
        print(self.text)
    
    def choose(self):

        print("What do you do?")
        print("(1) %s" % (self.branch1.choice))
        print("(2) %s" % (self.branch2.choice))

        answer = GoodInput2Opt("", '1', '2')

        if (answer):
            return self.branch1

        return self.branch2
