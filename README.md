🛡️ DOSSIÊ LUX CLIMATE: UNIT & SANITY TESTS
Este documento formaliza a estratégia de automação e os resultados obtidos na validação do motor lógico do Lux Climate. O projeto foca na antecipação de falhas (Shift-Left) e na garantia da integridade dos dados climáticos através de uma arquitetura de testes segregada.

🚀 Vantagem Estratégica
Esta estrutura permite uma esteira de QA extremamente ágil:

Testes de Sanidade: Feedback instantâneo para o desenvolvimento sobre a saúde do motor.

Testes Unitários: Garantia de cobertura total das regras de negócio e precisão dos cálculos.

🛠️ Como Executar o Projeto
Para garantir a qualidade localmente, siga os passos abaixo:

1. Preparar o Ambiente (Virtual Env):python3 -m venv venv
Bash
python3 -m venv venv
source venv/bin/activate
pip install pytest

2. Executar Testes Unitários (Cobertura de Lógica):
Bash
pytest tests/unit/test_engine_unit.py

3. Executar Testes de Sanidade (Validação Rápida):
Bash
pytest tests/sanity/test_sanity_motor.py

4. Executar a Suíte Completa:
Bash
pytest


📊 Evidências de Sucesso
Status do Motor: ✅ All tests passed
Velocidade de Execução: ~0.02s
Arquitetura: Python + Pytest


🛠️ Tecnologias Utilizadas no QA Engineer

Linguagem: Python

Framework de Teste: Pytest

Arquitetura: Domain-Driven Testing (DDT)

Abordagem: Shift-Left / TDD (Test Driven Development)




Um produto Lux by Or.💎
   
