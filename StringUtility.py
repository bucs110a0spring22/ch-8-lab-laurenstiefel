
class StringUtility:
  def __init__(self,string):
    self.word= string
  def __str__(self):
    return self.word
  
  def vowels(self):
    vowels ="aeiouAEIOU"
    vowelcount=0
    for c in self.word:
      if c in vowels:
 
      
        vowelcount= vowelcount+1
        if vowelcount > 4:
          return "many"
    return str(vowelcount)
  '''''This function counts the number of vowels in the strings and returns the number if it is less than 4. If it is greater than 4, it returns 'many'.
	args: self, vowels
	return: either the number of strings or the word many'''''
  def bothEnds(self):
    
    for c in self.word:
      
      if len(self.word) > 2:
        letter = self.word[0],self.word[1], self.word[-2],self.word[-1]
        string=''.join(letter)
        return string
      else: 
        return ""
    '''''This function prints the first and last two letters of each string. If the string is less than 2 letters it prints an empty string.
	args: self
	return: either the first 2 and last 2 letter of a string on an empty string'''''     
  def fixStart(self):
    if len(self.word) <= 1 :
      return self.word

    firstChar = self.word[0]
    result = [firstChar]
    for i in range(1, len(self.word)):
      if (self.word[i] == firstChar):
        result.append('*')
      else:
        result.append(self.word[i])

    
    resultString = ""
    for i in result:
      resultString += i

    return resultString  
  '''''This function replaces the second or greater appearences in a word with *s.
	args: self
	return: the resulting string with the *s'''''
  def asciiSum(self):
    li=[] 
    li[:0]=self.word 
    print (li)
    result=[]
    for i in range(len(li)):
      result.append(ord(li[i]))
      result = list(set(result))
    print(result)   
    final=sum(result) 
    return final
    
  '''''This function creates a sum of all the ascii values in the strings
	args: self
	return: final sum of integers'''''
  
  def cipher(self):
      cipher = ""
      for i in self.word:
        if i.isalpha():
          if i.isupper():
            alphabet = (ord(i) - 65 + len(self.word)) % (26)
            alphabet += 65
          if i.islower():
            alphabet = (ord(i) - 97 + len(self.word)) % (26)
            alphabet += 97
            letter = chr(alphabet)
        else:
          letter = i
          cipher += letter
      return cipher
  '''''This function shift the letters in a word by the number of letters in the word'.
	args: self
	return: the adjusted word'''''