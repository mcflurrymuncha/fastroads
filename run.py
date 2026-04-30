#!/usr/bin/env python3
"""Fastroads server + WebView + Discord RPC (safe + logged version)"""

import functools
import http.server
import socket
import socketserver
import threading
import urllib.parse
import time
import traceback
from datetime import datetime
from pathlib import Path

try:
    import webview
except ImportError:
    raise SystemExit("pywebview missing: pip install pywebview")

try:
    from pypresence import Presence
except ImportError:
    Presence = None


# ----------------------------
# LOGGING SYSTEM
# ----------------------------

ROOT = Path(__file__).resolve().parent
LOG_FILE = ROOT / "fastroads.log"

def log(msg: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

def log_exception():
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 50 + "\n")
        f.write(traceback.format_exc())
        f.write("=" * 50 + "\n\n")


# ----------------------------
# CONFIG
# ----------------------------

HOST = "127.0.0.1"
ICO_PATH = ROOT / "favicon_circle.ico"
DISCORD_CLIENT_ID = "1499447238923915274"


def load_icon_path():
    return str(ICO_PATH) if ICO_PATH.exists() else None


# ----------------------------
# HTTP SERVER
# ----------------------------

class GameRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        parsed = urllib.parse.urlparse(path)
        if parsed.path == "/null":
            path = "/null.html"
        return super().translate_path(path)


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, 0))
        return s.getsockname()[1]


def start_server(port: int):
    handler = functools.partial(GameRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer((HOST, port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


# ----------------------------
# RPC SYSTEM (Discord + arRPC compatible)
# ----------------------------

def start_rpc():
    if Presence is None:
        log("[RPC] pypresence not installed")
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

        log("[RPC] Connected successfully")
        return rpc

    except Exception as e:
        log("[RPC] Failed to connect")
        log_exception()
        return None


# ----------------------------
# MAIN APP
# ----------------------------

def main():
    log("=== Fastroads starting ===")

    try:
        port = find_free_port()
        server = start_server(port)
        url = f"http://{HOST}:{port}/"

        log(f"Server running at {url}")

        rpc = start_rpc()

        log("Launching WebView")

        webview.create_window(
            "f a s t r o a d s",
            url,
            width=1280,
            height=800,
            fullscreen=True,
        )

        icon = load_icon_path()

        webview.start(gui="edgechromium", icon=icon)

        if rpc:
            try:
                rpc.close()
            except:
                pass

        server.shutdown()
        server.server_close()

        log("Clean shutdown complete")

    except Exception:
        log_exception()
        raise


if __name__ == "__main__":
    main()
