import uvicorn
from fastapi import FastAPI, File

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    with open('test.jpg', 'wb') as f:
        f.write(file)
    return {
        "file_size": len(file),
        "message": '上传成功！'

    }


if __name__ == "__main__":
    uvicorn.run(app)
