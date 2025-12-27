from cpf_utils import validar_cep

def test_cep_valido():
    assert validar_cep("59015100") is True

def test_cep_invalido():
    assert validar_cep("123") is False
