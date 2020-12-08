#Imports, Variables and Functions
import source
import webbrowser
ukUS = source.ukUS
usUK = source.usUK
loopN = 0
wordN = ""
wordsP = ""

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
                Type !Updates to check for updates                                                        
                Type !CC to find out about this work's copyright protection            
                Type !Git to be sent to the GitHub repo                                              
                """)


    elif command == "!updates":
        # Check vertion number on github
        print("Updates is a WIP")
        print("")

    elif command == "!cc":
       print("""
                US/UK English Converter is protected by CC BY-SA 4.0
                Attribution-ShareAlike 4.0 International

                You are free to:
                # Share — copy and redistribute the material in any medium or format
                # Adapt — remix, transform, and build upon the material for any purpose, even commercially.

                Under the following terms:
                # Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
                You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
                # ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
                
                Attribution:
                Thomas Landstra
                thomaslandstra@gmail.com

                https://creativecommons.org/licenses/by-sa/4.0/
                enter command !CCL to be sent to the website
                """)

    elif command == "!ccl":
        webbrowser.open("https://creativecommons.org/licenses/by-sa/4.0/", new=2)

    elif command == "!git":
        webbrowser.open("", new=2)

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