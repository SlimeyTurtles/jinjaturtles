from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
0
questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
]
# creating 3 questions each one is getting a different question prompt and the are each getting different answers

#function
def run_test(questions):
    #loop
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)