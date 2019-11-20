import re;
from collections import Counter;

#Find most frequent k-mer in a given sequence
def mostFrequentWord(text, k):
    # get all words in text of length k
    limit = k -1
    text = text.lower()
    k_mers = []
    for i in range((len(text))-limit):
        k_mers.append(text[i:i+k])
    #Find most frequent k_mer
    return(Counter(k_mers).most_common(1)[0])

mostFrequentWord('atcaatgatcaacgttaaaatatatattatatatatatatataagcttctaagcATGATCAAGgtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagATGATCAAGagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaATGATCAAGctgctgctcttgatcatcgtttc',5);

## Update for clump finding problem
def clump_finding(seq, k):
    return "{} ({}, {})clump".format(mostFrequentWord(seq, k)[0], len(seq),mostFrequentWord(seq, k)[1])
print(clump_finding('gatcagcataagggtccCTGCAATGCATGACAAGCCTGCAGTtgttttac', 4))