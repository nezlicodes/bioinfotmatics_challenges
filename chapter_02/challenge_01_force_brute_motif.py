import re;

def count(text, pattern):
    return re.subn(pattern, '', text, flags=re.IGNORECASE)[1]

def hammingDistance(str1, str2):
    mismatches = 0;
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            mismatches +=1;
    return mismatches

def motif_enumeration(dna, k):
    mismatch = 0
    end = len(k)
    for i in range(len(dna)):
        read = dna[i:end]
        for j in range(len(read)):
            if(dna[j] != k[j]):
                mismatch +=1;
    return mismatch;
print(motif_enumeration('atgcatctatagatatat', 'atat'))