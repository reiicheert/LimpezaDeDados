import pandas as pd
import os

# =========================
# CRIAR PASTAS
# =========================
os.makedirs("processed", exist_ok=True)
os.makedirs("rejected", exist_ok=True)

# =========================
# LER DADOS
# =========================
df = pd.read_csv("Dados/DadosBases.csv")

print("TOTAL ORIGINAL:", len(df))

# =========================
# DUPLICADOS (SEPARA ANTES)
# =========================
duplicados = df[df.duplicated()]
df = df.drop_duplicates()

# =========================
# FALTANTES (IMPORTANTE: antes de drop)
# =========================
faltantes = df[df.isnull().any(axis=1)]

# agora remove do dataset limpo
df_limpo = df.dropna()

# =========================
# INVÁLIDOS (ex: zeros em dados médicos)
# =========================
colunas_medicas = [
    "Glucose",
    "Diastolic_BP",
    "Skin_Fold",
    "Serum_Insulin",
    "BMI"
]

invalidos = df_limpo[(df_limpo[colunas_medicas] == 0).any(axis=1)]

df_limpo = df_limpo[~(df_limpo[colunas_medicas] == 0).any(axis=1)]

# =========================
# SALVAR ARQUIVOS (AGORA CERTO)
# =========================

df_limpo.to_csv("processed/Dados_Limpos.csv", index=False)
faltantes.to_csv("rejected/Dados_Faltantes.csv", index=False)
duplicados.to_csv("rejected/Dados_Duplicados.csv", index=False)
invalidos.to_csv("rejected/Dados_Invalidos.csv", index=False)

# =========================
# DEBUG FINAL (ESSENCIAL)
# =========================
print("\n===== RESULTADO =====")
print("Limpos:", len(df_limpo))
print("Faltantes:", len(faltantes))
print("Duplicados:", len(duplicados))
print("Invalidos:", len(invalidos))