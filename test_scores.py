#!/usr/bin/env python3

print("The Test Scores Program")
print()
print("Enter 999 to end input")
print("=======================")

counter = 0
score_total = 0

while True:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <=100:
        score_total += test_score
        counter +=1
    elif test_score == 999:
        break
    else:
        print("Test score must be from 0 through 100.","Score discarded. Try again.")

average_score = round(score_total/counter)

print("=======================")
print(f"Total Score: {score_total}"
        f"\nNumber of Scores: {counter}"
        f"\nAverage Score: {average_score}")
print()
print("End of program. Bye!")
