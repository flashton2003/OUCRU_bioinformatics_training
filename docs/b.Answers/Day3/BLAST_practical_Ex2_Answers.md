**Exercise 2**

Q1. Longest is pKST313 (300 kbp), shortest is FII-S1 (215 bp).

Q2. Sequences where the name starts with lowercase p are usually plasmids e.g. pSBLT or pKST313.

Q3. rpoB and ompD are usually chromosomal, all the others are plasmid associated

Q4. ![Q4 answers](https://i.imgur.com/5IaqAtm.png)

Q5. It’s hard to give a definite answer here, need to look at the assemblies of a variety of k-mers sizes to see. Is the graph still quite tangled, indicating that the max k-mer size was not long enough? Or were there too many dead ends, indicating that long k-mers were given more weight in the assembly than they should be.  But just an exercise to try and get people thinking about the effect of k-mer size on assembly. SRR5451253 looks good. SRR3285401 and SRR5451282 look a bit more tangled. 

Q6. Yes in SRR5451253. No in SRR3285401. E.g. bottom left of the below. Maybe in SRR5451282, but not circular. Assembly graph of SRR5451253, plasmid is in bottom left:
![Assembly graph of SRR5451253, plasmid is in bottom left](https://i.imgur.com/P44FKxv.png)

Q7.
![See here](https://i.imgur.com/BXkRgNx.png)

Q8. It tells you, in combination with the structure of the graph, which parts are repeated.

Q9. Looks like there are two copies of ctx-M15, one on the plasmid and one on the chromosome. OmpD is included because the integron carrying ctx-M15 is inserted into the middle of OmpD. 

Bonus question Q10. OmpD is included because it is the gene which is disrupted by the ctx-m15