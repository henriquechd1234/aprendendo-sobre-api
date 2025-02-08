from main import app
from flask import render_template
from flask import jsonify, request
import requests


@app.route("/buscar-artista")
def buscar_artista():
    try: 
        get = request.args.get("q")
        if not termo: 
            return jsonify({"erro": "Parametro 'q' não foi encotrado"})
    
        params ={
            "q" : get,
            "index": 0,
            "limit": 10,
            "output": "json"
    }
        api = "https://api.deezer.com/search/artist"
        response = requests.get (api, params = params)



        return jsonify(response.json())
    except Exception as e:
        return jsonify({"errpo": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Usa a porta do Render ou 5000 localmente
    app.run(host="0.0.0.0", port=port)