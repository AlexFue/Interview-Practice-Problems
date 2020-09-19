Problem:
Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

For example:

word_split('themanran',['the','ran','man'])
['the', 'man', 'ran']

word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
['i', 'love', 'dogs', 'John']

word_split('themanran',['clown','ran','man'])
[]




Solution:
def word_split(phrase,list_of_words, output = None):
  if not output:
    output = []
  for word in list_of_words:
    if phrase.startswith(word):
      output.append(word)
      return word_split(phrase[len(word):], list_of_words, output)
  return output




Process:
There are many ways to approach this problem but the way we are going to be doing is checking all the words in list_of_words and seeing if phrase starts with them, keeping track if it does. 
We want to initialze a list so we do that only when output = none, here is where we will store the answers 
Once we initialze a list, we can then start by checking the phrase with each word in the list by using startswith()
startswith() is a python function that literally checks if it starts with a certain string, basically trying finding a substring in it and it returns a bool. 
so we use that to see if phrase starts with one of the list_of_words and if it does, we add it to the array.
we then use recursion and send the rest of the phrase (without the word we found in it), back into the function to check for even more words and put them in the output list also 
once we find no more words in the phrase, we return the output

