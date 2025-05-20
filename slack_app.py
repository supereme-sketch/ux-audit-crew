import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from ux_audit_crew import run_ux_audit
from config import settings

# Initialize the Slack app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Command to start a UX audit
@app.command("/ux-audit")
def handle_ux_audit(ack, command, say):
    """Handle the /ux-audit command"""
    ack()
    
    # Extract Figma URL from command
    figma_url = command.get('text', '').strip()
    if not figma_url:
        say("Please provide a Figma URL. Usage: `/ux-audit [Figma URL]`")
        return
    
    # Send initial message
    say(f"Starting UX audit for: {figma_url}\nThis might take a few minutes...")
    
    try:
        # Run the audit
        result = run_ux_audit(figma_url)
        
        # Split result into chunks (Slack has message size limits)
        chunks = [result[i:i+3000] for i in range(0, len(result), 3000)]
        
        # Send results
        for i, chunk in enumerate(chunks):
            if i == 0:
                say(f"*UX Audit Results:*\n{chunk}")
            else:
                say(chunk)
                
    except Exception as e:
        say(f"Error running UX audit: {str(e)}")

# Interactive message handler for buttons
@app.action("run_audit")
def handle_run_audit(ack, body, say):
    """Handle the 'Run Audit' button click"""
    ack()
    
    # Extract Figma URL from the message
    figma_url = body['message']['blocks'][0]['text']['text'].split('URL: ')[1]
    
    # Send initial message
    say(f"Starting UX audit for: {figma_url}\nThis might take a few minutes...")
    
    try:
        # Run the audit
        result = run_ux_audit(figma_url)
        
        # Split result into chunks
        chunks = [result[i:i+3000] for i in range(0, len(result), 3000)]
        
        # Send results
        for i, chunk in enumerate(chunks):
            if i == 0:
                say(f"*UX Audit Results:*\n{chunk}")
            else:
                say(chunk)
                
    except Exception as e:
        say(f"Error running UX audit: {str(e)}")

# Home tab view
@app.event("app_home_opened")
def handle_app_home_opened(client, event):
    """Handle app home opened event"""
    try:
        # Create the home tab view
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "UX Audit Crew",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Welcome to UX Audit Crew! 🎨\n\nUse `/ux-audit [Figma URL]` to analyze a Figma prototype."
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Quick Start:*\n1. Copy your Figma URL\n2. Type `/ux-audit`\n3. Paste the URL\n4. Wait for the analysis"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Features:*\n• Heuristic Evaluation\n• Accessibility Review\n• Responsive Design Check\n• UX Copy Analysis\n• Visual Hierarchy Review\n• Interaction Pattern Analysis"
                        }
                    }
                ]
            }
        )
    except Exception as e:
        print(f"Error publishing home tab: {e}")

if __name__ == "__main__":
    # Start the app in Socket Mode
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start() 