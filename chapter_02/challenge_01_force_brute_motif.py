import re;

def find_motif(dna, k):
    first = k[0]
    end = k[-1]
    for i in range(len(dna)):
        fragment = dna[i:]
        return re.search(r"(^a?t$)", dna[0:2])
print(find_motif('atgcatctatagatatat', 'atat'))