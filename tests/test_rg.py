from cpf_utils import validar_rg

def test_rg_valido():
    assert validar_rg("12.345.678-9") is True

def test_rg_invalido_repetido():
    assert validar_rg("11111111") is False
