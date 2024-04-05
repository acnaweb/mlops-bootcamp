"""Api"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    """Index"""

    return "xpto"


if __name__ == "__main__":
    uvicorn.run(app)
