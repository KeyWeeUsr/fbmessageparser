# fbmessageparser

Imagine you download an archive of all the stuff you do on Facebook with your
profile - posts, photos, even messages. Well, messages aren't saved in
a friendly format. This little script parses the messages for you from this
ugly and cluttered format:

    <html>
        <body>
            <div class="contents">
                <h1>Your Profile</h1>
                <div>
                    <!-- conversation -->
                    <div class="thread">
                        Participant 1, Participant 2, ...
                        <div class="message">
                            <div class="message_header">
                                <span class="user">User Name 1</span>
                                <span class="meta">
                                    Day, Full Date at Time Timezone
                                </span>
                            </div>
                        </div>
                        <!-- message body -->
                        <p>Hi</p>

                        <div class="message">
                            <div class="message_header">
                                <span class="user">User Name 2</span>
                                <span class="meta">
                                    Day, Full Date at Time Timezone
                                </span>
                            </div>
                        </div>
                        <!-- message body -->
                        <p>Not now</p>

                        <div class="message">
                            <div class="message_header">
                                <span class="user">User Name 1</span>
                                <span class="meta">
                                    Day, Full Date at Time Timezone
                                </span>
                            </div>
                        </div>
                        <!-- message body -->
                        <p>😂</p>

                        <div class="message">
                            <div class="message_header">
                                <span class="user">User Name 1</span>
                                <span class="meta">
                                    Day, Full Date at Time Timezone
                                </span>
                            </div>
                        </div>
                        <!-- message body: \n, sticker, ... -->
                        <p></p>
                    </div>
                    ...
                </div>
            </div>
            ...
        </body>
    </html>

to a very simple conversation files (`parsed_conversations/conv_NNNN.txt`):

    participant 1, participant 2, ...
    =================================
    User Name 1 | Day, Full Date at Time Timezone
    ---------------------------------------------
    Hi

    User Name 2 | Day, Full Date at Time Timezone
    ---------------------------------------------
    Not now

    User Name 1 | Day, Full Date at Time Timezone
    ---------------------------------------------
    😂

    User Name 1 | Day, Full Date at Time Timezone
    ---------------------------------------------
    <empty>

### But why?

* Splitting messages. It's better to split into conversation files because
  those are better to open even in an editor such as `Notepad` or likes that
  will gladly freeze if you try to open a slightly bigger file. Facebook puts
  everything into a single file with HTML clutter everywhere.

* HTML clutter means larger file. With simplifying the output I personally got
  about 20MB down of an original 60MB file. Quite insane, right? ;)

* Readability counts. Facebook dumps your messages into a single-line string
  therefore you either prettify the HTML and increase the size of the file
  massively or open the file in the browser - good luck with large files,
  you'll love the smooth scrolling - and copy-paste the conversations manually
  out of there - seriously, no one would do that.

### How to use

    pip install beautifulsoup4
    python main.py messages.htm

and all the conversations will be splitted to the separate folder
`parsed_conversations` right next to the `main.py` file.

#### Note: Python 2 is not supported
