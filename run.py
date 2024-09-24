import sys
import uvicorn
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run the FastAPI app with optional reload mode.")
    parser.add_argument("--reload", action="store_true", default=True,
                        help="Enable hot reload mode (default: enabled).")
    parser.add_argument("--no-reload", action="store_false", dest="reload", help="Disable hot reload mode.")
    args = parser.parse_args()
    return args.reload

def run_uvicorn(reload_choice, loop_type=None):
    if loop_type:
        uvicorn.run(app="main:app", host="127.0.0.1", port=8000, loop=loop_type, reload=reload_choice)
    else:
        uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=reload_choice)

if __name__ == "__main__":
    reload_choice = parse_args()

    if sys.platform == 'win32':
        if not reload_choice:
            # When reload is off, use winloop (no loop_type provided)
            import winloop
            winloop.run(run_uvicorn(reload_choice))
        else:
            # When reload is on, use asyncio's default event loop
            run_uvicorn(reload_choice, loop_type="asyncio")
    else:
        # On non-Windows platforms, use uvloop
        run_uvicorn(reload_choice, loop_type="uvloop")