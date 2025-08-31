from um import count

def test_count():
    assert count("um what's going on?") == 1
    assert count("Um is it still working?") == 1
    assert count("um, let's resume.") == 1