import functools

with open("mentees.txt", "r") as f:
    mentees = f.read().splitlines()
    mentees = [mentee for mentee in mentees if mentee != ""]


counter = 0


def sortcmp(A, B):
    global counter

    counter += 1

    print(f"Match {counter}")
    print(f"A: {A}")
    print(f"B: {B}")

    result = input("Result (A/B/D): ")
    print("")

    if result.lower() == "a":
        return -1
    elif result.lower() == "b":
        return 1
    elif result.lower() == "d":
        return 0
    else:
        print("Invalid result")
        return sortcmp(A, B)


sorted_mentees = sorted(mentees, key=functools.cmp_to_key(sortcmp))
print("=========")
print("Results")
print("=========")
sorted_mentees = sorted_mentees[::-1]
for mentee in sorted_mentees:
    print(mentee)
