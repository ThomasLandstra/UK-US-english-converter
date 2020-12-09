#Imports, Variables and Functions
import source
import webbrowser
import requests
import bs4

ukUS = source.ukUS
usUK = source.usUK
loopN = 0
wordN = ""
wordsP = ""

# Update Checking
v = "1.0.0"
vu = "https://api.github.com/repos/rust-lang/rust/releases/latest"
vUp = requests.get(vu)
vSoup = bs4.BeautifulSoup(vUp.text, "html.parser")
vSoup = str(vSoup)
vSoup = vSoup.split()
vSoup = vSoup[1]
uL = 0

while True:
    if vSoup[uL:uL+1] == '"':
        if vSoup[:uL] == v:
            print("Checked for Updates. No updates Available")
            break
        else:
            print("A new update is availale (" + vSoup[:uL] + "). Type !update to be taken to the releases page.")
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("A new update is availale!", "Version " + vSoup[:uL] + " of UK/US English translator is available.", threaded=True, duration=6)
            break
    elif uL == len(vSoup):
        print("Failed to check for updates")
        break
    uL += 1

#Introduction
print("")
print("Hello, welcome to US/UK english converter.")
print("Type '!Start' to begin the convertion or type '!Help' for more commands.")
print("")

# Main code
while True:
    command = input("Enter Command: ").lower() # Get user command and make lowercase for detection
    print("")

    # Help Command
    if command == "!help":
        print("""Type !Start to begin converting from US to UK english.
                Type !Help to open a help menu.                                                     
                Type !C to find out about this work's copyright protection            
                Type !Git to be sent to the GitHub repo                                              
                """)

    elif command == "!c":
       print("""
                US/UK English Converter is protected by the MIT license

                The MIT License

                Copyright (c) 2020 Luacrix Software, Inc. All Rights Reserved.

                Permission is hereby granted, free of charge, to any person obtaining a copy
                of this software and associated documentation files (the "Software"), to deal
                in the Software without restriction, including without limitation the rights
                to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
                copies of the Software, and to permit persons to whom the Software is
                furnished to do so, subject to the following conditions:

                The above copyright notice and this permission notice shall be included in
                all copies or substantial portions of the Software.

                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
                IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
                FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
                AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
                LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
                OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
                THE SOFTWARE.
                
                Optional Attribution:
                Thomas Landstra
                thomaslandstra@gmail.com

                enter command !CL to be sent to the license on github.
                """)

    elif command == "!update":
        webbrowser.open("https://github.com/Ludacrix-Software/UK-US-english-converter/releases", new=2)

    elif command == "!cl":
        webbrowser.open("https://github.com/Ludacrix-Software/UK-US-english-converter/blob/main/LICENSE", new=2)

    elif command == "!git":
        webbrowser.open("https://github.com/Ludacrix-Software/UK-US-english-converter", new=2)

    elif command == "!start":
        conTo = input("For UK to US type 1, for US to UK type 2: ") # Ask for US to UK or UK to US
        conTo = int(conTo) # Convert to Int
        rawText = input("Please paste your text here: ") # Get User Text
        words = rawText.split() # Convert User Text to a List
        if conTo == 1:
            loopN = 0
            for word in words: # For every word in user input
                for x in ukUS: # For every word in the uk to us english dictonary
                    if word == x: # If word is diffrent in US english
                        words[loopN] = ukUS[x] # change word to new word
                loopN += 1 

            print('''
        Converted Words Here:''')
            wordsP = ""
            for x in words: # Turn list into String
                wordsP = wordsP + " " + x
            print(wordsP)
            print("")                        

        elif conTo == 2:
            loopN = 0
            for word in words: # For every word in user input
                for y in usUK: # For every word in the us to uk english dictonary
                    if word == y: # If word is diffrent in UK english
                        words[loopN] = usUK[y] # change word to new word
                loopN += 1

            print('''
            Converted Words Here:''')
            wordsP = ""
            for x in words: # Turn list into String
                wordsP = wordsP + " " + x
            print(wordsP)
            print("")   

        else: # User input was not a 1 or a 2
            print("Error when choosing US to UK or UK to US")