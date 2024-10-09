# How to apply ML in NLP

## What's NLP
NLP is a field that involves Artificial Inteligence and CS, the goal is to process language, so computers can understand. It has so many application: email filters, smart assistents, search results [1](https://www.tableau.com/learn/articles/natural-language-processing-examples)

## How to use NLP with ML
To use NLP with ML we need to apply some techiniques, the point is to encoded text and make it understanble for machines.


### Clean Data
The single most important thing about working with raw text is to clean it to apply another techiniques as BOW and tf-idf. It imples:

- remove HTML
- remove emoticon
- etc

### Bag Of Words
Since ML models don't like to work with messy data, Bag Of Words (BOW)  is a techinique that consist in count the frequency of each word in a sentence, this way we create a vector from it., we call this multiplicity, the down side is that all syntaxe is lost but it helps encode text so the machine can understand and learn from it.

BOW works based on two fundamentals premisses

- know vocab
- count it

For exemple, let's see in practice what BOW does.

I like water
I like cake
I like life

Vocab.

'I', 
'like',
'water' 
'cake'
'life'

Each line is a document and the three line the corpus of text.Let's count the occurance based on our vocab in each document.

- i like water  = [1, 1, 0, 0]
- i like cake = [1, 1, 0, 1, 0]
- i like life  = [1, 1, 0, 0, 1]

### tfdif
Some words will apperar more than other, but it doesn't mean that they are more relevant, we need a techinique to downweight these words, one of them is td-idf.

### Tokenization
We apply tokenization to remove space and split the raw text. Or You could use more sophistichated techinique as Stemmer, that transforms the words for it root form.
- e.g running > runner.

### Stop Words
Stop Words eliminate unecessary words from our text and that has little of none meaning.

## References
- https://en.wikipedia.org/wiki/Bag-of-words_model
- https://machinelearningmastery.com/gentle-introduction-bag-words-model/
