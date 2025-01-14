# Cálculo de Métricas de Avaliação de Modelos de Classificação

## Descrição do Projeto
Este projeto tem como objetivo calcular as principais métricas de avaliação de modelos de classificação de dados, incluindo:
- Acurácia
- Sensibilidade (Recall)
- Especificidade
- Precisão
- F-score

O código implementa funções para calcular cada uma dessas métricas com base em valores fornecidos de uma matriz de confusão arbitrária.

## Tabela de Métricas

| Método            | Fórmula                 |
|--------------------|---------------------------|
| Sensibilidade      | VP / (VP + FN)            |
| Especificidade     | VN / (FP + VN)            |
| Acurácia          | (VP + VN) / N             |
| Precisão          | VP / (VP + FP)            |
| F-score            | 2 x (Precisão x Sensibilidade) / (Precisão + Sensibilidade) |

## Definições
- **VP**: Verdadeiros Positivos
- **VN**: Verdadeiros Negativos
- **FP**: Falsos Positivos
- **FN**: Falsos Negativos
- **N**: Total de elementos

## Exemplo de Uso
O código abaixo implementa as funções necessárias e utiliza uma matriz de confusão com valores arbitrários para demonstrar o cálculo das métricas.

```python
# Importando as bibliotecas necessárias
import numpy as np

# Funções para calcular cada métrica
def sensibilidade(vp, fn):
    """Calcula a sensibilidade (recall)."""
    return vp / (vp + fn)

def especificidade(vn, fp):
    """Calcula a especificidade."""
    return vn / (fp + vn)

def acuracia(vp, vn, n):
    """Calcula a acurácia."""
    return (vp + vn) / n

def precisao(vp, fp):
    """Calcula a precisão."""
    return vp / (vp + fp)

def f_score(precisao, recall):
    """Calcula o F-score."""
    return 2 * (precisao * recall) / (precisao + recall)

# Matriz de confusão (valores arbitrários)
VP = 50  # Verdadeiros Positivos
VN = 45  # Verdadeiros Negativos
FP = 5   # Falsos Positivos
FN = 10  # Falsos Negativos
N = VP + VN + FP + FN  # Total de elementos

# Cálculo das métricas
sensibilidade_valor = sensibilidade(VP, FN)
especificidade_valor = especificidade(VN, FP)
acuracia_valor = acuracia(VP, VN, N)
precisao_valor = precisao(VP, FP)
f_score_valor = f_score(precisao_valor, sensibilidade_valor)

# Exibindo os resultados
print(f"Sensibilidade (Recall): {sensibilidade_valor:.2f}")
print(f"Especificidade: {especificidade_valor:.2f}")
print(f"Acurácia: {acuracia_valor:.2f}")
print(f"Precisão: {precisao_valor:.2f}")
print(f"F-score: {f_score_valor:.2f}")
```

## Como Executar
1. Copie o código acima e cole no seu ambiente Google Colab ou outro ambiente Python.
2. Execute o código para calcular as métricas de avaliação.
3. Altere os valores de `VP`, `VN`, `FP`, e `FN` conforme necessário para testar diferentes cenários.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
