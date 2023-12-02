# objekts  how to deler it and printing plus adding
pro_dictionary = {
    "Bug": "rvived not only five centuries, but also the leap into electronic typesetting.",
    "key": "rvived not only five centuries, but also the leap into electronic typesetting."
}
# print(pro_dictionary["Bug"])
# to add a new key
pro_dictionary["newKey"] = "Hallo World"
# print(pro_dictionary)

# create an empty dictionary
dcy = {}

# wipe an existing dictionary
# pro_dictionary = {  }
# print(pro_dictionary)

# Edit an item in a dictionary
pro_dictionary["newKey"] = "is a new item"
# print(pro_dictionary)

# Loop through a dictionary
for key in pro_dictionary:
    print(key)
    print(pro_dictionary[key])


# ex1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for item in student_scores:
    scores = student_scores[item]

    if scores > 90:
        student_grades[item] = "Outstanding"
    elif scores > 80:
        student_grades[item] = "Exceeds Expectations"
    elif scores > 70:
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)

# EX2
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
