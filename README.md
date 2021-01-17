# testbioOT

A short **Python** program/wrapper to query the [Open Targets REST API](https://docs.targetvalidation.org/programmatic-access/rest-api) from the command line (CLI). 
The Open Targets Platform REST API allows language agnostic access to data available on the Open Targets Platform, that is, it looks up for the Ensembl gene ID or the disease ID (EFO, HP, Orphanet, MONDO) using a free text search.
Searching will return its Ensembl gene ID or the disease ID in addition to other data, such as names and IDs of orthologues, association counts, approved name and much more. 

 - target - A target identifier listed as an Ensembl gene ID
 - disease - A disease identifier listed as EFO, Orphanet, HP, or MONDO ID

The program accepts either a target or disease id, queries API, parses results, performs summary statistics and prints outputs.

### Requisites

The program requires two packages - '[opentargets](https://opentargets.readthedocs.io/en/latest)' and '[click](https://click.palletsprojects.com)'. To install, simply use pip (below)

	pip install opentargets
	pip install click

*Note: see documentations for full instructions / descriptions.*

### Usage

To run, simply use 'runOTcli.py' with target ID or disease ID (below). 

	python runOTcli.py -t ENSG00000197386
	python runOTcli.py -d ENSG00000197386

*Note: check paths - relative vs absolute.*

### Tests

xxx.
