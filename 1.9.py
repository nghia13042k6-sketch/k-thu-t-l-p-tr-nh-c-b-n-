print("sinh vien: Ho sy nghia")
print("Ma so SV : 245751030110012")
print("###################################")

s = input("Enter a string: ")

count_dict = {}

for ch in s:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

print(count_dict)

