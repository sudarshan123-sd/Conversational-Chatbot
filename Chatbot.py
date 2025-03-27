from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

# Reading YAML file
data = open('Dell Chatbot 1.yml', 'r', encoding='utf-8').read()

# Training the bot
trainer.train(data)

def botreply():
    question = questionField.get()
    try:
        answer = bot.get_response(question)
        print("Bot's response:", answer)  # Debugging statement
        textarea.insert(END, 'You: ' + question + '\n\n')
        textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
    except Exception as e:
        print("Error:", e)  # Print any errors that occur
    questionField.delete(0, END)



root = Tk()

root.geometry('600x700+110+40')
root.title('Dell Assistance')
root.config(bg='light blue')

# Load image files
try:
    logoPic = PhotoImage(file='output-onlinepngtools.png')
    askPic = PhotoImage(file='output-onlinepngtools (3).png')
except FileNotFoundError:
    print("Image files not found.")

logoPicLabel = Label(root, image=logoPic, bg='light blue')
logoPicLabel.pack(pady=12)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman', 18, 'bold'), height=16, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview())

questionField = Entry(root, font=('Poppins', 20, 'bold'))
questionField.pack(pady=15, fill=X)

askButton = Button(root, image=askPic, command=botreply)
askButton.pack()

root.mainloop()
