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

with open("urls.json", "r") as json_file: 
    data = json.load(json_file)
    total_number_of_items_in_data = len(data)
    array = []
    current_lead_number = 0

    for x in range(0, total_number_of_items_in_data):
        turn_into_string = str(current_lead_number)

        lead = (data[turn_into_string])
        url = lead[0]
        this_url = url["url"]

        array.append(this_url)
        current_lead_number+=1

    a=list(set(array))

    for val in a:
        test = val.rstrip('\r\n')
        print test