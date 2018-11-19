import random
question = input('Are You Single? Enter (Yes or No):')
random_number = random.randint(1, 10)
message = 'You are liar You have '+ str(random_number) + ' Boy friends'
if question=='Yes':
    print(message)
elif question=='No':
    print("Not necessary triangle Love")
else :
    print("Please Enter Yes Or No")