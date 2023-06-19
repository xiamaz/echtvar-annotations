#!/bin/bash

python dbscsnv.py -g hg19 /fast/work/projects/cubit/20.05/static_data/db/dbscSNV/1.1/GRCh37/dbscsnv.txt.gz | less
# python dbscsnv.py -g hg19 /fast/work/projects/cubit/20.05/static_data/db/dbscSNV/1.1/GRCh37/dbscsnv.txt.gz | echtvar encode dbscsnv.zip ./conf_dbscsnv.json -
