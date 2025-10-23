# فقط لتجربة البوت الرئيسي
class Bot:
    def __init__(self):
        self.token = "8355725528:AAF_w0v-jpRseHnDFbMBLxmN2OLj4FPUm-A"

    def send_message(self, chat_id, text):
        print(f"[MainBot] Sending message to {chat_id}: {text}")

def get_application():
    return Bot()
