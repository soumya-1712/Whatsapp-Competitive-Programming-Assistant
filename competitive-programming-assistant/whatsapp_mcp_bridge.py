from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from portia import McpToolRegistry, Portia
import os
from config import TOKEN, CLIST_API_KEY

app = Flask(__name__)


mcp_registry = McpToolRegistry.from_sse_connection(
    server_name="abbie-sir-mcp",
    url="https://abbie-sir-mcp-28gj.onrender.com/mcp/",
    headers={
        "Authorization": "Bearer moolikilooli",
        "Accept": "text/event-stream",
        "mcp-session-id": "0a0a64e0f3bf4098a933cee8eb09e556"  
    }
)

portia_agent = Portia(tool_registry=mcp_registry)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    """
    Endpoint to handle incoming WhatsApp messages via Twilio.
    """
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if not incoming_msg:
        msg.body("Sorry, I didn't get your message. Please try again.")
        return str(resp)

    try:
        plan = portia_agent.plan(incoming_msg)
        answer = plan.json()  

        msg.body(f"Answer:\n{answer}")
    except Exception as e:
        msg.body(f"Error processing your request: {str(e)}")

    return str(resp)

if __name__ == "__main__":
    # Get port from environment or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)