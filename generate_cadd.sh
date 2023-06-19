#!/bin/bash

# python cadd.py /fast/projects/cubit/current/static_data/db/CADD/v1.4/GRCh37/whole_genome_SNVs.tsv.gz | less
python cadd.py /fast/projects/cubit/current/static_data/db/CADD/v1.4/GRCh37/whole_genome_SNVs.tsv.gz | echtvar encode cadd.zip conf_cadd.json -
