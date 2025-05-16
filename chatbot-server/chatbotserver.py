import uvicorn
from llama_cpp.server.app import create_app
import os
# Định nghĩa biến môi trường
os.environ["MODEL"] = "models/google_gemma-3-4b-it-Q6_K_L.gguf"
os.environ["N_CTX"] = "16384"
os.environ["LLAMA_OFFLOAD_KQV"] = "1"
# os.environ["N_GPU_LAYERS"] = "20"

app = create_app()
# Chạy server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7500)
