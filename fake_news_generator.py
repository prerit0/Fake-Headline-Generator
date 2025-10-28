import random as r

Subjects = [
    'Salman Khan',
    'Virat Kohli',
    'Cristiano Ronaldo',
    'Kylie jenner'
    ]

Actions = [
    'Playing Football',
    'Caught cheating on his wife',
    'Wants to Sleep in garbage truck',
    'Fighting with President'
    ]

Objects = [
    'on the moon',
    'in the Parliament',
    'with a rabbit',
    'in a Hotel'
          ]

# This function helps to generate the output by taking random items from the the lists
def generate_headline(): 
     subject = r.choice(Subjects)
     action = r.choice(Actions)
     obj = r.choice(Objects)
     headline = f"{subject} {action} {obj}!"
     return headline

while True:
    # This is a try-exception method
    try:
        count = int(input("\nHow many headlines do you want to generate? "))
        print("\nGenerating Headlines...\n")
        
        for i in range(count):
            print(f"{i+1}. {generate_headline()}")
        
        again = input("\nDo you want to generate more? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for using Fake News Headline Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
