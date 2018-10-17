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

#======================================



def climbTheClocktower():
    return Node(
        choice="Climb the clocktower",
        text="""
You clamber up the rough side of the clocktower and get a spectacular view of the city.

""",
        branches=[
            die,
            ascend,
            ]
    )

continueRunning = Node(
    choice="Continue running",
    text="""
Unperturbed by this near setback, you continue your rush through the dingy space between the buildings.
""",
    branches=[
        die,
        ascend
    ]
)

investigateTheAbnormality = Node(
    choice="Investigate the abnormality",
    text="""
You turn around on your hands and knees and peer at the stone floor pavement.

You are greeting with the sight of a very thingy thing that looks thingy.
""",
    branches=[
        die,
        ascend
    ]
)

def raceThroughTheStreets():
    return Node(
        choice="Race through the streets",
        text="""
You take off running down the nearest allyway.

It twists and turns through dark corridors, loomed over by monumental buildings of cut stone.

What is this place? Where are its inhabitants?

These questions pass through your mind as you stumble over an abnormality in the path and nearly fall flat.
""",
        branches=[
            investigateTheAbnormality,
            continueRunning
        ]
    )

leapIntoAction = Node(
    choice="Leap into action",
    text="""
NO.

You are not a worthless piece of garbage person for having eaten a cabbage off of the ground.

Or maybe you are but that doesn't matter anymore. You have things to do and by God you're going to do them.
""",
    branches=[
        climbTheClocktower(),
        raceThroughTheStreets()
    ]
)

wallowUntilDeath = Node(
    choice="Wallow until death",
    text="""
You lie curled on the floor seething awash with powerful emotion beyond your ability to describe.
The sky grows dark as you slowly drain your body of fluids through your tears and turn into a dry husk.
Eventually, the wind picks up and your emaciated, leaflike body is lifted on the breeze and blown towards the horizon.

You are dead.
""",
    branches = [ ]
)

askYourselfWhy = Node(
    choice="Ask yourself why you would do that.",
    text="""
Disgust washes over you.

Why? Why would you do something so repulsive as eating a cabbage off of the ground?

Disgust is now replaced by shame as you fall to your knees weeping.

WHY?
""",
    branches=[
        wallowUntilDeath,
        leapIntoAction
    ]
)

eatACabbage = Node(
    choice="Eat a cabbage",
    text="""
You pick up one of the cabbages you've found laying on the ground and eat it. Gross.
""",
    branches=[
        askYourselfWhy,
        climbTheClocktower()
    ]
)


enterTheDoor = Node(
    choice="Enter the door.",
    text="""
You push the doors open and are bathed in brilliant light.
As your eyes adjust you find yourself standing in an open city square.
Nobody is around.
""",
    branches=[
        climbTheClocktower(),
        eatACabbage,
    ]
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
    branches=[
        enterTheDoor,
        walkAway
    ],
    isRoot=True
)