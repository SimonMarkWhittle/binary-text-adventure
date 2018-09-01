from util import NameInput
import json

class GameManager:
    class __GameManager:
        def __init__(self, _name):
            self.playerName = _name
            self.nodes = {}

        def __str__(self):
            return repr(self)

        def RegisterNode(self, node, key):
            self.nodes[key] = node

        def Save(self, currentNode):
            playerName = GameManager.instance.playerName

            save = None

            try:
                open('save.txt', 'x')
                with open('save.txt', 'w') as saveFile:
                    saveFile.write(json.dumps({})) 
            except:
                pass

            with open('save.txt', 'r') as saveFile:
                save = json.loads(saveFile.read())

            save[playerName] = currentNode

            print(save)

            with open('save.txt', 'w') as saveFile:
                saveFile.write(json.dumps(save))

        def Load(self, currentNodeKey):
            print("which character save do you want to load?")
            playerName = NameInput()
            loaded = GameManager.instance.nodes[currentNodeKey]
            save = None
            try:
                with open('save.txt', 'r') as saveFile:
                    save = json.loads(saveFile.read())
            except:
                print('ERROR: no save files')

            if save is not None:
                gotKey = False
                try:
                    nodeKey = save[playerName]
                    gotKey = True
                    loaded = GameManager.instance.nodes[nodeKey]
                    GameManager.instance.playerName = playerName
                except:
                    if gotKey:
                        print("ERROR: save corrupt")
                    else:
                        print("ERROR: no such save file")
            
            return loaded

    instance = None
    def __init__(self, _name):
        if not GameManager.instance:
            GameManager.instance = GameManager.__GameManager(_name)
        else:
            GameManager.instance.playerName = _name

    def __getattribute__(self, name):
        return getattr(self.instance, name)