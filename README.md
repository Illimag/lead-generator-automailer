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

## Visual Overview

![overview](overview.png)

## Overview

### Notes

This is an experimental software system built with Python2. 

Because a key component is the automatic poweron and poweroff of the two machines, access to the machine's BIOS or UEFI is required.

Which means this system will be difficult to setup with virtual machines, without advanced access to cloud services.

Another key component is one of the machines will need to be a Windows machine, because of the use of a Windows desktop automation software.

This Automation Software is UBOT Studio which is a pay to use software.

Included is the compiled executable as well as the UBOT file.

The reasoning behind this is that Craigslist has server-side JavaScript that hides client-side code until activated with user interaction on the web interface.

Additionally because File Transfer Protocol is used, access to the internet router to open ports maybe required.

This system requires File Locking functionality, to allow for multiple programs to write to one file.

Currently it is implemented with Portalocker, which is a cross-platform file locking dependency for Windows and Unix.

This system heavily relies on Rotating Proxies, which is a service that changes the IP Address of the machine with each request to the Craigslist servers.

As so without a service that provides Rotating Proxies, this system can not function at full capacity.

### Disclaimer

Because this software violates the Terms of Services of Craigslist this system is not be used.

This system has components purposely incomplete/missing and will not function.

### Lead generator and mail automation system.

The lead generator get leads from Craiglists. 

The lead generator system is on User2 and the Mail Automation system is on Desktop-E1V0N4N. 

The system takes in URLs and filters them based on keyword and removes duplicates. 

Then the system transfers the files via FTP to Desktop-E1V0N4N. 

Once the files, which are JSON objects are transfered via FTP to Desktop-E1V0N4N, WATCHDOG which is a python dependency automatically detects the file and runs check_master.py which takes the leads and compares them to the master.json file. 

Master.json is where all the leads are stored.

The new leads are added to the master.json and a new lead json object is created.

Watchdog detects this new lead json object and runs a UBOT STUDIO Executable. 

This executable takes the urls and converts them to email addresses.

This is because Craiglist has server-side javascript that doesn't show the HTML on the client-side without being activated on the client-side. 

So we are using UBOT STUDIO to automate the mouse click functionality of the system. 

UBOT STUDIO is a window's application. 

The email addresses are put into a CSV file.

Watchdog then runs another UBOT STUDIO executable, AUTO_LOAD.UBOT

This loads the CSV file into the mail server application and sends the mail automatically.

The mail server application was Mail-For-Good hosted on an AWS virtual machine.

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

## Usage 

Using this application is against Craigslist's Terms of Service. 

Highly recommend that this application should not be put into use. 

If put into use, the automailer functionality should not be applied.
