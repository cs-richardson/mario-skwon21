"""
mario.py - San Kwon
This code prints out a double half pyramid of an inputted height.
"""

#input height and check height
height = (input("Height: "))
while not height.isdigit() or int(height) < 0 or int(height) > 23:
    height = input("Height: ")
height = int(height)

#print mario blocks
for i in range(1, height + 1):
        blocks = "#" * i
        blank = " " * (height - i)
        print(blank + blocks + "  " + blocks + blank)
