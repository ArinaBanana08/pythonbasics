word = input()
vowels = list('aeiouy')


while word != 'quit!':
  if len(word) > 4:
    for i in range(1, len(word)):
      if (word[i] == 'r') and (word[i-1] == 'o') and (word[i-2] not in vowels):
        word = word[:i]+'u'+ word[i:]
  print(word)
  word = input()