count = 0
sum_num = 0 # מחזיר את סהכ המספרים
arr = []

while count < 5:
    num = int(input("Enter number222: "))
    sum_num += num
    count += 1
    arr.append(num)

avg = sum_num // count
print(f"avg is - {avg}")
for num in arr:
    if num > avg:
        print(num, end=" ")
print("helooooooo2212312322")
print("helooooooo2222")
