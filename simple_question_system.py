questions = [
    {
        'Question': 'What is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'What is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'What is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

correct_answers = 0
for question in questions:
    print(f'Question: {question["Question"]}')
    print()
    for index, option in enumerate(question['Options']):
        print(f"[{index}]: {option}")
    print()
    user_answer = input("Answer: ")
    if user_answer == question['Answer']:
        correct_answers += 1
        print("Correct!")
        print()
    else:
        print("Incorrect!")
        print()

print(f"You got {correct_answers} questions correct!")