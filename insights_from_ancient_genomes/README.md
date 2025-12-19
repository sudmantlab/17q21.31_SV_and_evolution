Genotype assignments found [here](insights_from_ancient_genomes/ancient_17q_blocks_merged_Feb2022_final.tsv).

To minimize technical artifacts, we filtered the dataset to retain only individuals with non-negative copy number estimates for both duplicated segments (H1D and H2D). We further excluded samples with unknown age or population labels, as well as individuals assigned to Africa, Asia, the Americas, or admixed populations. This filtering yielded a curated set of 644 ancient individuals from Eurasian populations.

### Copy-number sector assignment

For each individual, we assigned a copy-number “sector” based on the average copy number of the H1- and H2-associated segments (`H1.Avg.CN` and `H2.Avg.CN`). Copy-number states were discretized into integer-centered bins with a tolerance of ±0.5 copies, reflecting clustering observed in the data. Sectors were labeled using the format H1_CN_H2_CN (e.g. `2_2`, `3_4`), where each number corresponds to the inferred copy number of the respective haplotype segment.

We then reconciled inversion genotype (H1H1, H1H2, or H2H2) with copy-number sector assignments to infer complex structural genotypes. This mapping followed a predefined matrix of 1271 tag SNPs. This thereby integrates inversion orientation with CNV of _KANSL1_.

Individuals whose inversion status and copy-number sector could not be reconciled unambiguously were excluded. After this final filtering step, 626 ancient individuals remained with confidently assigned complex genotypes.
