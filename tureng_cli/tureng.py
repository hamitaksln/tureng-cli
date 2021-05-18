"""
Usage:
tureng.py tr <word>
tureng.py en <word>

-h --help help

"""
from docopt import docopt
from tureng_cli.get_tureng import get_word_list
from tureng_cli import __version__

def main():
    args = docopt(__doc__,version=__version__)
    
    word_type = ""
    word = args['<word>']
    if bool(args['tr']):
        word_type = "tr"
    if bool(args['en']):
        word_type = "en"
    
    word_list = get_word_list(word, word_type)[:10]
    print(f"Word: {word} Language: {word_type}\n{'-'*40}")
    for word in word_list:
        print(word)
    