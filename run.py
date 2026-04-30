#!/usr/bin/env python3
"""Run the Fastroads app in a local Python web server with a native WebView window + Discord RPC."""

import functools
import http.server
import socket
import socketserver
import threading
import urllib.parse
import time
import pypresence
from pathlib import Path

try:
    import webview
except ImportError:
    raise SystemExit(
        "pywebview is not installed. Install it with: python -m pip install pywebview"
    )

try:
    from pypresence import Presence
except ImportError:
    raise SystemExit(
        "pypresence is not installed. Install it with: python -m pip install pypresence"
    )

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
ICO_PATH = ROOT / "favicon_circle.ico"

# Put your Discord Application ID here
DISCORD_CLIENT_ID = "1"


def load_icon_path() -> str | None:
    return str(ICO_PATH) if ICO_PATH.exists() else None


class GameRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        parsed = urllib.parse.urlparse(path)
        if parsed.path == "/null":
            path = "/null.html"
        return super().translate_path(path)


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, 0))
        return sock.getsockname()[1]


def start_server(port: int) -> http.server.HTTPServer:
    handler = functools.partial(GameRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer((HOST, port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server
import time

try:
    from pypresence import Presence
except ImportError:
    Presence = None


def start_rpc():
    if Presence is None:
        print("[RPC] pypresence not installed, skipping RPC")
        return None

    try:
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()

        rpc.update(
            details="Playing Fastroads",
            state="In Game",
            large_image="logo",
            large_text="Fastroads",
            start=int(time.time())
        )

        print("[RPC] Connected (Discord or arRPC)")
        return rpc

    except Exception as e:
        print("[RPC] Not available:", e)
        return None

def main() -> None:
    port = find_free_port()
    server = start_server(port)
    url = f"http://{HOST}:{port}/"

    rpc = start_discord_rpc()

    print(f"Serving {ROOT} at {url}")

    webview.create_window(
        "f a s t  r o a d s",
        url,
        width=1280,
        height=800,
        fullscreen=True,
    )

    icon = load_icon_path()
    webview.start(gui="edgechromium", icon=icon)

    if rpc:
        rpc.close()

    server.shutdown()
    server.server_close()


if __name__ == "__main__":
    main()
