# API teste 01;
# Frameworks: FastAPI e Uvicorn (servidor);
# Compilar a API: uvicorn main:app -- reload.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title = "API de teste aula 1",
    version = "1.0.0",
    description = "API simples para ilustrar os conceitos básicos do REST")

# Chamando o @app por meio de uma função.

@app.get("/")
def boas_vindas():
    return{"mensagem": "Bem-vindos á aula API 02"}

# Chamado o @app por meio de uma funcão que possui uma variável. 

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return{"mensagem": f"Olá {nome}! Seja bem-vindo(a)"}

    # ---------- TERCEIRA EXECUÇÃO ----------

    @app.get("/corridas", response_model=List[Corrida], summary="Listar todas as corridas")
    def listar_corridas():
        return corridas_db

    @app.post(
        "/corridas",
        response_model=Corrida,
        status_code=201,
        summary="Criar uma nova corrida"
        )
    def criar_corrida(dados: CorridaCreate):
        global proximo_id


        preco_final = dados.preco if dados.preco is not None else calcular_preco(dados.distanica_km)
        nova_corrida = Corrida (
            id = proximo_id,
            passageiro = dados.passageiro,
            motorista = dados.motorista,
            origem = dados.origem,
            destino = dados.destino,
            distancia = dados.distancia_km,
            preco = preco_final,
            status  = "solicitada",
            criado_em= datetime.utcnow()          
        )

        corridas_db.append(nova_corrida)
        proximo_id +=1
        return nova_corrida
