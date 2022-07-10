# answer = input("Do you want to take this quiz? ")

#if answer != "yes":
    # quit()


def ifMain():
    answer = input("Do you want to take this quiz? ").lower()
    # print(answer)
    if answer == "no":
        # print(answer)
        print("Maybe next time!")
        quit()
    elif answer == "yes":
        print("Let's a go!")
    else:
        print("Answer was not yes or no.")
        quit()
    return


def quiz():
    score = 0
    answer = input("How old is Brian? ")
    if answer == "29":
        print("correct")
        score += 1
        print(str(score/5 * 100) + "% right")
    # elif answer != "29":
    #     print("That's wrong bro")
    #     print(f"{score * 100}% right") could be just ended with else for shorter code
    else:
        print("That's wrong bro")
        print(f"{score * 100}% right")
    return

def quiz1():
    score = 0
    # if quiz() == "correct":
    #     score += 2
    # if quiz() == "correct":
    #     score = 1
    answer = input("What day is the 3rd day of the week?: ").lower()
    if answer == "tuesday":
        print("correct")
        # score += 1
        print(str(score/5 * 100) + "% right")
    else:
        print("That's wrong bro")
        print(f"{score/5 * 100}% right")
        return

def quiz2():
    score = 0
    # if quiz1() == "correct":
    #     score = 2
    answer = input("What is the name of Chris's first dog?: ").lower()
    if answer == "benji":
        print("correct")
        score += 3
        print(str(score/5 * 100) + "% right")
    else:
        print("That's wrong bro")
        print(f"{score/5 * 100}% right")
        return
def quiz3():
    score = 0
    # if quiz2() == "correct":
    #     score = 3
    answer = input("What street did Brian and Chris grow up on?: ").lower()
    if answer == "copperfield":
        print("correct")
        score += 4
        print(str(score/5 * 100) + "% right")
    else:
        print("That's wrong bro")
        print(f"{score/5 * 100}% right")
        return

def quiz4():
    score = 0
    if quiz() != "correct":
        score -= 1
    if quiz1() != "correct":
        score -= 1
    if quiz2() != "correct":
        score -= 1
    if quiz3() != "correct":
        score -= 1
    # if quiz3() == "correct":
    #     score = 4
    answer = input("Where did they serve $2 jager bombs on 6th street?: ").lower()
    if answer == "latitude":
        print("correct")
        score += 5
        print(str(score/5 * 100) + "% right")
    else:
        print("That's wrong bro")
        print(f"{score/5 * 100}% right")
        return

def main():
    # ifMain()
    # quiz()
    # quiz1()
    # quiz2()
    # quiz3()
    # quiz4()
    return

#thought about the quiz game wrong, instead of breaking each block of code function to each question it should
# of been structure like this 1. def list(): list of question ||| 2. def answercheck(): ||| 3. def printscore():

# main()
questions = {"How old is Brian Dang? ": "29",
             "What is the 3rd day of the week? ": "tuesday",
             "What is the name of Chris's first dog? ": "benji",
             "What street did Chris and Brian grow up on? ": "copperfield",
             "Where did they serve $2 Jager bombs at on down town 6th street? ": "latitude"}

def quizgame():
    guesses = []
    correct_guesses = 0
    for answers in questions:
        print("----------------------------")
        guess = input(answers)
        guess = guess.lower()
        guesses.append(guess)

        correct_guesses += answercheck(questions.get(answers), guess)
        print(f'{correct_guesses/5 * 100 }%')
    print(f"thanks for playing you got {correct_guesses/5 * 100 }%")
    return

#if i want to improve my game ad a play again function
def answercheck(answers, guess):
    if answers == guess:
        print(f'correct!')
        return 1
    else:
        print(f'Wrong!')
        return 0

ifMain()
quizgame()


