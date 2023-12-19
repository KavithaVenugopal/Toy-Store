from flask import Flask, render_template, request

app = Flask(__name__)

# Toy inventory database (temporary)
toy_inventory = {
    '001': {'name': 'Teddy Bear', 'quantity': 100},
    '002': {'name': 'Toy Car', 'quantity': 150},
    '003': {'name': 'Doll', 'quantity': 120},
    '004': {'name': 'Remote Control Car', 'quantity': 100},
    '005': {'name': 'Board Game', 'quantity': 150},
    '006': {'name': 'Doll House', 'quantity': 120},
    '007': {'name': 'LEGO Set', 'quantity': 100},
    '008': {'name': 'Barbie Princess', 'quantity': 150},
    '009': {'name': 'Piggy Bank', 'quantity': 120},
}

@app.route('/')
def index():
    return render_template('index.html', toys=toy_inventory)

@app.route('/pack_toy_form')
def pack_toy_form():
    return render_template('pack_toy_form.html')


@app.route('/pack_toy', methods=['POST'])
def pack_toy():
    toy_id = request.form['toy_id']
    quantity = int(request.form['quantity'])

    if toy_id in toy_inventory and toy_inventory[toy_id]['quantity'] >= quantity:
        toy_inventory[toy_id]['quantity'] -= quantity
        return render_template('success.html', toy_name=toy_inventory[toy_id]['name'], quantity=quantity)
    else:
        return render_template('failure.html', toy_id=toy_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

