from modules.authentication import Authentication
from conf.config import API_KEY as API_KEY
import modules.db as db
import requests, json

#API key can be seen in UMLS profile page

#moved the key to ./conf/config so its not hardcoded here
apikey = API_KEY
URI = "https://uts-ws.nlm.nih.gov"
search_endpoint = "/rest/search/2020AA"
search_type = "normalizedWords"
libraries = "MTH"

AuthClient = Authentication(apikey)
tgt = AuthClient.gettgt()
pagenumber = 1

def db_check(content):

    ret_words = []
    # return also lists of mild, moderate, severe words
    mild_words = []
    moderate_words = []
    severe_words = []

    for word in content:

        # check also if the words can be found from mild, moderate, severe dbs:
        if word in db.mild_words:
            mild_words.append(word)
        if word in db.moderate_words:
            moderate_words.append(word)
        if word in db.severe_words:
            severe_words.append(word)

        # if word checked already and not in UMLS:
        if word in db.not_found_db:
            # no need to search again
            #print("word already checked and NOT found: " + word)
            print(word, end = ', ')
            continue

        # if word is checked and found already from UMLS:
        if word in db.found_db:
            #no need to search again
            #print("word already checked and found: " + word.upper())
            print(word.upper(), end = ', ')
            ret_words.append(word)
            continue

        # otherwise this is a new word, ask it from UMLS
        ticket = AuthClient.getst(tgt)
        query = {'string':word, 'ticket':ticket, 'searchType': search_type, 'sabs': libraries}
        r = requests.get(URI+search_endpoint, params=query)
        r.encoding = 'utf-8'
        items = json.loads(r.text)
        jsonData = items["result"]

        #pdb.set_trace()

        #if not found, save in not_found and continue
        if jsonData["results"][0]["ui"] == "NONE":
            #print(word)
            print(word, end=', ')
            db.not_found_db.append(word)
            continue

        #if found, save in found and append to word list
        else:
            #print(word.upper())
            print(word.upper(), end=', ')
            db.found_db.append(word)
            #add word to list
            ret_words.append(word)
    return ret_words, mild_words, moderate_words, severe_words

def db_keywords(keywords):

    keys_in_db = []

    for word in keywords:

        if word in db.not_found_db:
            # no need to search again
            print("word already checked and NOT found: " + word)
            continue

        if word in db.found_db:
            #no need to search again
            print("word already checked and found: " + word.upper())
            keys_in_db.append(word)
            continue

        ticket = AuthClient.getst(tgt)
        query = {'string':word, 'ticket':ticket, 'searchType': search_type, 'sabs': libraries}
        r = requests.get(URI+search_endpoint, params=query)
        r.encoding = 'utf-8'
        items = json.loads(r.text)
        jsonData = items["result"]

        #pdb.set_trace()

        #if not found, save in not_found and continue
        if jsonData["results"][0]["ui"] == "NONE":
            print(word)
            db.not_found_db.append(word)
            continue
        #if found, save in found and append to word list
        else:
            print(word.upper())
            db.found_db.append(word)
            #add word to list
            keys_in_db.append(word)
    return keys_in_db
