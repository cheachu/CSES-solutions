ans = 1
streak = input()
for i in streak:
    if streak[i] ==  streak[i+1]:
        ans += 1
print(ans)        