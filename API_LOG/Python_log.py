# myapp.py
import logging
import datetime
import requests
import xml.etree.ElementTree as ET
from tkinter import *  
 

def main():
    WriteLog("Run Main")
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    bt_CallWebservice = Button(frame, text="Call Oil Price",command =CallWSOilPrice)
    bt_CallWebservice.pack( side = LEFT)
    bt_close = Button(frame, text="Close" ,command  = closeapp)
    bt_close.pack( side = LEFT )
    
def WriteLog(taskevent):
    x = datetime.datetime.today().strftime('%Y%m%d')
    v_datetime = datetime.datetime.now()
     
    logging.basicConfig(filename= str(x)+'_logapp.log', level=logging.INFO)
    logging.info(str(v_datetime) + " : "+taskevent)
def closeapp():
   print ("Close App")
def CallWSOilPrice():
   response = requests.get("https://crmmobile.bangchak.co.th/webservice/oil_price.aspx")
   print("Response Status Code : "+str(response.status_code))
   WriteLog("CallWSOilPrice")
    
   x = response.content
   root = ET.fromstring(x)
   for child in root.findall('item'):
       xml_type = child.find('type').text
       xml_pricetoday = child.find('today').text
       xml_pricetmr = child.find('tomorrow').text
       xml_priceyes = child.find('yesterday').text
       xml_priceunit_th = child.find('unit_th').text
       
       print ("Oil Type : "+xml_type)
       print ("price today : "+xml_pricetoday)
       print ("price tomorrow : "+xml_pricetmr)
       print ("price yesterday : "+xml_priceyes)
       print ("unit_th : "+xml_priceunit_th)
       print ("-----------------------")
       
 
root = Tk()  
if __name__ == '__main__':
    main()
    root.mainloop()

