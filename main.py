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