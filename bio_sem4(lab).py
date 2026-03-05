from Bio import Entrez # entrez connects to ncbi
Entrez.email = "punyashrinag.sonu@gmail.com"
Gene = Entrez.efetch(db = "nucleotide", id = "EU498707", rettype = "fasta")
print(Gene.read())

from Bio import Entrez
Entrez.email = "punyashrinag.sonu@gmail.com"
info = Entrez.esearch(db="pubmed", term= "Malaria")
print(Entrez.read(info))

# DNA / RNA / Protein Sequence Generation
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
record1 = SeqRecord(Seq("VIVEKKESHRIREVA"),id = "WS_1111.1", name="VIVEKPROTEIN", description="toxic protein")
record2 = SeqRecord(Seq("ATGCATGCATGC"), id = "TEST001", name="VIVEKGENE", description="toxic gene")
record3 = SeqRecord(Seq("AUGCAUGCAUGC"), id = "TEST002", name="VIVEKRNA", description="toxic RNA")
print(record1.format("fasta"))
print(record2.format("fasta"))
print(record3.format("fasta"))

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Seq import MutableSeq
my_dna1 = Seq("ACGTTT")
print("my_dna1:", my_dna1)
#my_dna1[0] = "T"
#print(my_dna1)
my_dna2 = MutableSeq("ACGTTT")
print("my_dna2:", my_dna2)
my_dna2[0]= "T"
print("my_dna2_MutableSeq:", my_dna2)


record1 = SeqRecord(Seq("VIVEKKESHRIREVA"), id = "WS_1111.1", name="VIVEKGENE", description="toxic protein")
print(record1.format("fasta"))
print(len(record1))