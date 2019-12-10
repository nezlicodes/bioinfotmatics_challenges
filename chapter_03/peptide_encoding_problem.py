import translate_rna;

file = open('dnaSeq.txt')
dnaSeq = file.read()
file.close();

STANDARD_GENETIC_CODE = {
'UUU':'Phe', 'UUC':'Phe','UAU':'Tyr', 'UAC':'Tyr',
'UUA':'Leu', 'UCA':'Ser','UUG':'Leu', 'UCG':'Ser',
'CUU':'Leu', 'CUC':'Leu','CAU':'His', 'CAC':'His',
'CUA':'Leu', 'CUG':'Leu','CAA':'Gln', 'CAG':'Gln',
'AUU':'Ile', 'AUC':'Ile','AAU':'Asn', 'AAC':'Asn',
'AUA':'Ile', 'ACA':'Thr','AUG':'Met', 'ACG':'Thr',
'GUU':'Val', 'GUC':'Val','GAU':'Asp', 'GAC':'Asp',
'GUA':'Val', 'GUG':'Val','GAA':'Glu', 'GAG':'Glu',
'UCU':'Ser','UGU':'Cys','UAA':None,  'UAG':None,
'CCU':'Pro','CGU':'Arg','CCA':'Pro','CGA':'Arg',
'ACU':'Thr','AGU':'Ser','AAA':'Lys','AAG':'Lys',
'GCU':'Ala','GGU':'Gly','GCA':'Ala','GGA':'Gly',
'UCC':'Ser','UGC':'Cys','UGA':None,'UGG':'Trp',
'CCC':'Pro','CGC':'Arg','CCG':'Pro','CGG':'Arg',
'ACC':'Thr','AGC':'Ser','AGA':'Arg','AGG':'Arg',
'GCC':'Ala','GGC':'Gly','GCG':'Ala','GGG':'Gly'}

def transcript_dna(seq):
    rna_seq = seq.replace('T', 'U');
    return rna_seq

def peptide_encoding(dnaSeq, aa):
    j = 0
    limit = (len(aa) * 3) + 3
    while j+limit < len(dnaSeq):
        fragment = dnaSeq[j:j+limit]
        if (translate_rna.tranlateRNA(fragment) == aa):
            print(fragment)
        j += 1

print(peptide_encoding(dnaSeq, 'KEVFEPHYY'))