import random

# Додавання двох випадкових цілих чисел
random_int1 = random.randint(-100, 100)
random_int2 = random.randint(-100, 100)
addition_result = random_int1 + random_int2
print(f"Додавання двох випадкових цілих чисел: {random_int1} + {random_int2} = {addition_result}\n")

# Віднімання двох випадкових дійсних чисел
random_float1 = random.uniform(-100.0, 100.0)
random_float2 = random.uniform(-100.0, 100.0)
subtraction_result = random_float1 - random_float2
print(f"Віднімання двох випадкових дійсних чисел: {random_float1} - {random_float2} = {subtraction_result}\n")

# Множення двох дійсних чисел
random_float3 = random.uniform(-100.0, 100.0)
random_float4 = random.uniform(-100.0, 100.0)
multiplication_result = random_float3 * random_float4
print(f"Множення двох дійсних чисел: {random_float3} * {random_float4} = {multiplication_result}\n")

# Ділення двох дійсних чисел
random_float5 = random.uniform(-100.0, 100.0)
random_float6 = random.uniform(-100.0, 100.0)
try:
    division_result = random_float5 / random_float6
    print(f"Ділення двох дійсних чисел: {random_float5} / {random_float6} = {division_result}\n")
except ZeroDivisionError:
    print("Помилка: Ділення на нуль\n")

# Цілочисельне ділення двох цілих чисел
random_int3 = random.randint(-100, 100)
random_int4 = random.randint(-100, 100)
integer_division_result = random_int3 // random_int4
print(f"Цілочисельне ділення двох цілих чисел: {random_int3} // {random_int4} = {integer_division_result}\n")

# Остача від ділення випадкового цілого числа на випадкове ціле число
random_int5 = random.randint(-100, 100)
random_int6 = random.randint(-100, 100)
modulo_result = random_int5 % random_int6
print(f"Остача від ділення випадкового цілого числа на випадкове ціле число: {random_int5} % {random_int6} = {modulo_result}\n")

# Значення виразу: d**(-9)-(7*a+300/b)-10000%b
d = random.uniform(-100.0, 100.0)
a = random.uniform(-100.0, 100.0)
b = random.uniform(-100.0, 100.0)
expression_result = d**(-9) - (7*a + 300/b) - 10000 % b
print(f"Значення виразу: d**(-9) - (7*a + 300/b) - 10000%b: {expression_result}\n")
