"""from Bio import Entrez # entrez connects to ncbi
Entrez.email = "punyashrinag.sonu@gmail.com"
Gene1 = Entrez.efetch(db = "nucleotide", id = "EU498707", rettype = "fasta")
    # efetch - fetches data [db:database name, id:accession no, rettype: format type(eg fasta), retmode: format mode(eg text, xml), restart: starting record, retmax: number of records]
print(Gene1.read())
Gene2 = Entrez.esearch(db = "nucleotide", term = "newborn jaundice", retmax = "3")
print(Gene2.read())"""

# Program demonstrating DNA sequence editing using MutableSeq in Biopython
from Bio.Seq import MutableSeq


sequence = MutableSeq("ATTGACTTGCATCGCATCGACTCGACTCGACTACG")
print("original sequence:")
print(sequence)

#inserting a nucleotide
def baseSubs_nucl(sequence):
    print("Performing base substitution:")
    position = int(input ("enter the position"))
    new_base = input("enter the new base")
    sequence[position - 1] = new_base.upper()
    return sequence
#print(baseSubs_nucl(sequence))

#insertion
def insert_nucl(sequence):
    print("Performing insertion:")
    position = int(input ("enter the position"))
    new_base = input("enter the new base")
    sequence.insert(position, new_base.upper())
    return sequence
#print(insert_nucl(sequence))

#deletion
def deletion_nucl(sequence):
    print("Performing deletion")
    position = int(input ("enter the position"))
    new_sequence = sequence[ : position] + sequence[position+1 : ]
    return new_sequence
#print(deletion_nucl(sequence))

def complement_nucl(sequence):
    print("Finding complements:")
    complement_sequence = ""
    for base in sequence:
        if base == 'A':
            complement_sequence = complement_sequence + 'T'
        elif base == 'T':
            complement_sequence = complement_sequence + 'A'
        elif base == 'G':
            complement_sequence = complement_sequence + 'C'
        else:
            complement_sequence = complement_sequence + 'G'
    return complement_sequence
print(complement_nucl(sequence))
complement_nucl_variable = complement_nucl(sequence)

def reverse_complement(sequence, complement_nucl_variable):
    print("Reverse complement:")
    reverse = sequence[ : : -1]
    return reverse
print(reverse_complement(sequence, complement_nucl_variable ))







    



