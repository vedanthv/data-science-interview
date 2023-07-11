def josephus(n, k):
    # Creating a list of n people
    people = list(range(1, n + 1))

    # Starting index for counting
    index = 0

    while len(people) > 1:
        # Find the next person to eliminate
        index = (index + k - 1) % len(people)

        # Remove the eliminated person from the list
        people.pop(index)

    # Return the last remaining person
    return people[0]


# Example usage:
n = 7
k = 3
last_person = josephus(n, k)
print(f"The last person remaining is: {last_person}")