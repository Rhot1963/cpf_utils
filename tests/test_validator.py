from cpf_utils import validar_cpf

def test_cpf_valido():
    assert validar_cpf("529.982.247-25") is True

def test_cpf_invalido():
    assert validar_cpf("123.456.789-00") is False

def test_cpf_repetido():
    assert validar_cpf("11111111111") is False
