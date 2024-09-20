"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    fullarr = list(arr)
    srt= sorted(fullarr, reverse=True)
    for index in range(len(srt)):
        if srt[index]!=srt[index+1]:
            print(srt[index+1])
            break