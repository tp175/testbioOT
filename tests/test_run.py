# -*- coding: utf-8 -*-

"""Test the module can be imported."""

#import unittest
from runOTcli import main
from opentargets import OpenTargetsClient
from click.testing import CliRunner

def test_doMainCheckT():
    """Test that 'runOTcli' can be executed & passed."""

    runner = CliRunner()
    result = runner.invoke(main, ['-t', 'ENSG00000197386', '-d', ''])
    assert result.exit_code == 0
    assert 'Ave: 0.22770631865626045' in result.output

def test_doMainCheckD():
    """Test that 'runOTcli' can be executed & passed."""

    runner = CliRunner()
    result = runner.invoke(main, ['-t', '', '-d', 'Orphanet_399'])
    assert result.exit_code == 0
    assert 'Ave: 0.08807390987498148' in result.output

def test_doMainCheckN():
    """Test that 'runOTcli' can be executed & failed."""

    runner = CliRunner()
    result = runner.invoke(main, ['-t', '', '-d', ''])
    assert result.exit_code == 1
