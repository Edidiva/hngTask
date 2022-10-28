from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return { "slackUsername": 'Edikan', "backend":True, "age": 26, "bio": "I am tech ethusiast finding my way in this digital world of possibilities"}
    