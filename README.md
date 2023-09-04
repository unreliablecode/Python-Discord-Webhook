```markdown
# Discord Webhook Sender

This Python program allows you to send messages to a Discord webhook with full customization options. You can specify the webhook URL, message content, username, avatar URL, and even use an embed if you'd like.

## Getting Started

### Prerequisites

Before running the program, make sure you have Python installed on your system.

### Installation

1. Clone this repository or download the `discord_webhook_sender.py` file.

2. Install the required libraries if you haven't already. You can do this using pip:

   ```bash
   pip install requests
   ```

### Usage

1. Run the Python script:

   ```bash
   python discord_webhook_sender.py
   ```

2. Follow the prompts to input the following details:

   - Discord webhook URL: Provide the webhook URL you want to send the message to.

   - Message content: Enter the text message you want to send.

   - Username (optional): Specify a custom username for the sender (leave empty for the default).

   - Avatar URL (optional): Provide a custom avatar URL for the sender (leave empty for the default).

   - Use embed? (yes/no): Decide whether you want to send an embedded message or not.

   If you choose to use an embed, you will be prompted to provide details for the embed, including title, description, and color (in hexadecimal format).

3. The program will send your customized message to the specified Discord webhook. You will receive a success message if the message is sent successfully.

## Example

Here's an example of how to use the program:

```bash
python discord_webhook_sender.py
```

Enter the following details:

- Discord webhook URL: `https://discord.com/api/webhooks/your-webhook-url`
- Message content: `Hello, Discord!`
- Username (optional): `CustomBot`
- Avatar URL (optional): `https://example.com/custom-avatar.png`
- Use embed? (yes/no): `yes`
- Enter the embed title: `My Embed`
- Enter the embed description: `This is a custom embed message.`
- Enter the embed color (hexadecimal): `FF5733`

The program will send the customized message to the specified webhook.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `"https://discord.com/api/webhooks/your-webhook-url"` in the example with your actual Discord webhook URL.

Make sure to create a `LICENSE` file in your repository with the appropriate license text if you haven't already. You can choose any open-source license that suits your project.
