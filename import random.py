import random

coin = random.choice (["heads","tails"])
print(coin)

number = random.randint(1,1000)
print(number)

cards= ["cross", "triangle", "circle","star"]
random.shuffle (cards)
for card in cards:
    print(card)