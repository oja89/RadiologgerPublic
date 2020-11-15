from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def get_orig_sentences(content):
    """
    Dont remove anything, just list
    """

    sentences_list = []

    # take all sentences divided by dots
    sentences = sent_tokenize(content)

    for sentence in sentences:
        # do a new list
        sentence_as_list = []
        words = word_tokenize(sentence)
        for word in words:
            # add this word to the sentence
            sentence_as_list.append(word)

        # combine all sentences
        sentences_list.append(sentence_as_list)

    return sentences_list


def get_cleaned_sentences(content):
    """
    Parse the contents of file into lists
    """

    sentences_list = []
    # get stopwords, and
    stops = set(stopwords.words("english"))

    # take all sentences divided by dots
    sentences = sent_tokenize(content)

    for sentence in sentences:
        # do a new list
        sentence_as_list = []
        words = word_tokenize(sentence)
        words = [word.lower() for word in words if word.isalpha()]
        for word in words:
            # take stops out from the word lists
            if word not in stops:
                sentence_as_list.append(word)

        # combine all sentences
        sentences_list.append(sentence_as_list)

    return sentences_list