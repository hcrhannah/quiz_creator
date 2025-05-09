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
