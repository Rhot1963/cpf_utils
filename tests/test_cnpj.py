from cpf_utils import validar_cnpj

def test_cnpj_valido():
    assert validar_cnpj("45.723.174/0001-10") is True

def test_cnpj_invalido():
    assert validar_cnpj("11.111.111/1111-11") is False
