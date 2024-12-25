from fastapi import FastAPI
import routes

app = FastAPI()

# Include the post routes
app.include_router(routes)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API"}
