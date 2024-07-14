
my_str = "aaaaabbbbbcccccdddd"
new_str = ""
s = 0
for i in range(len(my_str)):
    if my_str[i] != my_str[i+1]:
        window = i - s + 1
        s = i+1
        print(my_str[i],window)

