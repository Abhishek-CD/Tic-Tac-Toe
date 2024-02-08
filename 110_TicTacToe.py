import os
def firstPattern() :
    print('       |       |       ')
    print('       |       |       ')
    print('_______|_______|_______')
    print('       |       |       ')
    print('       |       |       ')
    print('_______|_______|_______')
    print('       |       |       ')
    print('       |       |       ')
    print('       |       |       ')
def pattern(TTTarr) :
    os.system('cls')
    print('       |       |       ')
    print(f'    {TTTarr[0]}  |    {TTTarr[1]}  |    {TTTarr[2]}  ')
    print('_______|_______|_______')
    print('       |       |       ')
    print(f'    {TTTarr[3]}  |    {TTTarr[4]}  |    {TTTarr[5]}  ')
    print('_______|_______|_______')
    print('       |       |       ')
    print(f'    {TTTarr[6]}  |    {TTTarr[7]}  |    {TTTarr[8]}  ')
    print('       |       |       ')

def checkTie(tie):
    if all(x in tie for x in (1,2,3,4,5,6,7,8,9)) :
        return True
    else :
        return False
def check(arr) :
    if all(x in arr for x in (1,2,3)) or all(x in arr for x in (4,5,6)) or all(x in arr for x in (7,8,9)) or all(x in arr for x in (1,4,7)) or all(x in arr for x in (2,5,8)) or all(x in arr for x in (3,6,9)) or all(x in arr for x in (1,5,9)) or all(x in arr for x in (3,5,7)):
        return True
    else :
        return False
def Play() :
    arr1 = ['','','','','','','','','']
    arr2 = ['','','','','','','','','']
    tieArr = ['','','','','','','','','']
    TTTarr = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    firstPattern()
    while True :
        while True :
            print("PLAYER 1 - 'X' ")
            num1 = int(input('Enter position : '))
            if (num1 > 9) or (num1 in tieArr) :
                continue
            else :
                break
        TTTarr[num1 - 1] ='X'
        arr1[num1 - 1] = num1
        tieArr[num1 - 1] = num1
        pattern(TTTarr)
        tie = checkTie(tieArr)
        result1 = check(arr1)
        if result1 :
            print('PLAYER 1 WON')
            break
        else :
            pass
        if tie :
            print('TIE!!!')
            return
        while True :
            print("PLAYER 2 - 'O' ")
            num2 = int(input('Enter position : '))
            if (num2 > 9) or (num2 in tieArr):
                continue
            else :
                break
        TTTarr[num2 - 1] = 'O'
        arr2[num2 - 1] = num2
        tieArr[num2 - 1] = num2
        pattern(TTTarr)
        tie = checkTie(tieArr)
        result2 = check(arr2)
        if result2 :
            print('PLAYER 2 WON')
            break
        else :
            pass
        if tie :
            print('TIE!!!')
            return
os.system('cls')
Play()