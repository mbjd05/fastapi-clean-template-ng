import sys
import asyncio
import uvicorn
from main import app

config = uvicorn.Config(app=app, host="127.0.0.1", port=8000)
server = uvicorn.Server(config)

if __name__ == "__main__":
    print(sys.platform)
    if sys.platform in 'win32':
        import winloop
        winloop.run(server.serve())
    else:
        from uvicorn.loops.uvloop import uvloop_setup
        uvloop_setup()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(server.serve())
        loop.close()