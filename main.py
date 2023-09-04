import requests
import json

# User input for webhook URL
webhook_url = input("Enter the Discord webhook URL: ")

# User input for message content
message_content = input("Enter the message content: ")

# User input for username (optional)
username = input("Enter a username (optional): ")

# User input for avatar URL (optional)
avatar_url = input("Enter an avatar URL (optional): ")

# User input for whether to use embed (yes/no)
use_embed = input("Do you want to use an embed? (yes/no): ").lower() == "yes"

# Create the payload for the webhook message
payload = {
    "content": message_content,
    "username": username,
    "avatar_url": avatar_url,
    "embeds": [] if not use_embed else [
        {
            "title": input("Enter the embed title: "),
            "description": input("Enter the embed description: "),
            "color": int(input("Enter the embed color (hexadecimal): "), 16),
        }
    ],
}

# Send the webhook message
response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

# Check if the message was sent successfully
if response.status_code == 204:
    print("Webhook message sent successfully!")
else:
    print(f"Failed to send webhook message. Status code: {response.status_code}")
