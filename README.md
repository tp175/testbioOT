# testbioOT

A short **Python** program/wrapper to query the [Open Targets REST API](https://docs.targetvalidation.org/programmatic-access/rest-api) from the command line (CLI). 
The Open Targets Platform REST API allows language agnostic access to data available on the Open Targets Platform, that is, to look up a target ID (Ensembl gene) or disease ID (EFO, HP, Orphanet, MONDO).
Searching will return data such as names and IDs of orthologues, association counts, approved name and much more. 

 - Target - A target identifier listed as an Ensembl gene ID
 - Disease - A disease identifier listed as EFO, Orphanet, HP, or MONDO ID

The program/wrapper accepts a target or disease, queries the endpoint, parses results and performs statistical analysis - printed output (stdout).

### Requisites

The program/wrapper requires two packages - '[opentargets](https://opentargets.readthedocs.io/en/latest)' and '[click](https://click.palletsprojects.com)'.  
For easy installation, simply use pip (below).

	pip install opentargets
	pip install click

*Note: see individual documentations for full instructions.*

### Usage

To run, simply use `runOTcli.py` with `-t target ID` or `-d disease ID` (below). 

	python runOTcli.py -t ENSG00000197386
	python runOTcli.py -d Orphanet_399

*Note: check paths - relative vs absolute.*

### Development

The program/wrapper currently codes/checks for a handful of common errors - configuration of arguments, search type, evaluation of best match, etc. 
Further tests with '[pytest](https://docs.pytest.org)' (`/tests`) can be executed also (below) - more planned, suggestions welcomed.

	pytest tests/test_import.py
	pytest tests/test_run.py

.....