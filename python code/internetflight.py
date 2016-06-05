# -*- coding: utf-8 -*-
from xmlflight import *
import urllib
import smtplib
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
regKey = '0bIrS1znKGJAfGh%2BKcvBHYCvSUEKAVEjjx02Wn3JIFCaWWVYsAdZB0dCjsq%2BbF9BSsw%2B7IxBsDM0qo9D%2FQ87wA%3D%3D'

#openAPI 접속정보
server = "openapi.airport.kr/openapi/service"

# smtp 정보
host = "smtp.gmail.com" # SMTP 서버 주소.
port = "587"

# 출발 운항 정보 URI
def userDepartureURIBuilder(server,**user):
    str = "http://" + server + "/StatusOfPassengerFlights/getPassengerDepartures" +"?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
    
# 도착 운항정보 URI
def userArrivalURIBuilder(server,**user):
    str = "http://" + server + "/StatusOfPassengerFlights/getPassengerArrivals" +"?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
        
def Printtimeline():
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    print("운항상태를 선택하세요. 1.출발   2.도착")
    select = int(input("입력 :"))
    if select == 1:
        print("시간을 입력하세요. (형식 : HHMM)")
        s = str(input("Input start time :"))
        e = str(input("Input end time :"))
        
        uri = userDepartureURIBuilder(server,ServiceKey = regKey,from_time = s,to_time = e,airport="",flight_id="",airline="" )
        conn.request("GET",uri)
        
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Data downloading Complete!")
            return extractDepartureData(req.read())
        else:
            print("Failed! Please Retry.")
    elif select == 2:
        print("시간을 입력하세요. (형식 : HHMM)")
        s = str(input("Input start time :"))
        e = str(input("Input end time :"))
        uri = userArrivalURIBuilder(server,ServiceKey = regKey,from_time = s,to_time = e )
        conn.request("GET",uri)
        
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Data downloading Complete!")
            return extractArrivalData(req.read())
        else:
            print("Failed! Please Retry.")
            return None
    else:
        print("Wrong Input! Please Retry.")
        return None
            

def PrintAirport():
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    print("운항상태를 선택하세요.")
    select = int(input("1.출발공항   2.도착공항"))
    if select == 1:
        input_airport = input("공항코드를 입력하세요 : ")
        uri = userArrivalURIBuilder(server,ServiceKey = regKey,from_time = "",to_time = "",airport=input_airport,flight_id="",airline="" )
        conn.request("GET",uri)
        
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Data downloading Complete!")
            return extractDepartureData(req.read())
        else:
            print("Failed! Please Retry.")
    elif select == 2:
        input_airport = input("공항코드를 입력하세요 : ")
        uri = userDepartureURIBuilder(server,ServiceKey = regKey,from_time = "",to_time = "",airport=input_airport,flight_id="",airline="" )
        conn.request("GET",uri)
        
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Data downloading Complete!")
            return extractDepartureData(req.read())
        else:
            print("Failed! Please Retry.")
     
     
def PrintAirline():
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    print("운항상태를 선택하세요.")
    select = int(input("1.출발   2.도착"))
    if select == 1:
        input_airline = input("항공사 코드를 입력하세요 : ")
        uri = userArrivalURIBuilder(server,ServiceKey = regKey,from_time = "",to_time = "",airport="",flight_id="",airline=input_airline)
        conn.request("GET",uri)
        
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Data downloading Complete!")
            return extractDepartureData(req.read())
        else:
            print("Failed! Please Retry.")
    elif select == 2:
        input_airline = input("항공사 코드를 입력하세요 : ")
        uri = userArrivalURIBuilder(server,ServiceKey = regKey,from_time = "",to_time = "",airport="",flight_id="",airline=input_airline)
        conn.request("GET",uri)
        
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Data downloading Complete!")
            return extractDepartureData(req.read())
        else:
            print("Failed! Please Retry.")
        
        
def SearchFlight():
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    
    

        
def extractDepartureData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        airline = item.find("airline")
        airport = item.find("airport")
        chkinrange = item.find("chkinrange")
        estimatedDateTime = item.find("estimatedDateTime")
        flightid = item.find("flightid")
        gatenum = item.find("gatenumber")
        remark = item.find("remark")
        scheduleDateTime = item.find("scheduleDateTime")
        if len(airline) > 0:
            print("항공사 :",airline)
            print("항공 편명 :",flightid)
            print("도착 예정시간 :",scheduleDateTime)
            print("도착 변경시간 :",estimatedDateTime)
            print("출발 공항 :",airport)
            print("체크 인 카운터 :",chkinrange)
            print("탑승구 번호 :",gatenum)
            print("운항 상태 :",remark)
            return None
        
def extractArrivalData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        airline = item.find("airline")
        airport = item.find("airport")
        carousel = item.find("carousel")
        exitnum = item.find("exitnumber")
        estimatedDateTime = item.find("estimatedDateTime")
        flightid = item.find("flightid")
        gatenum = item.find("gatenumber")
        remark = item.find("remark")
        scheduleDateTime = item.find("scheduleDateTime")
        if len(airline) > 0:
            print("항공사 :",airline)
            print("항공 편명 :",flightid)
            print("도착 예정시간 :",scheduleDateTime)
            print("도착 변경시간 :",estimatedDateTime)
            print("출발 공항 :",airport)
            print("수하물 수취대 번호:",carousel)
            print("탑승구 번호 :",gatenum)
            print("출구 번호 :",exitnum)
            print("운항 상태 :",remark)
            return None

def sendMain():
    global host, port
    html = ""
    title = str(input ('Title :'))
    senderAddr = str(input ('sender email address :'))
    recipientAddr = str(input ('recipient email address :'))
    msgtext = str(input ('write message :'))
    passwd = str(input (' input your password of gmail account :'))
    msgtext = str(input ('Do you want to include book data (y/n):'))
    if msgtext == 'y' :
        keyword = str(input ('input keyword to search:'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
    
    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    #Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    #set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset = 'UTF-8')
    
    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)
    
    print ("connect smtp server ... ")
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)    # 로긴을 합니다. 
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    
    print ("Mail sending complete!!!")

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)
    
def LoadXMLDeparture():
    global conn, server, regKey , DataDoc
    import http.client
    conn = http.client.HTTPConnection(server)
    uri = userArrivalURIBuilder(server,ServiceKey = regKey,from_time = "",to_time = "",airport="",flight_id="",airline="")
    conn.request("Get",uri)
    req = conn.getresponse()
    print(req.status,req.reason)
    if int(req.status) == 200:
        cLen = req.getheader("Content-Length")
    DataDoc = req.read(cLen)