def repetitons_calculator(string):
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        
    print(count)

repetitons_calculator(str(input()))
