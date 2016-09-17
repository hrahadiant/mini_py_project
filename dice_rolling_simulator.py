# mini dice rolling simulator
import random

while True:
	dice = random.randint(1,6)
	roll = input("Roll dice press enter or q to quit> ")
	if roll.lower() == 'q':
		exit()
	print(dice)
