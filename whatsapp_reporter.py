from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'whatsapp:+14155238886'  # Your Twilio WhatsApp number

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    message = client.messages.create(
        from_=twilio_number,
        body=message,
        to=f'whatsapp:{to}'
    )
    print(f"Message sent to {to}. SID: {message.sid}")

if __name__ == "__main__":
    # Example: Send a WhatsApp message
    recipient_number = 'recipient_whatsapp_number'  # Update with the recipient's WhatsApp number
    message_text = 'Hello, this is a WhatsApp report!'
    send_whatsapp_message(recipient_number, message_text)
