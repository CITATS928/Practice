def closestNumbers(numbers):
    sorted_number = sorted(numbers)
    
    diff = sorted_number[1]-sorted_number[0]
    ls_result =[]
    
    for i in range(len(numbers)-1):
        fake_diff = sorted_number[i+1]-sorted_number[i]
        if fake_diff < diff:
            diff = fake_diff
            ls_result = []
            ls_result.extend([sorted_number[i], sorted_number[i+1]])
        elif fake_diff == diff:
            ls_result.extend([sorted_number[i], sorted_number[i+1]])
    
    
    for i in range(0, len(ls_result),2):
        print(ls_result[i], ls_result[i+1])
    

if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    closestNumbers(numbers)