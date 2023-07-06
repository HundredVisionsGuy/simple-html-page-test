"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html

required_elements = [("doctype", 1),
                     ("html", 1),
                    ("head", 1),
                    ("title", 1),
                    ("h1", 1),
                    ("p", 2)]
files = clerk.get_all_files_of_type("simple_html_page/", "html")


@pytest.mark.parametrize("element,num", required_elements)
def test_files_for_required_elements(element, num):
    for file in files:
        actual = html.get_num_elements_in_file(element, file)
        assert actual == num

def test_for_presence_of_html_files():
    assert len(files) > 0
