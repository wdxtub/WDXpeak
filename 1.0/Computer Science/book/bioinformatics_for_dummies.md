# Bioinformatics For Dummies

Jean-Michel Claverie and Cedric Notredame walks us through the tools and techniques of
bioinformatics.

# Finding Out What Bioinformatics Can Do For You

This chapter explained some biology basics such as nucleotides and amino acids. It also glosses over
sub-fields of bioinformatics:

* analyzing protein sequences (amino acids)
* analyzing DNA sequences (nucleotides)
* analyzing RNA sequences
* coding DNA to protein
* genomics

Some keywords and ideas are explained in this chapter that will be used throughout the rest of the
book.

Biological experiments were done **in vivo** or within a living organism. Eventually they began
experimenting **in vitro** or within an artificial environment (Latin for in glass). With
bioinformatics, part of the experiment can be done **in silico** or within silicon chips. Wet lab
work still needs to be done for emperical evidence, but bioinformatics lets you narrow down the
hypothesis of experiments.

**Proteins** are the worker macromolecules of cells. They're built from **amino acids**. Each amino
acid (sometimes called **residue**) has a 1-letter and 3-letter code that represents it. There are
20 amino acids in nature.

Amino acids are joined by **peptide bonds** which form from an `NH2` and `COOH` on each amino acid.
There will be an unused `NH2` and `COOH` on the first and last amino acid of the chain. These are
called the `N-terminus` and `C-terminus` of the protein chain. We typically read amino acid
sequences from N-terminus to C-terminus. Here's an example sequence:

    MAVLD
    Met-Ala-Val-Leu-Asp
    Methionine-Alanine-Valine-Leucine-Aspartic

Amino acid chains or proteins form 3D structures in our cells. The structure is dependent on the
sequence (some residues are hydrophobic and want to stay inside, others are hydrophillic and want to
be outside). The electrical charges of the amino acids also affect the structure. The function of a
protein is a consequence of its 3D structure:

    SEQUENCE => STRUCTURE => FUNCTION

**DNA or deoxyribonucleic acid** is another macromolecule in our cells. They're made up of
**nucleotides** which are represented by a set of four letters:

* A for Adenine
* C for Cytosine
* T for Thymine
* G for Guanine

DNA has "hooks" like amino acids known as the 5' phosphoryl and 3' hydroxyl. We read DNA from the 5'
to 3' positions. DNA takes the shape of a double helix. It has two complementary strands. For more
information about DNA, check out my notes in *Molecular Biology for Dummies* or *Khan Academy:
Biology*.

**RNA or ribonucleic acid** is transcribed from DNA and used to make proteins. RNA differs from DNA
by one nucleotide and is usually single stranded. Just switch out the `T` with a `U` for Uracil.
Single-stranded RNA typically forms hairpin structures with itself made of loops (unpaired region)
and stems (paired regions).

Some keywords for nucleotides:

* base, base pair, nucleoside, and nucleotides all slightly differ in definition but usually
  indicate the length of a sequence (ie 5 base pairs in length)
* nt stands for nucleotide
* bp stands for base pair
* kb (kilo-base) stands for 1000 bp
* Mb (mega-base) stands for 1 million bp

A DNA sequence can be translated to a protein sequence. Each three nucleotides (**triplet** or
**codon**) will be translated into one amino acid. There are three different ways to translate them
because of triplets (known as **reading frames**). Since there are two strands, there are six
possible reading frames for DNA. An **open reading frame** is a sequence that is missing a STOP
codon.

We used to sequence DNA by concentrating on individual genes. Now, we sequence the entire **genome**
of an organism. Studying the genome as a whole is called **genomics**. We sequence and discover what
genes do at the same time.

# How Most People Use Bioinformatics

In this chapter, the author shows us bioinformatics tools to find information like:

* medical information on any biological subject
* protein/DNA sequences
* sequence comparison and alignment

**PubMed** is a database of medical related articles. It's useful for references and bibliographic
resources. We'll start off by searching PubMed for the `dUTPase` protein:

1. Go to <http://www.ncbi.nlm.nih.gov/sites/entrez?db=pubmed>
2. Search PubMed for `dUTPase`
3. Click on any of the results to learn more about the protein.

The search box isn't just limited to topics. You can also search by author name. You can narrow down
your search results using fields:

1. Click the Display drop-down menu and choose MEDLINE
2. Use each field to narrow your search. There's TI for title, AB for abstracts, AD for lab address,
   AU for authors, and SO for journal.

You can use fields in the main search box by placing the field abbreviation in square brackets.
Here's how to search for the topic `duTPase` with the lab address in Chicago:

    dUTPase [TIAB] Chiago [AD]

You can also specify ranges or **limits** to your search fields. A good example is limiting your
search to recently review articles:

1. Search for `dUTPase`
2. On results page, click on the Limits tab
3. For "Type of Article" choose "Review"
4. Click "Go"

**ExPASy** is a site for protein information. It provides a database of information and tools for
protein analysis. Let's find the protein sequence of `dUTPase` in E. coli:

1. Go to <http://www.expasy.org/sport/> (the Swiss-Prot database)
2. Search for `dUTPase coli`
3. Click on a result
4. Click the FASTA format link to get the sequence

The result page is broken up into four parts. The top has the **primary accession number** and is a
unique identifier for this protein. The next section has a biochemical description of the protein
and a list of bibliographic references. The next section is a series of links to functional
classification schemes. Finally, the sequence section provides the actual amino acid sequence.

To do an advanced search of the Swiss-Prot database:

1. Go to <http://www.expasy.org/sprot/>
2. Click "Advanced Search in the UniProt Knowledgebase" link
3. Type `dUTPase` in the Description field, choose baker's yeast for Organism
4. Submit the form

To retrieve a list of related protein sequences:

1. Go to <http://www.expasy.org/sprot/> then go to Advanced Search in UniProt
2. Keep Swiss-Prot checked but deselect the TrEMBL box. The TrEMBL database is made of unsupervised
   translations of new DNA sequences while Swiss-Prot is curated by experts.
3. Search for `dUTPase`
4. On the results page, click "Select All" and then "Retrieve Sequences"

Not all DNA codes for proteins. It also includes regulatory regions and untranslated regions.
Expressed regions are called **exons** and interrupts are called **introns**. There are different
types of DNA sequences:

* primary transcript includes exons and introns
* mature transcript discards the introns
* protein-coding region is the open reading frame
* partial sequences

Let's get a DNA sequence for the coding region of a protein:

1. Go to <http://www.expasy.org/sprot/>
2. Enter the accession number `P06968` for E Coli dUTPase
3. Click the Cross-References link near top of the form. This section has links to other databases.
4. Click the "GenBank" link

The GenBank website is full of DNA information. The format consists of four parts:

1. Identifiers like accession number and locus name
2. Reference section
3. Features section like ribosome binding sites and protein coding segments (CDS)
4. Sequence section includes the nucleotides

You can save the sequence into FASTA format for use with other programs. It's available from the
Display drop-down at the top of the page.

**BLAST** is short for **Basic Local Alignment Search Tool** and is a sequence comparison tool. It
will find other proteins with sequences similar to yours. This acts like a Rosetta Stone, which will
help you identify the structure or function of your sequence by comparing it to a known sequence.

1. Go to <https://www.ncbi.nlm.nih.gov/BLAST/>
2. Click "blastp" to do a Protein-Protein BLAST
3. Select the "nr" (nonredundant) database which includes all protein sequences known to man
4. Paste a protein sequence (FASTA format works) and click "BLAST!"

If you used a known protein, the best matched protein will probably be an identical match. The
**E-Value** is a statistical score of each sequence. It represents the probability of getting a hit
on a database of the same size by chance. The lower the E-Value, the more significant the result.

You can also do multiple protein sequence alignments with ClustalW. Multiple alignments are used
for:

* identifying sequence positions for structural integrity or function
* define sequence signatures for protein families
* classify sequences and build evolutionary trees

Here's an example using the **Protein Information Resource (PIR)**:

1. Go to <http://pir.georgetown.edu>
2. Under Search/Analysis, choose Multiple Alignment
3. Paste the sequences in FASTA format
4. Click "Submit"

The results page will include a diagram of matched amino acids, functional signatures, and
phylogenetic trees.

# Using Nucleotide Sequence Databases

This chapter explores the DNA/genome databases available on the internet. The database to use is
GenBank which is maintained by:

* US National Center for Biotechnology Information (NCBI)
* European Molecular Biology Laboratory (EMBL)
* DNA Data Bank of Japan (DDBJ)

Prokaryotic gene DNA sequence are relatively easy to read. Here are the steps to find `E Coli
dUTPase gene`:

1. Go to <http://www.ncbi.nlm.nih.gov/entrez/>
2. Choose Nucleotide in the Search pull down
3. Search for `X01714` (the accession id)

The various sections of the resulting page:

* LOCUS is the locus name (arbitrary name), sequence size, molecule type, and its shape (linear or
  circular)
* DEFINITION is a short definition of the gene
* ACCESSION is a unique identifier
* VERSION has past IDs
* KEYWORDS are terms used for searching
* SOURCE is the common name of the organism
* ORGANISM is the organism host of this gene
* REFERENCE includes credits/links to relevant articles
* COMMENT is free formed miscellaneous text
* ORIGIN is the beginning of the raw sequence (ending with //)

The FEATURES table describes biological properties:

* source - specific regions of sequence
* promoter - coordinates of promoter element in sequence
* misc feature - misc coordinates
* RBS (Ribosome Binding Site) - location of last upstream element
* CDS (CoDing Segment) - location of gene's open reading frame

You can save the sequence data into FASTA format by using the menu at the top of the page.

Try searching for `AF018430`, a human gene. Some additional sections for eukaryotic genes are:

* DEFINITION includes the exon number now
* SEGMENT indicates that this particular gene is broken into segments and this particular segment is
  2 out of 4
* FEATURES this includes additional entries. The source now tells you which chromosome it comes
  from. Gene is a splicing recipe on how to reconstruct the mRNA sequence.

To find a gene without an accession number you can search for it using fields. To find the gene
above, search for:

    human [organism] AND dUTPase [Protein name]

# Using Protein and Specialized Sequence Databases

# Working with a Single DNA Sequence

# Working with a Single Protein Sequence

# Similarity Searches on Sequence Databases

# Comparing Two Sequences

# Building a Multiple Sequence Alignment

# Editing and Publishing Alignments

# Working with Protein 3D Structures

# Working with RNA

# Building Phylogenetic Trees

# Twelve Commandments for Using Servers

# Useful Bioinformatics Resources