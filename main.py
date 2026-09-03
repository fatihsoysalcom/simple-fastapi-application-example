from fastapi import FastAPI

# Create a FastAPI application instance.
# This 'app' object is what Gunicorn (and Uvicorn) will serve in a production setup.
app = FastAPI()

@app.get("/")
async def read_root():
    """
    A simple root endpoint that returns a welcome message.
    This demonstrates a basic GET request.
    """
    return {"message": "Merhaba, FastAPI Uygulamasına Hoş Geldiniz!"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    An endpoint that takes a path parameter 'name' and returns a personalized greeting.
    This shows how to define dynamic routes.
    """
    return {"message": f"Merhaba, {name}! FastAPI ile tanıştığına sevindim."}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """
    An endpoint demonstrating path parameters (item_id) and optional query parameters (q).
    This is a common pattern for retrieving specific resources.
    """
    if q:
        return {"item_id": item_id, "q": q, "message": "Bu bir öğe detay sayfasıdır."}
    return {"item_id": item_id, "message": "Bu bir öğe detay sayfasıdır."}

# This block allows running the application directly using 'python main.py' for local development.
# In a production environment, Gunicorn would typically manage Uvicorn workers,
# but this provides a convenient way to test the FastAPI application independently.
if __name__ == "__main__":
    import uvicorn
    # The host '0.0.0.0' makes the application accessible from outside localhost,
    # which is useful for testing in various environments.
    # The port '8000' is a common default for web applications.
    uvicorn.run(app, host="0.0.0.0", port=8000)
