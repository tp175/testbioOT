# testbioOT

A short Python program/wrapper to query the [Open Targets REST API](https://docs.targetvalidation.org/programmatic-access/rest-api) from the command line interface (CLI). 
Run analyses for target or disease id and provide summary statistics

### Requisites

The wrapper requires two packages '[opentargets](https://opentargets.readthedocs.io/en/latest)' and '[click](https://click.palletsprojects.com)'. 

	pip install opentargets
	pip install click

Please use docuemntation for full documentation.

### Usage

To run, simply run 'runOTcli.py' as below. 

	python runOTcli.py -t ENSG00000197386
	python runOTcli.py -d ENSG00000197386

Note do check paths - can be relative or absolute.

### Tests

xxx.
