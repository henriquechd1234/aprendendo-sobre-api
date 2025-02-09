from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from main import app

app.config['SECRET_KEY'] = 'chave secreta'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/chat")
def chat():
      return render_template("chat.html")

@socketio.on('msgrecebida')
def handle_message(data):
    print(f'Mensagem recebida: {data}')
    send(data, broadcast=True)


if __name__ == '__main__':
    import eventlet
    eventlet.monkey_patch()
    socketio.run(app)