import pytest
from contact_book import contacts, add_contact, view_contact, delete_contact

@pytest.fixture(autouse=True)
def reset_contacts():
    contacts.clear()

def test_add_contact():
    add_contact("Alice", "123-456-7890")
    assert "Alice" in contacts
    assert contacts["Alice"] == "123-456-7890"

def test_view_contact_found(capsys):
    add_contact("Bob", "987-654-3210")
    view_contact("Bob")
    captured = capsys.readouterr()
    assert "Bob: 987-654-3210" in captured.out

def test_view_contact_not_found(capsys):
    view_contact("Charlie")
    captured = capsys.readouterr()
    assert "Contact 'Charlie' not found." in captured.out

def test_delete_contact_found(capsys):
    add_contact("David", "555-123-4567")
    delete_contact("David")
    captured = capsys.readouterr()
    assert "Contact 'David' deleted." in captured.out
    assert "David" not in contacts

def test_delete_contact_not_found(capsys):
    delete_contact("Eve")
    captured = capsys.readouterr()
    assert "Contact 'Eve' not found." in captured.out
