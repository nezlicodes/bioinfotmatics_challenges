#Count the number of times a pattern repeats in a DNA seq
import re;
def count(text, pattern):
    return re.subn(pattern, '', text, flags=re.IGNORECASE)[1]

print(count('ACAACTATGCATACTATCGGGAACTATCCT' , 'ACTAT'))