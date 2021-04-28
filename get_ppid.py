import os
import sys
import requests
import time
import re
import getpass
from requests_ntlm3 import HttpNtlmAuth
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main(serviceTag,account, password):
    print(account)
    #password=''
    res=requests.get("https://quality.dell.com/search?tag="+serviceTag,verify=False,auth=HttpNtlmAuth(account,password))
    time.sleep(5)
    bs=BeautifulSoup(res.text,"html.parser")
    #print(bs.text)
    td=bs.select(".table.table-sm.table-striped.table-hover tbody tr td")
    counter = 0
    for td_item in td:
        counter=counter+1
        if td_item.text=="Base":       
            #print(counter, 'index')
            print ('*******************1********************')
            print(td[counter].text)
            print ('*******************2********************')
            print("PPID","Part","Commodity","Part Description")
            print(td[counter+1].text,td[counter+1].text[3:8],td[counter-1].text,td[counter].text)
        if td_item.text=="Motherboard":       
            #print(counter, 'index')
            #print(td.text)
            print ('*******************3********************')
            print("PPID","Part","Commodity","Part Description")
            print(td[counter+1].text,td[counter+1].text[3:8],td[counter-1].text,td[counter].text)
            break

if __name__=='__main__':
  from optparse import OptionParser
  parse=OptionParser()
  parse.add_option("-t", dest="tagFile", default="", help="Tagfile path")
  (opt, agrs)=parse.parse_args()
  print ('****************************************')
  print ('[Warning:]If input incorrectly a password might lead')
  print ('the account was locked since Dell security policy.')
  print ('****************************************')
	
  account=input(r'Account: if press enter indicate to use account asia-pacific\loudy_zhao ')
  if account=='':
    account=r'asia-pacific\loudy_zhao'
  password = getpass.getpass('Password: ')
  sys.exit(main(opt.tagFile, account, password))
