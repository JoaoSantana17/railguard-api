# RailGuard API

API desenvolvida com **Flask** para monitoramento de atividades suspeitas e alertas nas Linhas 8-Diamante e 9-Esmeralda da CPTM. Hospedada na Vercel.

> URL Base: https://railguard-api.vercel.app

---

###  Login

#### `GET /login`
Lista os usuários disponíveis (sem mostrar senhas).

#### `POST /login`
Realiza o login com `username` e `senha`.

**Body (JSON):**
```json
{
  "username": "admin",
  "senha": "1234"
}
```

---

###  Alertas

#### `GET /alertas`
Retorna todos os alertas cadastrados.

#### `POST /alertas`
Adiciona um novo alerta.

**Body (JSON):**
```json
{
  "Linha": "8-Diamante",
  "vagao": "2",
  "atividade": "Movimentação Suspeita"
}
```

#### `PUT /alertas/<id>`
Atualiza o status de um alerta existente.

**Body (JSON):**
```json
{
  "status": "resolvido"  // ou "ignorado", "ativo"
}
```

#### `DELETE /alertas/<id>`
Remove um alerta pelo ID.

---

### Monitoramento

#### `GET /monitoramento`
Retorna os dados de todas as linhas e vagões monitorados.

#### `GET /monitoramento/<linha>`
Retorna os dados de uma linha específica (`8-diamante` ou `9-esmeralda`).

---

