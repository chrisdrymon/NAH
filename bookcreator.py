from pathlib import Path

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
    bookstring = 'NA28-{:02}-{}.txt'.format(i, book)
    Path(bookstring).touch()
    i += 1
