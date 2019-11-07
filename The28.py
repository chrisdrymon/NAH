from bs4 import BeautifulSoup
import requests

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
    hyperlink = 'https://www.nestle-aland.com/en/read-na28-online/text/bibeltext/lesen/stelle/{}/'.format(i+49)

    # reset the chapter list for each book
    chapList = []

    # for each book, open the book file
    bookString = 'NA28-{:02}-{}.txt'.format(i, book)
    file = open(bookString, 'w')

    # make the soup
    source = requests.get(hyperlink).text
    soup = BeautifulSoup(source, 'lxml')
    chapters = soup.find('ul', id='chapterNav')
    chaps = chapters.findAll('a')

    # for each book, grab each individual chapter URL and store them in chapList
    for link in chaps:
        chapList.append(link.attrs['href'])

    # go to URL for each chapter in each book, grab the text of the chapter
    for chapter in chapList:
        source = requests.get(chapter).text
        soup = BeautifulSoup(source, 'lxml')
        chapterText = soup.findAll('div', class_='markdown')

        # write each chapter to the book file
        for passage in chapterText:
            file.write(passage.text)

    # close the files
    file.close()

    # update
    print(bookString, 'complete.')

    # iterate
    i += 1


