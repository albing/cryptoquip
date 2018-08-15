'''Cryptoquip solver'''

orig = input("Original text: ")
solved = [None for _ in orig]

def remaining():
    '''Print the unused characters'''

    r=[x for x in 
        'abcdefghijklmnopqrstuvwxyz'
        if x not in solved]
    print(r)

def display():
    '''Print the interpolated message'''

    for i, ch in enumerate(solved):
        if ch is None:
            print(orig[i], end='')
        else: print(ch, end='')
    print()

def subs(old, new):
    '''Substitute one character for another'''

    if new in solved:
        ipt = input("Already exists; continue? y/N")
        if ipt not in "yY" or ipt is None or ipt == "":
            return

    for i, ch in enumerate(orig):
        if ch == old:
            solved[i] = new

if __name__ == "__main__":
    while(True):
        display()
        ipt = input("Xy: ")

        if "?" in ipt:
            remaining()
        elif len(ipt) == 2:
            if ipt[1] == " ":
                subs(ipt[0], None)
            else: subs(ipt[0], ipt[1])
        else:
            print("Substitute X with y; '?' to see available letters")

