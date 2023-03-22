import json


def f(age, courses, average):
    number = 0
    with open('test.json',encoding='utf8') as f:
        file = json.load(f)
    for person in file:
        for course in person["studies"]["courses"]:
            if course["name"] == courses:
                sum=0
                count=0
                for grade in course["grades"]:
                    sum += grade
                    count += 1
                if (sum/count) >= average and person["age"] >= age:
                    number += 1
    return number

    
print(f(21, "statistics", 4) )