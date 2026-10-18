# API teste 01;
# Frameworks: FastAPI e Uvicorn (servidor);
# Compilar a API: uvicorn main:app -- reload.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title = "API de teste aula 1",
    version = "1.0.0",
    description = "API simples para ilustrar os conceitos básicos do REST")

# Chamando o @app por meio de uma função.

@app.get("/")
def boas_vindas():
    return{"mensagem": "Bem-vindos á aula API 02"}
