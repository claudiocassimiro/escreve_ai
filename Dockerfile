# Use a imagem oficial do Python como base
FROM python:3.10-slim-bullseye

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt ./

# Instala as dependências listadas no requirements.txt
RUN pip install -r requirements.txt

# Copia o restante do código fonte para o contêiner
COPY . .

# Expõe a porta em que a aplicação Flask irá rodar
EXPOSE 4000

# Comando para iniciar o servidor Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
