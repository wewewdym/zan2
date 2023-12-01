def find_maximum_value(input_list):
if not input_list: # проверяем, что список не пуст
return None

max_value = input_list[0] # принимаем первое значение как начальное максимальное значение

for num in input_list:
if num > max_value: # если текущее число больше максимального значения
max_value = num # обновляем максимальное значение

return max_value

n=int(input())
input_list =[]

for i in range (n):
num=int(input())
input_list.append(num)

print("Максимальное значение в списке:", find_maximum_value(input_list))
