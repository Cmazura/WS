#MENGENAL NOMBOR

import random

def main():
    """MENEKA NOMBOR 1 HINGGA 10"""
    print("TEKA NOMBOR!")

x = random.randint(1,10)
guess = None

while x !=guess: #USING WHILE

    guess=int(input("Pilih nombor 1 hingga 10:"))

#using elif
    if x == guess:
        print("WOW HEBAT!")
    elif x>guess:
        print("CUBA NOMBOR LEBIH BESAR")
    elif x<guess:
        print("CUBA NOMBOR LEBIH KECIL")

main()

