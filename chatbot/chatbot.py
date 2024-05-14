import tkinter as tk
from tkinter import scrolledtext, END
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hello %1']],
    ['(bye|(.*) bye)', ['bye it was a great interaction']],
    ['(hi|hello|yo|hey)', ['Hey', 'ooye hoye']],
    ['(assalmualikum|assalmualikum (.*))', ['Walekumassalam']],
    ['((.*)help?|(.*)help(.*))', ['i can fix you but in future']],
    ['((.*) name?|(.*)name (.*)?)', ['My name is Zeel but you can call me yours(Bg music:Treat me like white teas)']],
    ['how are you(.*)', ['I am just a bunch of code, but thanks for asking!']],
    ['(good morning|morning)', ['Good morning to you too!']],
    ['(good afternoon|afternoon)', ['Good afternoon! How can I assist you today?']],
    ['(good evening|evening)', ['Good evening! What can I do for you?']],
    ['(good night|night)', ['Good night! Have a great sleep!']],
    ['(tell me a joke|joke)', ['Why dont scientists trust atoms? Because they make up everything!']],
    ['(tell me a fact|fact)', ['Did you know the shortest war in history was between Zanzibar and England in 1896? Zanzibar surrendered after 38 minutes!']],
    ['((weather|temperature|forecast) of (.*))', ['Bhai google search karle']],
    ['(allah hafiz|(.*)allah hafiz)', ['allah hafiz dua me yaad']],
    ['(aur bhai kaisa hai?)', ['mast bhai tu bata?']],
    ['((.*)kar sakte ho?)' , ['bhot kuch kar sakte hai par abhi nahi']],
    ['(naam kya hai?)' , ['zeel hai ji']]
]
chatbot = Chat(pairs, reflections)


class ChatInterface:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.font = ("Comic Sans MS", 14)  # Define the font

        self.chat_history = scrolledtext.ScrolledText(master, state='disabled', bg='#1e1e1e', fg='white', font=self.font)
        self.chat_history.pack(expand=True, fill='both')

        self.input_frame = tk.Frame(master, bg='#1e1e1e')
        self.input_frame.pack(fill='x')

        self.input_box = tk.Entry(self.input_frame, bg='#2e2e2e', fg='white', insertbackground='white', font=self.font)
        self.input_box.pack(side='left', expand=True, fill='x')
        self.input_box.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, bg='#2e2e2e', fg='white', font=self.font)
        self.send_button.pack(side='right')

    def send_message(self, event=None):
        message = self.input_box.get()
        self.display_message("You: " + message)
        response = chatbot.respond(message)
        self.display_message("Bot: " + response)
        self.input_box.delete(0, 'end')

    def display_message(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert('end', message + '\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.see('end')


def main():
    root = tk.Tk()
    root.configure(bg='#1e1e1e')  # Set root background color to dark gray
    chat_interface = ChatInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
