import re

def cleanhtml(raw_html):

  cleanr = re.compile('<.*?>')

  cleantext = re.sub(cleanr,'', raw_html)

  return cleantext

## Open the file with read only permit
f = open('output_deadpool.txt')
## Read the first line
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    line = f.readline()
    new = cleanhtml(line)
    print(new)
f.close()