#Tokenization of paragraph/sentances

#Every text preprocessing will be done by nltk library..
import nltk


from nltk.stem import PorterStemmer

#in paragraph you will see the words like of, the, from, and, our, them this kind of words are repeating again and again, and these words are not playing a better role
#when we are handling positive and negative anlysis so STOPWORDS is helps us to remove these kind of words in english.
from nltk.corpus import stopwords

#After importing nltk we need to download  all the library inside nltk -- It will dowloaded at particular server index index -- https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
# The download directory is -- C:\Users\Administrator\AppData\Roaming\nltk_data
nltk.download()

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""

#We have to convert this paragraph to sentances
#sent_tokenize() is a method takes paragraph and it applies regular expression inside that function... THis function is responsible to convert the paragraph into sentances
sentances = nltk.sent_tokenize(paragraph)

#to print the stopwords in english
#print(stopwords.words('english'))

#create the object of the PorterStemmer()
stemmer = PorterStemmer()

#Stemming
#range of for loop is 1 to 31 for this specific example
for i in range(len(sentances)):
    #this is for convert the sentance into words
    words = nltk.word_tokenize(sentances[i])

    #stemming(temmer.stem(words)) will be done if the condition of for loop (for word in words if word not in set(stopwords.words('english'))
    #below is known as list comprehension
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]

    #after doing stemming will join the words in sentances.
    sentances[i] = ' '.join(words)





print(sentances)
#Tokenizing words
#words = nltk.word_tokenize(paragraph)
#print(words)
