from pathlib import WindowsPath
from bs4 import BeautifulSoup
from urllib.request import urlopen
import jsonlines, json
from collections import Counter
import re
from nltk.stem import PorterStemmer
import os

        
def create_inverted_index(file_name):

    key = 0 # for assigning document id
    url_id_map = dict({})   # map each url to an id
    inverted_index  = dict({})
    
    # read each JSON file, and add url to the map
    with open(file_name, "r") as file:
        for file_path in file:
            file_path = WindowsPath(file_path.strip("\n"))
            print("Reading content from", file_path)
            with open(file_path, "r") as file:
                
                # get a json object
                jsonObj = json.load(file)
        
                # get the url and tokens (including its frequency). 
                url = jsonObj["url"]
                content = jsonObj["content"]
                tokens = frequency_word_per_url(content)
                
                # map each url to a document id
                url_id_map[key] = url
        
                # update the posting list for each token
                for token in tokens:
                    if token not in inverted_index:
                        inverted_index[token] = {key: tokens[token]}
                    else:
                        inverted_index[token][key] = tokens[token]
        
                # update doc id
                key += 1

    return url_id_map, inverted_index





def frequency_word_per_url(content):
    #given a url returns a dictionary: key-> word, value-> frequency of word
    #words in dictionary are stemmed

    #https://docs.python.org/3/library/re.html used to with re.findall to find all valid words in url
    #https://www.geeksforgeeks.org/python-stemming-words-with-nltk/ used for learining PorterStemmer
    # resp = urlopen(url)
    # html = resp.read()

    soup = BeautifulSoup(content, 'html.parser')
    for cur in soup(['script', 'style']):
        cur.extract()

    text = soup.get_text(separator=" ")
    words = re.findall(r"\b\w+\b", text.lower())

    stemmer = PorterStemmer()
    stemmed_word_lis = [stemmer.stem(word) for word in words]

    frequency = Counter(stemmed_word_lis)

    return dict(frequency)




def save_url_id_to_file(url_id_map):
    with open("url_id.json", 'a') as file:
        json.dump(url_id_map, file, indent=3)
    print("Finished writing to file.")





def save_index_to_file(inverted_index):
    with open("inverted_index.jsonl", 'a') as file:
        for token in inverted_index:
            data = {token: inverted_index[token]}
            json.dump(data, file)
            file.write("\n")
    
    print("Finished writing to file.")


### Report Helper Functions ###
def get_unique_token_count(file_path):
    """
    Counts the unique tokens in a given file.

    Args:
        file_path (str): Path to the file.

    Returns:
        int: Number of unique tokens.
    """
    unique_tokens = set()
    with open(file_path, 'r') as f:
        for line in f:
            token = line.strip().split()[0]  # Assuming the word is the first element
            unique_tokens.add(token)
    return len(unique_tokens)

def get_file_size_kb(file_path):
    """
    Gets the size of a file in KB.

    Args:
        file_path (str): Path to the file.

    Returns:
        float: File size in KB.
    """
    size_bytes = os.path.getsize(file_path)
    size_kb = size_bytes / 1024  # Convert to KB
    return round(size_kb, 2)


def get_average_list_size_per_token(file_path):
    """
    Computes the average number of URLs per token in the file.

    Args:
        file_path (str): Path to the file.

    Returns:
        float: Average list size per token.
    """
    total_urls = 0
    total_tokens = 0
    with open(file_path, 'r') as f:
        for line in f:
            urls = line.strip().split()[1:]  # Assuming URLs follow the token
            total_urls += len(urls)
            total_tokens += 1

    if total_tokens == 0:
        return 0.0
    
    return round(total_urls / total_tokens, 2)



if __name__ == '__main__':

    # run collect_file_path.py to get the txt file (named "JSON_file_path.txt")
    file_name = "JSON_file_path.txt"

    # create inverted_index
    url_id_map, inverted_index = create_inverted_index(file_name)

    # save the map to file
    save_url_id_to_file(url_id_map)
    save_index_to_file(inverted_index)
     
    