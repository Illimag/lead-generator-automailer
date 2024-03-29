# encoding=utf8

#    Copyright (C) Jae Min (John) Kim. All Rights Reserved
#    This program is free software; you can redistribute it 
#    and/r modify it under the terms of either the GNU General 
#    Public License or the Artistic License. THIS SOFTWARE 
#    IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
#    TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
#    FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
#    SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE 
#    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
#    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
#    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
#    AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
#    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
#    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
#    EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import json
import time
from ftplib import FTP_TLS
import os

# keywords are not cap sensitive. lower case w in "web" will also look for upper case "Web" and vice versa.
keywords = ["web", "Cloud", "Desktop","Mobile","Tablet","Server","Router","Switch","Embedded","Software","Hardware","Engineer","Architect","Scientist","Programmer","Developer","Branding","Graphics","UI","UX","Designer","IoT","Wearable","Technologies","Technologies","Scalable",
"Databases", "Data","Datacenter","computing","Networking","Innovation","Creativity","Social","Media","SEO","ASO","SEM","SMM","Object-Oriented","Procedural","Functional","Programming", "design", "designer", "website", "portfolio", "logo", "poster", "flyer", "ecommerce",
]

leads_with_keywords = {}
current_lead_number = 0
current_url_number = 0


with open("lead2.json", 'r') as json_file:
    data = json.load(json_file)
    total_number_of_items_in_data = len(data)
    #print total_number_of_items_in_data
    #print data
    for x in range(0, total_number_of_items_in_data):
        turn_into_string = str(current_lead_number)
        lead = (data[turn_into_string])
        #print lead
        title = lead[0]
        #print title
        text_in_title = title["title"]

        for keyword in keywords:
            if keyword in text_in_title:
                lead = (data[turn_into_string])
                #print lead
                url = lead[1]
                title = lead[0]
                #print url
                this_title = title["title"]
                this_url = url["url"]
                #print this_url
                leads_with_keywords[current_url_number] = []

                leads_with_keywords[current_url_number].append({'title':this_title})
                leads_with_keywords[current_url_number].append({'url':this_url})
                current_url_number+=1
                break

        current_lead_number+=1
with open('out2_lead.json', 'w') as outfile:  
    json.dump(leads_with_keywords, outfile)
exit

ftp=FTP_TLS()
ftp.set_debuglevel(2)
ftp.connect('0000', 0000)
ftp.sendcmd("USER user")
ftp.sendcmd("PASS password")
file = open('out2_lead.json','rb')     
ftp.storbinary('STOR out2_lead.json', file) 
file.close()  
ftp.close()

os.remove("lead2.json")
os.remove("out2_lead.json")