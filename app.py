from flask import Flask, request, jsonify, send_from_directory
import uuid
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Simple in-memory storage for auctions
auctions = {}

@app.route('/create_auction', methods=['POST'])
def create_auction():
    data = request.json
    auction_id = str(uuid.uuid4())
    auctions[auction_id] = {
        'item': data.get('item'),
        'bids': [],
        'status': 'open'
    }
    return jsonify({'auction_id': auction_id}), 201

@app.route('/place_bid/<auction_id>', methods=['POST'])
def place_bid(auction_id):
    if auction_id not in auctions:
        return jsonify({'error': 'Auction not found'}), 404
    if auctions[auction_id]['status'] != 'open':
        return jsonify({'error': 'Auction closed'}), 400
    data = request.json
    # blind bid: only store encrypted/blob value in real system; here we store as-is
    auctions[auction_id]['bids'].append({
        'bid_id': str(uuid.uuid4()),
        'bidder': data.get('bidder'),
        'amount': data.get('amount')
    })
    return jsonify({'status': 'bid placed'}), 200

@app.route('/close_auction/<auction_id>', methods=['POST'])
def close_auction(auction_id):
    if auction_id not in auctions:
        return jsonify({'error': 'Auction not found'}), 404
    auctions[auction_id]['status'] = 'closed'
    return jsonify({'status': 'closed'}), 200

@app.route('/reveal_winner/<auction_id>', methods=['GET'])
def reveal_winner(auction_id):
    if auction_id not in auctions:
        return jsonify({'error': 'Auction not found'}), 404
    if auctions[auction_id]['status'] != 'closed':
        return jsonify({'error': 'Auction not closed yet'}), 400
    bids = auctions[auction_id]['bids']
    if not bids:
        return jsonify({'winner': None}), 200
    winner = max(bids, key=lambda b: b['amount'])
    return jsonify({'winner': winner}), 200

@app.route('/suggest_bid', methods=['POST'])
def suggest_bid():
    data = request.json
    item = data.get('item', '').lower()
    # Simple AI-like suggestion based on keywords
    if 'laptop' in item or 'computer' in item:
        suggestion = 500
    elif 'phone' in item or 'mobile' in item:
        suggestion = 200
    elif 'car' in item or 'vehicle' in item:
        suggestion = 5000
    else:
        suggestion = 100  # Default
    return jsonify({'suggestion': suggestion})

@app.route('/')
def index():
    return send_from_directory('.', 'frontend.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
