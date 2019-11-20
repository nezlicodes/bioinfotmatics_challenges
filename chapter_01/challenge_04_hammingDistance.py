def hammingDistance(str1, str2):
    mismatches = 0;
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            mismatches +=1;
    return mismatches
print(hammingDistance('3234fsdfs', '3234fsdfs'))