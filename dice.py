#arr = []
from random import randint

#
# for i in range(0, 1000000):
#     arr.append(randint(1, 15))
# count_1 = 0
# count_2 = 0
# count_3 = 0
# count_4 = 0
# count_5 = 0
# count_6 = 0
# count_7 = 0
# count_8 = 0
# count_9 = 0
# count_10 = 0
# count_11 = 0
# count_12 = 0
# for k in arr:
#     if k == 1:
#         count_1 = count_1 + 1
#     if k == 2:
#         count_2 = count_2 + 1
#     if k == 3:
#         count_3 = count_3 + 1
#     if k == 4:
#         count_4 = count_4 + 1
#     if k == 5:
#         count_5 = count_5 + 1
#     if k == 6:
#         count_6 = count_6 + 1
#     if k == 7:
#         count_7 = count_7 + 1
#     if k == 8:
#         count_8 = count_8 + 1
#     if k == 9:
#         count_9 = count_9 + 1
#     if k == 10:
#         count_10 = count_10 + 1
#     if k == 11:
#         count_11 = count_11 + 1
#     if k == 12:
#         count_12 = count_12 + 1
#
# print(f"1: {count_1 / 1000000 * 100}%")
# print(f"2: {count_2 / 1000000 * 100}%")
# print(f"3: {count_3 / 1000000 * 100}%")
# print(f"4: {count_4 / 1000000 * 100}%")
# print(f"5: {count_5 / 1000000 * 100}%")
# print(f"6: {count_6 / 1000000 * 100}%")
# print(f"7: {count_7 / 1000000 * 100}%")
# print(f"8: {count_8 / 1000000 * 100}%")
# print(f"9: {count_9 / 1000000 * 100}%")
# print(f"10: {count_10 / 1000000 * 100}%")
# print(f"11: {count_11 / 1000000 * 100}%")
# print(f"12: {count_12 / 1000000 * 100}%")
total = []
for i in range(0, 100):
    n = 0
    done = False
    while not done:
        n = n + 1
        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []
        arr6 = []

        arr1.append(randint(1, 6))
        arr2.append(randint(1, 6))
        arr3.append(randint(1, 6))
        arr4.append(randint(1, 6))
        arr5.append(randint(1, 6))
        arr6.append(randint(1, 6))
        if 1 in arr1 and 2 in arr2 and 3 in arr3 and 4 in arr4 and 5 in arr5 and 6 in arr6 :
            done = True
            total.append(n)
            break

print(sum(total)/len(total))
print(total)