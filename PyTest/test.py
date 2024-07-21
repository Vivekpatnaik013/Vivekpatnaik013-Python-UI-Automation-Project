
def most_tips(user_ids, tips):
    max_pair = (-1, -1)

    for (user, tip) in zip(user_ids, tips):
        if tip > max_pair[1]:
            max_pair = (user, tip)

    return max_pair[0]
user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102]
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]
result=most_tips(user_ids,tips)
print(result)


























