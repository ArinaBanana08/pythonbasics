import random

participants =  ["Me","Ya","Onemore"]

random.shuffle(participants)

for i in range(len(participants)):
   giver = participants[i]
   receiver = participants[(i + 1) % len(participants)]
   print(giver, "is the Secret Santa for",receiver)
