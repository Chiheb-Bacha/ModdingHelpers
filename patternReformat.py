while True: 
    print("Enter a pattern in the '\\xAB' format")
    pattern = input()
    pattern = [b for b in pattern.split("\\x") if b]
    print(pattern)
    print("Enter a mask in the 'x?x' format")
    mask = input()
    if len(mask) != len(pattern):
        print("Pattern and mask length don't match")
        continue
    else:
        i = 0
        for c in mask:
            if c == '?':
                pattern[i] = '?'
            i = i+1
    newPattern = ""
    for byte in pattern:
        newPattern = newPattern + byte + " "
    print(newPattern)