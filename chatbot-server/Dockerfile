# Sử dụng Python 3.10 làm base image
FROM python:3.10.16

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_PATH="/app/chatbot-server/models/google_gemma-3-12b-it-Q5_K_M.gguf"
ENV N_CTX="16384"
ENV N_GPU_LAYERS="20"

EXPOSE 7500

# Chạy server LLM
CMD uvicorn chatbotserver:app --host 0.0.0.0 --port 7500