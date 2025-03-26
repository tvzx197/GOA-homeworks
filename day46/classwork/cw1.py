def repeats(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    sum_unique = 0
    for num, cnt in count.items():
        if cnt == 1:
            sum_unique += num
    
    return sum_unique