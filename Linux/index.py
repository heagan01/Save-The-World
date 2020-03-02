import os

x = 3
y = 1
completed = 0

def drawBoxes():
    print('|   |   |   |   |')
    print('|   |   |   |   |')
    print('|___|___|___|___|')
    pass

def drawBoxesWithTree():
    print('|   |   |   |   |')
    print('|   |   |   | * |')
    print('|___|___|___|___|')
    pass

def drawBoxTop():
    print('|   |   |   |   |')

def drawTopOfBox():
    print(' ___ ___ ___ ___')

def drawBoxBottom():
    print('|___|___|___|___|')

def updateImage():
    global x
    global y
    global completed

    os.system('clear')

    if completed == 1:
        if x == 1:
            if y == 1:
                drawTopOfBox()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
            elif y == 2:
                drawTopOfBox()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
            elif y == 3:
                drawTopOfBox()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
            else:
                drawTopOfBox()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
        elif x == 2:
            if y == 1:
                drawTopOfBox()
                drawBoxes()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
            elif y == 2:
                drawTopOfBox()
                drawBoxes()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
            elif y == 3:
                drawTopOfBox()
                drawBoxes()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
            else:
                drawTopOfBox()
                drawBoxes()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
        elif x == 3:
            if y == 1:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
                drawBoxes()
            elif y == 2:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
                drawBoxes()
            elif y == 3:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
                drawBoxes()
            else:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
                drawBoxes()
        else:
            if y == 1:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
            elif y == 2:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
            elif y == 3:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
            else:
                drawTopOfBox()
                drawBoxes()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
    else:
        if x == 1:
            if y == 1:
                drawTopOfBox()
                drawBoxTop()
                print('| * |   |   | * |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
            elif y == 2:
                drawTopOfBox()
                drawBoxTop()
                print('|   | * |   | * |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
            elif y == 3:
                drawTopOfBox()
                drawBoxTop()
                print('|   |   | * | * |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
                drawBoxes()
        elif x == 2:
            if y == 1:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
            elif y == 2:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
            elif y == 3:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
            else:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
                drawBoxes()
                drawBoxes()
        elif x == 3:
            if y == 1:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
                drawBoxes()
            elif y == 2:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
                drawBoxes()
            elif y == 3:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
                drawBoxes()
            else:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
                drawBoxes()
        else:
            if y == 1:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('| * |   |   |   |')
                drawBoxBottom()
            elif y == 2:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   | * |   |   |')
                drawBoxBottom()
            elif y == 3:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   |   | * |   |')
                drawBoxBottom()
            else:
                drawTopOfBox()
                drawBoxesWithTree()
                drawBoxes()
                drawBoxes()
                drawBoxTop()
                print('|   |   |   | * |')
                drawBoxBottom()
    pass

def action():
    global x
    global y
    global completed

    if x == 1:
        if y == 3:
            completed = 1
    elif x == 2:
        if y == 4:
            completed = 1

    updateImage()
    getPlayerMovement()
    pass

def getPlayerMovement():
    global x
    global y

    if completed == 1:
        print('1) Up')
        print('2) Left')
        print('3) Down')
        print('4) Right')
        print('5) Action')
        print('6) Complete the tutorial')
    else:
        print('1) Up')
        print('2) Left')
        print('3) Down')
        print('4) Right')
        print('5) Action') 

    movement = raw_input('Please enter in your movement: ')

    if movement == 'w':
        x -= 1
    elif movement == 'a':
        y -= 1
    elif movement == 's':
        x += 1
    elif movement == 'd':
        y += 1
    elif movement == 'q':
        action()
    elif movement == '1':
        x -= 1
    elif movement == '2':
        y -= 1
    elif movement == '3':
        x += 1
    elif movement == '4':
        y += 1
    elif movement == '5':
        action()
    elif movement == '6':
        if completed == 1:
            completeTutorial()

    updateImage()
    getPlayerMovement()
    pass

def menu():
    os.system('clear')

    print('Save The World')
    print('\n')
    print('1) Start The Game')

    command = raw_input('Please enter in your input: ')

    if command == '1':
        updateImage()
        getPlayerMovement()
    pass

menu()