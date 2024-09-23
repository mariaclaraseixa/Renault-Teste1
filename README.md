---

# Programa de Conversão de Áudio e Análise de Sentimento

Este projeto realiza a conversão de arquivos de áudio no formato `.ogg` para `.mp3`, transcreve os áudios usando o modelo **Whisper** da OpenAI e, em seguida, realiza uma **análise de sentimento** do texto transcrito. A análise de sentimento é feita por meio da **API GPT-3** da OpenAI, com os resultados sendo armazenados em arquivos `.sentimento`.

## Funcionalidades
1. **Conversão de Áudio**: Converte arquivos de áudio no formato `.ogg` para `.mp3`.
2. **Transcrição de Áudio**: Transcreve o conteúdo dos arquivos `.mp3` usando o modelo Whisper.
3. **Análise de Sentimento**: Realiza a análise de sentimento sobre o texto transcrito usando a API GPT-3.
4. **Armazenamento Seguro da Chave API**: A chave da API é armazenada de maneira segura em um arquivo separado que é ignorado pelo Git.

## Como Usar

### Pré-requisitos
1. **Python 3.x**
2. Instalar as dependências necessárias:

   Você pode instalar todas as bibliotecas necessárias usando o comando:

   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve incluir:
   ```text
   openai
   pydub
   whisper
   ffmpeg
   ```

3. **Instalar FFmpeg**:  
   O FFmpeg é necessário para a conversão de arquivos de áudio. Você pode instalá-lo no Mac usando Homebrew:
   
   ```bash
   brew install ffmpeg
   ```

   Para outras plataformas, consulte [FFmpeg Download](https://ffmpeg.org/download.html).

### Configuração da Chave API

O programa usa a API GPT-3 da OpenAI para realizar a análise de sentimento. Para garantir que a chave da API seja mantida segura, siga os passos abaixo:

1. **Crie um arquivo chamado `chave.segredo`** na raiz do projeto.

   O conteúdo deste arquivo deve ter o seguinte formato:

   ```text
   chave=sk-seu_valor_da_chave_aqui
   ```

   - Substitua `sk-seu_valor_da_chave_aqui` pela sua chave de API da OpenAI.

2. **Adicione o arquivo `chave.segredo` ao `.gitignore`** para garantir que ele não seja versionado com o controle de versão do Git.

   Exemplo de um arquivo `.gitignore`:

   ```text
   # Ignorar o arquivo de chave da API
   chave.segredo
   ```

   **Isso garantirá que a chave da API seja mantida em segurança e não seja exposta em repositórios públicos.**

### Execução

Depois de configurar as dependências e adicionar sua chave API, você pode executar o programa da seguinte maneira:

1. Verifique se os arquivos `.ogg` estão presentes na pasta de áudios que você deseja processar.

2. Defina o caminho correto para a pasta contendo os arquivos `.ogg` no script (por exemplo, `directory_path`).

3. Execute o programa para processar os arquivos:

   ```bash
   python seu_programa.py
   ```

   O programa realizará os seguintes passos:
   - Converterá todos os arquivos `.ogg` para `.mp3`.
   - Transcreverá o conteúdo dos arquivos `.mp3` em arquivos `.txt`.
   - Analisará o sentimento dos textos transcritos e gravará os resultados em arquivos `.sentimento`.

### Estrutura de Arquivos

Após a execução do programa, você verá a seguinte estrutura de arquivos no diretório de saída:

```text
/audios
    ├── exemplo_audio.ogg        # Arquivo de áudio original
    ├── exemplo_audio.mp3        # Arquivo convertido
    ├── exemplo_audio.txt        # Transcrição do áudio
    └── exemplo_audio.sentimento # Análise de sentimento
```

### Exemplo de Saída

- O arquivo `.txt` conterá o texto transcrito do áudio.
- O arquivo `.sentimento` conterá o texto original e a análise de sentimento.

Exemplo de conteúdo do arquivo `.sentimento`:

```text
Texto Original: Este é um exemplo de áudio transcrito. Hoje estou me sentindo ótimo!
Análise de Sentimento: O sentimento do texto parece ser positivo, indicando felicidade e satisfação.
```

### Segurança

Para garantir que a chave API não seja exposta, nunca compartilhe o arquivo `chave.segredo` publicamente. O arquivo `.gitignore` deve sempre conter a entrada para ignorar este arquivo.

### Contribuição

Caso queira contribuir para este projeto, sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

---

Isso explica o funcionamento geral do programa, os requisitos e a configuração da chave API, além de instruir os usuários sobre como garantir a segurança ao usar a chave da API.
