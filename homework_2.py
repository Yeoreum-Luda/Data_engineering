subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [[subjects[i], grades[i]] for i in range(4) ]

print(gradebook)

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

gradebook[5][1] += 5

gradebook[2].remove(gradebook[2][1])

gradebook[2].append("Pass")

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)