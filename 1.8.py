
print("sinh vien: Ho sy nghia")
print("Ma so SV : 245751030110012")
print("###################################")



a, b = 1, 2
total = 0

print(a, end=" ")

while a <= 4_000_000:
    if a % 2 == 0:
        total += a

    a, b = b, a + b
    print(a, end=" ")

print("\nSum of even numbers in Fibonacci series:", total)
