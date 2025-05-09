with open("quiz.txt", "r") as file:
    content = file.read()

# Split into questions
raw_questions = content.strip().split('---')

for q in raw_questions:
    print(q)
    print("-----")
