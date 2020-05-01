#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


import os
import logging
import sys
import time
import subprocess


from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.ERROR)

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer, filename):
        self.observer = observer
        self.filename = filename

    def on_created(self, event):
        #print "e=", event
        if not event.is_directory and event.src_path.endswith(self.filename):
            print "file created"
            self.observer.stop()

        #cwd = os.getcwd()  # Get the current working directory (cwd)
        #files = os.listdir(cwd)  # Get all the files in that directory
        #print("Files in '%s': %s" % (cwd, files))

        os.system('py -2 ../check_master.py')

        # Because another file is created which is out_lead.json
        # Watchdog runs the clean_leads script again.
        # But because there is no lead.json because spider.py hasen't
        # It throws a missing file error.
        # Currently this is fine for now.
        # But eventually a solution should be for Watchdog to watch 
        # For specific file.

        # Watchdog runs the clean_leads.py with os.system.
        # Because the run_watchdog.py file is located in test_leads
        # When clean_leads.py is run
        # All files paths are relative to the run_watchdog.py file.

def main(argv=None):
    path = "."
    filename = "test"
    observer = Observer()
    event_handler = MyEventHandler(observer, filename)
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    observer.join()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))