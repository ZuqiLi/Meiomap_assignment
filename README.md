# Meiomap_assignment

Each BED file exhibits the phasing states of all maternal hetSNPs in a cell with oocyte/egg in the first trio being the reference.
The Python script (phasing.py) reads in the input data, calculate phase value and output regions of different phases for each cell.

Note 1: Only heterozygous maternal SNPs are selected for phasing. Therefore, the whole chromosome is splitted into multiple regions by both different phases and homozygous/NC maternal SNPs.

Note 2: NC SNPs in either reference or target cell will cause noise and be neglected to change the phase.

Note 3: Since oocyte as the reference is haploid, Heterozygous reference SNPs are results of erroneous calls and hence also neglected for phasing.
