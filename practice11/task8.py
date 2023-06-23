import random

num_elements = 5

first_list = [random.randint(10, 30) for _ in range(num_elements)]
second_list = [random.randint(10, 30) for _ in range(num_elements)]

third_list = [first_list[i] + second_list[i] for i in range(num_elements)]

average = sum(third_list) / num_elements

maximum = max(third_list)
minimum = min(third_list)

print(f"First list: {first_list}")
print(f"Second list: {second_list}")
print(f"Third list: {third_list}")
print(f"Average: {average}")
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")
