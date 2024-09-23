import sys
import asyncio
import uvicorn
import argparse

import winloop.loop

from main import app


# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Run the FastAPI app with optional reload mode.")
    # --reload is True by default, and --no-reload can disable it
    parser.add_argument("--reload", action="store_true", default=True,
                        help="Enable hot reload mode (default: enabled).")
    parser.add_argument("--no-reload", action="store_false", dest="reload", help="Disable hot reload mode.")
    args = parser.parse_args()
    return args.reload


if __name__ == "__main__":
    reload_choice = parse_args()  # Get the --reload or --no-reload argument value (True/False)

    if sys.platform == 'win32':
        if not reload_choice:
            # When reload is off, use winloop
            config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, reload=False)
            server = uvicorn.Server(config)
            winloop.run(server.serve())
        else:
            # When reload is on, use asyncio's default event loop
            uvicorn.run("main:app", host="127.0.0.1", loop="asyncio", port=8000, reload=True)
    else:
        # On non-Windows platforms, use uvloop
        uvicorn.run("main:app", host="127.0.0.1", loop="uvloop", port=8000, reload=reload_choice)
