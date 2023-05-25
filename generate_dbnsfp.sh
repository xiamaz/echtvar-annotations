#!/bin/bash

python dbnsfp.py ./dbnsfp \
	-f Polyphen2_HDIV_score \
	-f Polyphen2_HDIV_pred \
	-f SIFT_score \
	-f SIFT_pred \
	-f MutationTaster_score \
	-f MutationTaster_pred \
	-f REVEL_score \
	-f BayesDel_addAF_score \
	-f BayesDel_addAF_pred \
	-f CADD_phred \
	--json > conf.json

python dbnsfp.py ./dbnsfp \
	-f Polyphen2_HDIV_score \
	-f Polyphen2_HDIV_pred \
	-f SIFT_score \
	-f SIFT_pred \
	-f MutationTaster_score \
	-f MutationTaster_pred \
	-f REVEL_score \
	-f BayesDel_addAF_score \
	-f BayesDel_addAF_pred \
	-f CADD_phred \
  | echtvar encode dbnsfp.zip conf.json -
