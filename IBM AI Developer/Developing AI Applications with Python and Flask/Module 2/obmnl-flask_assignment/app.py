# Import libraries
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# Instantiate Flask functionality

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

def get_total_balance(transactions):
    return sum(transaction['amount'] for transaction in transactions)

# Read operation
@app.route('/', methods=['GET'])
def get_transactions():

    return render_template(
            'transactions.html', 
            transactions = transactions, 
            total_balance = {"total" : get_total_balance(transactions)}
            )

# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            'id': len(transactions) + 1,            # Generate a new ID based on the current length of the transactions list
            'date': request.form['date'],           # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value from the form and convert it to a float
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    
    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")
    
# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):

    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction=transaction)
        
        return {"message": "Transaction not found"}, 404
            
    date = request.form['date']           # Get the 'date' field value from the form
    amount = float(request.form['amount'])# Get the 'amount' field value from the form and convert it to a float
    # Find the transaction with the matching ID and update its values
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transaction['date'] = date       # Update the 'date' field of the transaction
            transaction['amount'] = amount   # Update the 'amount' field of the transaction
            break                            # Exit the loop once the transaction is found and updated
    # Redirect to the transactions list page after updating the transaction
    return redirect(url_for("get_transactions"))

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

@app.route(rule='/search', methods=['GET', 'POST'])
def search_transactions():

    if request.method == 'GET':
        return render_template('search.html')
    
    min_amount = float(request.form.get('min_amount'))
    max_amount = float(request.form.get('max_amount'))

    filtered_transactions = [transaction for transaction in transactions if min_amount <= transaction['amount'] <= max_amount]
    return render_template('transactions.html', transactions=filtered_transactions)

@app.route('/balance')
def total_balance():
    return f'Total balance: {get_total_balance(transactions)}'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)