dictionary = {
    'lit':'',
    'rn':'',
    'l_ratio':'<',
    'ratio':'>',
    'fake': 'None',
    'nocap':'True',
    'cap':'False',
    'bruh':'def',
    'zesty vibe_check':'elif',
    'zesty':'else',
    'vibe_check':'if',
    'yall':'for',
    'vent':'while',
    'workout':'+=',
    'cheat_day':'-=',
    'l_rizz':'/=',
    'no_rizz':'//=',
    'rizz':'*=',
    'fuck_around':'try',
    'find_out':'except',
    'yapper':'sys',
    'timer':'time',
    'holup':'delay',
    'touch_grass':'exit',
    'slay':'import',
    'be':'=',
    'valid':'==',
    'invalid':'!=',
    'yapfest':'str',
    'nerd_num':'float',
    'nerd':'math',
    'num':'int',
    'waffle': 'print',
    'simp': 'input',
    'clap_back': 'return',
    'yap': 'yield',
    'gaslight': 'assert',
    'iykyk': 'nonlocal',
    'main_character': 'global',
}

from re import search
from sys import argv

def tokener(sentence):
    split_value = []
    tmp = ''
    cansplit = True
    for c in sentence:
        if c == '"' or c == "'":
            cansplit = False if cansplit else True
        if c == ' ' and cansplit:
            split_value.append(tmp)
            tmp = ''
        elif c in ['(', ')', '{', '}', '[', ']', ':', '>', '<', '/', '-', '|', '&', '^', '%', '$', '!', '=', '+', '.']:
            split_value.append(tmp)
            tmp = ''
            split_value.append(c)
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    return split_value

fin = open(argv[1], "r")
out = ""
for i in fin.readlines():
    spaces = len(i) - len(i.lstrip())
    j = ' ' * spaces
    for token in tokener(i.strip()):
        if token != 'lit':
            try:
                j += dictionary[token] + ' '
            except KeyError:
                j += token + ' '
    else_if = search('else if', j)
    if else_if:
        j = j.replace('else if', 'elif')
    j += '\n'
    out += j
    #print(j, end='')
exec(out)
