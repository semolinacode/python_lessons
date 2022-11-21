import pytest
import dz5


@pytest.mark.parametrize('string', [
                        'a',
                        '1',
                        ' a',
                        'as3',
                        '1d',
                        ])
def test_isalpha(string: str):
        assert dz5.k_isalpha(string) == string.isalpha()


@pytest.mark.parametrize('string', [
                        'a',
                        '1',
                        ' A',
                        'aS3',
                        '1d',
                        'Ss',
                        ])
def test_islower(string: str):
    assert dz5.k_islower(string) == string.islower()


@pytest.mark.parametrize('string', [
                        'a',
                        '1',
                        ' A',
                        'Aed',
                        'AAs',
                        'SsS',
                        'sdsS',
                        ])
def test_istitle(string: str):
    assert dz5.k_istitle(string) == string.istitle()


@pytest.mark.parametrize('string', [
                        'a',
                        '1',
                        ' a',
                        'Aed',
                        'AAs',
                        'SsS',
                        ])
def test_upper(string: str):
    assert dz5.k_upper(string) == string.upper()


@pytest.mark.parametrize('string, substr', [
                        ('a', 'a'),
                        ('1', '1'),
                        (' aaas', 'as'),
                        ('Aed', 'f'),
                        ('hello', 'lol'),
                        ('hello', 'lo'),
                        ('hello', 'hello'),
                        ])
def test_endswith(string: str, substr: str):
    assert dz5.k_endswith(string, substr) == string.endswith(substr)


@pytest.mark.parametrize('string, substr', [
                        ('a   a', 'a'),
                        ('1', '2'),
                        (' aaas', ' '),
                        ('Aed', ''),
                        ('hello', 'l'),
                        ('hello', 'o'),
                        ])
def test_count(string: str, substr: str):
    assert dz5.k_count(string, substr) == string.count(substr)


@pytest.mark.parametrize('string', [
                        ' a',
                        '   1 ',
                        '    e  a       ',
                        'Aed\n  ',
                        ' AAs\t  ',
                        'SsS',
                        ])
def test_strip(string: str):
    assert dz5.k_strip(string) == string.strip()


@pytest.mark.parametrize('string, oldvalue, newvalue, count', [
                        ('hello', 'l', 'w', 0),
                        ('hello', 'l', 'w', 1),
                        ('hello', 'l', 'w', 2),
                        ('hello', 'l', 'w', 3),
                        ('hello', 'l', 'w', 300),
                        ('hello', 'q', 'w', 1),
                        ('hello', 'll', 'a', 1),
                        ('hello', 'll', 'a', 2),
                        ('hello', 'o', '@@', 1),
                        ('hello', 'hello', '@@', 1),
                        ('hello', 'hello', '@@', 2),
                        ('s', 'ss', 'a', 1),
                        ('', '', 'a', 1),
                        ])
def test_replace(string: str, oldvalue: str, newvalue: str, count: int):
    assert dz5.k_replace(string, oldvalue, newvalue, count) == string.replace(oldvalue, newvalue, count)
