# -*- coding: utf-8 -*-

from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler,HTTPServer
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

#global
conn = None
regKey = '0bIrS1znKGJAfGh%2BKcvBHYCvSUEKAVEjjx02Wn3JIFCaWWVYsAdZB0dCjsq%2BbF9BSsw%2B7IxBsDM0qo9D%2FQ87wA%3D%3D'
language = "KR"

#OpenAPI 접속 정보
server = "openapi.airport.kr/openapi/service/"

#smtp 정보
host = "smtp.gmail.com" #Gmail SMTP 서버 주소
port = "587"

def userURIBuilderArrival(server,**user):
    str = "http://"+server+"StatusOfPassengerFlights/getPassengerArrivals?"
    for key in user.keys():
        str += key +"="+user[key] + "&"
    return str
    
def AirLineArrival(line):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderArrival(server,ServiceKey = regKey,airline = line,from_time="1000",to_time="1030")
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataArrival(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def FlightIDArrival(flightid):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderArrival(server,ServiceKey = regKey,flight_id = flightid)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataArrival(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def TimeLineArrival(start,end):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderArrival(server,ServiceKey = regKey,from_time = start,to_time = end)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataArrival(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def AirportArrival(Airport):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderArrival(server,ServiceKey = regKey,airport = Airport)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataArrival(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def extractDataArrival(strXml):
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        airline = item.find("airline")
        flightid = item.find("flightid")
        scheduleDateTime = item.find("scheduleDateTime")
        estimatedDateTime = item.find("estimatedDateTime")
        airport = item.find("airport")
        carousel = item.find("carousel")
        exitnumber = item.find("exitnumber")
        if len(flightid.text)>0:
            print("\n출발 항공 :",airport,"\t항공사:",airline,"\t항공편명:",flightid,\
            "\n도착시간(예정->변경):",scheduleDateTime,"->",estimatedDateTime,\
            "\n출구 :",exitnumber,"\t수하물수취대 :",carousel)
    
    
def connectOpenAPIServer():
    global conn,server
    conn = HTTPConnection(server)
    
def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True
    

def sendMsg():
    global host,port
    html = ""
    title = str(input('Title:'))
    senderAddr = str(input('Sender email address :'))
    recipientAddr = str(input('recipient email address:'))
    msgtext = str(input('write message :'))
    passwd = str(input('write your password :'))
    
    import mysmtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    msg = MIMEMultipart('alternative')
    
    msg['Subject']=title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    msgPart = MIMEText(msgtext,'plain')
    flightPart = MIMEText(html,'html',_charset = 'UTF-8')
    
    msg.attach(msgPart)
    msg.attach(flightPart)
    
    print("Connect smtp Server....")
    s = mysmtplib.MySMTP(host,port)
    s.ehlo()
    s.login(senderAddr,passwd)
    s.sendmail(senderAddr,[recipientAddr],msg.as_string())
    s.close()
    
    print("Mail sending Complete!!!")
    
