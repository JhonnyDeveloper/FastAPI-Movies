from main import app


@app.get("/movies")
async def read():
    return {"message": "Hello World"}


@app.get("/movies/{id}")
async def get(id: int):
    return {"message": "Hello World"}


@app.post("/movies")
async def create():
    return {"message": "Hello World"}


@app.put("/movies/{id}")
async def update(id: int):
    return {"message": "Hello World"}


@app.patch("/movies/{id}")
async def edit(id: int):
    return {"message": "Hello World"}
