from Bio import Entrez
Entrez.email = "punyashrinag.sonu@gmail.com"
Gene = Entrez.efetch(db = "nucleotide", id = "EU498707", rettype = "fasta")
print(Gene.read())