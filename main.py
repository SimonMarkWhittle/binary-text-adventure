from nodes import root
from util import GoodInput2Opt

def main():
    done = False

    node = root
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