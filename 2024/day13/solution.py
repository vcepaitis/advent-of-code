import numpy as np

def check_integer(a, eps=1e-3):
    delta = a % 1
    if abs(delta) < eps or abs(1-delta) < eps: 
        return True

#  Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# a = np.array([[94, 22], [34, 67]])
# b = np.array([8400, 5400])
tokens = 0

with open("input") as f:
    lines = f.read().split("\n\n")
    for line in lines:
        line = line.strip()
        lineA, lineB, linePrize = line.split("\n")
        lineAX = lineA.split(" ")[2].rstrip(",").split("+")[1]
        lineAY = lineA.split(" ")[3].split("+")[1]
        lineBX = lineB.split(" ")[2].rstrip(",").split("+")[1]
        lineBY = lineB.split(" ")[3].split("+")[1]
        prizeX = linePrize.split(" ")[1].rstrip(",").split("=")[1]
        prizeY = linePrize.split(" ")[2].split("=")[1]
        a = np.array([[int(lineAX), int(lineBX)], [int(lineAY), int(lineBY)]])
        b = np.array([int(prizeX), int(prizeY)])
        # part 2
        b += 10000000000000


        nA, nB = np.linalg.solve(a, b)
        print(a)
        print(b)
        print(nA, nB)
        if check_integer(nA) and check_integer(nB):
            print("solved")
            nA = round(nA)
            nB = round(nB)
            print(nA, nB)
            # part 1
            # if nA <= 100 and nB <= 100: 
            tokens += nA*3 + nB
        else:
            print("Didn't solve")
                
print(tokens)
