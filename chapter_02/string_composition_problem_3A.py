def composition_n(DNA):
    frg = []
    for i in range(len(DNA) -2):
        frg.append(DNA[i:i+3])
    return sorted(frg)

print(composition_n('TATGGGGTGC'));