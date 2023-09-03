from utils import dicts


def test_existing_key():
    data = {"vcs": "mercurial"}
    result = dicts.get_val(data, "vcs")
    assert result == "mercurial"

def test_existing_key_with_default():
    data = {"vcs": "mercurial"}
    result = dicts.get_val(data, "vcs", "git")
    assert result == "mercurial"

def test_non_existing_key_with_default():
    data = {}
    result = dicts.get_val(data, "vcs", "git")
    assert result == "git"

def test_non_existing_key_with_custom_default():
    data = {}
    result = dicts.get_val(data, "vcs", "bazaar")
    assert result == "bazaar"