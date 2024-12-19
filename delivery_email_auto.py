#!/usr/bin/env python
# coding: utf-8

# In[1]:


#installing the necessary libraries

get_ipython().system('pip install boto3')


# In[2]:


get_ipython().system('pip install schedule')


# In[3]:


import pandas as pd
import boto3
import time
import schedule


# In[4]:


#load dataset
shipment = pd.read_csv("C:/Users/Chika/Downloads/shipment_data (1).csv")


# In[5]:


shipment.head(5)


# In[6]:


# setting up an AWS Simple Email Service (SES)
ses_client = boto3.client(
    'ses',
    region_name='eu-north-1',
    aws_access_key_id='AKIAVWABJYDCUSNQOLTZ',  
    aws_secret_access_key='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' 
)


# In[7]:


# Function to send emails
def send_email(recipient, shipment_id, origin, destination, estimated_delivery):
    subject = f"Shipment #{shipment_id} Delivered Successfully!"
    body = (
        f"Dear Customer,\n\n"
        f"Your shipment with ID #{shipment_id} has been successfully delivered.\n\n"
        f"Details:\n"
        f"- Origin: {origin}\n"
        f"- Destination: {destination}\n"
        f"- Estimated Delivery Date: {estimated_delivery}\n\n"
        f"Thank you for choosing our service!"
    )
    
    try:
        response = ses_client.send_email(
            Source="nancychika398@gmail.com",  
            Destination={
                "ToAddresses": [recipient]
            },
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body}}
            }
        )
        print(f"Email sent successfully to {recipient} for Shipment ID {shipment_id}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")


# In[8]:


# Function to check for Delivered shipments and send emails
def check_and_send_emails():
    print("Checking for Delivered shipments...")
    data = fetch_data()  # Fetch the updated dataset
    for shipment in data:
        shipment_id = shipment["shipment_id"]
        if shipment["status"] == "Delivered" and shipment_id not in notified_shipments:
            send_email(
                recipient=shipment["email"],
                shipment_id=shipment_id,
                origin=shipment["origin"],
                destination=shipment["destination"],
                estimated_delivery=shipment["estimated_delivery"]
            )
            notified_shipments.add(shipment_id)  # Mark shipment as notified
    print("Check complete.")


# In[9]:


# Schedule the check every 6 hours
schedule.every(6).hours.do(check_and_send_emails)


# In[ ]:


# Run the scheduler
if __name__ == "__main__":
    print("Starting email automation...")
    while True:
        schedule.run_pending()
        time.sleep(1)


# In[ ]:




