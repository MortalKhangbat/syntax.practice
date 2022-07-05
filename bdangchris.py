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
    if answer == "30":
        print("correct")
        score += 1
        print(str(score * 100) + "% right")
    return

def main():
    # ifMain()
    quiz()
    return

main()

