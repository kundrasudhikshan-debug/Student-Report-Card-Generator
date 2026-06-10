print("=== Personal Portfolio ===")

name = "Sudhikshan"
age = 16
hobbies = ["Programming", "Mathematics", "Minecraft"]
skills = ["Python", "Git", "Problem Solving"]

print("\nName:", name)
print("Age:", age)

print("\nHobbies:")
for hobby in hobbies:
    print("-", hobby)

print("\nSkills:")
for skill in skills:
    print("-", skill)

visitor = input("\nEnter your name: ")
print("Nice to meet you,", visitor)

print("\nThank you for visiting my portfolio!")