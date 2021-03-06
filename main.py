import heapq
import os

import conf.config as config
import modules.filework as filework
from modules.cleaners import get_cleaned_sentences, get_orig_sentences
from modules.db_search import db_check, db_keywords
from modules.freqcounter import get_freqs

reports = config.REPORTDIR
summaryfolder = config.SUMMARYFOLDER
summaryname = config.SUMMARYNAME
sent_amount = config.SENTAMOUNT


def get_files():
    """
    get all paths to .txt files in REPORTDIR (./reports)
    """
    files = filework.get_files(reports)
    return files

# parse each file, dictionarize it
def dofile(filename):
    """
    do summary for one file, return summary, keywords, most_valuable
    """
    file = filename

    # we want 2 objects, 1 with the original article (that is the file)
    # and formatted, parsed text, which is now the parsefile
    print(file)
    content = open(file).read()

    # converted lowercase etc
    parsed = get_cleaned_sentences(content)

    # use "original" for summary
    original = get_orig_sentences(content)

    # for each file, a summary
    summary = []
    # also take the "original" keywords separately to not mess with freqs etc.
    keywords = []

    # also mild, moderate, severe
    mild_list = []
    moderate_list = []
    severe_list = []

    #for each sentence
    for sentence in parsed:

        # If this sentence starts with "Keywords", we dont need do this
        # just print the sentence.
        if sentence[0] == "keywords":
            print("a keyword sentence")
            stopwords = ["keyword", "keywords"]
            for word in sentence:
                if word not in stopwords:
                    keywords.append(word)

            # dont let loop go to append again
            continue
        # else, use the sentence
        # check if the words are in db, return those that are
        # THIS IS VERY TIME CONSUMING!
        else:
            db_words, milds, moderates, severes = db_check(sentence)

        # append these to the summary
        summary.append(db_words)
        # append these only if there are something to output
        if len(milds) > 0:
            mild_list.append(milds)
        if len(moderates) > 0:
            moderate_list.append(moderates)
        if len(severes) > 0:
            severe_list.append(severes)


    # check this again against the original file?
    # calculate word freq from db_words
    wordfreq = get_freqs(summary)

    # check each original sentence against the wordfreq?
    # take whole sentences that have most wordfreq value?
    sentencevalues = {}
    i = 0
    for sentence in original:
        sentencevalue = 0
        for word in sentence:
            if word in wordfreq:
                # value of the word is
                value = wordfreq[word]
                sentencevalue += value
        #print(sentences, sentencevalue)
        # use number for sentence ordering, cause it is a list
        sentencevalues[i] = sentencevalue
        i += 1

    #print(sentencevalues)
    # take 3 sentences with highest sentencevalue
    order = heapq.nlargest(sent_amount, sentencevalues, key=sentencevalues.get)
    #print(order)

    most_valuable = []
    for i in range(0, len(order)):
    # take these sentences

        most_valuable.append(original[order[i]])


    return summary, keywords, most_valuable, mild_list, moderate_list, severe_list, parsed, original

def get_reportname(file):
    """
    use the filename to name the log file
    get filename without extension from originalfile
    """
    reportname = os.path.splitext(os.path.basename(file))[0]
    return reportname


def get_outputname(reportname):
    """
    name the outputfile and put it in the summaries folder
    """
    outputfile = summaryfolder + "/" + reportname + summaryname
    return outputfile


# new version with found words, original keywords and the most valuable sentence
def outputstuff(output_content, outputfile):
    """
    write the contents, log the folder and lines written to print
    it writes always on top of earlier!
    """
    lines_written = filework.write_list_to_file(output_content, outputfile)
    print(outputfile, lines_written)
    return 1

########

def main():
    """
    if ran as main, do the normal procedure as this did earlier
    """

    # get the filelist
    files = get_files()

    # check every file
    for file in files:
        summary, keywords, most_valuable, mild_list, moderate_list, severe_list, parsed, original = dofile(file)

        # get name from report file
        reportname = get_reportname(file)

        # get name for outputfile
        outputfile = get_outputname(reportname)

        # check if the keywords are in the database
        keys_in_db = db_keywords(keywords)

        # format the output
        original = ["Original text: "] + original + ["\n"]
        parsed = ["Lowercased and without stopwords: "] + parsed + ["\n"]
        summary = ["Matched against UMLS: "] + summary + ["\n"]
        keywords = ["Keywords: "] + keywords + ["\n"]
        most_valuable = ["Most valuable sentences calculated: "] + most_valuable + ["\n"]
        mild_list = ["Milds: "] + mild_list + ["\n"]
        moderate_list = ["Moderates: "] + moderate_list + ["\n"]
        severe_list = ["Severes: "] + severe_list + ["\n"]
        keys_in_db = ["Keywords found from UMLS db: "] + keys_in_db + ["\n"]

        # outputcontent order
        output_content = original + parsed + summary + keywords + most_valuable + mild_list + moderate_list + severe_list + keys_in_db

        # do writing to that file
        outputstuff(output_content, outputfile)

    print("all done")

if __name__ == "__main__":
    main()