import xml.etree.cElementTree as Et
import os

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

for book in booknames:

    # make the file names
    bookstring = 'NA28-{:02}-{}.txt'.format(i, book)
    openTextPath = os.path.join(os.getcwd(), 'OpenTextNTv1', '{:02}_{}_full.xml'.format(i, book.lower()))
    newFileName = 'OpenText-{:02}-{}.xml'.format(i, book)

    # open the files
    plainTextFile = open(bookstring, 'r')
    openTextFile = open(openTextPath, 'r')

    # parse the XML
    tree = Et.parse(openTextFile)
    root = tree.getroot()

    # make plain text a word list
    wordList = []
    for line in plainTextFile:
        for word in line.split():
            wordList.append(word)

    # iterate through opentext xml
    j = 0
    for logos in tree.iter('w'):

        # set word equal to equivalent word in plain text
        uniWord = wordList[j]
        logos.text = uniWord
        j += 1

    # close the open files
    plainTextFile.close()
    openTextFile.close()

    # iterate to next word in txt file
    i += 1

    # save the file
    tree.write(newFileName, encoding='UTF-8')
    print(newFileName, "complete.")
