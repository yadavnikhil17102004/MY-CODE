print("creating spam word list type stop to complete the list")

spamlist = ["spam","bot","noob","hack"]

while True:
    spamword = input("Enter a spam word: ")
    if spamword == "stop":
        break
    spamlist.append(spamword)
print("spamlist creation completed")
print("scanning")
while True:
    sentence = input("type sentence to check :")
    if any(word in sentence for word in spamlist):
        print("spam detected")
    else:
        print("no spam detected")

