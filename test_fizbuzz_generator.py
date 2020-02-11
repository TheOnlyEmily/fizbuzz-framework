import pytest

from fizbuzz_generator import fiz_buzz


def test_generator_up_to_15():
    fb_list = [r for r in fiz_buzz(16)]

    assert fb_list[0] == 1
    assert fb_list[1] == 2
    assert fb_list[2] == "fiz"
    assert fb_list[3] == 4
    assert fb_list[4] == "buzz"
    assert fb_list[5] == "fiz"
    assert fb_list[6] == 7
    assert fb_list[7] == 8
    assert fb_list[8] == "fiz"
    assert fb_list[9] == "buzz"
    assert fb_list[10] == 11
    assert fb_list[11] == "fiz"
    assert fb_list[12] == 13
    assert fb_list[13] == 14
    assert fb_list[14] == "fizbuzz"
