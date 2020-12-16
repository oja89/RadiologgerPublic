from main import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from modules.db_search import db_keywords
#Parse texts from lists
def parser(parsed_to_be):
    parsed = ""
    for sentence in parsed_to_be:
        for word in sentence:
            parsed += word
            parsed += " "
        parsed += "\n"
    return parsed

def loop_list(loop):
    output = ""
    for list in loop:
        for word in list:
            output += word
            output += ", "
    size = len(output)
    output = output[:size-2]
    return output
    




def do_summary():
    #Delete previous text
    T.delete('1.0', END)
    
    #Deny clicks on button while script is running. If the command is ran while the loop everything breaks.
    button_choose.config(command=lambda: None)
    file = askopenfilename()
    #get the filelist
    #files = get_files()

    #check file
    summary, keywords, most_valuable, mild, moderate, severe, parsed, original = dofile(file)
    #get name from report file
    reportname = get_reportname(file)
    
    #Get db keywords
    keys_in_db = str(db_keywords(keywords))
    #get name for outputfile
    outputfile = get_outputname(reportname)

    output_content = summary + keywords + most_valuable
    #do writing to that file
    outputstuff(output_content, outputfile)

    #Parse the name
    reportname = reportname.replace("-", " ")

    #Parse all
    parsed = parser(parsed)
    summary = parser(summary)
    most_valuable = parser(most_valuable)
    mild = "Milds: " + loop_list(mild)
    moderate = "Moderates: " + loop_list(moderate)
    severe = "Severes: " +  loop_list(severe)
    keys_in_db = "Keywords found from UMLS db: " + keys_in_db
    text = "Filename: "+ str(reportname) + "\n" +  "\n" +"Lowecased and without stopwords: " + "\n"+ parsed +"\n"+ "\n"+"Matched against UMLS  " + "\n"+ summary +"\n"+ "\n"+"Keywords:"+ "\n"+ str(keywords) + "\n" + "\n" + "Summary:" + "\n" + most_valuable + "\n"+ "\n"+ mild + "\n"+ "\n" + moderate + "\n"+  "\n"+ severe + "\n" + "\n" + keys_in_db
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