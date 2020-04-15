
from collections import Counter


name1 = 'marimuthu'
name2 = 'kiran'
main_str = 'FLAMES'

name1_set = set(name1)
name2_set = set(name2)

common_lett = name1_set.intersection(name2_set)
unique_letter = name1_set.difference(name2_set)
summ = name2_set.difference(name1_set)
unique_letter.update(summ)
print(unique_letter)
print(common_lett)
cou_1 = Counter(name1)
cou_2 = Counter(name2)
count = 0

for letter in unique_letter:
    count += cou_1[letter] if letter in cou_1 else cou_2[letter]

for letter in common_lett:
    summa = 0
    summa += cou_1[letter]
    summa += cou_2[letter]
    count += summa % 2

res_str = 'FLAMES'*25

strike_count = count
print(count)
loop_count = 6

while loop_count > 1:
    let = res_str[strike_count-1]
    res_str = res_str[strike_count:]
    res_str = res_str.replace(let, '')
    loop_count -=1
print(res_str)


