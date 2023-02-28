"""
Name: Pawar Sumit Vikas
Mail Application with GUI
"""
import smtplib
import customtkinter as ct

#Setting appearance
ct.set_appearance_mode("dark")
ct.set_default_color_theme('blue')

def send_email(to_entry, subject_entry, message_text):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your-email@example.com', 'Your-App-Pass')
    # Get the recipient, subject, and message from the form
    to = to_entry.get()
    subject = subject_entry.get()
    message = message_text.get('1.0', 'end')

    # Send the email
    msg = f'Subject: {subject}\n\n{message}'
    server.sendmail('your-email@example.com', to, msg)

    # Close the server
    server.quit()

def main():
    # Create the main window
    window = ct.CTk()
    window.title('Mail Application')
    window.geometry('700x200')

    # Create the frames
    top_frame = ct.CTkFrame(window)
    top_frame.pack(side='top')
    bottom_frame = ct.CTkFrame(window)
    bottom_frame.pack(side='bottom')
   
    # Create the widgets
    to_label = ct.CTkLabel(top_frame, text='To:',bg_color='green')
    to_label.pack(side='left')
    to_entry = ct.CTkEntry(top_frame,height=50,width=300,font=("bold",20))
    to_entry.pack(side='left')
    subject_label = ct.CTkLabel(top_frame, text='Subject:',anchor="center",bg_color='green')
    subject_label.pack(side='left')
    subject_entry = ct.CTkEntry(top_frame,height=50,width=300,font=("bold",20))
    subject_entry.pack(side='left')
    message_label = ct.CTkLabel(bottom_frame, text='Message:', bg_color='green')
    message_label.pack(side='left')
    message_text = ct.CTkTextbox(bottom_frame,height=100,width=300,font=("bold",20))
    message_text.pack(side='left')
    send_button = ct.CTkButton(bottom_frame, text='Send', command=lambda: send_email(to_entry, subject_entry, message_text))
    send_button.pack(side='left')
    cancel_button = ct.CTkButton(bottom_frame, text='Cancel', command=window.destroy)
    cancel_button.pack(side='left')
    


    # Start the main loop
    window.mainloop()
if __name__ == '__main__':
    main()

