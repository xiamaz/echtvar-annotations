#!/bin/bash

HUMREF=/fast/projects/cubit/current/static_data/reference/GRCh37/hs37d5/hs37d5.fa

python process_spliceai.py ../spliceai_scores.masked.snv.hg19.vcf.gz | echtvar encode ../spliceai.zip conf_spliceai.json -
# python process_spliceai.py ../spliceai_scores.masked.snv.hg19.vcf.gz | less

# bcftools norm -m - -w 10000 -f $HUMREF -O b "/fast/projects/cubit/current/static_data/db/gnomAD/release2.0.2/GRCh37/gnomad.genomes.r2.0.2.sites.vcf.gz" | echtvar encode ../gnomad_v202_genomes.zip conf_gnomad_genomes.json -
