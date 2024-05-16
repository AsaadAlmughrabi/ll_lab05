import pytest
from s_Linken_List.s_Linken_List import LinkedList

# Test the append method
def test_append():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert len(lst) == 3
    assert str(lst) == "1-->2-->3-->"

# Test the delete_node method
def test_delete_node():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.delete_node(2) == True
    assert len(lst) == 2
    assert str(lst) == "1-->3-->"

    # Test deleting a non-existent node
    assert lst.delete_node(4) == False

# Test the __len__ method
def test_len():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert len(lst) == 3

# Test the __str__ method
def test_str():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert str(lst) == "1-->2-->3-->"

# Test the __getitem__ method
def test_getitem():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3

    # Test getting an index out of range
    with pytest.raises(IndexError):
        lst[3]