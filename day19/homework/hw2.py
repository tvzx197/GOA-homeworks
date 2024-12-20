number = [10, 20, 30, 40, 50]
def find_max(numbers):
    # დავიწყებთ პირველ რიცხვთან
    max_num = numbers[0]
    
    # გადავივლით ყველა რიცხვზე სიაში
    for num in number:
        if num > max_num:
            max_num = num
    
    return max_num



print("max num is :", find_max(number))
