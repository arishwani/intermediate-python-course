import random
def main(): 

	#dice_rolls = 2
	dice_rolls = int(input('How many dice would you like to roll? '))
	dice_size = int(input('How many sides are the dice? '))

	dice_sum = 0
	for i in range(0,dice_rolls):
		#roll = random.randint(1,6)
		roll = random.randint(1,dice_size)
		dice_sum = dice_sum + roll
		#OR use dice_sum += roll
		#print(f'You rolled a {roll}')
		if roll == 1:
			print(f'You rolled a {roll}! Critical Fail')
			'''When changing a value we had 
			assumed to be a specific number previously, 
			we need to make sure the rest of our code 
			still makes sense. All dice start with one, so our if 
			statement regarding one still makes sense. Our elif statement regarding six doesn't though, as it is no longer guaranteed to be the highest number. Let's make it so our "Critical Success" line is printed to whatever the highest number of our desired dice is. The highest number a dice can roll is the same as the number of sides, so we just to replace our elif statement with:'''
		#elif roll == 6:
		elif roll == dice_size:
			print(f'You rolled a {roll}! Critical Fail')
		else:
			print(f'You rolled a {roll}')
	print(f'You have rolled a total of {dice_sum}')



if __name__== "__main__":
  main()