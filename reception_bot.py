# فقط لتجربة بوت الاستقبال
class ReceptionBot:
    def __init__(self):
        self.token = "8365752104:AAGM9Cz0GJ4lyys6Yo3hJ0S7gYZq1SMSwPc"

    def send_message(self, chat_id, text):
        print(f"[ReceptionBot] Sending message to {chat_id}: {text}")

def get_application():
    return ReceptionBot()
