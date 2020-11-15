from main import *
from tkinter import *
from tkinter.filedialog import askopenfilename

#Parse texts from lists
def parser(parsed_to_be):
    parsed = ""
    for sentence in parsed_to_be:
        for word in sentence:
            parsed += word
            parsed += " "
        parsed += "\n"
    return parsed


def do_summary():
    #Delete previous text
    T.delete('1.0', END)
    
    #Deny clicks on button while script is running. If the command is ran while the loop everything breaks.
    button_choose.config(command=lambda: None)
    file = askopenfilename()
    #get the filelist
    #files = get_files()

    #check file
    summary, keywords, most_valuable = dofile(file)

    #get name from report file
    reportname = get_reportname(file)

    #get name for outputfile
    outputfile = get_outputname(reportname)

    output_content = summary + keywords + most_valuable
    #do writing to that file
    outputstuff(output_content, outputfile)

    #Parse the name
    reportname = reportname.replace("-", " ")

    #Parse all
    summary = parser(summary)
    keywords = parser(keywords)
    most_valuable = parser(most_valuable)
    
    text = "Filename: "+ str(reportname) + "\n" +  "\n" +"Stopwords parsed from the sentences: " + "\n"+ summary +"\n"+ "\n"+ keywords + "\n" + "\n" + "Most valuable sentences:" + "\n" + most_valuable
    T.insert(END, text) 
    
    #Make the button command available again
    button_choose.config(command=do_summary)
    
#GUI SETUP
window=Tk()
window.title("Radiologist Report Summarization")
window.geometry("1000x900+20+40")

Tk().withdraw()

T = Text(window, height = 800, width = 400, bd=10, pady=5, wrap=WORD, xscrollcommand=set(), yscrollcommand=set()) 
l = Label(window, text = "Summary") 

button_choose = Button(window, command=do_summary)
button_choose['text'] = "Choose file to summarize"
button_choose['background'] = 'gray'
button_choose.pack()

l.pack()
T.pack()

#GUI loop
window.mainloop()