print("sinh vien: Ho sy nghia")
print("Ma so SV : 245751030110012")
print("###################################")

result = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))

print(",".join(result))
