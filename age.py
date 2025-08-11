import time

age = int(input("Please enter your age for research purposes: "))

print("Searching the cosmos")
time.sleep(1)

print("Reviewing your search history")
time.sleep(1)

print("Taking a break")
time.sleep(1)

print("Eating biryani")
time.sleep(1)

if age < 14:
    print("You are still a child")
elif age == 14:
    print("You are the perfect age")
else:
    print("You are way too old")