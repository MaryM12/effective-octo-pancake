##Complementator
compl_dna = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
compl_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A', 'a': 'u', 'c': 'g', 'g': 'c', 'u': 'a'}
transcr = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 'u', 'c': 'g', 'g': 'c', 't': 'a'}
# create DNA or RNA complement sequence. If not stated explicitly, creates DNA
def complement(seq):
    for se in seq:
        if (se not in compl_dna) &  (se not in compl_rna):
            return "Invalid symbol(s)! Try again!"
    if 'u' in seq.lower() and 't' in seq.lower():
        return "Invalid alphabet! U in T in one sequence!" 
    elif 't' in seq.lower():
        new_letters = [compl_dna[se] for se in seq] 
        return ''.join(new_letters)
    elif 'u' in seq.lower():
        new_letters = [compl_rna[se] for se in seq] 
        return ''.join(new_letters) 
    else:
        new_letters = [compl_dna[se] for se in seq] 
        if 'a' in seq.lower():
            print("I guess it is DNA")
        return ''.join(new_letters)        
# create mRNA transcript sequence
def transcribe(seq):
    for se in seq:
        if (se not in compl_dna) &  (se not in compl_rna):
            return "Invalid symbol(s)! Try again!"
    if 'u' in seq.lower() and 't' in seq.lower():
        return "Invalid alphabet! U in T in one sequence!" 
    elif 'u' in seq.lower():
        return "Sorry, reverse transcription is not provided :("
    rna_letters = [transcr[se] for se in seq] 
    return ''.join(rna_letters)
# create reverse DNA or RNA sequence
def reverse(seq): 
    for se in seq:
        if (se not in compl_dna) &  (se not in compl_rna):
            return "Invalid symbol(s)! Try again!"
    if 'u' in seq.lower() and 't' in seq.lower():
        return "Invalid alphabet! U in T in one sequence!" 
    else:
        return ''.join(letters[::-1])

while True:
   command = str(input('Enter command: '))
   if (command != 'exit') & (command != 'complement') & (command != 'reverse complement') & (command != 'transcribe') & (command != 'reverse'):
       print('Invalid command!')
       continue
   if command == 'exit':
       print('Chao!')
       break
   letters = str(input('Enter sequence: '))
   if command == 'complement':
       print(complement(letters))
   if command == 'reverse complement':
       print(complement(letters[::-1]))
   if command == 'transcribe':
       print(transcribe(letters))
   if command == 'reverse':
       print(reverse(letters))    
