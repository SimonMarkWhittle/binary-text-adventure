from node import Node

die = Node(
    choice="die",
    text="""
you die and cease to be
"""
)

ascend = Node(
    choice="ascend",
    text="""
you ascend to the heavens and become a god
"""
)

enterTheDoor = Node(
    choice="Enter the door.",
    text="""
You push the doors open and are bathed in brilliant light.
As your eyes adjust you find yourself standing in an open city square.
Nobody is around.
""",
    branch1=die,
    branch2=ascend
)

walkAway = Node(
    choice="Walk away.",
    text="""
You walk away never to return.
"""
)

root = Node(
    text="""
You stand before a grand door of intricately carved stone.
""",
    branch1=enterTheDoor,
    branch2=walkAway
)
