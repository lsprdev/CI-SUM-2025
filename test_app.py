from app import sumF

def test_sumF():
    assert sumF(1, 2) == 3
    assert sumF(-1, 1) == 0
    assert sumF(0, 0) == 0
    assert sumF(100, 200) == 300
    assert sumF(-100, -200) == -300
    assert sumF(1.5, 2.5) == 4.0
    assert sumF(-1.5, 1.5) == 0.0