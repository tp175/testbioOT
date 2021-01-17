# testbioOT

A short **Python** program/wrapper to query the [Open Targets REST API](https://docs.targetvalidation.org/programmatic-access/rest-api) from the command line (CLI). 
The Open Targets Platform REST API allows language agnostic access to data available on the Open Targets Platform, that is, to look up a target ID (Ensembl gene) or disease ID (EFO, HP, Orphanet, MONDO).
Searching will return data such as names and IDs of orthologues, association counts, approved name and much more. 

 - target - A target identifier listed as an Ensembl gene ID
 - disease - A disease identifier listed as EFO, Orphanet, HP, or MONDO ID

The program/wrapper here accepts either a target or disease, queries the endpoint, parses results and performs summary statistics (with outputs printed).

### Requisites

The program/wrapper requires two packages - '[opentargets](https://opentargets.readthedocs.io/en/latest)' and '[click](https://click.palletsprojects.com)'.  
For easy installation, simply use pip (below).

	pip install opentargets
	pip install click

*Note: see individual documentations for full instructions.*

### Usage

To run, simply use 'runOTcli.py' with `-t` and target ID or `-d` and disease ID (below). 

	python runOTcli.py -t ENSG00000197386
	python runOTcli.py -d ENSG00000197386

*Note: check paths - relative vs absolute.*

### Tests

xxx.
