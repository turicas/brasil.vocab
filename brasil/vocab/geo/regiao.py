#!/usr/bin/env python
# coding: utf-8

regiao_por_uf = {'AC': 'Norte',
                 'AP': 'Norte',
                 'AM': 'Norte',
                 'PA': 'Norte',
                 'RO': 'Norte',
                 'RR': 'Norte',
                 'TO': 'Norte',
                 'AL': 'Nordeste',
                 'BA': 'Nordeste',
                 'CE': 'Nordeste',
                 'MA': 'Nordeste',
                 'PB': 'Nordeste',
                 'PE': 'Nordeste',
                 'PI': 'Nordeste',
                 'RN': 'Nordeste',
                 'SE': 'Nordeste',
                 'DF': 'Centro-Oeste',
                 'GO': 'Centro-Oeste',
                 'MT': 'Centro-Oeste',
                 'MS': 'Centro-Oeste',
                 'ES': 'Sudeste',
                 'MG': 'Sudeste',
                 'RJ': 'Sudeste',
                 'SP': 'Sudeste',
                 'PR': 'Sul',
                 'RS': 'Sul',
                 'SC': 'Sul',
}

ufs_por_regiao = {'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
                  'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN',
                               'SE'],
                  'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
                  'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
                  'Sul': ['PR', 'RS', 'SC'],
}
