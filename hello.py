#!/usr/bin/env python3
"""Hello World Mult Linguas

Dependendo da lingua configurada no ambiente 
o programa exibe a mensagem correspondente

Como usar:
Necessario utilizar as informações carregadas na variável LANG 

Exemplo: 
    export LAN=pt_BR

Executar:
    python3 hello.py
        ou
    ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Caio Bueno"
__license__ = "Unlicense"

import os
language = os.getenv("LANG", "en_US")[:5]
# export LANG=en_US.utf8
# export LANG=pt_BR.utf8

msg_en = "Hello, Python!"
msg_pt = "Olá, Python!"

if language == "en_US":
    # Exibir texto
    print(msg_en)

    # Exibir texto em letras minusculas
    print(msg_en.lower())

    # Exibir texto em letras maisculas
    print(msg_en.upper())

elif language == "pt_BR":
    # Exibir texto
    print(msg_pt)

    # Exibir texto em letras minusculas
    print(msg_pt.lower())

    # Exibir texto em letras maisculas
    print(msg_pt.upper())
    