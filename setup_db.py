import psycopg2

def setup_database():
    # Homebrew wala connection bina password ke
    conn = psycopg2.connect(dbname="postgres", user="param", password="", host="localhost", port="5432")
    cursor = conn.cursor()
    
    # Table banana
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (customer_id SERIAL PRIMARY KEY, name VARCHAR(100), signup_date DATE);
    CREATE TABLE IF NOT EXISTS orders (order_id SERIAL PRIMARY KEY, customer_id INT, order_date DATE, total_amount DECIMAL(10, 2));
    """)
    
    # Dummy Data daalna
    cursor.execute("""
    INSERT INTO customers (name, signup_date) VALUES ('Alice', '2026-09-01'), ('Bob', '2026-09-15') ON CONFLICT DO NOTHING;
    INSERT INTO orders (customer_id, order_date, total_amount) VALUES (1, '2026-09-10', 150.00), (2, '2026-09-20', 50.00) ON CONFLICT DO NOTHING;
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Database Setup Complete!")

if __name__ == "__main__":
    setup_database()
