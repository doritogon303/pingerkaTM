from flask import Flask, render_template, redirect
from threading import Thread
import os

id = os.environ['id']

app = Flask('')


@app.route('/')
def main():
    return redirect(
        f"https://discord.com/api/oauth2/authorize?client_id={id}&permissions=133136&scope=bot"
    )


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
