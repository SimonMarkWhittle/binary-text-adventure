
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
            print("[Bad input]\n")

    return answer