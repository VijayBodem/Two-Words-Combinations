word = input().split()  # raju plays cricket
word.sort()
#print(word)
length = len(word)
list_ = []
for i in range(length):
    for j in range(i+1,length):
        three_words = word[i] + " " + word[j] 
        list_.append(three_words)
set_words = list(set(list_))
#print(set_words)
set_words.sort()
for i in set_words:
    print(i)

# cricket plays
#cricket raju
#plays rajuis