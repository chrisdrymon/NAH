import string
booknames = ['Matthew',
'Mark',
'Luke',
'John',
'Acts',
'Romans',
'1Corinthians',
'2Corinthians',
'Galatians',
'Ephesians',
'Philippians',
'Colossians',
'1Thessalonians',
'2Thessalonians',
'1Timothy',
'2Timothy',
'Titus',
'Philemon',
'Hebrews',
'James',
'1Peter',
'2Peter',
'1John',
'2John',
'3John',
'Jude',
'Revelation']

i = 1

while i < 6:

    # for each book, open the book file
    bookString = 'NA28-{:02}-{}.txt'.format(i, booknames[i-1])
    file = open(bookString, 'r')
    strungFile = file.read()
    file.close()

    dePuNumber = str.maketrans('', '', "⸀⸁⸂·⸃;,.—01234567890")
    dePunct = str.maketrans('', '', string.punctuation)
    deEnglish = str.maketrans('', '', string.ascii_letters)

    strungFile = strungFile.translate(dePuNumber).translate(dePunct).translate(deEnglish)

    # close the files
    file = open(bookString, 'w')
    file.write(strungFile)
    file.close()

    # update
    print(bookString, 'translated.')

    # iterate
    i += 1
