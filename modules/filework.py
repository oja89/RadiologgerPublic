import os

def get_files(repdir):
    """
    Open the dir, and print all txt files inside
    """
    filelist = []
    for root, dirs, files in os.walk(repdir):
        for file in files:
            # print(os.path.join(root, file))
            # print(file)

            # for each file with .txt
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                filelist.append(filepath)

    return filelist

def write_list_to_file(content, logfile):
    """
    Write parsed stuff to outputfile
    """

    f = open(logfile, "w+")
    lines = 0

    for sentences in content:
        lines += 1

        for words in sentences:

            f.write(words)
            f.write(" ")
        f.write("\n")

    f.close()

    return lines

def write_string_to_file(content, logfile):
    """
    Write parsed stuff to outputfile
    """

    f = open(logfile, "w+")
    lines = 0

    for sentences in content:
        f.write(sentences)
        f.write("\n")
        lines += 1

    # write to file
    f.write("\n")
    lines += 1

    f.close()

    return lines