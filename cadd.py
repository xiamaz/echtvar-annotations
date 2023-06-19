r"""
Example:
    First create json file:

$ python dbnsfp.py dbNSFP4.3a.zip -f SIFT4G_converted_rankscore -f SIFT_score \
   -f Polyphen2_HDIV_score -f Polyphen2_HDIV_pred --json \
   > conf.json

Then use that conf file (with same command except without --json) and pipe results  to echtvar encode.

$ python dbnsfp.py \
        dbNSFP4.3a.zip \
        -f SIFT4G_converted_rankscore \
        -f SIFT_score \
        -f Polyphen2_HDIV_score \
        -f Polyphen2_HDIV_pred \
        | echtvar encode dbsnfp.zip conf.json -

"""
import sys
import argparse
import re
import os

import zipfile
import gzip

position_lookup = {
        "hg18": ("hg18_chr", "hg18_pos(1-based)"),
        "hg19": ("hg19_chr", "hg19_pos(1-based)"),
        "hg38": ("#chr", "pos(1-based)"),
}

lower_is_more_damaging = [
        "SIFT_score",
        "SIFT4G_score",
        "FATHHMM_score",
        "PROVEAN_score",
]

vcf_header = """##fileformat=VCFv4.3
##source=echtvar-cadd
##CADD=https://cadd.gs.washington.edu/download
##reference=%s
"""

def get_field_lookup(z):
    readme_path = [f for f in os.listdir(z) if "readme" in f.lower() and not f.endswith("pdf")][0]
    fh = open(f"{z}/{readme_path}", 'r')
    txt = fh.read()
    lookup = {}
    for m in re.finditer(r'(^\d+\t)(.*?)(?=^\d)', txt, re.MULTILINE | re.DOTALL):
      col, desc = m.groups(1)[1].replace('\n', ' ').replace('\r', '').replace('"', "'").replace('\t', '').split(':', 1)
      lookup[col] = desc.strip()
    return lookup

def getfloat(f, reducer):
    if f == ".": return '.'
    r = [x for x in f.split(';') if x != '.']
    if len(r) == 0: return '.'
    return "%.4g" % reducer(map(float, r))

def getstring(f):
    if f == '.': return '.'
    r = [x for x in f.split(';') if x != '.']
    if len(r) == 0: return '.'
    return ",".join(r)

def main(path, out_fh=sys.stdout):
    # z = zipfile.ZipFile(path, mode='r')

    print(vcf_header % "hg19", end="", file=out_fh)
    for c in list(range(1, 23)) + ["X", "Y", "M"]:
        print(f'##contig=<ID=chr{c}>', file=out_fh)
    header = None
    for field in [{
        "id": "CADD_RawScore",
        "desc": "CADD Raw score value"
    }, {
        "id": "CADD_PHRED",
        "desc": "CADD Phred scaled score value. In most cases this is the needed CADD Value"
    }]:
      print(f'##INFO=<ID={field["id"]},Number=1,Type=Float,Description="{field["desc"]}">', file=out_fh)
    print("#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO", file=out_fh)

    with gzip.open(path, mode="rt") as gfile:
        header = gfile.readline()
        columns = gfile.readline()
        for line in gfile:
            chr, pos, ref, alt, rawScore, phred = line.strip().split("\t", 6)
            print(f'chr{chr}\t{pos}\t.\t{ref}\t{alt}\t32\tPASS\tCADD_RawScore={rawScore};CADD_PHRED={phred}', file=out_fh)

if __name__ == "__main__":

    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("zip", help="CADD tsv gz file")

    a = p.parse_args()
    main(a.zip)
