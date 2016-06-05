# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1  #XML 문서 파일 디스크립터
DataDoc = None #XML문서 파싱한 후 반환된 DOC객체 변수
    



def PrintDOMtoXML():
    if checkDocument():
        print(DataDoc.toxml())


def DocFree():
    if checkDocument():
        DataDoc.unlink()
        
        
def checkDocument():
    global DataDoc
    if DataDoc == None:
        print("Error : Document is empty")
        return False
    return True