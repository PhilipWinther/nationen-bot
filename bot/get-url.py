import requests
import json
import random
from collections import OrderedDict
from bs4 import BeautifulSoup
import time


url0 = 'https://eb.dk'
url1 = 'https://ekstrabladet.dk/opinionen/'
url2 = 'https://ekstrabladet.dk/nyheder/'
url3 = 'https://ekstrabladet.dk/sport/'
url4 = 'https://ekstrabladet.dk/krimi/'
url5 = 'https://ekstrabladet.dk/emaer/'
url6 = 'https://ekstrabladet.dk/vrangen/'
url7 = 'https://ekstrabladet.dk/underholdning/'
url8 = 'https://ekstrabladet.dk/musik/'
url9 = 'https://ekstrabladet.dk/forbrug/'
url10 = 'https://ekstrabladet.dk/vin/'
url11 = 'https://ekstrabladet.dk/ferie/'
url12 = 'https://ekstrabladet.dk/biler/'
url13 = 'https://ekstrabladet.dk/Haandvaerkeren/'
url14 = 'https://ekstrabladet.dk/sex_og_samliv/'
url15 = 'https://ekstrabladet.dk/dagsorden/'

headers_list = [
    # Firefox 77 Mac
     {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Firefox 77 Windows
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Chrome 83 Mac
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    },
    # Chrome 83 Windows
    {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
]


# Create ordered dict from Headers above
ordered_headers_list = []
for headers in headers_list:
    h = OrderedDict()
    for header,value in headers.items():
        h[header]=value
    ordered_headers_list.append(h)

#make only 1 call#
for i in range(1,2):
    #Pick a random browser headers
    headers = random.choice(headers_list)

proxies={
        'http': 'http://',
        'https': 'http://'
        },
print("Getting link 1")
response0 = requests.get(url0, headers=headers)
time.sleep(10)
print("Getting link 1")
response1 = requests.get(url1, headers=headers)
time.sleep(10)
print("Getting link 2")
response2 = requests.get(url2, headers=headers)
time.sleep(10)
print("Getting link 3")
response3 = requests.get(url3, headers=headers)
time.sleep(10)
print("Getting link 4")
response4 = requests.get(url4, headers=headers)
time.sleep(10)
print("Getting link 5")
response5 = requests.get(url5, headers=headers)
time.sleep(10)
print("Getting link 6")
response6 = requests.get(url6, headers=headers)
time.sleep(10)
print("Getting link 7")
response7 = requests.get(url7, headers=headers)
time.sleep(10)
print("Getting link 8")
response8 = requests.get(url8, headers=headers)
time.sleep(10)
print("Getting link 9")
response9 = requests.get(url9, headers=headers)
time.sleep(10)
print("Getting link 10")
response10 = requests.get(url10, headers=headers)
time.sleep(10)
print("Getting link 111")
response11 = requests.get(url11, headers=headers)
time.sleep(10)
print("Getting link 12")
response12 = requests.get(url12, headers=headers)
time.sleep(10)
print("Getting link 13")
response13 = requests.get(url13, headers=headers)
time.sleep(10)
print("Getting link 14")
response14 = requests.get(url14, headers=headers)
time.sleep(10)
print("Getting link 15")
response15 = requests.get(url15, headers=headers)



response0.headers = headers
response1.headers = headers
response2.headers = headers
response3.headers = headers
response4.headers = headers
response5.headers = headers
response6.headers = headers
response7.headers = headers
response8.headers = headers
response9.headers = headers
response10.headers = headers
response11.headers = headers
response12.headers = headers
response13.headers = headers
response14.headers = headers
response15.headers = headers



link0 = BeautifulSoup(response0.content, 'html.parser')
link1 = BeautifulSoup(response1.content, 'html.parser')
link2 = BeautifulSoup(response2.content, 'html.parser')
link3 = BeautifulSoup(response3.content, 'html.parser')
link4 = BeautifulSoup(response4.content, 'html.parser')
link5 = BeautifulSoup(response5.content, 'html.parser')
link6 = BeautifulSoup(response6.content, 'html.parser')
link7 = BeautifulSoup(response7.content, 'html.parser')
link8 = BeautifulSoup(response8.content, 'html.parser')
link9 = BeautifulSoup(response9.content, 'html.parser')
link10 = BeautifulSoup(response10.content, 'html.parser')
link11 = BeautifulSoup(response11.content, 'html.parser')
link12 = BeautifulSoup(response12.content, 'html.parser')
link13 = BeautifulSoup(response13.content, 'html.parser')
link14 = BeautifulSoup(response14.content, 'html.parser')
link15 = BeautifulSoup(response15.content, 'html.parser')



file1 = open('eblinks.py','w', encoding="utf-8")

file1.write('def removeduplicate(x):' + '\n' + ' ' + 'return list(dict.fromkeys(x))' + '\n' + '\n')

file1.write('def listToString(list):' + '\n' + '    ' + 'str1 = ' + '"\\n"' + '\n' + '    ' + 'return (str1.join(list))' + '\n')

file1.write('eblinks = [' + '\n')
file1.close()







file1 = open('eblinks.py','a', encoding="utf-8")

#get all links with no matter class

print("Writing to file from link 0")
for a0 in link0.find_all('a', href=True):
    file1.write('"' + a0['href'] + '"' + ',')

print("Writing to file from link 1")
for a1 in link1.find_all('a', href=True):
    file1.write('"' + 'https://ekstrabladet.dk' + a1['href'] + '"' + ',')

print("Writing to file from link 2")
for a2 in link2.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk'  + a2['href'] + '"' + ',')

print("Writing to file from link 3")
for a3 in link3.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a3['href'] + '"' + ',')

print("Writing to file from link 4")
for a4 in link4.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a4['href'] + '"' + ',')

print("Writing to file from link 5")
for a5 in link5.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a5['href'] + '"' + ',')

print("Writing to file from link 6")
for a6 in link6.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a6['href'] + '"' + ',')

print("Writing to file from link 7")
for a7 in link7.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a7['href'] + '"' + ',')

print("Writing to file from link 8")
for a8 in link8.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a8['href'] + '"' + ',')

print("Writing to file from link 9")
for a9 in link9.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a9['href'] + '"' + ',')

print("Writing to file from link 10")
for a10 in link10.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a10['href'] + '"' + ',')

print("Writing to file from link 11")
for a11 in link11.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a11['href'] + '"' + ',')

print("Writing to file from link 12")
for a12 in link12.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk'  + a12['href'] + '"' + ',')


print("Writing to file from link 13")
for a13 in link13.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a13['href'] + '"' + ',')

print("Writing to file from link 14")
for a14 in link14.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a14['href'] + '"' + ',')

print("Writing to file from link 15")
for a15 in link15.find_all('a', href=True):
    file1.write('"'  + 'https://ekstrabladet.dk' + a15['href'] + '"' + ',')

print("done writing all links")

file1.close()


print("writing rest")

file1 = open('eblinks.py','a', encoding="utf-8")
file1.write('\n' + ']' + '\n' + 'mylist = removeduplicate(eblinks)' + '\n')
file1.write('convertedStr = listToString(mylist)' + '\n')
file1.write('file2 = open("eblinks-cleaned.txt","w", encoding="utf-8")' + '\n' + 'file2.write(convertedStr)' + '\n' + 'file2.close()')
file1.write("""

bad_words = ['https://ekstrabladet.dkhttps:/']

with open('eblinks-cleaned.txt') as oldfile, open('eblinks-cleaned-1.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)



""")



file1.close()

