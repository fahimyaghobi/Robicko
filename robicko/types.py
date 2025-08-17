class Message:
    def __init__(self, chat_id, text):
        self.chat = type("Chat", (), {"id": chat_id})
        self.text = text
