# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)
    for i in range(0, len(string)-sub_len+1):
        if string[i:i+sub_len] == sub_string:
            counter+=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)