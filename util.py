
def MakeInputMessage(options):
    string = "[Please input "

    length = len(options)

    string += "'" + str(options[0]) + "'"

    if length == 1:
        return string + "]"
    elif length == 2:
        return string + " or '" + str(options[1]) + "']"

    for count in range(length - 2):
        string += ", '" + str(options[count + 1]) + "'"

    return string + ", or '" + str(options[length -1]) + "']"

def GoodInput(message, options, pleaseInput=True):
    goodInput = False

    inputMsg = ""
    if pleaseInput:
        inputMsg = MakeInputMessage(options)

    while not goodInput:
        if (message != ""):
            print(message)

        inpt = str(input(inputMsg + "\n"))

        if inpt in options:
            goodInput = True
        else:
            print("[Bad input]\n")

    return inpt

def GoodInput2Opt(message, opt1, opt2):
    goodInput = False
    answer = False

    while not goodInput:
        if (message != ""):
            print(message)

        inpt = input("[Please input '%s' or '%s']" % (opt1, opt2) + "\n")

        if inpt == opt1:
            answer = True
            goodInput = True
        elif inpt == opt2:
            answer = False
            goodInput = True
        else:
            print("\n[Bad input]\n")

    return answer

def NameInput():
    string = ""

    done = False
    while not done:
        print ("\n[name must be 15 or fewer characters]")
        print("name:")
        inpt = str(input())

        length = len(inpt)
        if length <= 15:
            done = True
            string = inpt

    return string

if __name__ == "__main__":
    options = ['foo', 'bar', 'baz']

    resp = GoodInput("Dewit", options, True)
    print(resp)
