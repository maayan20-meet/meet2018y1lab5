name = input("what is your name")

print("Hello there" + " " + name.capitalize())
print("your name is " + str(len(name)) + " letters long!")
print("The first letter of your name is " + name[0].capitalize() + " and your last letter is " + name[-1].capitalize())

mood = input("how are you feeling?").lower()

if mood == "good":
    print("good!")

if mood == "bad":
    print("sorry to hear that")

else:
    print("dont know what that means")

