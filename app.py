from flask import Flask, render_template, request

app = Flask(__name__)

# Calculation function
def calculate_total(principal, interest_per_100_rupees, time_years, time_months, time_days):
    # Convert time to years by summing all units
    total_time_in_years = time_years + (time_months / 12) + (time_days / 365)
    
    # Calculate total interest in rupees
    total_interest = (principal / 100) * interest_per_100_rupees *12* total_time_in_years
    
    # Calculate total amount (principal + interest)
    total_amount = principal + total_interest
    return total_amount, total_interest

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get form data, handling empty input by using 0 as default
            principal = float(request.form['principal'])
            interest_per_100_rupees = float(request.form['interest_per_100_rupees'])
            time_years = float(request.form.get('time_years', 0) or 0)
            time_months = float(request.form.get('time_months', 0) or 0)
            time_days = float(request.form.get('time_days', 0) or 0)
            
            # Perform calculation
            total_amount, total_interest = calculate_total(principal, interest_per_100_rupees, time_years, time_months, time_days)
            
            # Render template with results
            return render_template('index.html', total_amount=total_amount, total_interest=total_interest)
        
        except ValueError:
            # In case of input error (non-numeric values)
            return render_template('index.html', error="Invalid input. Please ensure all fields are filled with correct values.")
    
    # For GET request, simply render the form with no results
    return render_template('index.html', total_amount=None, total_interest=None)

if __name__ == '__main__':
    app.run(debug=True)
