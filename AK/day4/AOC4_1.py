import hashlib


input = "yzbqklnj"
input1 = "abcdef609043"

sum = 0
check = 0

def inputEncode(toEncode):
    return hashlib.md5(toEncode.encode('utf-8')).hexdigest()

while 1:
    hashed = str(inputEncode(input+str(sum)))
    if hashed[0:5] == "00000" and check == 0:
        print(f"first task: {sum}")
        check = 1
    elif hashed[0:6] == "000000":
        print(f"second task: {sum}")
        break
    sum += 1

