PGRTK graphs and principal bundle decompositions for HGSVC and HPRC samples found [here](haplotype_resolved_structures/humans/pgrtk)

PGRTK graphs and principal bundle decompositions for primate samples found [here](haplotype_resolved_structures/primates/pgrtk)

Haplotype assignments for humans found here

Principal bundle sequences (e.g. `0.0-3.0-7.0-4.0-8.0-5.0-6.0-2.0-4.1-7.1-2.1-5.0-6.0-2.0-4.1-7.1-2.1-5.0-6.0-2.0-1.0`) are encoded as bundle identities separated by hyphens. Each bundle (indicated by a number) is referred to by its identifier (a number) followed by a . and then a 0 or 1 indicating it's orientation (direct or inverted respectively)

Input data for SVByEye was generated using the minimap2 command: `minimap2 -x asm5 -c --eqx -D -P --dual=no {input} {input} > {output}` on the extracted sequences. `asm20` was used for primate samples.
