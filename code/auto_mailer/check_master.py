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
import os
import portalocker

current_lead_number = 0
current_lead_number1 = 0
current_url_number = 0

# Get outputted leads
# put json object into var
# Get length of the dict
with open("out_lead.json", 'r') as json_file:
    data = json.load(json_file)
    total_number_of_items_in_data_out_lead = len(data)

os.remove("out_lead.json")

# Get master json file
# put json object into var
# Get length of the dict
with open("../master.json",'r+') as master_json:
    portalocker.lock(master_json, portalocker.LOCK_EX)
    master = json.load(master_json)
    total_number_of_items_in_data_master_json = len(master)

    # Iterate through all the leads in the outputted file
    for x in range(0, total_number_of_items_in_data_out_lead):
        # Turn the current lead number into a string
        # Because it is a string in the json object
        turn_into_string = str(current_lead_number)
        # Get the data related to the key
        lead = (data[turn_into_string])
        url = lead[1]
        text_in_url = url["url"]
        # Reset the lead number for master json
        # Need this so start at 0 every time new lead from outputted file 
        # Check if duplicate
        current_lead_number1 = 0

        # Iterate through all the leads in master json.
        for y in range(0, total_number_of_items_in_data_master_json):
            turn_into_string1 = str(current_lead_number1)
            lead1 = (master[turn_into_string1])
            url1 = lead1[1]
            text_in_url1 = url1["url"]
            
            # When the loop has iterated through all the leads
            # Break out of loop
            if (current_lead_number1 == total_number_of_items_in_data_master_json):
                break

            # If it is a duplicate, remove that key in the dict
            if (text_in_url == text_in_url1):
                #print "this is a duplicate: " + text_in_url
                #print current_lead_number
                data.pop(turn_into_string, None)
            current_lead_number1+=1

        # If Iterate through all leads in outputted json
        # Break out of loop
        count_total = total_number_of_items_in_data_out_lead - 1
        if(current_lead_number == count_total):
            break
        current_lead_number+=1


    # Recreates dict with keys starting from 0
    counter = 0
    number_of_new_leads = len(data)
    array = {}    
    for key, value in data.iteritems():
        #print key

        turn_into_string2 = str(counter)
        array[turn_into_string2] = value
        #print value
        counter+=1
        #total_number_of_items_in_data_master_json

    # Export file new_lead.json
    with open("new_lead.json", 'w') as outfile:  
        json.dump(array, outfile)
        exit

    # Append the new leads to the master.json file
    add_to_end = total_number_of_items_in_data_master_json
    for key, value in data.iteritems():
        turn_into_string3 = str(add_to_end)
        master[turn_into_string3] = value
        add_to_end+=1



    master_json.seek(0)
    json.dump(master, master_json)
    master_json.truncate()
    portalocker.unlock(master_json)