import pdfplumber
import os
import conf.config

pdffolder = conf.config.PDFFOLDER
txtfolder = conf.config.TXTFOLDER

def get_pdfs(dir):
    """
    Open the dir, and print all txt files inside
    """
    filelist = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            # print(os.path.join(root, file))
            # print(file)

            # for each file with .txt
            if file.endswith(".pdf"):
                filepath = os.path.join(root, file)
                filelist.append(filepath)

    return filelist


def write_to_file(content, outputfile):
    """
    Write parsed stuff to outputfile
    """

    f = open(outputfile, "w+")

    # remove nonascii (caused unicode errors)
    encode = content.encode("ascii", "ignore")
    text = encode.decode()

    f.write(text)

    f.close()
    return 0


def pdf_to_txt(file):
    """
    PDF to TXT
    """
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            pagetext = page.extract_text()
            text += pagetext
        return text


# get all paths to .pdf files in PDFFOLDER (./pdfs)
files = get_pdfs(pdffolder)

# create a txt file for all pdf files
n_of_files = 0
for file in files:
    n_of_files += 1
    text = pdf_to_txt(file)
    # use the filename to name the log file
    # get filename without extension from originalfile
    reportname = os.path.splitext(os.path.basename(file))[0]

    # name the outputfile and put it in the summaries folder
    outputfile = txtfolder + "/" + reportname + ".txt"
    write_to_file(text, outputfile)

print(n_of_files)