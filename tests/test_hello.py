import logging
import pytest
from click.testing import CliRunner
from segandiaye_toolkit.cli import hello

def test_hello_output():
    runner = CliRunner()
    result = runner.invoke(hello, ['--name', 'Alice'])
    
    assert result.exit_code == 0
    assert "Hello Alice!" in result.output

def test_hello_logs(caplog):
    runner = CliRunner()

    with caplog.at_level(logging.INFO):
        result = runner.invoke(hello, ['--name', 'Bob'])

    assert result.exit_code == 0
    assert "Hello Bob!" in result.output
    assert "✅ Hello executed." in caplog.text
