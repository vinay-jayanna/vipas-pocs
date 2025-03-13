from fastapi import FastAPI, Request, WebSocket, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
import httpx
from starlette.middleware.cors import CORSMiddleware
import websockets
import asyncio
from fastapi.responses import Response


app = FastAPI()


# Configure CORS middleware for the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Dummy authentication dependency
async def verify_token(token: str):
    if token != "secret_token":
        raise HTTPException(status_code=401, detail="Invalid token")

# @app.middleware("http")
async def forward_to_streamlit1(request: Request, call_next):
    # Temporarily return a simple response to bypass forwarding logic
    return Response(content="Test response", status_code=200)


@app.middleware("http")
async def forward_to_streamlit(request: Request, call_next):
    streamlit_url = f'http://localhost:8051'
    
    if request.url.path.startswith("/ws"):
        return await call_next(request)

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=streamlit_url,
            headers={key: value for key, value in request.headers.items() if key.lower() != 'host'},
            content=await request.body(),
            follow_redirects=True
        )

        return Response(content=response.content, status_code=response.status_code, headers=dict(response.headers))

@app.websocket("/ws/{path:path}")
async def websocket_proxy(websocket: WebSocket, path: str):
    await websocket.accept()
    streamlit_ws_url = f"ws://localhost:8051/ws/{path}"
    
    async with websockets.connect(streamlit_ws_url) as upstream:
        while True:
            receive_task = asyncio.create_task(websocket.receive_text())
            send_task = asyncio.create_task(upstream.recv())
            done, pending = await asyncio.wait(
                {receive_task, send_task},
                return_when=asyncio.FIRST_COMPLETED,
            )

            if receive_task in done:
                message = receive_task.result()
                await upstream.send(message)
            else:
                receive_task.cancel()

            if send_task in done:
                message = send_task.result()
                await websocket.send_text(message)
            else:
                send_task.cancel()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
