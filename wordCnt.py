#title = wrdCnt
#import file, count qty of words and provide frequency of each occurence for each word.

#open file, handle edge cases:
fname = raw_input('Enter File Name: ')

if len(fname) == 0: fname = 'words.tggxt'

try:
    fhand = open(fname)

except:
    print 'This', fname, 'did not work.'
    quit()

#work space:
import string

counts = dict()

#print prepositions #test

for line in fhand:
    line = line.rstrip()  
    line = line.translate(None, string.punctuation)
    line = line.translate(None, string.digits)
    line = line.lower()
    line = line.split()
    wrds = line
    for wrd in wrds:
        counts[wrd]=counts.get(wrd,0) + 1

#print counts.items() #test

lettercounts = sorted( [ (cnt, wrd) for wrd,cnt in counts.items() ], reverse = True)

#print lettercounts #test
cnt_ltr_freq = list()
totalcounts = 0

for cnt, wrd in lettercounts:
    totalcounts += cnt

print 'The total number occurrences of all words in this file: ', totalcounts

for cnt, wrd in lettercounts:
    freq = float(cnt) / float(totalcounts)
    cnt_ltr_freq.append ([wrd,cnt,float(freq * 100)])
    
for x in cnt_ltr_freq:
    print x[0], x[1], round(x[2],2), '%'