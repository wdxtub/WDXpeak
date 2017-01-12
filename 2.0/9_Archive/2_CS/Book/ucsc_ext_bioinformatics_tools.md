# UCSC Extension: Bioinformatics Tools, Databases, and Methods

My notes for UCSC Extension's Bioinformatics Tools course taught by Lee Kozar. This course is an
introduction to the public domain tools and databases like GenBank, PBD, and BLAST.

The notes are in a question/answer format. They go better with the slides from lectures.

# Bioinformatics Databases

## What database do you search for info about introns in a gene?

You can use the GenBank database managed by NCBI <http://www.ncbi.nlm.nih.gov>. Search in the Genome
database, the GenBank format includes introns.

## What database do you search for genetic diseases caused by a gene?

OMIM or the Online Mendelian Inheritance in Man database can be used to search for information about
genetic diseases <http://www.ncbi.nlm.nih.gov/omim>.

## What database do you search for gene therapy information with a gene?

NCBI's Genetics & Medicine database would be a good place to search. Also, PubMed would be useful.

## What database do you search for info about polymorphic variation in a gene?

There is currently no specialized database for polymorphic variants.

## Can you use SRS to search sequence databases?

Yes, the Sequence Retrieval System was developed for that purpose.

## Can you use MeSH to search sequence databases?

No, Medical Subject Headings are strictly for medical literature purposes.

## Why are there so many bioinformatics databases?

Because each organization wants to own their own data. They each start with a question in mind and
they develop a database/format specifically to answer that question.

## If you have a sequence in GenBank format, why would you convert it to FASTA?

Not all softwares accept the GenBank format as input. You may have to convert it to FASTA to work
with it.

## Can a FASTA file hold more than one sequence?

Yes, it can hold as many sequences as you like. The format uses a `>` character as a delimiter.
Here's an example:

    >filename00    One line descriptive text
    GATACCATATACCATAGGATTCATTTA
    >filename01    One line of text
    TACTACCTTACGATCCAGGTAACTACA

## How does a computer know when a sequence starts/ends in a GenBank file?

The keyword `ORIGIN` denotes the start of a sequence and a double forward slash `//` denotes the end
of a sequence.

## Can a GenBank file hold more than one sequence?

Yes it can. Each sequence can have its own annotations like LOCUS and DEFINITION also.

## Can a sequence only file hold more than one sequence? Why/why not?

No it cannot. A sequence only file has no delimeters, just a single sequence. Since `ACTG` are the
only characters allowed, there would be no way to separate the sequences.

## What is the EST database used for?

Expressed Sequence Tags databases hold partial cDNA sequences. They're only the expressed sequences.
They're the most interesting sequences in the genome, since those are the ones being used.

## Why would you place "limits" on your search of the GenBank database?

To narrow down your search and find what you're looking for. You can specify filters like organism.

## What info is lost on conversion of GenBank sequence to FASTA?

A lot of the annotatations are lost because FASTA only contains the filename, sequence, and one line
of descriptive text. Some of the annotations that are lost include:

* Chromosome Region
* Gene Region
* What to assemble to get the mature protein

## Can that information be put back if you convert back to GenBank?

No, not unless you somehow coded for it in the single descriptive line of the FASTA file.

## What information is lost when a SwissProt file is converted to FASTA format?

The SwissProt file contains many annotations that are lost including:

* Locus
* Accession ID
* Links to other research documents
* Links to other DBs
* Organism name

# Literature Searching

## Why is MeSH useful?

The Medical Subject Headings were developed to control vocabulary. It solves the problem of having
no structured vocabulary for the large amounts of data in our databases.

The keywords from MeSH makes it easier for someone to search the database and find something
relevant.

## What are the advantages and disadvantages of a controlled vocabulary?

The advantage is that it standardizes terms. A scientist may have thought his paper was about a
certain gene, but a librarian will standardize the name so someone searching for it will find all
relevant documents.

It also limits the number of major points in an article to 3-4. Searches could turn up too many
documents - because each document may mention a keyword only once b/c it's slightly related. By
limiting it, keywords only match the document if it's a major point of the article.

Unfortunately, the keywords you want to use might not be included in the vocabulary yet. It takes a
while to enter MeSH. Also, your article may have more than 3-4 major points.

Straight from the lecture advantages:

* represent a subject concept, no synonyms needed
* find relevant articles that may not be mentioned in a title or abstract
* focus search, eliminate irrelevant records

Straight from the lecture disadvantages:

* scientific jargon not covered
* indexers may be inconsistent
* not every concept in an article can get thesaurus term

## What database do you search to find a gene given the discoverer's last name?

Use the SRS provided by EMBL <http://srs.ebi.ac.uk/srsbin/cgi-bin/wgetz?-page+srsq2+-noSession>.

One of the headers you can search by is the author's name of a paper.

## What searches can't be done at the PubMed/Medline database site?

PubMed/Medline are strictly medical databases. If what you're searching for is scientific but not
related to the medical field, it won't be there.

## What is contained in the annotation part of the sequence?

Annotations include the accession number, locus, definition, keywords, source organism, references,
authors, links to other DBs, and more.

## What is more important, annotation or sequence? Why?

The annotation is more important because it has the secondary data, such as conclusions of
experiments and links to other relevant material. The annotations give meaning to the data.

## What does "parsing" do to a database?

A computer "parses" data in order to understand it. It's easier to parse data when it's in a
standardized format - such as the headers. This makes it easy to extract data from annotations. We
can parse a flat file database.

During lecture, we also discussed NLP (Natural Language Processing). NLP can be applied to articles
for computers to parse entire articles - not just the header information. This would make indexing
extremely efficient as we could automatically index articles based entirely on their content.

## Why are relational databases better than flat file databases?

It's easier to do complex searches with relational databases and they store data more efficiently.

## What database/terms do you use to find human growth hormone protein sequence?

Use NCBI's protein database. Search for "human growth hormone". You can place the entire search term
in quotes to match the exact phrase. Or you can make your search more granular by searching for
"growth hormone" AND "homo sapien".

## How does SRS differ from NCBI Search tools?

SRS allows you to search precisely using the headers.

## Why would you place "limits" on your search of the PubMed database?

To narrow your search and find exactly what you're looking for.

# Statistics in Bioinformatics

## Why is probability and statistics important for bioinformatics?

You can separate good results from bad results using statistical inference with biological insight.
Using probability/statistics, you can ask yourself if an outcome is reasonable.

## How often would you find any dinucleotide sequence in a random sequence?

The nucleotide alphabet is made up of four letters: A, T, G, C. There are sixteen different
possibilities for any dinucleotide sequences:

    [ ] [ ]
     4 * 4 = 16

So you would expect to find any dinucleotide `1/16` times in a random sequence.

## How often would you find any tri-nucleotide sequence in a random sequence?

There are 64 different possibilities.

    [ ] [ ] [ ]
     4 * 4 * 4 = 64

So you'd epxect to find any tri-nucleotide sequence `1/64` times in a random sequence.

## Given a nucldeotide sequence with random distribution, what can you conclude?

That there's nothing particular special about the sequence. The actual average distribution of the
human genome is:

    A .295
    C .205
    G .205
    T .295

## Given a non-random distribution, what does it tell you?

That there's specific biology going on with this sequence.

## When would you use a Hidden Markov Model to analyze a sequence?

To determine if a sequence is the member of a certain family. It is a position specific scoring
matrix.

## What is information theory used for in bioinformatics?

Information theory deals with transmission of messages. Sequence data can be thought of as messages.
For example, a popular method of analyzing proteins for secondary structure uses information theory
(GOR Method).

## How often do you expect a single nucleotide to appear in a random sequence?

25% of the time because the nucleotide alphabet is made of four letters.

## Is a sequence random if the four nucleotides appear in same frequency?

Yes, if they appear in about the same frequency. The actual distribution is a little different. A's
and T's occur more often than C's and G's.

## What further tests would you do to make sure the sequence is random?

_To answer this, come up with some sequences that had the same distribution of nucleotides but was
not random._

You can start looking at di-nucleotide patterns or tri-nucleotide patterns. It could still be 1/4
but be `AAAACCCCTTTTGGGG`.

## How often would you find the cut site for HindIII in a random sequence?

The recognition site for HindIII is:

    AAGCTT

That's 6 nucleotides in length. The number of possible permutations are

## What is a sliding window technique and why is it useful?

As you change the window size, the results will also change. Patterns will start appearing. Small
windows have noisy data, larger windows are smoother.

It's used to analyze the signal in data and to help find patterns. It helps filter out the noise.

## Why is leucine the most common amino acid?

Leucine has more codons that code for it than the other amino acids. There are 20 amino acids, but
64 possibilities from triplet nucleotides.

Proteins that need to be expressed frequently will tend to have more amino acids that are frequently
expressed.

## What is a codon preference table? When would you use one?

A codon frequency table includes the frequency that a codon occurs for a human gene (and for other
species and organelle). You can use it to go backwards from knowledge of a protein to figure out the
DNA sequence, with a certain probability.

## Can the selection of a codon be used to regulate transcription rate?

Yes, some codons are more likely to be expressed than others. The gene expression could occur at the
transcription level.

## Can the selection of a codon be used to regulate gene expression?

Yes, some codons are more likely to be expressed than others.

## If you shuffle a sequence, will the single nucleotide frequencies change?

No, the frequency would stay the same. You're just getting a different permutation.

## You shuffle a sequence and di-nucleotide frequencies stay constant. Why?

Some nucleotide pairs are not randomly distributed. For instance, there could be a high probability
of getting G after a C. It's different than P(g) or just P(c).

## How is a bioinformatics experiment designed?

1. Go to the database, get training set
2. Collect data on probabilities of events
3. Calculate frequencies

## Where does the data from a bioinformatics experiment come from?

Online databases like SwissProt or GenBank.

## How do you know if a bioinformatics experiment worked?

Do a Bayesian analysis to make sure your results are "correct" to a certain degree of belief.

## What is Bayes Equation? Why is it so useful?

    P(b | a) = P(a | b) * P(b) / P(a)

This equation has four variables. You usually have access to three, so you can solve for the unknown
probability.

# Sequence Comparison

## Why compare sequences?

We sequenced the human genome, but we don't know what a lot of it does. Just like hieroglyphics, we
can compare sequences with unknown functionality to sequences whose functionality we know to learn
more.

You can answer the questions:

* is sequence A evolutionary related to sequence B?
* is there a functional relationship?

## Why compare a sequence to itself, won't that just find a perfect match?

To find internal duplications.

## Why penalize gaps? How are gaps penalized?

It'd be too easy to score high if you don't penalize gaps. For instance, one alignment with a
massive gap would score the same as a perfect alignment. Or an alignment with many tiny gaps would
score the same as a perfect alignment.

Gaps are penalized by the number of gaps and the length of each gap.

## Why do you need a scoring function?

The scoring function acts as a way to judge whether an alignment is statistically significant. It's
only useful in terms of relativeness - to tell whether one alignment is better or worse than
another.

## What is a sequence comparison matrix used for?

It's a method to assign a score to alignments. One sequence is listed on the horizontal axis and
another sequence is listed on the vertical axis. At some intersections, a score or penalty is given.
The sum of all squares is the total score of the alignment.

## Why not use an identity matrix for proteins?

For amino acids, often times you can substitute amino acids and still come up with a protein that
acts functionally the same. For nucleotides, different codons still code for the same amino acids.

## How do you know if a sequence comparison is correct?

Use statistics to tell whether it's significant or if it could have happened by random chance. You
can compare the score with other alignments. If you've only got two sequences, you could shuffle and
compute the z-score.

## What are sub-optimal alignments and why are they important?

The best alignment from a biological point of view may not be the best alignment from a
computational point of view. The sub-optimal alignments are the ones that don't result in the best
score but may have helical regions or active sites aligned better than the "optimal" alignment.

## How do you choose what sequence comparison matrix to use?

Each comparison matrix has its own goals. PAM is for evolutionary related sequences. BLOSUM uses
related protein regions instead of similar sequences. You also want to check how sensitive the
algorithm is for scoring.

## What is the goal of sequence comparison? A good alignment shows what?

The goal of sequence comparison is to determine if two sequences are related either in terms of
evolution or functionality. A good alignment means it's more likely that the two sequences are
related.

## What is the difference between similarity and homology?

Homology means evolutionary related sequences. Similarity means the sequences share certain patterns
but it's not known whether they're evolutionary related or not. Any similarity could have been by
convergent evolution.

## What is the difference between orthologs and paralogs?

Orthologs are genes in different species that derive from a common ancestor and may or may not have
the same function. Paralogs are genes within a single species that diverged by gene duplication.

## When would you use a global alignment and when would you use a local?

A global alignment is used to compare the entire specific gene on a chromosome. A local alignment is
used to find patterns in genes, so you can shuffle them left or right to find the best score.

## What are the advantages and disadvantages of a dot matrix comparison?

The dot matrix is a great visual tool that shows patterns which might otherwise be missed.
Unfortunately, there might be too much noise to discern patterns.

## What do gaps along the diagonal of a dot matrix comparison represent?

This particular position in both sequences do not match.

## How would you reduce the noise in a dot matrix alignment?

You can use the sliding window technique. Determine a window size and stringency. A high stringency
will reduce the noise. Too high will also reduce the signal.

## What do off diagonal lines represent in a dot matrix alignment?

Patterns within regions of sequences.

## Why do we use the term INDEL to describe a gap in an alignment?

INDEL stands of insertion or deletion. It's used when we don't know whether a gap is an insertion in
one sequence or a deletion in another sequence. Both satisfy the end comparison.

## What parameters in the LALIGN alignment program would you use?

_For the scenario of a computer giving you an alignment that had no gaps._

The gap penalties wouldn't matter.

## What does a negative number in the PAM sequence comparison matrix tell you?

That the amino acid isn't a good substitution and effects the functionality of the translated
protein.

## Two sequences are found to be similar, are they also homologous?

No, there might be a good chance that it's homologous but we have no idea.

## What is the best gap penalty to use?

Use a high gap penalty if you want your alignments to be strict.

## How does the software still manage to do a good job?

_You usually want an alignment program to align sequences based on evolutionary events or align
according to functional regions. However, the software doesn't know anything about the biology of
the sequences being aligned._

It uses statistics to tell you if this alignment could have happened by chance. If there's a small
chance that it could have happened randomly, you know there's some biology going on.

## How are whole genome comparisons different than small sequence comparisons?

Small sequence comparisons are useful to find motifs, or patterns, which could yield similar
functionality.

## Will a gene be on chromosome 1 of a mouse if it's on human chromosome 1?

No, genes are located on different chromosomes for different species.

## What is synteny?

Gene clusters that are on the same chromosome location in two different species.

# Multiple Alignment

## What can be learned from multiple alignments? What do they answer?

* phylogenetic trees
* finding blocks or motifs
* revealing functionality

## What further analyses can be done with the results of a multiple alignment?

A good alignment is critical for further analysis:

* functional domains, motifs, blocks
* protein families
* evolutionary analysis
* structural analysis
* secondary structure prediction

## What is the most important step in the multiple alignment process?

You need to pick related sequences.

## Why don't we use the method that guarantees best alignment?

It's too computationally expensive. It would take too long.

## How does a progressive pairwise alignment work?

1. Align A and B first
2. Then add sequence C to the previous alignment
3. Keep adding sequences, align the most closely related sequences first. Insert gaps as needed.

## What is a dendrogram? How is it used?

A dendrogram is better known as a guide tree. It's used to determined which order sequences should
be aligned (by giving scores to alignments).

## Why use a monospaced font when viewing/printing a multiple alignment?

It's easier to view alignments when each nucleotide/amino acid is properly aligned font-wise.

## How can you tell whether a multiple alignment is correct?

You use a scoring function. All scoring methods attempt to minimize the number of evolutionary
events required to describe the divergence of the sequences.

## What are some databases of multiple alignments?

* BaliBase (Reference DB)
* Profiles
* BLOCKS
* PFAM

## How can multiple alignment databases be used?

In the future, alignments won't be done from scratch. The optimized alignment will be available in
databases. New sequences will be added to existing alignments. Multiple alignment databases have
common domains and their alignments.

## What alignment algorithm does Clustal use?

Clustal uses a heuristic (rule based) alignment method: progressive alignment.

## How does the most recent version of Clustal differ from the original version?

The recent ClustalW (W stands for Weighted) gives different weights to sequences and parameters in
different parts of the alignment to try and create an alignment that makes sense biologically.
There's a large penalty for closely related sequences and a small one for divergent sequences.

## The best scored alignment might not be the correct alignment. Why?
## How is T-Coffee an improvement over other methods of multiple alignments?

T-Coffee uses clustal global alignment with local alignment and weighting to determine the best
alignment. It's slower but more accurate.

## When wouldn't you want to do a multiple alignment?

When the sequences aren't related. If the sequences include short non overlapping fragments. If
sequences do not share common ancestry. If sequences have large, variable, N- and C-terminal
overhangs.

## How would you analyze a protein with domains X,Y,Z against protein with Z,X?

Only match up the domains which are present in both proteins.

## What is a consensus sequence?

A consensus sequence is a single sequence which represents multiple ones. It's similar to an
"average". You can have different rules to define the consensus - it could be use the nucleotide
that's most common or more expected.

## What is a sequence logo?

It's an image of a sequence where the size of the individual letters depict the relative frequency
of occurrence.

## Can you use ClustalX to align only two sequences? Is ClustalX the best way?
## Should you use only one comparison matrix for the following scenario?

_You're aligning many sequences and some are evolutionary close, others are evolutionary distant._

No, you should use Clustal which will vary the table. You could use BLOSUM62 which is just the
average, but Clustal is your best tool.

## How does Clustal resolve the problem of evolutionary closeness and distance?

It uses varying tables for alignment. It stands for "Cluster Alignment". It uses pairwise
progressive alignment.

## How can you search a database using a multiple alignment? Name some methods.
## What is the best method for searching a database using a multiple alignment?

# Database Searching

## What questions can be answered using database searching?

* determine what ortholog or paralog exists for a particular protein or the gene that encodes it
* determine what proteins or genes are present in a particular organism
* determine the identity of a particular protein or DNA sequence, based on its similarity to known
  sequences
* discover new genes
* determine the published variants for a particular gene or protein sequence
* investigate the transcriptome database to identify novel splice variants
* discover which amino acid residues within an alignment are conserved

From database searching #2:

* I have just sequenced something, has someone already found it?
* I have a sequence of unknown function, is there homology with another sequence that has a known
  function?
* I found a new protein in a lower organism, is there homology in a higher species?

## How is sequence comparison different from database searching?

Sequence comparison searches for similarity, database searching searches for homologous sequences.
You assume homology with a good score for database searching.

Sequence comparison is for global alignments whereas with database searching the best local
alignments determine top scores.

Sequence comparison requires sensitivity whereas database searching the speed is of utmost
importance. Database searching includes many false positives.

## Explain the tradeoff between speed and sensitivity in database searches.
## Why would you want to give up sensitivity to achieve speed?

There's not enough computational power to have 100% sensitivity. Also, you will problem lose many
true positives.

## Can sequence comparison techniques be used to do database searches?

It's a thourough search but slow.

## Why does BLAST do a faster database search than other methods?

BLAST uses a pre-indexed database.

## When would you want to use a BLOSUM 80 comparison matrix?

To align very closely related sequences.

## When would you use the BLASTX program?

To compare a nucleotide query vs protein database.

## Which of DNA or protein sequences do you use for evolutionary distant matches?

I'd use the protein sequences because the alphabet is larger and there's not the problem that
multiple codons code for the same amino acid.

## You're searching if a specific sequence is in the DB, do parameters matter?
## What are the limitations to BLAST?

You can only search for a single query, can't do complex queries, can't search for multiple
sequences.

## How does the window size improve search speed or sensitivity?

I think it would help improve the speed because the "keyword" to use for the index is larger.

## What is an expectation value?

It's the number of sequences you would expect to find with this score (or better) if you searched
another database of the same size. 0 is a good score. 1 is a bad score.

## What is the best expectation value you can get?

Zero.

## Is an E value of 6e^-12 good or bad?

It's borderline, you'd have to use biological knowledge to rate it.

## What is a Z-score?

The number of standard deviations away from the mean.

## Will the expectation value be the same for two searches that's months apart?

No, because it's based on the size of the database.

## Why can you infer homology with a DB search, but not with sequence comparison?
## What is a false positive? What is a false negative?

False positives are non homologous results that are returned. False negatives are results that are
missing from your search which are homologous and should have been returned.

## What does the TFASTA program do?

TFASTA takes a protein sequence and compares it to a nucleotide database by translating the DNA in
all reading frames.

## Is translating DNA or backtranslating a protein better for searching? Why?

Translating a DNA because multiple codons can code for the same amino acid.

## You backtranslate protein and do a DNA search, why no good match?

Backtranslating amino acids results in multiple codons.

## GenBank has only one strand for each sequence, how do you search the opposite?

There's an option to search for complementary sequence. Or you can use a program to output the
complementary and search for that.

## Does GenBank use PAM or BLOSUM for searching DNA sequences?
## What is the value of searching a DB and looking at different reading frames?

To see different results. Since the database pre-indexes, if your frame is too large it may produce
false negatives.

## What are frame-shift mutations?

Genetic mutation caused by INDELs that's not evenly divisible by three. It results in a completely
different translation from the original.

## Can you use BLAST to do a sequence comparison with only two sequences?

No. You can only do one query.

## Why filter sequences? When would filtering not be a good idea?

Remove sequences of low complexity so you get fewer false positives. Masking uses a database of
known repeat regions whereas filtering uses an algorithm to filter regions of low complexity.

# Database Searching #2

## How does PSI-BLAST work? Why is it better than BLAST?

It builds a PSSM (Position Specific Scoring Matrix) from the first BLAST search, then uses it for
your actual search. This lets you search for sequences that are similar to a gorup of sequences
(instead of a specific query). BLAST limits you to a single sequence.

1. Run Blast
2. Select representative "hits"
3. Use hits to create a PSSM
4. Use the PSSM to search the database

## Does PSI-BLAST work with DNA?

It only works with proteins.

## Can you use BLAST to compare two sequences?

Nope, it's limited to a single sequence.

## Can you send multiple sequences to BLAST at one time?

Nope, it's limited to a single sequence.

## What is better to use as a query sequence, DNA or protein?

Protein, because there are more letters in the alphabet so less likely to have matches based on
random chance. It's easier to filter out repetitive regions.

## Give 3 examples for not translating DNA to protein before doing a DB search.

* You need the introns for some reason
* You need the regulatory DNA

## Why are pattern searches more sensitive than searching with a single sequence?
## Why is a consensus sequence not very good to represent a multiple alignment?

IT finds sequences that are very similar to the consensus, but not sequences that are still in the
family (but slightly differ from the consensus).

## Why break up long protein or nucleotide sequences before doing a DB search?

To find patterns within the sequence as opposed to a long match.

## What comparison matrix would you use to find evolutionary distance sequences?

PAM-1 or BLOSUM-100 for small evolutionary distance, PAM-400 or BLOSUM-30 for large evolutionary
distance.

## There's a new gene in humans, why find the same gene in a simpler organism?

It's much easier to do experiments in the simpler organism (ie. it's hard to do experiments on
humans!)

## What does the following mean?

_You discovered an ORF and do a DB search and find nothing statistically significant._

## What's the advantage of searching using different reading frames?
## Why is filtering a sequence useful?

To filter out the noise or filter out repetitive regions that mean nothing. Over 50% of DNA is
repetitive, keeping the DNA there will increase the chance of false negative matches during database
search.

## What does filtering do?

Filters out junk DNA, decreasing sensitivity.

# Biological Patterns

## Why is searching using a pattern created from a family of proteins better?

_Why is searching a database using a pattern created from a family of proteins a better strategy
than just searching a database with a single protein sequence that is a known member of the family
of proteins?_

We need to understand what patterns do then look for these patterns in sequences of unknown
functions. If you find a pattern of known function, you can figure out wht a protein or nucleotide
sequence can do.

## What is a motif?

Patterns in protein sequences that create a structure.

## What is a regular expression?

A concise and fliexble expression for matching strings of text aka pattern matching.

## Why should you not use a consensus sequence to search for other members?

_A consensus sequence is created from a multiple alignment of a family of related sequences, why
should you not use one to search a database for other members of the family that was used to create
the consensus?_

A consensus sequence only shows one choice at each position. It doesn't account for ambiguities.
Consensus sequences are made to reduce the amount of information. You need to be able to accoutn for
a pattern where having two or more molecules in one position are equally valid.

## Why would you ignore commonly found patterns?

_Such as described in the Prosite database._

These are repeat DNAs that don't mean anything. They don't provide any use for searching.

## What are some names of protein pattern databases?

* Prosite
* eMotif

## What is a PSSM?

Position Specific Scoring Matrix, it's a matrix of scores used to score a protein pattern. The left
axis are the amino acids. You move left to right, adding the score for each amino acid.

## Why does a PSSM do a better job of describing a pattern than other methods?

It's a more flexible search and gives specific weight to each position in a pattern.

## What are you looking for when searching a protein pattern DB with protein seq?

Proteins in the same family.

## What is more sensitive, a PSSM or a motif?

Motifs have fewer false positives, so it's more sensitive than PSSM.

## Why is Blocks better than Prosite?

Blocks of aligned sequences from highly conserved regions that have been defined by the Prosite
databases. When you compare a sequence to an entry in the BLOCKS database, the BLOCK is converted to
a PSSM.

## Why is a HMM better than a Profile PSSM?
## If two genes have the same expression pattern, what does it tell you?
## What does the following tell you?

_You do a pattern search using a protein of unknown function and find nothing significant._

## What is a sequence logo?
## You have a sequence of unknown function. What pattern DB do you search?
## How would you test out a pattern to see if it was any good?
## Describe the pattern in words.

    C-A-x-T-[K,R]-x(4)-C-H

## How do you search SwissProt for other sequences with same function, given:

_You have several protein sequences with the same function._

## Could "grep" miss a restriction site given a GenBank sequence?
## What needs to be done so "grep" can see any pattern in a GenBank file?
## Which pattern is less likely to find a match on SwissProt and why?

    G-A-L-I-V-T-S
    P-C-K-W-M-Y-H-Q

# Annotations

## What are the steps in annotating a genome?

* Identification and prediction of genes
* Characterization of gene features
* Chacterization of genome features
* Prediction of gene function
* Prediction of pathways
* Integration with known biological data
* Comparative genomics

## What is annotation?

The process of interpreting genomic sequence information, defining signal regions, open reading
frames and defining the function of the regions.

## Does sequence/variations of sequence tell you everything about effects?

_Does determining the sequence and sequence variations of a gene tell you everything about how that
gene or loss of that gene will effect the organism? Why or why not?_

No, there's still the regulatory regions.

## How does GenScan work?

GenScan uses statistical methods to annotate a gene. It compares many splice sites and uses Maximal
Dependence Decomposition (MDD) which captures dependencies between positions.

It look sfor ORFs using a variety of techniques:

* Hexamer Composition of Introns & Exons
* 5' 3' Splice Signal
* Reading Frame
* Exon-Intron length
* Promoter or Poly A signals

## Why is determining gene structure more difficult in eukaryotes than prok?

Eukaryotes have more non-coding DNA, introns/exons, repetitive regions. There are more
post-transcriptional modifications and psuedogenes.

## What genes can GenScan not find?

## GenScan isn't perfect, why doesn't it matter when trying to identify a protein?

## How do you identify a potential gene in a prokaryote?

Look for the start and stop codons in the sequence.

## How do you determine if a predicted gene is correct using computer techniques?

Search the existing databases for your gene.

## When can you not tell whether a predicted gene is correct?

Do a lab experiment. Place the gene into a plasmid and see if it gets expressed properly.

## What test determines if a genomic region is a gene for a tRNA molecule?

Looking for tRNA promoter sequences or for that cloverleaf folding pattern.

## Do you know all the genes that cause human disease? Why or why not?

_Given that we sequenced the entire human genome._

No, we still don't understand what particular sequences or variations of those sequences mean.

## You sequenced bacteria genome and want to find all genes. Do you use GenScan?

_Why or why not?_

No, it only works with vertebrates, maize, and some flower.

## You sequenced fruit fly genome and want to find all genes. Do you use GenScan?

_Why or why not?_

No, it only works with vertebrates, maize, and some flower.

## You want to analyze a human genomic region and send the DNA sequence to GenScan.

_Now what do you do with the results in order to complete the analysis?_

Go to Embel and perform a pairwise alignment using the amino acid sequence from GenScan and the
actual amino acid sequence from GenBank. Compare the results between GenScan and the pairwise
alignment.

## Why is GenScan useful if you can look up the info in GenBank/SwissProt?
## What is a Genome Wide Association Study? What can it tell us?

Association analysis performed with a panel of polymorphic markers adequately spaced to capture most
of the linkage disequilibrium information in the entire genome in the study population.

It studies the SNPs. Do changes in a single nucleotide actually affect the phenotype? We need to
separate the real effects with noise.

## How does the Gene Ontology classify a gene?

There are three descriptors:

* molecular function
* biological process
* cellular component

Let's use DNA Polymerase as an example:

* function => add dNTPs to 5' end of dsDNA template
* prcoess => DNA replication
* cell component => nucleus

## Why is this an improvement over the way GenBank/SwissProt categorizes an entry?

It has a controlled vocabulary. The gene name can change but the GO doesn't. Often times you'll miss
information when searching for a gene because the gene name changed.

## What is the difference between GenScan and Grail?

Grail uses multiple parameters and hidden markov models. It combines prediction techniques with
database entries.

# Primer and Sequencing

## Why is it difficult to sequence repetitive regions using shotgun sequencing?

Shotgun sequencing uses overlapping regions to re-assemble fragments. Sequences with repetitive
regions are difficult to re-assemble because there are too many false overlaps.

## Why can't you use sequence comparison software to design primers?

Sequence comparison software tries to align sequences that are similar or homologous. Primers need
to be complementary. Also, primer design requires more than just complements. You need to be sure
the primer doesn't wrap onto itself.

## How is fragment assembly different from multiple alignment or sequence comparison?

With fragment assembly, you're looking for overlaps between your fragments. These overlaps much have
100% match, there can be no gaps.

## Why is primer design important?

Primers are used to synthesize DNA. It's useful to create DNA or CDNA libraries. Some other uses:

* making molecular tweezers
* nanoswitches
* DNA computers
* nanosensors
* create complicated DNA structures

## Why do we want a fragment assembly program to generate a consensus sequence?

_Previously we said a consensus sequence is not good for describing a biological pattern and
capturing all the sequence variation present in a pattern._

## What do you have to do to be confident this is not a sequencing error?

_You have sequenced a nucleotide fragment and found that the nucleotide in position 23 is a G. How
can you be sure that it actually is a G and not another nucleotide._

Nucleotides in the middle usually have a higher rate of being correct than nucleotides on each ends.
You could do sequencing walking to verify with just the small fragment that you're concerned about.

## How would you sequence only these regions of the genome?

_If only 5% of the human genome codes for proteins._

You could sequence the post-processed mRNA and use its complementary for the cDNA. You could also
use the reverse-transcriptase enzyme to backtranslate it back into DNA.

## What does the strategy above miss?

The introns.

## How do dot plots for sequence comparison and fragment assembly alignments differ?

With fragment assembly, the sequences are much shorter than the overall alignment. Internal gaps are
heavily penalized since a gap indicates you missed a base. You can only use identity matrix.

## Why are thermodynamic parameters important in primer design?

For the primer's reaction with DNA. It needs to be optimized so it can anneal with the DNA. Some of
the reaction conditions are:

* salt concentration
* DNA concentration
* temperature of hybridization
* temperature of melting

GC bonds are stronger than AT bonds which will raise the melting point.

## Why those parameters not important in the following?

* fragment assembly
* multiple alignments
* database searching

## How would you test out the primer to make sure there were no mispriming sites?

_You want to find a primer that will hybridize to only one gene in a genome._

Do a database search using the original BLAST, without gaps.

## Does increasing the GC content in a primer raise/lower the melting temp? Why?

It raises the melting temperature because GC bonds are stronger than AT bonds (triple hydrogen bonds
vs double hydrogen bonds).

## How can you make sure there's no other site that it could hybridizes to?

_You have designed a primer to a plasmid._

Do a database search using BLAST.

## What software would you use for the above?

BLAST.

## Why do we sequence many times more than the length of the region being sequenced?

We have to re-assemble the fragments, which require that we have multiple overlaps. The more
overlaps, the better since it lowers the probability that any overlap could have happened by chance.

# Phylogenetic Analysis

## What do you need to start with before you can do phylogenetic analysis?

You you to start with similar sequences. If you choose bad sequences, you'll get bad output. You
need the output from a multiple alignment (some software will do the alignment for you, some
software requires the output because you might want to do manual adjustments).

An example of when you want to edit the output: gaps. You want to put gaps where it makes biological
sense - such as in between separate helices.

## Is it better to use DNA or protein sequences when doing phylogenetic analysis?

For evolutionary distant sequences, it's best to use protein sequences. It's always better to use
protein sequences unless they're evolutionary close. If two sequences are too close, there may not
be any difference between the amino acid sequences.

## Why correct sequence distances?

Correcting sequences accounts for nucleotides which change back. For example, `C` changes to `T`
which changes back to `C` in a later step. It also fixes the comparison of two sequences by adding a
common parent between the two instead of just assuming that one evolved into the other.

## Are phylogenetic trees actually how the sequences evolved or are just models?

They're just models. For actual proof, you'll need palentological evidence.

## Does a phylo tree showing gene evolution describe species evolution?

No. A single gene is not enough evidence for the evolution of a species evolving. It just means the
rate of the gene evolving is close for those two species. You'll need to throw more data to get the
species evolution info.

## How far is the inferred ancestral sequence separated from A?

_You find that two sequences A and B are separated by a distance of 6._

6 steps.

_Is that the only possibility?_

No, it's just the shortest. Nucleotides could change back, eg A -> C -> A.

## How can you determine which tree is probably correct?

_You do a phylogenetic analysis and your tree drawing program returns more than one tree that could
explain how the sequences evolved._

The simpler tree with fewer steps is usually correct. Nature is lazy. You can also use probability
to analyze your results. Some nucleotides are more likely to mutate into other nucleotides.

## Can you use this dendrogram to infer how the sequences evolved?

_You do a multiple alignment and it creates a dendrogram._

No, guide trees don't take common parents into account when comparing two sequences. If you infer
from it, you'll miss the common parent.

## Do all proteins evolve at the same rate in an organism?

No, they do not. There's a wide range of variety for each protein.

## Does the same protein evolve at the same rate in different organisms?

Sometimes their rate is similar. Most of the time they're different.

## What is the best method to do a phylogenetic analysis of a multi-domain protein?

Separate the domains and analyze each one individually. The domains were most likely independent and
then got connected over time. If you analyze them as connected domains, you can only go as far back
as when they originally fused.

## How is the evolutionary distance between two sequences calculated?

It's the number of substitutions/changes to get from one parent sequence to the child sequence.

## What is more likely, a complicated evolutionary path or a simple evolutionary path?

Nature is lazy, a simple evolutionary path.

## What is an exhaustive search and why is it not the best method?

_To use to find the optimal phylogenetic tree._

An exhaustive search assembles every possible tree and evaluates the distances to find the best one.
It's too computationally expensive and should only be used when you only have a few sequences.

## How would you do that?

_You have a collection of related proteins and you want to find the region that is probably the
active site._

The conserved amino acids in a phylogenetic tree indicate the active site.

# Microarray Technology

## What can a microarray experiment tell you?

A microarray experiment is used to analyze gene expression in a cell.

## What do the colors in a heat map tell you?

The expression level (via the amount of mRNA) of each gene.

## What are the limitations of microarray experiments?

* they have a high error rate
* microarray tells mRNA levels, we want protein levels
* they're expensive, currently ~$400 a chip

## Will full genome sequencing replace microarrays?

No, genome sequencing just tells you the sequence. Microarrays will tell you if the DNA is being
expressed or not.

## Why is normalization useful?

Normalization is done to compare two chips. It cleans up the data. It lets you see the data better.
For example, the data might be too compact or too exponential. Use the log function to make it
linear.

## What are the different types of microarrays?

* affymetrix
* spotted array

## How is the initial image of a gene chip converted into a heat map?

A computer shoots a laser through the gene chip to detect the levels of expression via fluorescence.

## Can the results of two different microarray experiments be combined?

Yes, often times experiments are run over again to make sure there weren't any errors.

## How is clustering used to analyze microarray data?

Colors of similar expression levels are clustered together. You look for deviations away from the
mean. You have an average color in the matrix of colors.

## Are there any microarray databases?

Yes, here are the big three:

* GEO (NCBI) - Gene Expression Omnibus
* SMD - Stanford Microarray Database
* ArrayExpress (EBI)