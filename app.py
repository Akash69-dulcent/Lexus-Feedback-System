from flask import Flask, render_template, request
import pymysql

# Database connection function for XAMPP
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,  # Default XAMPP MySQL port
        user="root",
        password="",  # Default XAMPP MySQL password is empty
        database="akash",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # Returns results as dictionaries
    )

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key
    register_resources(app)
    return app

def register_resources(app):
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
        mysql = None
        cur = None
        lexis = []
        
        try:
            # Get database connection
            mysql = get_db_connection()
            cur = mysql.cursor()
            
            if request.method == "POST":
                customer = request.form.get('customer')
                dealer = request.form.get('dealer')
                rating = request.form.get('rating')
                comments = request.form.get('comments')
                
                # Validate all fields are filled
                if customer and dealer and rating and comments:
                    try:
                        cur.execute("INSERT INTO lexis(customer, dealer, rating, comments) VALUES(%s, %s, %s,  %s)",
                                  (customer, dealer, rating, comments))
                        mysql.commit()
                        print("Data inserted successfully!")
                    except pymysql.Error as e:
                        mysql.rollback()
                        print(f"Error inserting data: {e}")
                else:
                    print("All fields are required!")
            
            # Fetch all records to display
            cur.execute("SELECT * FROM lexis")
            lexis = cur.fetchall()
            
        except pymysql.Error as e:
            print(f"Database error: {e}")
            lexis = []
        
        finally:
            # Clean up database resources
            if cur:
                cur.close()
            if mysql:
                mysql.close()
        
        return render_template('index.html', lexis=lexis)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)