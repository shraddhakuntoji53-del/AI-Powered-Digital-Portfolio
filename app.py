from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Shraddha Portfolio Backend")

# Allow all origins so frontend can connect easily
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the frontend HTML file"""
    return FileResponse("index.html")

@app.post("/contact")
async def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    """Handle contact form submissions"""
    print(f"📩 New message from {name} ({email}): {message}")
    return JSONResponse({"status": "success", "message": f"Thanks {name}, your message has been received!"})

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
