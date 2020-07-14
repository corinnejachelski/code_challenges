def decryptPassword(s):

    password = []
    nums = []

    for char in s:
        if char.isnumeric() and char != '0':
            nums.append(char)

    print(nums)

    for i in range(len(s)-1):
        if s[i].isupper() and s[i+1].islower():
            password.append(s[i+1])
            password.append(s[i])
        if s[i].islower() and s[i+1] != '*':
            password.append(s[i])
        if s[i] == '0':
            num = nums.pop()
            password.append(num)

    password.append(s[-1])

    return "".join(password)

print(decryptPassword("43Ah*ck0rr0nk"))