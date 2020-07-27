###############################################
#
#     Script to extract most common words
#             from a given website
#
#                     by
#
#              Code Monkey King
#
###############################################

# packages
from urllib.request import urlopen
from html.parser import HTMLParser
import json
import collections

# words parser class
class WordsParser(HTMLParser):
    # tags to search text within
    search_tags = ['p', 'div', 'span', 'a', 'h1', 'h2', 'h2', 'h3', 'h4']
    
    # current tag
    current_tag = ''
    
    # common word list
    common_words = {}
    
    # handle starting tag
    def handle_starttag(self, tag, attr):
        # store current tag
        self.current_tag = tag        
            
    # handle tag's data
    def handle_data(self, data):
        # make sure current tag matches search tags
        if self.current_tag in self.search_tags:
            # loop over word list within current tag
            for word in data.strip().split():
                # convert word to lowercase and filter characters
                common_word = word.lower()
                common_word = common_word.replace('.', '')
                common_word = common_word.replace(':', '')
                common_word = common_word.replace(',', '')
                common_word = common_word.replace('"', '')
                
                # filter words
                if (
                       len(common_word) > 2 and
                       common_word not in ['the', 'and', 'all'] and
                       common_word[0].isalpha()
                   ):

                    try:
                        # try to update count of a given word if available
                        self.common_words[common_word] += 1
                    
                    except:
                        # store current common word
                        self.common_words.update({common_word: 1})
    
# main driver
if __name__ == '__main__':
    # target URL to scrape
    url = 'https://clj.uic.edu/'
    
    # make HTTP GET request to the target URL
    response = urlopen(url)
    
    # extract HTML document from response
    html = response.read().decode('utf-8', errors='ignore')
    
    # create words parser instance
    words_parser = WordsParser()
    
    # feed HTML to words parser
    words_parser.feed(html)
    
    # count common words with counter
    words_count = collections.Counter(words_parser.common_words)
    
    # extract 25 most comon words
    most_common = words_count.most_common(25)
    
    # loop over most common words
    for word, count in most_common:
        print(word, str(count) + ' times', sep=": ")
    


















    
    
