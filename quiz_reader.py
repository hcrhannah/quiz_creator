import random

with open("quiz.txt", "r") as file:
    content = file.read()

raw_questions = content.strip().split('---')

questions = []

for raw_q in raw_questions:
    lines = raw_q.strip().split('\n')
    if len(lines) < 6:
        continue

    question_text = lines[0].split(": ", 1)[1]
    a = lines[1][3:]
    b = lines[2][3:]
    c = lines[3][3:]
    d = lines[4][3:]
    answer = lines[5].split(": ")[1]

    questions.append({
        'question': question_text,
        'choices': {'a': a, 'b': b, 'c': c, 'd': d},
        'answer': answer
    })

print(questions)


random.shuffle(questions)

# Start the quiz
score = 0

print("📚 Welcome to the Quiz! Answer by typing a, b, c, or d.\n")

for idx, q in enumerate(questions, start=1):
    print(f"Question {idx}: {q['question']}")
    print(f"a) {q['choices']['a']}")
    print(f"b) {q['choices']['b']}")
    print(f"c) {q['choices']['c']}")
    print(f"d) {q['choices']['d']}")



    while True:
        user_answer = input("Your answer (a/b/c/d): ").lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            break
        print("Invalid input. Please enter a, b, c, or d.")

    
    if user_answer == q['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")


print(f"You got {score} out of {len(questions)}")
