from util import GoodInput2Opt, GoodInput, NameInput
from gameManager import GameManager

GameManager(None)

from nodes import root

def NewOrLoad():
    startNode = None

    answer = GoodInput("Choose Start Option", ['new', 'load'])

    if answer == 'new':
        NewGame()
        startNode = root
    elif answer == 'load':
        while GameManager.instance.playerName is None:
            startNode = GameManager.instance.Load(root.key)

    return startNode

def NewGame():
    print('What are you called?')
    name = NameInput()
    GameManager.instance.playerName = name
    GameManager.instance.Save(root.key)

def main():
    done = False

    node = NewOrLoad()
    while not done:
        node.display()
        if node.isEnding:
            done = not GoodInput2Opt("Play Again?", 'y', 'n')
            node = root
            print("\n==========\n")
        else:
            nextNode = node.choose()
            node = nextNode
            print("\n----------\n")
        ...
    ...


if __name__ == "__main__":
    main()