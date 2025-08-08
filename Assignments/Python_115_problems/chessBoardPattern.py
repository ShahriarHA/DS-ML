# 33. Chessboard Pattern: Write a Python program using nested loops to print a chessboard pattern (alternating “X” and “O” characters) of size 8×8

for row in range(0,8):
    for col in range(0,8):
        if (row + col) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  
