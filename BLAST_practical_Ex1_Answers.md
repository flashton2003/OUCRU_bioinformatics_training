**Exercise 1**

Q1. There are 10 sequences in the Salmonella antigens file. They are named with an identifier and the antigenic structure they encode.

Q2. Outfmt 6 (tabular) is the best format for Excel

Q3. There are 12 columns in the output.

Q4. Use `head -n 4 Salm_1_vs_salmonella_antigens.tsv`

Q5. The columns are separated by tabs.

Q6. The results are presented in a different format (which may be more familiar if you have used the NCBI BLAST website, but which is less convenient for analysing lots of different results.

Q7. Proteins vs salm1 should be tblastn. Salmonella antigens vs salm1 is still just blastn, the choice of which sequence is query and which is database is somewhat arbitrary, the larger sequence or the sequence file being compared against multiple other sequences is usually the database.

Q8. Query sequence id, subject sequence id, percent identical bases, alignment length, number of mismatches, number of gap openings in the match, position in the query where the blast match starts, position in the query where the blast match ends, position in the subject where the blast match starts, position in the subject where the blast match ends, expect value, bit score.

Q9. There are 36 BLAST hits.

Q10. You could filter by e-value `-evalue 1e-5` or `-evalue 0.00001`, but you might miss some interesting hits. You shouldn’t apply filters by default, always look at all the results generated and then filter.

Q11. The best column to sort by is bitscore as more discriminatory than e-value.

Q12. Salmonella 1 is Mbandaka, Salmonella 2 is Braenderup, Salmonella 3 is Colindale, Salmonella 4 is Stanley, Salmonella 5 is Typhi, Salmonella 6 is Typhimurium.

Q13. You see multiple hits because `fljB` hits against `fliC` and vice versa because these two proteins have homologous areas.

Q14.  You can just BLAST sections of the genome against the full NCBI nt/nr BLAST database. A section of around 50 kbp of e.g. Salm_1 will give a 100% hit against Mbandaka, and a 99% hit against some other serotypes.