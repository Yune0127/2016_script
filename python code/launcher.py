# -*- coding: utf-8 -*-


loopFlag = 1
from internetflight import *



def printmenu():
    print("====================================")
    print("항공사로 검색하기 : l")
    print("공항으로 검색하기 : a")
    print("시간대로 검색하기 : t")
    print("검색하기 : s")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("====================================")
    


def launcherFunction(key):
    if key == 'l':  #항공사
        PrintAirline()
    elif key == 'a':    #공항
        PrintAirline()
    elif key == 't':    #시간대
        Printtimeline()
    elif key == 's':    #검색하기
        SearchFlight()
    elif key == 'p':    #dom -> xml
        PrintDOMtoXML()
    elif key == 'w':
        LoadXMLDeparture()
    elif key == 'q':    #그만하기
        Quit()
    else:
        print ("error : unknow menu key")




def Quit():
    global loopFlag
    loopFlag = 0
    DocFree()



##### run #####
while(loopFlag > 0):
    printmenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("종료되었습니다.")