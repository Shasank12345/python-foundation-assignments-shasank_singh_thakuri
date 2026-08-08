#STUDENT SCORE DICTIONARY

student_scores={
    "Ram" : 78,
    "Shasank" : 55,
    "Gopal" : 94,
    "Hari" : 61,
    "Syam" : 48
}
print("The student's who scored :")
for name,score in student_scores.items():
    print(f"{name}: {score}")


print("\nThe student's with score above 60 :")
score_abv_60={name:score for name ,score in student_scores.items() if score>=60} #dictiomary comprehension
for name,score in score_abv_60.items():
    print(f"{name}: {score}")

high_score=max(student_scores.values())
for name,score in student_scores.items():
    if score==high_score:
        print(f"\nThe student with highest score is {name} with score {score}")

total=sum(student_scores.values())
average_score=total/len(student_scores)
print(f"\nThe average score: {average_score:.3f}")
