

from stack import Stack
print('''
 _____                                   __   _   _                   _ 
|_   _|____      _____ _ __ ___    ___  / _| | | | | __ _ _ __   ___ (_)
  | |/ _ \ \ /\ / / _ \ '__/ __|  / _ \| |_  | |_| |/ _` | '_ \ / _ \| |
  | | (_) \ V  V /  __/ |  \__ \ | (_) |  _| |  _  | (_| | | | | (_) | |
  |_|\___/ \_/\_/ \___|_|  |___/  \___/|_|   |_| |_|\__,_|_| |_|\___/|_|

\n''')


print("Let's play Towers of Hanoi!!")

class Stack:

    def __init__(self, name=""):
        self.name = name
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)

    def get_name(self):
        return self.name

    def print_items(self):
        max_len = 2 * num_disks  # This will provide enough room for each disk
        ascii_art = [" " * max_len for _ in range(num_disks)]
        for idx, disk_size in enumerate(self.items):
            disk = "==" * disk_size
            ascii_art[num_disks - idx - 1] = disk.center(max_len)
        return ascii_art

    Stack.push = push
    Stack.pop = pop
    Stack.peek = peek
    Stack.is_empty = is_empty
    Stack.get_name = get_name


left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [left_stack, middle_stack, right_stack]

# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("\nHow many disks do you want to play with?\n"))

for disk in range(num_disks, 0, -1):
    left_stack.push(disk)


num_optimal_moves = (2 ** num_disks - 1)
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))


# Get User Input
def get_input():
    choices = [stack.get_name()[0].upper() for stack in stacks]

    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))

        user_input = input("").upper()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


# Play the Game

num_user_moves = 0


def print_stacks(stacks):
    stack_arts = [stack.print_items() for stack in stacks]
    for lines in zip(*stack_arts):
        print('   '.join(lines))
    print(*[stack.get_name().center(2 * num_disks) for stack in stacks], sep='   ')


while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...\n")
    print_stacks(stacks)

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.get_size() == 0:
            print("\nInvalid Move. Try Again")

        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break

        else:
            print("\nInvalid Move. Try Again")

print_stacks(stacks)
print('''
                    ____    ____  ______    __    __     ____    __    ____  __  .__   __.  __  
                    \   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  | 
                     \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  | 
                      \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  | 
                        |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__| 
                        |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__) 
                                                                            
''')
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}\n".format(num_user_moves,
                                                                                               num_optimal_moves))
