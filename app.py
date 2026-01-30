from flask import Flask, request, jsonify, send_from_directory
import uuid
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auctions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Auction(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), default='open')
    bids = db.relationship('Bid', backref='auction', lazy=True)

class Bid(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    auction_id = db.Column(db.String(36), db.ForeignKey('auction.id'), nullable=False)
    bidder = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/create_auction', methods=['POST'])
def create_auction():
    data = request.json
    auction_id = str(uuid.uuid4())
    new_auction = Auction(id=auction_id, item=data.get('item'))
    db.session.add(new_auction)
    db.session.commit()
    return jsonify({'auction_id': auction_id}), 201

@app.route('/place_bid/<auction_id>', methods=['POST'])
def place_bid(auction_id):
    auction = Auction.query.get(auction_id)
    if not auction:
        return jsonify({'error': 'Auction not found'}), 404
    if auction.status != 'open':
        return jsonify({'error': 'Auction closed'}), 400
    data = request.json
    bid_id = str(uuid.uuid4())
    new_bid = Bid(id=bid_id, auction_id=auction_id, bidder=data.get('bidder'), amount=data.get('amount'))
    db.session.add(new_bid)
    db.session.commit()
    return jsonify({'status': 'bid placed'}), 200

@app.route('/close_auction/<auction_id>', methods=['POST'])
def close_auction(auction_id):
    auction = Auction.query.get(auction_id)
    if not auction:
        return jsonify({'error': 'Auction not found'}), 404
    auction.status = 'closed'
    db.session.commit()
    return jsonify({'status': 'closed'}), 200

@app.route('/reveal_winner/<auction_id>', methods=['GET'])
def reveal_winner(auction_id):
    auction = Auction.query.get(auction_id)
    if not auction:
        return jsonify({'error': 'Auction not found'}), 404
    if auction.status != 'closed':
        return jsonify({'error': 'Auction not closed yet'}), 400
    bids = Bid.query.filter_by(auction_id=auction_id).all()
    if not bids:
        return jsonify({'winner': None}), 200
    winner = max(bids, key=lambda b: b.amount)
    return jsonify({'winner': {'bidder': winner.bidder, 'amount': winner.amount}}), 200

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
