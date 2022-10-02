# Declaring arrays for inputs, where index 0 is count of that input type for the madlib we use
noun, plurNoun, presVerb, bodyPart, adj = [1], [2], [2], [1], [2]

for i in range(1, noun[0] + 1):
    noun.append(input("Enter a noun: "))

for i in range(1, plurNoun[0] + 1):
    plurNoun.append(input("Enter a plural noun: "))

for i in range(1, presVerb[0] + 1):
    presVerb.append(input("Enter a present tense verb: "))

for i in range(1, bodyPart[0] + 1):
    bodyPart.append(input("Enter a plural body part: "))

for i in range(1, adj[0] + 1):
    adj.append(input("Enter a adjective: "))

print("\nYour mad lib:\n")
print(f"Today, every student has a computer small enough to fit into his '{noun[1]}'.\n\
He can solve any math problem by simply pushing the computer's little '{plurNoun[1]}'.\n\
Computers can add, multiply, divide, and '{presVerb[1]}'. They can also '{presVerb[2]}' better than a human.\n\
Some computers are '{bodyPart[1]}'.\nOthers have a/an '{adj[1]}' screen that shows all kinds of\
 '{plurNoun[2]}' and '{adj[2]}' figures.")
