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

def tranlateRNA(rnaSeq):
    proteinSeq = '';
    i = 0;
    while i+3 < len(rnaSeq):
        codon = rnaSeq[i:i+3]
        peptide = STANDARD_GENETIC_CODE[codon]
        if peptide is None:
            break;
        proteinSeq += peptide
        i +=3;
    return proteinSeq;

print(tranlateRNA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'));
