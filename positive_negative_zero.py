positive = 0
negative = 0
zero = 0
while True:
    number = int(input("Enter a number: "))
    if number == 99:
        break
    if number < 0:
        negative += 1
    if number > 0:
        positive += 1
    else:
        zero += 1
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")



0





