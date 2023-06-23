text = "Рядок"
print(list(text))

new_list = []
for i in text:
    new_list.append(i)
print(new_list)

new_list2 = [i for i in text]
print(new_list2)