from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("Hello, There") == "Hll, Thr"
    assert shorten("spreadsheet") == "sprdsht"
    assert shorten("Unit Tests") == "nt Tsts"
    assert shorten("Example 1:") == "xmpl 1:"