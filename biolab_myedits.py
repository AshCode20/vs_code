from Bio import Entrez # entrez connects to ncbi
Entrez.email = "punyashrinag.sonu@gmail.com"
Gene1 = Entrez.efetch(db = "nucleotide", id = "EU498707", rettype = "fasta")
    # efetch - fetches data [db:database name, id:accession no, rettype: format type(eg fasta), retmode: format mode(eg text, xml), restart: starting record, retmax: number of records]
print(Gene1.read())
Gene2 = Entrez.esearch(db = "nucleotide", term = "newborn jaundice", retmax = "3")
print(Gene2.read())
