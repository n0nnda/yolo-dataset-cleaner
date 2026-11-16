# YOLO Dataset Cleaner – Images & Labels

Script desenvolvido em Python para verificar, comparar e organizar datasets utilizados no treinamento de modelos de inteligência artificial com YOLO (You Only Look Once).

## 📌 Sobre o projeto

Durante o treinamento de modelos YOLO para reconhecimento e identificação de personagens em jogos, é importante manter as imagens e suas respectivas anotações (*labels*) organizadas.

Cada imagem utilizada no treinamento precisa possuir um arquivo de anotação correspondente, contendo informações sobre as classes e as coordenadas dos objetos identificados.

O objetivo deste script é identificar inconsistências entre as pastas `images` e `labels`, removendo automaticamente os arquivos que não possuem correspondência.

## ⚙️ Tecnologias utilizadas

- **Python:** linguagem utilizada para desenvolver o script.
- **Pathlib:** biblioteca nativa do Python para manipulação de arquivos e diretórios.
- **YOLO:** modelo de visão computacional utilizado no treinamento.

## 📂 Estrutura do dataset

O script trabalha com duas pastas principais:

```text
train/
├── images/
│   ├── personagem_001.jpg
│   ├── personagem_002.jpg
│   └── personagem_003.jpg
│
└── labels/
    ├── personagem_001.txt
    ├── personagem_002.txt
    └── personagem_004.txt
```

- `images/`: armazena as imagens utilizadas no treinamento.
- `labels/`: armazena os arquivos de anotação correspondentes às imagens.

## 🧠 Funcionamento

O script executa as seguintes etapas:

1. **Importação:** utiliza a biblioteca `pathlib` para trabalhar com arquivos e diretórios.
2. **Definição dos caminhos:** configura os diretórios onde estão armazenadas as imagens e anotações.
3. **Identificação:** percorre as pastas utilizando `iterdir()` e obtém os nomes dos arquivos sem suas extensões através de `.stem`.
4. **Comparação:** utiliza conjuntos (`set`) para comparar os nomes dos arquivos e identificar aqueles que não possuem correspondência.
5. **Exclusão:** utiliza o método `unlink()` para remover permanentemente os arquivos sem correspondência.
6. **Finalização:** informa no terminal quais arquivos foram excluídos e quando a verificação foi concluída.

## 💻 Como executar

**1. Abra o CMD ou terminal do Windows.**

**2. Entre no diretório onde está localizado o script:**

```bash
cd script
```

**3. Execute o arquivo Python:**

```bash
python verifica.py
```

**Observação:** antes de executar, altere os caminhos das pastas `images` e `labels` no código-fonte para corresponder à localização do seu dataset.

## 🎯 Objetivo

Automatizar a limpeza e validação inicial de datasets utilizados no treinamento de modelos YOLO, garantindo que as imagens e suas respectivas anotações possuam correspondência.

Essa organização ajuda a reduzir inconsistências nos arquivos e facilita a preparação dos dados para o treinamento de modelos de visão computacional.

## ⚠️ Observações importantes

- A comparação considera o nome completo do arquivo, ignorando sua extensão.
- Arquivos como `personagem_001.jpg` e `personagem_001.txt` são considerados correspondentes.
- Arquivos sem correspondência são excluídos permanentemente.
- O script verifica apenas os arquivos diretamente dentro das pastas, sem percorrer subdiretórios.
- Recomenda-se realizar um backup do dataset antes da execução.

**Limitação:** o script verifica somente a correspondência entre os nomes dos arquivos. Não valida o conteúdo das anotações, classes, coordenadas ou integridade das imagens.