from modules.authentication import Authentication
from conf.config import API_KEY as API_KEY
import modules.db as db
import requests, json

#API key can be seen in UMLS profile page

#moved the key to ./conf/apilogin so its not hardcoded here
apikey = API_KEY
URI = "https://uts-ws.nlm.nih.gov"
search_endpoint = "/rest/search/2020AA"
search_type = "normalizedWords"
libraries = "MTH"

AuthClient = Authentication(apikey)
tgt = AuthClient.gettgt()
pagenumber = 1

def db_check(content):
    #list_of_words = content.split(" ")

    ret_words = []
    #for word in list_of_words:

    #print(content)
    for word in content:
        #print(word)

        # if word in wordlist:
        if word in db.not_found_db:
            # no need to search again
            print("word already checked and NOT found: " + word)
            continue

        if word in db.found_db:
            #no need to search again
            print("word already checked and found: " + word.upper())
            ret_words.append(word)
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
            ret_words.append(word)
    return ret_words
