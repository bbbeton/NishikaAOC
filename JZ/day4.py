import hashlib

input = "ckczppom"

n = 1
while True:
    check = input + str(n)
    if hashlib.md5(check.encode()).hexdigest()[:5] == "00000":
        break
    n += 1
print(n)

n = 1
while True:
    check = input + str(n)
    if hashlib.md5(check.encode()).hexdigest()[:6] == "000000":
        break
    n += 1
print(n)
