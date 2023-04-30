import random

correct_answers = 0
for i in range(1, 11):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    question = f"Question {i}: {x} x {y} = "
    answer = int(input(question))
    if answer == x*y:
        print("Right!")
        correct_answers += 1
    else:
        print("Wrong. The answer is", x*y)
print("You got", correct_answers, "questions right out of 10.")