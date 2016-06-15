# -*- coding: utf-8 -*-

from internetflightarrival import *

def userURIBuilderDeparture(server,**user):
    str = "http://"+server+"StatusOfPassengerFlights/getPassengerDepartures?"
    for key in user.keys():
        str += key +"="+user[key] + "&"
    return str
    
def AirLineDeparture(line):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderDeparture(server,ServiceKey = regKey,airline = line)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataDeparture(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def FlightIDDeparture(flightid):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderDeparture(server,ServiceKey = regKey,flight_id = flightid)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataDeparture(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def TimeLineDeparture(start,end):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderDeparture(server,ServiceKey = regKey,from_time = start,to_time = end)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataDeparture(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def AirportDeparture(Airport):
    global server,regKey,conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilderDeparture(server,ServiceKey = regKey,airport = Airport)
    conn.request("GET",uri)
    
    req = conn.getresponse()
    print(req.status)
    if int(req.stats) == 200:
        print("Complete!")
        return extractDataDeparture(req.read())
    else:
        print("OpenAPI request has bee failed!!")
        return None

def extractDataDeparture(strXml):
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
        chkinrange = item.find("chkinrange")
        exitnumber = item.find("exitnumber")
        if len(flightid.text)>0:
            print("\n도착 항공 :",airport,"\t항공사:",airline,"\t항공편명:",flightid,\
            "\n도착시간(예정->변경):",scheduleDateTime,"->",estimatedDateTime,\
            "\n출구 :",exitnumber,"\t체크인카운터 :",chkinrange)
    
    
