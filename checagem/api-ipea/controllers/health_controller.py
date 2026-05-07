from flask import jsonify

def health():

    return jsonify({
        "status": "online",
        "api": "ipea-api"
    })
