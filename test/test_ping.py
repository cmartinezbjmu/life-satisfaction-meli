"""Ping pong test."""
from flask import url_for


def test_api_ping_return_200(client):
    assert client.get(url_for("ping.ping_ping")).status_code == 200


def test_api_ping_returns_pong(client):
    res = client.get(url_for("ping.ping_ping"))
    assert res.data == b"pong"
