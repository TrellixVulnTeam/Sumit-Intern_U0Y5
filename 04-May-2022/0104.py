print("""You enter a dark room with two doors.
2 Do you go through door #1 or door #2?""")

door = int(input(">"))

if door == 1 :
     print("There's a giant bear here eating a cheese cake.")
     print("What do you do?")
     print("1. Take the cake.")
     print("2. Scream at the bear.")

bear = input("> ")

if bear == "1":
    print("The bear eats your face off. Good job!")
elif bear == "2":
    print("The bear eats your legs off. Good job!")
elif bear == "3":
    print(f"Well, doing {bear} is probably better.")
    print("Bear runs away.")

else:

    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

insanity = input("> ")