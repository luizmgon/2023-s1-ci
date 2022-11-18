import pytest
from models import PasswordValidator, ValidationResponse


def test_empty_str_should_raise_http_400_exception():
    # given
    validator = PasswordValidator(content="")
    with pytest.raises(Exception):  # then
        # when
        validator.password_validate()


def test_7_chars_str_should_raise_http_400_exception():
    # given
    validator = PasswordValidator(content="1@Ab1@A")
    with pytest.raises(Exception):  # then
        # when
        validator.password_validate()


def test_8_chars_str_should_validate():
    # given
    expected_response = ValidationResponse(message="OK")
    # when
    actual_response = PasswordValidator(content="1@Ab1@Ab").password_validate()
    # then
    assert expected_response == actual_response


def test_9_chars_str_should_validate():
    # given
    expected_response = ValidationResponse(message="OK")
    # when
    actual_response = PasswordValidator(content="1@Ab1@Ab1").password_validate()
    # then
    assert expected_response == actual_response
