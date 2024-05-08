def calculate_score(person_info, scores):

    name, age, gender, height, weight = person_info

    total_score = sum(scores)

    is_adult = age >= 18

    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Height:", height)
    print("Weight:", weight)
    print("Total Score:", total_score)
    print("Adult:", is_adult)

person_info = ("John", 25, "Male", 175, 70)
scores = [85, 90, 75, 88, 92]
calculate_score(person_info, scores)