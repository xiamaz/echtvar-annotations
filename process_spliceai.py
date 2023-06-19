#!/usr/bin/env python
import sys
import gzip

infile = gzip.open(sys.argv[1], "rt")

INFO_LINES="""##INFO=<ID=SpliceAI_score,Number=A,Type=Float,Description="Maximum SpliceAI score">
##INFO=<ID=SpliceAI_type,Number=A,Type=String,Description="Type of change associated with maximum SpliceAI score, either acceptor gain (AG), loss (AL) or donor gain (DG), loss (DL)">\n"""

for line in infile:
    if "#INFO" in line:
        continue
    if "#CHROM" in line:
        sys.stdout.write(INFO_LINES)
        sys.stdout.write(line)
        break
    sys.stdout.write(line)



for line in infile:
    *parts, l_info = line.split("\t")
    s = {}
    s['AG'], s['AL'], s['DG'], s['DL'] = map(float, l_info.split("=", 1)[1].split("|")[2:6])
    s_max = max(s, key=s.get)
    sys.stdout.write("\t".join(parts) + f"\tSpliceAI_score={s[s_max]};SpliceAI_type={s_max}\n")

infile.close()
