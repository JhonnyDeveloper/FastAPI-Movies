from main import app


@app.get("/schedules")
async def read():
    return {"message": "Hello World"}


@app.get("/schedules/{id}")
async def get(id: int):
    return {"message": "Hello World"}


@app.post("/schedules")
async def create():
    return {"message": "Hello World"}


@app.put("/schedules/{id}")
async def update(id: int):
    return {"message": "Hello World"}


@app.patch("/schedules/{id}")
async def edit(id: int):
    return {"message": "Hello World"}
