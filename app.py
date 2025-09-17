from flask import Flask, request, jsonify
from ledger import Ledger

app = Flask(__name__)
ledger = Ledger()
ledger.load_ledger()

@app.route('/claims', methods=['GET'])
def get_claims():
    return jsonify([entry.to_dict() for entry in ledger.entries])

@app.route('/claims', methods=['POST'])
def add_claim():
    data = request.get_json()
    claim = data.get('claim')
    if not claim:
        return jsonify({'error': 'Claim is required'}), 400
    entry = ledger.add_entry(claim)
    return jsonify(entry.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)