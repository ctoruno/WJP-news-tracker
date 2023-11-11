import os
import pandas as pd
from dotenv import load_dotenv
import translators as ts
from newsdataapi import NewsDataApiClient

# Loading API KEY from environment
load_dotenv()
NEWSDATA_API = os.getenv("newsdata_api")
api = NewsDataApiClient(apikey = NEWSDATA_API)

# Defining keywords in english
keywords_en = ["Rule of Law Index", "World Justice Project"]

# Defining a translating function 
languages   = ["zh", "ar", "ru", "fr", "de", "es", "pt", "it", "ja", "ko", "hi", "id"]
def keytrans(key, targetlang):
    """
    This functions gathers a keyword in a specific target language and it returns
    its english translation using the Google translation engine.

    Parameters:
        key:        String. Text to translate.
        targetlang: String. Language of the target language.
    """
    result = ts.translate_text(
        key, 
        translator = "google",
        from_language = "en",
        to_language = targetlang
    )
    return result

# Translating keywords to other languages
keywords_other = [keytrans(key = k, targetlang = x) 
                  for x in languages
                  for k in keywords_en]

# Full list of keywords
keywords = keywords_en + keywords_other

# Defining a function to fetch news articles
def newsfetch(key):
    """
    This function collects a specific keyword and uses the NewsData API to scrap
    news articles from their massive archive.

    Parameters:
        key: String. Keyword(s) to search for in the NewsData API.
    """
    
    print(f"Searching news articles for: {key}")

    counter = 1
    print("Page no. " + str(counter) + " of results")

    # Fetching news articles
    response = api.archive_api(q = f'"{key}"')
    data     = pd.DataFrame(response)
    results  = pd.DataFrame(response["results"])

    if data.empty == False:
        np = data.loc[0,"nextPage"]
        while np is not None:
            counter  = counter + 1
            print("Page no. " + str(counter) + " of results")
            response = api.archive_api(q    = f'"{key}"',
                                    page = np)
            data     = pd.DataFrame(response)
            results  = pd.concat([results, pd.DataFrame(response["results"])])
            
            np = data.loc[0,"nextPage"]

    return results

# Applying function to the full list of keywords
fetch_data = [newsfetch(x) for x in keywords]
master = pd.concat(fetch_data)
master_unique = master.drop_duplicates(subset = ["article_id"])

# Saving data
master_unique.to_csv("master.csv")