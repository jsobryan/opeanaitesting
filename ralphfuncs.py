import re
import random
import nltk
from ralphlists import *
from ralphprompts import *
import inflect


p = inflect.engine()
def pluralize(x):
    plural_items = [p.plural(item) for item in x]
    return plural_items

def randthing(x):
    return random.choice(x)

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text


#   def text_cleaner(text, cleaners: list[str]):
#   for string in cleaners:
#       text = re.sub(string, text)
#   text = " ".join(text.split())
#   return text

def readfile(file_name):
    with open(file_name) as f:
        content = f.read()
        return content

file_list = ['corpse.txt', 'poemfodder2.txt', '36cannibals.txt', 'corpse.txt']

def randnoun(textsource):
    source = readfile(textsource)
    tokens = nltk.word_tokenize(source)
    pos_tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in pos_tags if pos.startswith('NN')]
    return(random.choice(nouns))

def generate_text(text):
    with open(text, 'r') as file:
         contents = file.read()
         words = contents.split()

    max_number = len(words)
    max_difference = 2000

    x = random.randint(1, round((max_number/2)))
    y = random.randint(x+100,x + 1000)
    newtext = ' '.join(words[x:y])
    return(f'{newtext}')


def randtext():
    x = random.choice(file_list)
    return generate_text(x)

def rant(story):
    return story + " The response will be given in the form of a lengthy, rambling, incoherent, psychotic rant made of unique, non-repeating text"


def randpres():
    random_pres = randthing(preslist)
    return random_pres

def hallucinations():
    hallucinations = ["Satan","John Madden","corn dogs","meat","dildos"]
    hallucinations.append(randpres())
    return random.choice(hallucinations)

def randnum():
    return random.randint(1,11)

def readfile(file_name):
    with open(file_name) as f:
        content = f.read()
        return content

def bandname(textsource):
    number = randnum()
    source = readfile(textsource)
    tokens = nltk.word_tokenize(source)
    pos_tags = nltk.pos_tag(tokens)
    adjectives = [word for word, pos in pos_tags if pos.startswith('JJ')]
    nouns = [word for word, pos in pos_tags if pos.startswith('NN')]
    if number % 2 == 0:
        x = (f'The {random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()}')
    else:
        x = (f'{random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()}')
    return x

def replace_text(textsource, outputfile):
    number = randnum()
    with open(textsource, 'r') as f:
        source = f.read()
    tokens = nltk.word_tokenize(source)
    pos_tags = nltk.pos_tag(tokens)
    adjectives = [word for word, pos in pos_tags if pos.startswith('JJ')]
    nouns = [word for word, pos in pos_tags if pos.startswith('NN')]
    random_adjective = random.choice(adjectives)
    random_noun = random.choice(nouns)

    new_tokens = []
    for word, pos in pos_tags:
        if pos.startswith('JJ'):
            new_tokens.append(random_adjective)
        elif pos.startswith('NN'):
            new_tokens.append(random_noun)
        else:
            new_tokens.append(word)

    new_text = ' '.join(new_tokens)

    with open(outputfile, 'w') as f:
        f.write(new_text)

    return new_text

for item in old_barn_items:
    ralph_items.append(item)




