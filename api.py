from fastapi import FastAPI
import uvicorn
import sqlite3
app = FastAPI()

@app.get("/")
async def index():
    with sqlite3.connect("banco.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        query = 'SELECT * FROM fruta'
        
        cur.execute(query)

        data = [dict(d) for d in cur.fetchall()]
        return data


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=7777)