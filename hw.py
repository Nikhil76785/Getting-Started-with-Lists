start = int(input("Start: "))
end = int(input("End: "))

x1 = start
x2 = start + 1
x3 = start + 2

sq1 = x1 * x1
sq2 = x2 * x2
sq3 = x3 * x3

squares = [sq1, sq2, sq3]

even = []
odd = []

if sq1 % 2 == 0:
    even.append(sq1)
else:
    odd.append(sq1)

if sq2 % 2 == 0:
    even.append(sq2)
else:
    odd.append(sq2)

if sq3 % 2 == 0:
    even.append(sq3)
else:
    odd.append(sq3)

print("Squares:", squares)
print("Even squares:", even)
print("Odd squares:", odd)

# It was a bit complicated but I managed to do it!