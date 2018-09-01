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

#======================================

eatACabbage = Node(
    choice="Eat a cabbage",
    text="""
You pick up one of the cabbages you've found laying on the ground and eat it. Gross.
""",
    branch1=die,
    branch2=ascend
)

climbTheClocktower = Node(
    choice="Climb the clocktower",
    text="""
You clamber up the rough side of the clocktower and get a spectacular view of the city.
""",
    branch1=die,
    branch2=ascend
)

enterTheDoor = Node(
    choice="Enter the door.",
    text="""
You push the doors open and are bathed in brilliant light.
As your eyes adjust you find yourself standing in an open city square.
Nobody is around.
""",
    branch1=climbTheClocktower,
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
    branch2=walkAway,
    isRoot=True
)
