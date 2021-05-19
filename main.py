from twilio.rest import Client
from keys import Twillo_Account_sid, Twillo_Auth_token, Twillo_message_id,my_phone_number
from vaccine_slot_api import available_vaccine_info

client = Client(Twillo_Account_sid, Twillo_Auth_token) 

message_body = str(available_vaccine_info)
 
message = client.messages.create(  
                              messaging_service_sid=Twillo_message_id,
                              body= message_body,      
                              to= my_phone_number
                          ) 
 
print(message.sid)