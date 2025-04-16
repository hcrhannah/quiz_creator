question_number = 1
while True:
    print("Enter your question (or type 'exit' to stop):")
    question = input("Enter question: ")
    if question.lower() == "exit":
        break
    a = input("Choice a: ")
    b = input("Choice b: ")
    c = input("Choice c: ")
    d = input("Choice d: ")

    while True:
        answer = input("Correct answer (a/b/c/d): ").lower()
        if answer in ['a', 'b', 'c', 'd']:
            break
        print("Invalid input. Please enter a, b, c, or d.")
        
    print("Question:", question)
    print("a)", a)
    print("b)", b)
    print("c)", c)
    print("d)", d)
    print("Answer:", answer)

    with open("quiz.txt", "a") as file:
        file.write(f"Question #{question_number}: {question}\n")
        file.write("a) " + a + "\n")
        file.write("b) " + b + "\n")
        file.write("c) " + c + "\n")
        file.write("d) " + d + "\n")
        file.write("Answer: " + answer + "\n")
        file.write("---\n")

    question_number += 1
