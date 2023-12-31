# -*- coding: utf-8 -*-
"""Whisper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10qIKKUTdr1pMEiieE0fyQgWOf1owejsx
"""

!pip install openai-whisper

import whisper
import os

modelo = whisper.load_model("base")
resultado = modelo.transcribe("teste.mp3")

texto = resultado['text']
idioma = resultado['language']

print(f'Transcrição: {texto} \nIdioma: {idioma}')

with open('arquivo.txt','w') as f:
  f.write(f'{texto}')