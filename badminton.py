import itertools
players_dic = {
    "С" : 1,
    "В" : 2,
    "Н" : 3,
    "Ю" : 4
}



list_of_players = ['Ю', 'Н', 'В', 'С']
# n = int(input("Enter number of players : "))
# for i in range(0, n):
#     player = str(input('Add player: '))
#     list_of_players.append(player)

# test print of .get()
# print(list)
#
# print(players_dic.get(list_of_players[0]))
# print(players_dic.get(list_of_players[1]))
# print(players_dic.get(list_of_players[2]))
# print(players_dic.get(list_of_players[3]))

# try zip
# values = []
# for i in range(len(list_of_players)):
#     values.append(players_dic.get(list_of_players[i]))
#
# print(values)
#
# result = zip(list_of_players, values)
# print(list(result))

# main part - shuffle
names = list(itertools.combinations(list(list_of_players), 2))
#[('Ю', 'Н'), ('Ю', 'В'), ('Ю', 'С'), ('Н', 'В'), ('Н', 'С'), ('В', 'С')]

print(names)

names_list = []
for i in names:
    i = list(i)
    names_list.append(i)

# [['Ю', 'Н'], ['Ю', 'В'], ['Ю', 'С'], ['Н', 'В'], ['Н', 'С'], ['В', 'С']]
print(names_list)


# try pandas replace names -> numbers (doesn't work)
# import pandas as pd
# numbers_list = []
# for i in names_list:
#     repl = list((pd.Series(i)).map(players_dic))
#     numbers_list.append(repl)

# [[3, 4], [3, 5], [3, 2], [4, 5], [4, 2], [5, 2]]
# print(numbers_list)

# replace names -> numbers
numbers_list = []
for i in names_list:
    res = [ele if ele not in players_dic else players_dic[ele] for ele in i]
    numbers_list.append(res)

print(numbers_list)


# main logic
semi_final = []
final = []


for i in numbers_list:
    for j in range(len(numbers_list)-1):
        if sum(i) - sum(numbers_list[j]) in [0, -1, 1]:
            sum_list = i + numbers_list[j]
            final.append(sum_list)


for i in semi_final:
    if i not in final:
        final.append(i)



super_final = []
for i in final:
    if len(set(i)) == 4:
        super_final.append(i)

print(super_final)
