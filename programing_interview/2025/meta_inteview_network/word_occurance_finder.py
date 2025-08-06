# with open("file.txt", 'r', encoding='utf-8') as file:
#     text = file.read().lower()  # Read and convert to lowercase
#     print(text)
#     words = text.split()
#     print(words)

my_dict = {}
with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        # print(line.strip())  # Removes trailing newline characters
        for word in line.split():
            my_dict[word] = my_dict.get(word,0)+1

# print(my_dict)

list_of_list = []

for key,value in my_dict.items():
    list_of_list.append([key,value])

list_of_list.sort(key=lambda test: test[1], reverse=True)
print(list_of_list)

# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# print(sorted_dict)