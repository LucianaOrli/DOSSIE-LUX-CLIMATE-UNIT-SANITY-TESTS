import pytest

# Simulando a classe de negócio do Lux Climate
class LuxEngine:
    def check(self, temps):
        # Regra: 5 dias ou mais com temp >= 35
        return 'ONDA DE CALOR' if len([t for t in temps if t >= 35]) >= 5 else 'Normal'

def test_onda_de_calor_positiva():
    e = LuxEngine()
    assert e.check([35, 36, 35, 40, 35]) == 'ONDA DE CALOR'

def test_temperatura_insuficiente():
    e = LuxEngine()
    # Apenas 4 dias acima de 35
    assert e.check([35, 35, 35, 35, 30]) == 'Normal'
