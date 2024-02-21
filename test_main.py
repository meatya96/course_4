import pytest
from operations import Operations


@pytest.fixture
def operations_instance():
    option = {
        "date": "2024-02-19T08:30:00.123456",
        "description": "Перевод организации",
        "from": "Visa Platinum 2256483756542539",
        "to": "Счет 78808375133947439319",
        "operationAmount": {
            "amount": 1000,
            "currency": {"name": "USD"}
        }
    }
    return Operations(option)


def test_data(operations_instance):
    expected_date = "19.02.2024"
    assert operations_instance.data() == expected_date


def test_description(operations_instance):
    expected_description = "Перевод организации"
    assert operations_instance.description() == expected_description


def test_from(operations_instance):
    expected_from = "Visa Platinum 2256 83** **** 2539"
    assert operations_instance._from_() == expected_from


def test_to(operations_instance):
    expected_to = "Счет **9319"
    assert operations_instance.to() == expected_to


def test_operationAmount(operations_instance):
    expected_amount = "1000 USD"
    assert operations_instance.operationAmount() == expected_amount
