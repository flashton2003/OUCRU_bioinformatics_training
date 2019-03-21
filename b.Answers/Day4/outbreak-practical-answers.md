**Part 1**

Q1. Because an earthquake will disrupt many basic services like water pipes, and cholera is a water borne disease.

Q2. *V. cholera* has two chromosomes

Q3. There are 3 processes in the command

Q4. Disty calculates the pairwise SNP distance between all isolates, it outputs a symmetric distance matrix. `process_disty_output.py` takes the symetric distance matrix and converts it to an upper right distance matrix with one value per line. `histogram.py` plots a histogram on the command line.  Information on `disty` is [here](https://github.com/c2-d2/disty) and histogram.py is [here](https://github.com/bitly/data_hacks). `process_disty_output.py` is a script I wrote.

Q5. Median pairwise SNP distance is 61 SNPs. It doesn’t desribe the distribution well because there are three peaks in the distribution.

Q6. There are three peaks in the distribution, one at low SNP distance (0-10), one at intermediate (50-60) and one at high(ish) (140-151). The low SNP distance pairs represent very closely related isolates, like we might see in an outbreak, the medium and high pairs represent the distance between different clades in the tree, and the population structure within the tree. See picture in outbreak practical directory [TODO].

Q7. There are 40 samples in the comparison. In the upper-triangular  pairwise distance matrix, not including self-self comparisons there are `N * (N - 1) / 2` comparisons; For `N = 40` this is `40 * 39 / 2 = 780.`

Q8. “K3P+ASC chosen according to BIC” Kimura 3 Parameter, and ASC, which stands for ascertainment bias correction. This needs to be applied when only variable sites are being input into the tree. BIC is bayesian information criterion.

Q9. One. See "BEST NUMBER OF THREADS: 1" in IQTREE log. Because I/O takes time, so it is not always the quickest to divide tasks between different processors.

Q10. Example tree is [here](https://microreact.org/project/TuDufF5vs)

Q11. Yes

Q12. Not very strong. There is not very much diversity within the outbreak, which will always make it difficult for there to be geographical signal. There is a sub-clade of the outbreak separated by 1 SNP from the others, most of the isolates from northern Haiti are in here, but there are also some isolates from southern Haiti.

Q13. Nepal

Q14. Something like "We have put WGS data from the Haitian cholera outbreak into the context of other genomes from global databases. All of the cholera isolates from Haiti formed a single phylogenetic group (were monophyletic), indicating that the outbreak had a clonal origin. In the global dataset, the most closely related genome was from *V. cholera* isolated in Nepal. This is quite strong evidence that the Haitian outbreak strain shared a recent common ancestor with *V. cholera* circulating in Nepal. However, it is hard to be confident about these findings based on only a single Nepalese genome. There was not a lot of geographical structure within the genomes from Haiti, suggesting that population movement has resulted in the effacement of phylo-geographical associations. The lack of diversity within the outbreak makes such signal difficult to detect."

**Part 2**

Q1. `-bb 1000` ultrafast bootstrapping with 1000 re-samples, means each node in the tree. 

Q2. No, there are some very closely related genomes from Nepal, e.g. SRR308715

Q3. No. Tells you that there are multiple circulating cholera clones/clades in Nepal.

Q4. The inferred ancestor of all the *V. cholerae* in our tree (not the reference genome).

Q5. Probably not. Adding in bootstraps for a whole genome SNP tree is not very informative. Most branches have high support, shorter branches will have poor support, but this is because they rely on a small number of SNPs. Does this mean those evolutionary relationships are not valid? No. It means we are less certain of them than of a longer branch, but this information is also conferred by branch length. If you have a long branch in a whole genome SNP tree which has poor bootstrap support, that's a warning flag, you should investigate further

Q6. We have confirmed that the Haitian outbreak strain shares a recent common ancestor with South Asian/Nepalese genomes. We are now confident that this geographical region is the likely origin of this outbreak.

Advanced Question 1. (0.0012 / 0.029)  * 987 = 41 SNPs

Advanced Question 2. 34 SNPs. Why is it different? Evolutionary model, measurement error?
