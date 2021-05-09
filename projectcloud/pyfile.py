f=open('book1.txt','rt',encoding="utf8")
book1=f.read()
f.close()
f2=open('book2.txt','rt',encoding="utf8")
book2 = f2.read()
f2.close()
import string
word=book1.split()
table = str.maketrans( '','',string.punctuation)
book1= [w.translate(table) for w in word]
word2=book2.split()
book2= [w.translate(table) for w in word2]
book1=[word.lower() for word in book1]
book2=[word.lower() for word in book2]
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words2 = set(stopwords.words('english'))
book1 = [w for w in book1 if not w in stop_words2]
c=0
for x in set(book1):
    for y in set(book2):
        if x==y and x!='' and y!='' :
            print(x)
            c=c+1
            
print(c)
