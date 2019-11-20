import re;
from collections import Counter;

#Find most frequent k-mer in a given sequence
def mostFrequentWord(text, k):
    # get all words in text of length k
    limit = k -1
    k_mers = []
    for i in range((len(text))-limit):
        k_mers.append(text[i:i+k])
    #Find most frequent k_mer
    print(Counter(k_mers).most_common(1)[0][0])

mostFrequentWord('ACAACTATGCATACTATCGGGAACTATCCT',5);
mostFrequentWord('ACTGACTCCCACCCC', 3);