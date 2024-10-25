"""
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  S= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

def minion_game(string):
    # your code goes here
    stuart_score=0
    kevin_score=0
    vowels=['A','E','I','O','U']
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score+=len(string)-i
            #for j in range(i,len(string)):
                #kevin_score+=1
                #print(string[i:j+1])
        if string[i] not in vowels:
            stuart_score+=len(string)-i
            #for k in range(i, len(string)):
                #stuart_score+=1
                #print(string[i:k+1])
    
    if kevin_score>stuart_score:
        print(f'Kevin {kevin_score}')
    elif stuart_score>kevin_score:
        print(f'Stuart {stuart_score}')
    else:
        print('Draw')

    

if __name__ == '__main__':
    s = input()
    minion_game(s)