import tkinter as tk      #for GUI
from tkinter import messagebox as tkMessageBox   #import message box as an application
from tkinter import *
import speech_recognition as sr     #installing this for recognising the voice you speak to the system
import pyttsx3 as pt          #installing this for system to answer to you
import pywhatkit as pwk       #installing this for playing song
import datetime as dt      #installing this for date and time 
import wikipedia as wk  #installing this for wikipedia results
import pyjokes as pyj    #installing this for generating a random joke

root = tk.Tk()      #initializing tkinter 

def program():
    tkMessageBox.showinfo( "Voice Controlling System", "Click here to start the program")
       #creating object listener that listens to your voice
    listener = sr.Recognizer() 

    #creating object speaker that responds to you       
    speaker = pt.init()             

    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)       #voices[1].id is just for system to speak in female voice(default voice is of male)...It can speak in male voice at voices[0].id
    
    speaker.say('Hi friend')          #initially saying these two lines and then waiting for user to respond
    speaker.say('I am rosie')
    speaker.say('What can i do for you?')
    speaker.runAndWait()
    
    #speaking whatever parameter it is in text and then waiting for user to respond
    def talk(text): 
        speaker.say(text)     
        speaker.runAndWait()        #waiting for the user to respond after running above

    def take_command():    #function for taking command from user
        try:            
            #this try block is when sometimes when microphone does not work or when system sometime errors in recognizing the voice
        
            with sr.Microphone() as x:     
                #running of microphone to listen to user voice as naming it as source x
            
                tkMessageBox.showinfo( "Voice Controlling System", "Starting to listen....")     #popping up message that system is ready to listen
            
                #now the listener variable that is recognizing the voice, recognize the voice from source x  
                voice = listener.listen(x)
            
                #now that voice is transferred into text using google API and is stored in variable called command
                command = listener.recognize_google(voice)  
                command = command.lower()
            
                #now if rosie/rosy is there in command, only then it will enter the loop
                if 'rosie' in command: 
                    command = command.replace('rosie','')   #replacing rosie/rosy word by null string as we need to identify the task from this command list of strings and rosie/rosy word itself has no use in it
                    print(command)      #printing the command that is printing what the user just said
                    
                elif 'rosy' in command:
                    command = command.replace('rosy','')   #replacing rosie/rosy word by null string as we need to identify the task from this command list of strings and rosie/rosy word itself has no use in it
                    print(command)      #printing the command that is printing what the user just said
                    
                    
        except:     
            #simply passing the except block that is simply not doing anything for error or exception above
            pass

        return command  #returning command

    def run_command(command):       #now running that command we just heard from user and answering him back his/her reply
    
        #for playing any song or video
        if 'play' in command:
            song = command.replace('play','')       #replacing word play
            text = Text(root,height=5,width=100)    #replying in GUI format in text
            text.insert(INSERT, command)
            text.insert(END, "\n\tPlaying :"+song)
            text.pack()
            talk('playing ' + song)   #speaker talking that he is playing the particular song you asked for
            print("playing :",song)   #printing the same as rosie/rosy just said
            pwk.playonyt(song)  #playing song on youtube
    
        #for knowing time
        elif 'time' in command:
            time = dt.datetime.now().strftime('%I:%M %p')   #setting the format of time...I set the time as hr:min system and also showing AM and PM
            print("Current time is :",time)     #printing and reading out the time
            text = Text(root,height=5,width=100)    #replying in GUI fomrat in text
            text.insert(INSERT, command+"?")
            text.insert(END, "\n\tCurrent time is :"+time)
            text.pack()
            talk('Current time is :'+time)  #rosie/rosy replies..
    
        #for knowing about someone
        elif 'who is' in command:
            info = wk.summary(command,1) #storing info of that thing in 1 line from wikipedia in variable info
            text = Text(root,height=5,width=100)    #replying in GUI format in text
            text.insert(INSERT, command+"?")
            text.insert(END, "\n\t"+info)
            text.pack()
            print(info)     #printing and talking that info
            talk(info)
    
       #for knowing about something    
        elif 'what is' in command:
            info = wk.summary(command,1) #storing info of that thing in 1 line from wikipedia in variable info
            text = Text(root,height=5,width=100)    #replying in GUI format in text
            text.insert(INSERT, command+"?")
            text.insert(END, "\n\t"+info)
            text.pack()
            print(info)     #printing and talking that info
            talk(info)
        
        elif 'are you single' in command:
            text = Text(root,height=5,width=100)    #replying in GUI format in text
            text.insert(INSERT, command+"?")
            text.insert(END, "\n\tSorry! I am in relationship with python... Better luck next time!!")
            text.pack()
            print("Sorry! I am in relationship with python... Better luck next time!!") #printing and replying the message written
            talk('Sorry, I am in relationship with python')
            talk('Better luck next time')
            
        elif 'how are you' in command:
            text = Text(root,height=5,width=100)    #replying in GUI format in text
            text.insert(INSERT, command+"?")
            text.insert(END, "\n\tI am great!! I request you to wear mask, keep yourself sanitized and stay safe by staying at home. How can I help you?")
            text.pack()
            print("I am great!! I request you to wear mask, keep yourself sanitized and stay safe by staying at home. How can I help you?")   #printing and replying the message written
            talk('I am great')
            talk('I request you to wear mask')
            talk('keep youself sanitized and stay safe by staying at home')
            talk('How can I help you')
    
        elif 'joke' in command: #asking a joke
            d=pyj.get_joke()    #generating a random joke and storing it in variable d
            text = Text(root,height=5,width=100)    #replying in GUI format in text
            text.insert(INSERT, command)
            text.insert(END, "\n\t"+d)
            text.pack()
            print(d)    #printing and speaking the joke that we just generated and stored in d
            talk(d)
        
        else:           #if rosie/rosy don't understand what you say
            tkMessageBox.showinfo( "Voice Controlling System", "Pardon Please!!") 
            print("Pardon Please...")
            talk('Pardon Please')

    def main():         #main function
        user_command = take_command()  #taking command from user
    
        while 'thanks' not in user_command:      #if thank you in the command that means asking to end the program
            run_command(user_command)       #running the command which is obtained from user
            print("Task Completed")         
            tkMessageBox.showinfo( "Voice Controlling System", "Task Completed!!")  #printing this after every command executed
            user_command = take_command()   #asking user to give commands until user says thank you
        
        else:       #if thank you mentioned, meaning you need to end the program, then run this block
            talk('Thank you sir')
            talk('See you next time')
            tkMessageBox.showinfo( "Voice Controlling System", "Thank you sir!! See you next time...")
            print("Thank you sir!! See you next time...")
        
    main()  #running main function

#a button named 'Welcome to Voice Controlling System\nClick Here!!' by which after clicking, command named program that is function named program is called for running   
d = tk.Button(root, text ="Welcome to Voice Controlling System\nClick Here to start ROSIE!!", command = program)   
d.pack()
root.mainloop()     #running the application 
