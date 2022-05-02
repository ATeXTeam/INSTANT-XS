# Owner: ATeXTeam
# project founder: Naveed Usman also known as SNUcoder
# Date: 4-28-22 1:08pm

print('please wait... \n')


import time
import getpass
import geocoder
import os
import webbrowser
import smtplib
username = getpass.getuser()
g = geocoder.ip('me')
print("\n============================================================ Hello", username, "from", g.city,"============================================================\n" )

def opt_A():
    print("which terminal do you want me to open?: \n")
    print("A. Open windows terminal")
    print("B. Open Powershell")
    print("C. Open Command prompt")

    A_options = input("Your option: ")
    if A_options == 'A':
        os.startfile(f'''C:\\Users\\{username}\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe''')
    elif A_options == 'B':
        os.startfile('''C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe''')
    elif A_options == 'C':
        os.startfile('''C:\\Windows\\System32\\cmd.exe''')
    elif A_options == '$Quit':
        pass
    else:
        print("HUH?!")

    print("Opened your terminal :)\n")

def opt_B():
    print("A. Search engine")
    print("B. Open a website")
    B_options = input("Your option: ")

    if B_options == 'A':
        search = str(input("What do you want to search?: "))
        search = search.replace(" ", "+")
        print("Which search engine?\n")
        print("A. Brave")
        print("B. Google")
        print("C. Duckduckgo")
        print("D. Bing")    
        Search_option = input("Your search engine options: ")
    
        if Search_option == 'A':
            webbrowser.open(f"https://search.brave.com/search?q={search}")
        elif Search_option == 'B':
            webbrowser.open(f"https://www.google.com/search?q={search}")
        elif Search_option == 'C':
            webbrowser.open(f"https://duckduckgo.com/?q={search}&ia=web")
        elif Search_option == 'D':
            webbrowser.open(f"https://www.bing.com/search?q={search}")
        elif Search_option == '$Quit':
            pass
        else:
            print("What kind of search engine is that?\n")
            
            pass
    
    if B_options == 'B':
        web_options = str(input("Which website do you want to visit?: "))
        webbrowser.open(web_options)
    elif B_options == '$Quit':
        pass
    
    print("DONE! :)\n")

    def opt_C():
        print("What do you want me to do?")
        print("A: Open VScode")
        print("B: Open PyCharm")
        print("C: Compile a C file")
        C_option = input("Your option: ")
        if C_option == 'A':
            os.startfile(f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif C_option == 'B':
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe")
        elif C_option == 'C':
            print("It will come soon! untill then listen this")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif C_option == '$Quit':
            pass
        else:
            print("HUH?!")
 


time.sleep(1.8)
print("What can I do for you??? :)")
print("A. Terminal options")
print("B. Browser options")
print("C. Dev options")
print("D. Send an Email")
while 1:
    option = input("Your option: ")
    if option == 'A':
        opt_A()
    elif option == 'B':
        opt_B()
    elif option == 'C':
        opt_C()
    elif option == 'D':
        Email_user = input("Enter your Email: ")
        Email_Password = input("Enter your Email password: ")
    
        Email_reciever = input("Enter reciever's Email: ")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(Email_user, Email_Password)
            subject = input("Subject: ")
            body = input("Message: ")
            
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(Email_user, Email_reciever, msg)

            print("email sent!")
            time.sleep(2)
            pass 
    
    elif option == '$RRsu':
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    elif option == '$Quit':
        exit()
    
    else:
        print("LOL, what are you trying to say?\n")

# The Improvements of V0.3.0 are...
# 1) Opening other terminals like powershell and cmd instead of only windows Terminal app
# 2) Opening search engines and apps
# 3) search what you want in the terminal
# 4) Send Email
