import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Charger les données depuis votre fichier JSON
with open('j-citation.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

@app.route("/api/citations", methods=["GET"])
def get_citations():
    # Paramètres de pagination
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    
    # Calcul de l'indice de début et de fin pour la pagination
    start_index = (page - 1) * per_page
    end_index = min(start_index + per_page, len(data['data']))
    
    # Extraction des données paginées
    paginated_data = data['data'][start_index:end_index]
    
    # Retourner les données paginées
    return jsonify({
        "page": page,
        "per_page": per_page,
        "total": data['total'],
        "data": paginated_data
    })

if __name__ == "__main__":
    app.run(debug=True)
