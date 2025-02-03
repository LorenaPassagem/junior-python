#%%
import pandas as pd
import numpy as np

# %%
"""Tabela com NaN"""
transation = {
    "Dia":["19/01", "20/01", "23/01"],
    "Valor Total Vendas":[np.NaN, 834.47, 15378.12],
    "Qtd Total Vendas":[3, np.nan, 5],
    "Ticket Medio":[320.52, 119.21, np.nan]
}

df_vendas = pd.DataFrame(transation)
df_vendas
# %%
"""Usando o Fill na para preenche-la"""
df_vendas = df_vendas.fillna({
            'Valor Total Vendas':df_vendas['Ticket Medio'] * df_vendas['Qtd Total Vendas'],
            'Qtd Total Vendas':df_vendas['Valor Total Vendas'] / df_vendas['Ticket Medio'],
            'Ticket Medio': df_vendas['Valor Total Vendas'] * df_vendas['Qtd Total Vendas']
           }
        )
# %%
df_vendas

# %%
