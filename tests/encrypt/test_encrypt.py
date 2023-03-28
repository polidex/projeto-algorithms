from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('polido', 'i')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(765, 4)

    assert encrypt_message('polido', 3) == 'lop_odi'

    assert encrypt_message('polido', 4) == 'od_ilop'

    assert encrypt_message('polido', 9) == 'odilop'