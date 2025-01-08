import random

print("ჩაიფიქრე რიცხვი 1-დან 100- მდე.")


low = 1
high = 100
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = random.randint(low, high)
    print(f"მე ვფიქრობ, რომ რიცხვი არის {guess}")
    
    
    response = input("თუ ეს რიცხვი არის ძალიან მაღალი, დაწერე 'მაღალი'. თუ ძალიან დაბალი, დაწერე 'დაბალი'. თუ სწორია, დაწერე 'სწორია'.: ").lower()
    
    if response == "სწორია":
        print(f"გილოცავ! მე ვიცოდი, რომ შენი რიცხვი {guess} იყო!")
        break
    elif response == "მაღალი":
        high = guess - 1
    elif response == "დაბალი":
        low = guess + 1
    else:
        print("გთხოვ, შეიყვანე სწორი პასუხი.")
    
    attempts += 1

if attempts == max_attempts:
    print(f"სამწუხაროდ, ვერ იპოვე სწორი რიცხვი")