
from tkinter import *
from PIL import Image, ImageTk
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



def generate():
    input_text = questionField.get()

    try:
        if 'hi' in input_text.lower():
            response = "Hello how can i help You"
        elif "who made you" in input_text.lower() or "created you" in input_text.lower():
            response = "I have been created by DELL Copmany ."
        elif "I am having problem" in input_text.lower() or "having problem" in input_text.lower() or "problem" in input_text.lower():
            response = "what is problem, Tell me in details..!"  
        elif "check the warranty status of my Dell laptop" in input_text.lower(): 
            response = "You can check the warranty status by visiting our website and entering the service tag or express service code."
        elif "warranty status" in input_text.lower():
            response = "You can check the warranty status by visiting our website and entering the service tag or express service code."
        elif "recommended system requirements for running heavy software on a Dell desktop" in input_text.lower() or "system requirements" in input_text.lower():
            response = "The recommended system requirements vary depending on the software. However, for heavy software, we generally recommend a higher-end processor, ample RAM (at least 8GB), and a dedicated graphics card."
        elif "update drivers for my Dell printer" in input_text.lower() or "update drivers" in input_text.lower():
            response = "You can update drivers for your Dell printer by visiting our website and searching for your printer model. Then, download the latest drivers and follow the installation instructions."
        elif "Dell laptop is running slow" in input_text.lower():
            response = "There are several steps you can take to improve the performance of your Dell laptop, such as uninstalling unused programs, running disk cleanup, disabling startup programs, and upgrading hardware components like RAM or storage."
        elif"laptop running slow" in input_text.lower():
            response = "There are several steps you can take to improve the performance of your Dell laptop, such as uninstalling unused programs, running disk cleanup, disabling startup programs, and upgrading hardware components like RAM or storage."    
        elif "reset my Dell laptop to factory settings" in input_text.lower() or "reset to factory settings" in input_text.lower() or "reset" in input_text.lower():
            response = "You can reset your Dell laptop to factory settings by accessing the recovery partition during boot-up or by using the Dell OS Recovery Tool if your system is not bootable."
        elif "upgrade the RAM on my Dell Inspiron laptop" in input_text.lower() or "upgrade the RAM" in input_text.lower() or "upgrade RAM" in input_text.lower():
            response = "In most cases, yes, you can upgrade the RAM on your Dell Inspiron laptop. However, it's recommended to check your laptop's specifications and compatibility before purchasing new RAM modules."
        elif "Dell monitor is not displaying anything" in input_text.lower():
            response = "First, ensure that all cables are securely connected. If the issue persists, try connecting the monitor to another device to determine if the problem lies with the monitor or the computer."
        elif "monitor not displaying" in input_text.lower():
            response = "First, ensure that all cables are securely connected. If the issue persists, try connecting the monitor to another device to determine if the problem lies with the monitor or the computer."
        
        elif "transfer files from my Dell laptop to an external hard drive" in input_text.lower() or "transfer files" in input_text.lower():
            response = "You can transfer files from your Dell laptop to an external hard drive by connecting the hard drive to your laptop via USB, then dragging and dropping the files you want to transfer to the external hard drive."
        elif "Dell's return policy" in input_text.lower() or "return policy" in input_text.lower():
            response = "Dell's return policy may vary depending on the product and region. Generally, you can return a product within a specified period for a refund or exchange, subject to certain conditions."
        elif "contact Dell customer support" in input_text.lower() or "contact customer" in input_text.lower() or "customer support" in input_text.lower():
            response = "You can contact Dell customer support through phone, email, or live chat. Visit our website for contact information specific to your region."
        elif "Dell's flagship laptop series" in input_text.lower() or "flagship laptop" in input_text.lower() or "laptop series" in input_text.lower():
            response = "Dell XPS series."
        elif "check the warranty status of my Dell laptop" in input_text.lower() or "warranty status" in input_text.lower():
            response = "You can check the warranty status on Dell's website by entering your service tag or express service code."
        elif "Dell's customer support phone number" in input_text.lower() or "customer support phone nunber" in input_text.lower() or "phone number" in input_text.lower:
            response = "Dell's customer support number is 1-800-624-9896."
        elif "update drivers on my Dell computer" in input_text.lower() or "update drive on computer" in input_text.lower():
            response = "You can update drivers through Dell's support website or by using Dell Update application."
        elif "Dell monitor series is known for its high refresh rates" in input_text.lower() or "monitor" in input_text.lower() or "high refresh rates monitor" in input_text.lower():
            response = "Dell Alienware monitors are known for high refresh rates."
        elif "troubleshoot a blue screen error on my Dell PC" in input_text.lower() or "troubleshoot" in input_text.lower() or "blue screen error" in input_text.lower():
            response = "You can try booting into Safe Mode, updating drivers, or running diagnostics using Dell SupportAssist."
        elif "Dell Preferred Account" in input_text.lower() or "Preferred Account" in input_text.lower() or "account" in input_text.lower:
            response = "Dell Preferred Account is a financing option available for Dell purchases."
        elif "track my Dell order" in input_text.lower() or "my oreder" in input_text.lower or "track order" in input_text.lower:
            response = "You can track your Dell order through the Dell website using your order number or email address."
        elif "create My Account on Dell.com" in input_text.lower() or "create my account" in input_text.lower() or "my account" in input_text.lower():
            response = "To create 'My Account' on Dell.com, perform the following steps: Open: My Account. Select 'Create a Dell.com account'. Fill in the required fields. Select 'Complete Registration' at the bottom of the form."
        elif "error message when I attempt to register or update My Account" in input_text.lower() or "error message on my account" in input_text.lower() or "error on register my account" in input_text.lower() :
            response = "If you're receiving an error message when attempting to register or update 'My Account', it could be due to the following reasons: 1. 'This email address already exists': This error indicates that there is an existing 'My Account' profile created using the same email address. You can use the 'Forgot Password' link to retrieve the password associated with the email. 2. 'This Customer Number is already tied to another member's profile': This error indicates you already have an existing account using that Customer Number. Try to log into the existing account. You can request your original 'My Account' password if you have forgotten it."
        elif "forgotten My Account login password" in input_text.lower() or "forgotten my passwors" in input_text.lower() or "login password" in input_text.lower():
            response = "If you have forgotten your 'My Account' login password, you can have it sent to you by email. Open: My Account. Select 'Forgot your Password?' Enter your email address in the Email Address box. This must be the email address that is currently registered in your 'My Account' profile. Select 'Continue'. If you have lost or misplaced the password for the email address that was used to create your My Account password, you have two options: Reset your email address password. Refer to your email provider for more information. "
        elif "change my order" in input_text.lower():
            response = "Unfortunately, once your order has been submitted, it is immediately entered into our order processing system and cannot be changed. Before placing your order, please make sure you have included everything you need as we cannot make any changes once the order is processed."
        elif "my order" in input_text.lower():
            response = "Unfortunately, once your order has been submitted, it is immediately entered into our order processing system and cannot be changed. Before placing your order, please make sure you have included everything you need as we cannot make any changes once the order is processed."

        elif "thank you" in input_text.lower():
            response = "You're welcome!" 
    except:
        response = "I don't understand, I can search the web for you. Do you want to continue?"
    return response

def bot_reply():
    response = generate()
    input_text = questionField.get()
    textarea.insert(END, 'You: ' + str(input_text) + '\n\n')
    textarea.insert(END, 'Bot: ' + str(response) + '\n\n')
    questionField.delete(0, END)

root = Tk()
root.geometry('600x700+110+40')
root.title('Dell Assistance')
root.config(bg='light blue')

# Load images (replace with your image paths)
logo_path = os.path.join(os.getcwd(), 'logo.jpg')
ask_path = os.path.join(os.getcwd(), 'ask.jpg')
if os.path.exists(logo_path) and os.path.exists(ask_path):
    logo_img = Image.open(logo_path).resize((200, 200))
    logo_pic = ImageTk.PhotoImage(logo_img)
    ask_img = Image.open(ask_path)
    ask_pic = ImageTk.PhotoImage(ask_img)
else:
    print("Image files not found.")

logoPicLabel = Label(root, image=logo_pic, bg='light blue')
logoPicLabel.pack(pady=12)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

scrollbar = Scrollbar()

textarea = Text(centerFrame, font=('times new roman', 18, 'bold'), height=16, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('Poppins', 20, 'bold'))
questionField.pack(pady=15, fill=X)

askButton = Button(root, image=ask_pic, command=bot_reply)
askButton.pack()

root.mainloop()
