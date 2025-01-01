def repetitions_calculator(string):
    max_count = 1
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1  
    max_count = max(max_count, count)
    
    print(max_count)

repetitions_calculator(input())

