import pytest
import os
from project import get_user_input, calc_total_and_tax, print_pdf

def test_get_user_input_positive(monkeypatch):

    inputs = iter(["desk", "5", "5", "chair", "3", "3", ""])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = get_user_input()

    assert result == [{"line_item": "desk", "item_cost": 5.0, "item_quantity": 5.0}, {"line_item": "chair", "item_cost": 3.0, "item_quantity": 3.0}]

def test_get_user_input_negative(monkeypatch):

    with pytest.raises(StopIteration):

        inputs = iter(["Cat", "five", "three", ""])

        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        get_user_input()

    with pytest.raises(StopIteration):

        inputs = iter(["Dog", 0, 5, ""])

        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        get_user_input()

    with pytest.raises(StopIteration):

        inputs = iter(["Bird", 5, -2, ""])

        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        get_user_input()

def test_get_user_input_none(monkeypatch):

    input = iter([""])

    monkeypatch.setattr('builtins.input', lambda _: next(input))

    result = get_user_input()

    assert result == []


def test_get_user_input_exit(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: exec('raise(EOFError)'))

    with pytest.raises(SystemExit) as excinfo:
        get_user_input()

    assert "--Exited with Ctrl+D--" in str(excinfo.value)




def test_calc_total_and_tax():

    assert calc_total_and_tax([{"line_item": "desk", "item_cost": 5.0, "item_quantity": 5.0}, {"line_item": "chair", "item_cost": 3.0, "item_quantity": 3.0}]) == (34.0, 6.46, 40.46)

    with pytest.raises(ValueError):

        calc_total_and_tax([{"line_item": "desk", "item_cost": "five", "item_quantity": "five"}, {"line_item": "chair", "item_cost": "three", "item_quantity": "three"}])

    assert calc_total_and_tax([{"line_item": "desk", "item_cost": 123.4, "item_quantity": 0.1}, {"line_item": "chair", "item_cost": 6.6, "item_quantity": 3.2}]) == (33.46, 6.3574, 39.8174)




def test_print_pdf(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    items = [{'line_item': 'coffee', 'item_quantity': 1.0, 'item_cost': 5.50}]

    filename = print_pdf(items, 5.50, 1.04, 6.54)

    assert os.path.exists(filename)
    assert filename.startswith("Invoice_")
    assert filename.endswith(".pdf")

    assert os.path.getsize(filename) > 0



