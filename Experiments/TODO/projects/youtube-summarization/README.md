---
title: YouTubeSummarizerTheEconomistVersion
emoji: 🌍
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
license: mit
---


# Sumarização
Sumarizar é uma das habilidades mais populares entre os LLMs, como o GPT. Consiste em fazer um resumo de um conteúdo que pode ser áudio ou texto.

## Descrição do projeto
O objetivo do projeto é construir uma interface web usando Streamlit, capaz de receber a URL de um vídeo no YouTube e, após a seleção de um modelo (mT5, Pegasus, BART), mostrar um resumo do vídeo.

![](https://hermes.dio.me/assets/articles/5c5744de-df49-4078-a309-056dbedcfa0b.png)

### Etapas
![image](https://github.com/CllsPy/Generative_AI/assets/96326019/82694630-e47b-4d00-9fe9-bcf0fd69b167)

1. Acessar a transcrição dos vídeos (automáticamente)
2. Tratar a o texto obtido e ajustar para um formado que os LLMs entendam
3. Mostrar saída considerando qual dos três modelos foi escolhido (mT5, Pegasus ou BART)

## Requeriments
O processo foi inteiramente no Google Colabs e em seguida tranferido ao HuggingFace Spaces para deployment. A linguagem utilizada foi Python.

### Pacotes

```python
torch
Transformers
Streamlit
youtube-transcript-api
sentencepiece
```

## Considerações
Dentre suas limitações estão o idioma, ainda não ajustei para que seja capaz de sumarizar vídeos em PT, muito em função dos modelos escolhido (tentarei o GPT-2 no futuro) e pela carência em transcrições dos vídeos em alguns canais.

O código está disponível no Github e online no Huggingface para quem tiver curiosidade em testar ou aprimorar o código.
