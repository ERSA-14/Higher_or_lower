import random
from game_data import data
from art import logo, vs

print(logo)
A = {}
B = {}

current_score = 0
continue_playing = True

def Intial():
	global A
	global B
	A = random.choice(data)
	B = random.choice(data)
	print(f"Campare A : {A['name']} , a {A['description']} , from {A['country']} ")
	print(vs)
	print(f"Against B : {B['name']} , a {B['description']} , from {B['country']} ")

Intial()

def camparsion():
	global continue_playing
	global current_score
	user_choice = input("which do you think has more follower A or B \n").lower()
	
	if user_choice == 'a':
		if A['follower_count'] > B['follower_count']:
			current_score += 1
			print(f"You guessed right, Your current score is {current_score}")
		else:
			continue_playing = False
			print(f"You lose , your final score is {current_score}")
			return
			
	elif user_choice == 'b':
		if B['follower_count'] > A['follower_count']:
			current_score += 1
			print(f"You guessed right, Your current score is {current_score}")
		else:
			continue_playing = False
			print(f"You lose , your final score is {current_score}")
			return
	
	else:
		print("Enter a valid response, You lose")
		return
	return
	
while continue_playing:
	camparsion()
	if continue_playing == True:
		print("\n" * 5)
		A = B
		B = random.choice(data)
		print(f"Campare A : {A['name']} , a {A['description']} , from {A['country']} ")
		print(vs)
		print(f"Against B : {B['name']} , a {B['description']} , from {B['country']} ")
	