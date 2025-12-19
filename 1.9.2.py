print("sinh vien: Ho sy nghia")
print("Ma so SV : 245751030110012")
print("###################################")

s = input("Enter a string: ")

count_dict = {}
for ch in s:
    count_dict[ch] = s.count(ch)

print(count_dict)
