"""
Test for HTML and CSS validity
"""
from file_clerk import clerk
import pytest
from webcode_tk import validator

html_files = clerk.get_all_files_of_type("simple_html_page/", "html")
css_files = clerk.get_all_files_of_type("simple_html_page/", "css")

def get_html_validity_results(html_files: list) -> list:
    html_validity_results = []
    css_validity_results = []
    for file in html_files:
        errors = validator.get_markup_validity(file)
        expected = f"{file}: No Errors Found."
        if not errors:
            result = expected
            html_validity_results.append((result, expected))
        else:
            for error in errors:
                error_message = error.get("message")
                result = f"{file}: {error_message}"
                if "CSS" in error_message:
                    css_validity_results.append((result, expected))
                html_validity_results.append((result, expected))
    return html_validity_results, css_validity_results

def get_css_validity_results(css_results: list) -> None:
    for file in css_files:
        css_code = clerk.file_to_string(file)
        errors = validator.validate_css(css_code)
        errors = validator.get_css_errors_list(errors)
        expected = f"{file}: No Errors Found."
        if not errors:
            result = expected
            css_results.append((result, expected))
        else:
            for error in errors:
                result = f"{file}: {error}"
                css_results.append((result, expected))

html_results, css_results = get_html_validity_results(html_files)
get_css_validity_results(css_results)

@pytest.mark.parametrize("result,expected", html_results)
def test_html_validity(result, expected):
    assert result == expected

@pytest.mark.parametrize("result,expected", css_results)
def test_css_validity(result, expected):
    assert result == expected
