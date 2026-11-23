sum = 0
average = 0
count = 0
maximum = None

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    sum += number
    count += 1

    if maximum is None:
        maximum = number
    else:
        maximum = max(maximum, number)
if count > 0:
    average = sum / count

print(f"sum: {sum}")
print(f"average: {average}")
print(f"count: {count}")
print(f"maximum: {maximum}")
