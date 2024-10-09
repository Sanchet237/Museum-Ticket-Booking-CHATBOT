from chatbot import get_chatbot_response
from payment import confirm_booking
from tkinter import *
from tkinter import scrolledtext
import threading

# Initialize the main window
root = Tk()
root.title("Chatbot")
root.geometry("500x600")  # Set the window size
root.minsize(400, 500)    # Allow resizing to a minimum size

# Configure grid to make it resizable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def send():
    user_input = e.get()
    send_message = "You -> " + user_input
    txt_area.config(state=NORMAL)
    txt_area.insert(END, "\n" + send_message)
    txt_area.config(state=DISABLED)  # Make text read-only
    txt_area.yview(END)
    
    # Clear the input field
    e.delete(0, END)
    
    # Start a new thread to get the chatbot response
    threading.Thread(target=get_response, args=(user_input,)).start()

def get_response(user_input):
    # Get the chatbot response
    response = get_chatbot_response(user_input, "user1")
    bot_message = "Bot -> " + response
    txt_area.config(state=NORMAL)
    txt_area.insert(END, "\n" + bot_message)
    txt_area.config(state=DISABLED)
    txt_area.yview(END)

# Create the ScrolledText area for displaying the conversation
txt_area = scrolledtext.ScrolledText(root, wrap=WORD, state=DISABLED, font=("Helvetica", 12), bg="#F0F0F0")
txt_area.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Create the entry widget for user input
e = Entry(root, width=80, font=("Helvetica", 12), bg="#FFFFFF")
e.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Create the send button
send_button = Button(root, text="Send", font=("Helvetica", 12), command=send, bg="#4CAF50", fg="white", padx=10, pady=5)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Run the main loop
root.mainloop()
