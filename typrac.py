import random
import sys
import os

numberSet = "1234567890"
shiftNumberSet = "!@#$%^&*()"
otherSet = ",./<>?;':\"[]{}\\-=_+"

setDict = {"numbers": numberSet,
            "shiftnumbers": shiftNumberSet,
            "others": otherSet}
escapeKey = '\x1B'

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

if __name__ == "__main__":

    os.system('clear')
    single_input = _GetchUnix()
    char_in = ''
    practiceSet = numberSet + shiftNumberSet + otherSet

    if len(sys.argv) > 1:
        if sys.argv[1] in setDict:
            practiceSet = setDict[sys.argv[1]] 

    char_test = practiceSet[random.randint(0, len(practiceSet)-1)]
    while char_in != escapeKey:
        print(char_test)
        char_in = single_input()
        print(char_in)
        if char_in == escapeKey:
            pass
        elif char_test == char_in:
            os.system('clear')
            char_test = practiceSet[random.randint(0, len(practiceSet)-1)]
            print('Pass')
        else:
            print('Fail')
    os.system('clear')

