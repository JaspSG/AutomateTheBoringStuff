#! python3
#mclip.py - A multi-clipboard program

import sys, pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2: #Check for existence of command line arg
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase, [0] is the file name mclip.py.

if (keyphrase in TEXT):
    pyperclip.copy(TEXT[keyphrase])
    print ('Text for: ' + keyphrase + ' copied to clipboard.')
else:
    print('Keyphrase not found')
