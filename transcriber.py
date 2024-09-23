import os
from pydub import AudioSegment
import whisper
import ssl
import urllib.request

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


def ler_chave_api(arquivo_segredo):
    """
    Lê a chave da API do arquivo 'chave.segredo'.
    O arquivo deve ter a estrutura: chave=valor
    """
    with open(arquivo_segredo, 'r') as file:
        for linha in file:
            if linha.startswith("chave="):
                return linha.split('=')[1].strip()  # Extrai o valor após 'chave='
    raise ValueError("Chave da API não encontrada no arquivo.")


# Ler a chave da API do arquivo 'chave.segredo'
api_key_file = 'chave.segredo'
openai.api_key = ler_chave_api(api_key_file)


def ogg_to_mp3(directory):
    """
    Converts all ogg files in the specified directory to mp3 and saves them with the same name.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".ogg"):
            ogg_file = os.path.join(directory, filename)
            mp3_file = os.path.join(directory, filename.replace('.ogg', '.mp3'))

            # Load the ogg file and export it as mp3
            audio = AudioSegment.from_file(ogg_file)
            audio.export(mp3_file, format="mp3")
            print(f"Converted {filename} to mp3")


def transcribe_audio(directory):
    """
    Transcribes all mp3 files in the specified directory and writes the transcript to a text file.
    """
    # Load the Whisper model (you can choose between 'tiny', 'base', 'small', 'medium', 'large')
    model = whisper.load_model("base")

    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            mp3_file = os.path.join(directory, filename)
            txt_file = os.path.join(directory, filename.replace('.mp3', '.txt'))

            # Transcribe the mp3 file
            print(f"Transcribing {filename}...")
            result = model.transcribe(mp3_file)

            # Save the transcription to a text file
            with open(txt_file, 'w') as f:
                f.write(result['text'])
            print(f"Transcription saved to {txt_file}")

            # Após a transcrição, realizar análise de sentimento
            realizar_analise_sentimento(txt_file)


def realizar_analise_sentimento(txt_file):
    """
    Realiza a análise de sentimento de um arquivo de texto transcrito.
    """
    with open(txt_file, 'r') as file:
        texto_para_analise = file.read()

    # Realizar a análise de sentimento usando a API da OpenAI
    resultado_sentimento = analisar_sentimento(texto_para_analise)

    # Salvar o resultado da análise de sentimento em um arquivo .sentimento
    sentimento_file = txt_file.replace('.txt', '.sentimento')
    with open(sentimento_file, 'w') as file:
        file.write(f"Texto Original: {texto_para_analise}\n")
        file.write(f"Análise de Sentimento: {resultado_sentimento}")

    print(f"Análise de sentimento salva em {sentimento_file}")


def analisar_sentimento(texto):
    """
    Faz uma chamada à API da OpenAI para realizar a análise de sentimento de um texto.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",  # Ou o modelo de sua preferência
        prompt=f"Analise o sentimento do seguinte texto: {texto}",
        max_tokens=60,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()


def process_ogg_files(directory):
    """
    Process ogg files in a directory by converting them to mp3 and transcribing them.
    """
    ogg_to_mp3(directory)
    transcribe_audio(directory)


# Exemplo de uso:
"""
Use which ffmpeg at terminal to discover where the tool is installed
"""
AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"
AudioSegment.ffprobe = "/opt/homebrew/bin/ffprobe"
directory_path = "/Users/mariaclaraseixascheffel/PycharmProjects/crm/audios"
process_ogg_files(directory_path)