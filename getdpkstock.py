#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2021,2,30

@author: Loudy_Zhao
'''
import sys,requests
import re
import urllib3
from requests_ntlm import HttpNtlmAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


def NoFoundData(content.decode('utf-8')):
    return re.match(r'<td>No Records Found</td>',content.decode('utf-8')) 
def HtmlStock2Dict(content)
    soup = BeautifulSoup(content)
    soup.unicode
    tables = soup.findAll('tr',"grid-alternatereportitem")
    tab=tables[0]
    Dict={}
    for td in tab.findAll('td'):
        Dict (td.getText())
    
    
    
    
def main(partList, account, password,ccn):
    
    class user_info: #a validated account premit to access digital product key mangement web site
        user=r'asia-pacific\loudy_zhao'
        #user=account
        pwd='Dell_z_100c'
        #pwd=password
    class http:# DPK inventory stock report page
        url_login='https://cirrus-cdaportal.dell.com/LKM/Reports/DPKQueryReport.aspx'
        url_stockreport='https://cirrus-cdaportal.dell.com/LKM/Reports/StockStatusViewReport.aspx'


        
    class get:
        def __init__(self,text):
            self.text=text
            self.textDecode=text.decode('utf-8') #python3 required bytes-like instead of chart-like
        def get_vie(self):
            rex=r'''<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)"'''
            vie=re.findall(rex,self.text)
            return vie
        
        def get_vie_gen(self):
            rex=r'''<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)"'''
            vie_Gen=re.findall(rex,self.text)
            return vie_Gen
        def get_vie_validation(self):
            rex=r'''<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)"'''
            vie_valid=re.findall(rex,self.text)
            return vie_valid
        def get_vie3(self):
            rex=r'''<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)"'''
            vie=re.findall(rex,self.textDecode)
            return vie
        
        def get_vie_gen3(self):
            rex=r'''<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)"'''
            vie_Gen=re.findall(rex,self.textDecode)
            return vie_Gen
        def get_vie_validation3(self):
            rex=r'''<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)"'''
            vie_valid=re.findall(rex,self.textDecode)
            return vie_valid



    class head: # contain Http header required by LKM web site
        h1={
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'Accept-Encoding': 'gzip, deflate,br',
          'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
          'Cache-Control': 'max-age=0',
          'Connection': 'keep-alive',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Host': 'cirrus-cdaportal.dell.com',
          'Origin': 'https://cirrus-cdaportal.dell.com',
          'Referer': 'https://cirrus-cdaportal.dell.com/LKM/Reports/StockStatusViewReport.aspx',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
          }
#         h2=h1.copy()
          h1['Referer']= http.url_stockreport
#         h2['Referer']=http.url_stockreport
          
    class pay_load: #pay_load class to hold pay_load in HTTP header
        pay_load_LKM={
    'ctl00$MainContent$lboxCCN':'',
		'ctl00$MainContent$txtDellPartNo':'',
		'ctl00$MainContent$lboxStatus':'',
		'ctl00$MainContent$ddlKeyType':'0',
		'ctl00$MainContent$ddlProdClassType':'0',
		'ctl00$MainContent$btnViewReport':'View Report',
		'ctl00$MainContent$ddlExportFileType':'0'
		}
		

    class post_view_data: #getting aspx view data on report page
        data={'__VIEWSTATE':'','__EVENTVALIDATION':'','__VIEWSTATEGENERATOR':''}
    Class LKMStatus:
        unallocated='10002' #this is status class indicates dpk status for inventory
        
    Class CCN: # All CCN id definded by license key managment site
        M10000='8'
        C10000='3'
        I10000='7'
        DAO='1'
        E10000='6'
             
        
    class open_html_login: #let's start to send http request to the LKM report page.
        session = requests.Session()
        session.auth = HttpNtlmAuth(user_info.user,user_info.pwd)
        s_first=session.get(http.url_login,verify=False) # access the query page,get the authorization thru NTLM 
        s_first_content=s_first.content
        #print(s_first_content)
        s=session.get(http.url_login) #access the second but the same query page again to update view_validation
        #s0=session
        #print (dir(s0))
        s_content=s.content
        cook=s.cookies #save cookie
        #print (s_content)
        #get view info from login page contents if sucessfully
        vie=get(s_content).get_vie3()
        vie_gen=get(s_content).get_vie_gen3()
        vie_validation=get(s_content).get_vie_validation3()
        #save View which should save to Http protocal header
        post_view_data.data['__VIEWSTATE']=vie
        post_view_data.data['__EVENTVALIDATION']=vie_validation
        post_view_data.data['__VIEWSTATEGENERATOR']=vie_gen
        
        #print (vie)
        #print (vie_gen)
        #print (vie_validation)       
        pay_load.pay_load_LKM.update(post_view_data.data) # update view parameters in payload
        
        #start to built http request with content
        if (ccn!=''and partList !=''): #CCN name need to change it to ID
        	if ccn.upper()=='M10000':
        		ccn_id=CCN.M10000
        	elif ccn.upper()=='C10000':
        		ccn_id=CCN.C10000
        	elif ccn.upper()=='I10000':
        		ccn_id=CCN.I10000
        	elif ccn.upper()=='E10000':
        		ccn_id=CCN.E10000
        	elif ccn.upper()=='DAO':
        		ccn_id=CCN.DAO
        		         	
        pay_load.pay_load_LKM['ctl00$MainContent$lboxCCN']=ccn_id
        pay_load.pay_load_LKM['ctl00$MainContent$txtDellPartNo']=partList # seperated by comma '22C12,3RF54'
        pay_load.pay_load_LKM['ctl00$MainContent$lboxStatus']= LKMStatus.unallocated #only query inventory at unallocated under specific CCN
        s2=session.post(http.url_stockreport,cookies=cook,data=pay_load.pay_load_LKM,headers=head.h1)
     		if (NoFoundData(s2.content))
        			print ("it could not find any data, exit.")
        			sys.exit(0)
        #Getting stock data
        soup=BeautifulSoup(s2.content)
        soup.unicode
        


if __name__=='__main__':
	from optparse import OptionParser
	parse=OptionParser()
	parse.add_option("-t", dest="partList", default="", help="available parts in a list")
	parse.add_option("-a", dest="account", default="asia-pacific\XXXX", help="domain account")
	parse.add_option("-p", dest="password", default="",help='account password')
	parse.add_option("-c", dest="ccn", default="M10000",type = "string",help='inventory CCN value')
	(opt, agrs)=parse.parse_args()
	sys.exit(main(opt.partList, opt.account, opt.password, opt.ccn))
