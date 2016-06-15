# -*- coding: utf-8 -*-
loopflag = 1

from internetflightdeparture import *


def printMenu():
    print("\n====================================\n")

    print("     T : 시간 조회")
    print("     L : 편명 조회")
    print("     A : 항공사 조회")
    print("     P : 공항 조회")
    print("     E : 결과 이메일로 전송")
    print("     Q : 프로그램 종료")
    
    print("\n====================================\n")
    
    

def launcherFunction(key):
    if key == 'A' or key == 'a':
        num = int(input("1.출발  2.도착  :"))
        airline = input("항공사 입력 :")
        if num == 1:
            AirLineDeparture(airline)
        elif num == 2:
            AirLineArrival(airline)
        else:
            print("잘못된 입력입니다.")
    elif key =='L' or key =='l':
        num = int(input("1.출발  2.도착  :"))
        flightid = input("항공 편명 입력 :")
        if num == 1:
            FlightIDDeparture(flightid)
        elif num == 2:
            FlightIDArrival(flightid)
        else:
            print("잘못된 입력입니다.")
    elif key == "T" or key == "t":
        num = int(input("1.출발 2.도착  :"))
        start = input("From time :")
        end = input("To time :")
        if num == 1:
            TimeLineDeparture(start,end)
        elif num == 2:
            TimeLineArrival(start,end)
        else:
            print("잘못된 입력입니다.")
    elif key == "P" or key == "p":
        num == int(input("1.출발   2.도착  :"))
        airport = input("공항 코드 :")
        if num == 1:
            AirportDeparture
        elif num == 2:
            AirportArrival(airport)
        else:
            print("잘못된 입력입니다.")
    elif key == "E" or key == "e":
        pass
    elif key == "Q" or key == "q":
        Quitflight()
        
        
        
def Quitflight():
    global loopflag
    loopflag = 0



while(loopflag>0):
    printMenu()
    inputkey = str(input("메뉴 선택 :"))
    launcherFunction(inputkey)