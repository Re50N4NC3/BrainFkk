# symbols table
rawTable = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,./<>?;:[]{}|!@#$%^&*()_+-='
table = [x for x in rawTable]

# create empty array of bytes
bytesArray = []
bytesAmount = 30000

for i in range(0, bytesAmount):
    bytesArray.append(0)

# instructions (code) array
rawInstruction = '++.'  # unedited text of the instruction
instructions = [x for x in rawInstruction]  # change rawInstruction to array of characters
instructionsLength = len(instructions)  # check length of instruction for further use

pointer = 0  # position of pointer at bytes array
position = 0  # position in code

brackets = 0  # amount of unbalanced brackets
menuOption = 0  # picked menu option
path = 'null'  # path to .txt file with instructions


# if position encounters "[" symbol, jump to the corresponding "]" symbol, if value at pointer position is other than 0
def beg_bracket(pos):  # beg_bracket(position in instruction)
    if instructions[pos] == '[':
        if bytesArray[pointer] != 0:  # check value of at the pointer position
            pos += 1
        else:
            bra = 1  # brackets are unbalanced

            while True:
                pos += 1  # move forward in instructions

                if instructions[pos] == '[':  # found unbalancing bracket in the code
                    bra += 1

                if instructions[pos] == ']':  # found balancing bracket in the code
                    bra -= 1

                if bra == 0:  # brackets are balanced, continue code execution
                    pos += 1
                    break


# if position encounters "]" symbol, go back to the corresponding "[" symbol
def end_bracket(pos):  # end_bracket(position in instruction)
    bra = 1  # brackets are unbalanced
    while True:
        pos -= 1  # move backwards in code

        # searching for brackets
        if instructions[pos] == ']':  # found unbalancing bracket in the code
            bra += 1

        if instructions[pos] == '[':  # found balancing bracket in the code
            bra -= 1

        if bra == 0:  # brackets are balanced, continue code execution
            break


# Main loop
print("Brain Fkk interpreter\n")
while True:
    # Menu
    print("\n Menu:\n 1 = read code from .txt file\n 2 = write code\n 3 = execute\n 4 = exit")
    menuOption = int(input())

#  read from txt
    if menuOption == 1:
        path = input('Enter .txt file path:\n')
        file = open(path, 'r')
        rawInstruction = file.read()
        instructions = [x for x in rawInstruction]
        instructionsLength = len(instructions)
        print('Loaded code:')
        print(*instructions, sep="")

# manually enter the code
    if menuOption == 2:
        print('Enter code:\n')
        rawInstruction = input()
        instructions = [x for x in rawInstruction]
        instructionsLength = len(instructions)

# execute code, clear bytes, and pointers
    if menuOption == 3:
        print('Clearing caches...')
        pointer = 0
        position = 0

        for z in range(0, bytesAmount):  # clear bytes
            bytesArray[z] = 0

        print(*bytesArray, sep=' ')  # print cleared bytes
        print('Executing code...')

# exit
    if menuOption == 4:
        print('Exiting...')
        break

    # Execution Loop
    while menuOption == 3:
        if position == len(instructions):  # reached end of code
            print('Brain Fkk complete\n  Bytes:')
            print(*bytesArray, sep=' ')
            break

        # check for instructions
        #  when < is found and if pointer doesn't exceed bytesArray max value increase pointer by 1
        if instructions[position] == '>' and pointer < len(bytesArray):
            pointer += 1

        #  when > is found and if pointer isn't equal to 0, decrease pointer by 1
        elif instructions[position] == '<' and pointer != 0:
            pointer -= 1

        # when + is found, increase value of byte at which pointer is actually on
        elif instructions[position] == '+':
            bytesArray[pointer] += 1

        # when + is found, decrease value of byte at which pointer is actually on
        elif instructions[position] == '-':
            bytesArray[pointer] -= 1

        # when . is found, print value from byte, using ascii table
        elif instructions[position] == '.':
            print(table[bytesArray[pointer]])

        # take numerical value from keyboard, and put it as byte value
        elif instructions[position] == ',':
            bytesArray[pointer] = int(input('Enter value of byte at position  ' + str(position)))

        # check if current byte is not equal to 0, if it is, jump to corresponding ]
        elif instructions[position] == '[':
            beg_bracket(position)

        # go to corresponding [ in instruction
        elif instructions[position] == ']':
            end_bracket(position)

        position += 1  # go to the next instruction
