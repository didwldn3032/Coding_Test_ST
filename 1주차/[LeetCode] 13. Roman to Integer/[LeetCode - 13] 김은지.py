sv_pairs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

try:
    s = input("s = ")
    if len(s) < 1 or len(s) > 15:
        print("입력 문자열의 길이는 1이상 15이하입니다.")
except:
    print("error")

res = 0

keys = list(sv_pairs.keys())
values = list(sv_pairs.values())

res_ = (values[keys.index(c)] for c in s)
res = sum(res_)

print("Output: " + str(res))
print("Explanation: ")