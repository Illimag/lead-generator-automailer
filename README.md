
# lead-generator-automailer

    Copyright (C) 2019 Hillotech, LLC. All Rights Reserved
    This program is free software; you can redistribute it 
    and/r modify it under the terms of either the GNU General 
    Public License or the Artistic License. THIS SOFTWARE 
    IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
    TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
    FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
    SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE 
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
    AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
    EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

![overview](overview.png)

## Overview

### Lead generator and mail automation system.

The lead generator get leads from Craiglists. The lead generator system is on User2 and the Mail Automation system is on Desktop-E1V0N4N. The system takes in URLs and filters them based on keyword and removes duplicates. Then the system transfers the files via FTP to Desktop-E1V0N4N. 

Once the files, which are JSON objects are transfered via FTP to Desktop-E1V0N4N, WATCHDOG which is a python dependency automatically detects the file and runs check_master.py which takes the leads and compares them to the master.json file. Master.json is where all the leads are stored.

The new leads are added to the master.json and a new lead json object is created.

Watchdog detects this new lead json object and runs a UBOT STUDIO Executable. 

This executable takes the urls and converts them to email addresses.

This is because Craiglist has server-side javascript that doesn't show the HTML on the client-side without being activated on the client-side. So we are using UBOT STUDIO to automate the mouse click functionality of the system. UBOT STUDIO is a window's application. 

The email addresses are put into a CSV file.

Watchdog then runs another UBOT STUDIO executable, AUTO_LOAD.UBOT

This loads the CSV file into the mail server application and sends them.

## Automation Procedure

The two machines:

    User0

    Desktop-E1V0N4N

Automatically power-on:

    5:00AM

Automatically power-off:

    11:59AM

At power-on, the file:

    starter.py

Is automatically run.

At power-off, the file:

    closer.py

Is automatically run:

## Lead Generator

### Craiglist Scraper

Rotating IP Addresses and User Agents to spoof Craiglist. 

The main program that scrapes is the:

    spider.py

The spider.py file cycles through the URLS which are divided into lead_cycles.

The lead_cycles depend on the traffic of the URLS.

Updates to the:

    spider_cycle.txt

Which keep track on the cycle number.

Once a cycle is completed, the spider.py updated the spider_cycle.txt to the next cycle.

### Filters

Filter based on keywords and duplicates.

    clean_lead.py

Combines the keyword filter and the FTP transfer.

### FTP

The ftp server is located on the Desktop-E1V0N4N machine.

### Urls to Email

Currently using Ubot Studio to get EMAILS from the URLS. 
Need something that will click the button, because without it the <div></div> with the emails won't show. 
Sever-side Javascript?

### Mail Automation

Ubot studio executable runs automatically sends mail.

With Mail for Good and AWS SES, we can send the emails.

### Usage 

Using this application is against Craigslist's Terms of Service. 

Highly recommend that this application should not be put into use. 

If put into use, the automailer functionality should not be applied.