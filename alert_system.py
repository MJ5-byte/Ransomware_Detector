from twilio.rest import Client

# Twilio Credentials (Replace with your own)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH = "your_twilio_auth"
TWILIO_PHONE = "+1234567890"
USER_PHONE = "+0987654321"

def send_alert():
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body="🚨 WARNING: Ransomware activity detected on your system!",
        from_=TWILIO_PHONE,
        to=USER_PHONE
    )
    print("✅ Alert Sent!")
