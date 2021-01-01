def dna_to_rna(dna_seq):
  rna = dna_seq.replace('T', 'U')
  return rna
# the above function replaces every T in the seq with a U, thus coverting the sequence to its RNA counterpart
print("Enter a DNA Sequence")
input_DNA = input()
print(dna_to_rna(input_DNA))