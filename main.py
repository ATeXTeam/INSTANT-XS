# Owner: ATeXTeam
# project founder: Naveed Usman aka SNUcoder
# Date: 4-13-22 2:40pm

print('please wait... \n')

import time
import getpass
import geocoder
import os
import webbrowser

username = getpass.getuser()
g = geocoder.ip('me')
print ( "\n============================================================ Hello", username, "from", g.city,"============================================================\n" )

time.sleep(1.8)
print("What can I do for you??? :)")
print("A. Terminal options")
print("B. Browser options")
print("C. Open VScode")
print("D. Special options")
while 1:
    option = input("Your option: ")
    if option == 'A':
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
        else:
            print("HUH?!")

        print("Opened your terminal :)\n")

    elif option == 'B':
        print("A. Search engine")
        print("B. Open a website")
        B_options = input("Your option: ")

        if B_options == 'A':
            print("Which search engine?\n")
            print("A. Brave")
            print("B. Google")
            print("C. Duckduckgo")
            print("D. Bing")

            Search_option = input("Your option: ")
            if Search_option == 'A':
                webbrowser.open("https://search.brave.com")
            elif Search_option == 'B':
                webbrowser.open("https://google.com")
            elif Search_option == 'C':
                webbrowser.open("https://duckduckgo.com/")
            elif Search_option == 'D':
                webbrowser.open("https://www.bing.com/")
            else:
                print("What kind of search engine is that?\n")

            print("Opened your search engine :)")
            pass
        if B_options == 'B':
            web_options = str(input("Which website do you want to visit?: "))
            webbrowser.open(web_options)

        print("Opened the website :)\n")

    elif option == 'C':
        print("Opens VScode")
        os.startfile(f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif option == 'D':
        print("Never gonna give you up")
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
    else:
        print("LOL, what are you trying to say?\n")

# The Improvements of V0.2.0 are...
# 1) Opening other terminals like powershell and cmd instead of only windows Terminal app
# 2) Opening search engines and apps
