"""This script prompts a user to enter a message to encode or decode
   using a classic Caeser shift substitution (3 letter shift)"""

import sys

WORD_DICT = {}

def read_words(length):
    word_file = open("/usr/share/dict/words", "r")
    for line in word_file:
        line = line.strip().lower()
        if len(line) == length:
            add_to_graph(line)

def is_similar(word, word_two):
    difference = sum([word[i] != word_two[i] for i in range(len(word))])
    if difference == 1:
        return True
    else:
        return False

def add_to_graph(word):
    similar = set()
    for key in WORD_DICT:
        if is_similar(key, word):
            similar.add(key)
            if word not in WORD_DICT[key]:
                WORD_DICT[key].add(word)
    WORD_DICT[word] = similar

def find_path(start, end):
    visited, path = set(), [start]
    while path:
        next_word = path.pop(0)
        if next_word == end or end in WORD_DICT[next_word]:
            visited.add(next_word)
            return visited
        elif next_word not in visited:
            visited.add(next_word)
            path.extend(WORD_DICT[next_word]-visited)
    return visited

if len(sys.argv) != 3:
    print """Invalid arguments: Usage is ./search <start word> <end word>"""
    sys.exit(0)

if len(sys.argv[1]) != len(sys.argv[2]):
    print """Both words must be same length."""
    sys.exit(0)

read_words(len(sys.argv[1]))
print find_path(sys.argv[1], sys.argv[2])
