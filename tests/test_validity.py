import pytest
import os
import subprocess

@pytest.fixture
def html_validation():
    command = ["html5validator", "--root", "src/", "--skip-non-html"]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout.decode("utf-8")

@pytest.fixture
def css_validation():
    command = ["html5validator", "--root", "src/", "--skip-non-css"]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout.decode("utf-8")

def test_html_validation(html_validation):
    assert html_validation == ""

def test_css_validation(css_validation):
    assert css_validation == ""