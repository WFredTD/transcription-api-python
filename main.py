# Importa as bibliotecas necessárias para criar a API, manipular arquivos e o modelo Whisper.
import whisper
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import tempfile

# Configura uma variável de ambiente que informa ao Whisper onde o FFmpeg está instalado.
# Isso garante que a biblioteca sempre encontre o executável, independentemente das configurações do sistema.
os.environ["FFMPEG_BINARY"] = r"C:\ffmpeg\bin\ffmpeg.exe"

# Cria a instância principal do FastAPI com metadados para documentação.
app = FastAPI(
    title="API de Transcrição de Áudio e Vídeo",
    description="""
    Esta API transcreve arquivos de áudio e vídeo para texto usando o modelo de IA de código aberto Whisper da OpenAI.

    - **Usa o modelo `medium` do Whisper** para uma alta precisão.
    - **Suporta múltiplos formatos**: Áudios (`.opus`, `.mp3`, `.wav`, etc.) e vídeos (`.mp4`, `.mov`, etc.).
    - **Documentação interativa automática** em `/docs` (Swagger UI) e `/redoc`.
    """,
    version="1.0.0",
)

# Carrega o modelo de IA do Whisper.
# O modelo 'medium' é escolhido para um bom equilíbrio entre velocidade e precisão.
print("Carregando o modelo Whisper...")
model = whisper.load_model("medium")
print("Modelo Whisper carregado.")

# Monta uma rota para servir arquivos estáticos.
# Isso permite que o servidor Python hospede o seu frontend (index.html).
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a rota principal (/) que servirá o arquivo index.html.
# include_in_schema=False evita que esta rota apareça na documentação da API.
@app.get("/", include_in_schema=False)
async def serve_frontend():
    print("Requisição GET recebida para a página inicial.")
    html_file_path = os.path.join("static", "index.html")
    with open(html_file_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# Define a rota POST para a transcrição, onde o frontend enviará o arquivo de áudio.
@app.post(
    "/transcrever_audio/",
    summary="Transcreve um arquivo de áudio ou vídeo para texto.",
    description="""
    Recebe um arquivo de áudio ou vídeo e retorna o texto transcrito.

    **Parâmetros:**
    - `audio_file`: O arquivo de áudio ou vídeo a ser transcrito.
    """,
    tags=["Transcrições"],
)
async def transcrever_audio(audio_file: UploadFile = File(...)):
    try:
        print(f"Iniciando o processo de upload do arquivo: {audio_file.filename}")
        
        # Cria um arquivo temporário seguro no sistema para armazenar o arquivo enviado.
        # O 'tempfile' é usado para evitar problemas de permissão e caminho.
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.filename)[1]) as temp_file:
            print(f"Caminho do arquivo temporário criado: {temp_file.name}")
            # Lê o conteúdo do arquivo de forma assíncrona.
            content = await audio_file.read()
            # Escreve o conteúdo no arquivo temporário.
            temp_file.write(content)
            file_path = temp_file.name

        print(f"Arquivo temporário salvo com sucesso. Tamanho: {len(content)} bytes.")

        print("Chamando o modelo Whisper para transcrição...")
        # Usa o modelo Whisper para transcrever o áudio do arquivo temporário.
        transcription = model.transcribe(file_path, fp16=False)

        print("Transcrição concluída.")
        
        # Deleta o arquivo temporário após a transcrição para liberar espaço.
        os.remove(file_path)
        print("Arquivo temporário removido.")
        
        # Retorna a transcrição em formato JSON para o frontend.
        return {"transcricao": transcription["text"]}
    
    except Exception as e:
        # Em caso de erro, imprime a mensagem no terminal para depuração.
        print(f"Erro na transcrição: {e}")
        # Retorna uma mensagem de erro para o frontend.
        return {"erro": str(e), "detalhes": "Erro no processo de transcrição. Verifique o log do servidor para mais informações."}

# Configura e inicia o servidor Uvicorn.
# Ele hospeda a aplicação FastAPI e a torna acessível via HTTP.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
