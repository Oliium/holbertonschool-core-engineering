"use strict";

const WS_URL = "ws://localhost:8000/ws";

const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const formEl = document.getElementById("form");
const inputEl = document.getElementById("input");
const sendBtn = formEl.querySelector(".composer__send");

let socket = null;

function timestamp() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
    });
}

function addMessage(text, kind) {
    const li = document.createElement("li");
    li.className = "msg msg--" + kind;
    li.textContent = text;

    if (kind !== "sys") {
        const time = document.createElement("span");
        time.className = "msg__time";
        time.textContent = timestamp();
        li.appendChild(time);
    }

    messagesEl.appendChild(li);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function setConnected(connected) {
    statusEl.textContent = connected ? "connected" : "disconnected";
    statusEl.className = "status " + (connected ? "status--on" : "status--off");
    sendBtn.disabled = !connected;
}

function connect() {
    socket = new WebSocket(WS_URL);

    socket.onopen = () => {
        setConnected(true);
        addMessage("Connection established", "sys");
    };

    socket.onmessage = (event) => {
        addMessage(event.data, "recv");
    };

    socket.onclose = () => {
        setConnected(false);
        addMessage("Connection lost — retrying in 3s…", "sys");
        setTimeout(connect, 3000);
    };

    socket.onerror = () => {
        socket.close();
    };
}

formEl.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = inputEl.value.trim();
    if (!text || !socket || socket.readyState !== WebSocket.OPEN) {
        return;
    }
    socket.send(text);
    addMessage(text, "sent");
    inputEl.value = "";
    inputEl.focus();
});

setConnected(false);
connect();
