#!/bin/bash

HUMREF=/fast/projects/cubit/current/static_data/reference/GRCh37/hs37d5/hs37d5.fa

bcftools norm -m - -w 10000 -f $HUMREF -O b "/fast/projects/cubit/current/static_data/db/gnomAD/release2.0.2/GRCh37/gnomad.exomes.r2.0.2.sites.vcf.gz" | echtvar encode ../gnomad_v202_exomes.zip conf_gnomad_exomes.json -

bcftools norm -m - -w 10000 -f $HUMREF -O b "/fast/projects/cubit/current/static_data/db/gnomAD/release2.0.2/GRCh37/gnomad.genomes.r2.0.2.sites.vcf.gz" | echtvar encode ../gnomad_v202_genomes.zip conf_gnomad_genomes.json -
