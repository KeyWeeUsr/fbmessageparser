# py3
# pip install beautifulsoup4
import os
import sys
from os.path import join, dirname, abspath
from bs4 import BeautifulSoup

# linux \n, windows \r\n
lineend = '\r\n'
DIR =  join(dirname(abspath(__file__)), 'parsed_conversations')
if len(sys.argv) >= 2 and '--help' not in sys.argv:
    inp = sys.argv[1]
else:
    exit("Use with 'python -m fbmessageparser /path/to/messages.htm'")

# read everything as bytes and decode
try:
    input('Opening {}? Stop with Ctrl + C'.format(inp))
except EOFError:
    exit()

os.mkdir(DIR)
with open(inp, 'rb') as f:
    cont = f.read().decode('utf-8')

# split too big FB messages file by conversations
splitted = [
    '<div class="thread">' + sp if i != 0 else sp
    for i, sp in enumerate(cont.split('<div class="thread">'))
]

# parse splitted threads and create separate files
for i, part in enumerate(splitted):
    soup = BeautifulSoup(part, 'html.parser')
    threads = soup.find_all('div', attrs={'class': 'thread'})
    output = {}

    for thread in threads:
        # silly-ish fetching because of this:
        # <div class="thread">names<div class=message">etc
        thread_title = str(thread)
        thread_title = thread_title.strip(
            '<div class="thread">'
        )
        thread_title = thread_title[:thread_title.find(
             '<div class="message">'
        )]
        # always strip \r\n \n or other raw stuff
        thread_title = thread_title.strip()

        messages = []
        conversation = thread.find_all('div', attrs={'class': 'message'})
        print('Parsing conversation of length:', len(conversation))

        for message in conversation:
            author = message.find_next(
                'span', attrs={'class': 'user'}
            ).text.strip()

            time = message.find_next(
                 'span', attrs={'class': 'meta'}
            ).text.strip()

            text = message.find_next('p').text.strip()
            # replace CRLF with LF
            text = text.replace('\r\n', lineend)

            separator = '-' * len(time + ' | ' + author)
            messages.append(
                author + ' | ' + time + lineend + separator + lineend + text
            )
        output[thread_title] = (lineend * 2).join(messages)

    for out in output:
        file = join(DIR, 'conv_{}.txt'.format(str(i).zfill(4)))
        with open(file, 'wb') as f:
            f.write(out.encode('utf-8'))
            f.write(lineend.encode('utf-8'))
            f.write(b'=' * len(out))
            f.write(lineend.encode('utf-8'))
            f.write(output[out].encode('utf-8'))
