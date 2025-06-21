import pymysql # Connecting and using MySQL database
from datetime import date

# AWS RDS database connection
db_host="database-1.cyuht5zo7uqk.us-east-1.rds.amazonaws.com" 
db_user="admin"
db_pass="Lzybear123"
db_name="workout"

# Establish connection to the MySQL database
connection = pymysql.connect(host = db_host, database = db_name, user = db_user, password = db_pass)
print("Connected to the database")
# Print MySQL server version to verify connection
cursor = connection.cursor()
cursor.execute('SELECT version()')
db_version = cursor.fetchone()
print(db_version)

cursor.close()
# Create a new cursor for queries
cursor = connection.cursor()
# Logs a new workout to the database
def log_workout(): 
    user_id = int(input("User ID: "))
    exercise_name = input("Exercise name: ")
    duration = int(input("Duration (minutes): "))
    weight = float(input("Weight used (lbs): "))
    today = date.today()
    # Adds workout data to the workout table
    cursor.execute("""
        INSERT INTO workouts (user_id, exercise_name, duration, weight, workout_date)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, exercise_name, duration, weight, today))
    connection.commit()
    print("Workout logged.")
# Logs daily health data
def log_health_data():
    user_id = int(input("User ID: "))
    weight = float(input("Weight (lbs): "))
    calories_burned = int(input("Calories burned: "))
    today = date.today()
    # Adds health data into the health_data table
    cursor.execute("""
        INSERT INTO health_data (user_id, weight, calories_burned, health_date)
        VALUES (%s, %s, %s, %s)
    """, (user_id, weight, calories_burned, today))
    connection.commit()
    print("Health data logged.")
# Displays workouts and health data for a given user
def view_user_data():
    user_id = int(input("Enter your User ID: "))
    # Display all workouts for this user
    print("\nWorkouts:")
    cursor.execute("""
        SELECT exercise_name, duration, weight, workout_date
        FROM workouts
        WHERE user_id = %s
    """, (user_id,))
    workouts = cursor.fetchall()
    if workouts:
        for w in workouts:
            print(f"Exercise: {w[0]}, Duration: {w[1]} min, Weight: {w[2]} lbs, Date: {w[3]}")
    else:
        print("No workouts found.")
    # Display all health data for user
    print("\nHealth Data:")
    cursor.execute("""
        SELECT weight, calories_burned, health_date
        FROM health_data
        WHERE user_id = %s
    """, (user_id,))
    healths = cursor.fetchall()
    if healths:
        for h in healths:
            print(f"Weight: {h[0]} lbs, Calories Burned: {h[1]}, Date: {h[2]}")
    else:
        print("No health data found.")
# Deletes a single workout or health record by ID
def delete_data():
    print("\nDelete Menu")
    print("1. Delete Workout")
    print("2. Delete Health Record")
    choice = input("Select an option: ")

    if choice == "1":
        user_id = int(input("User ID: ")) # User choose to delete workout
        cursor.execute("SELECT id, exercise_name, workout_date FROM workouts WHERE user_id = %s", (user_id,))
        records = cursor.fetchall()

        if not records:
            print("No workouts found.")
            return
        # Display workout entries with id's
        print("\nWorkouts:")
        for rec in records:
            print(f"ID: {rec[0]}, Exercise: {rec[1]}, Date: {rec[2]}")
        # User selects which one to delete
        delete_id = int(input("Enter the ID of the workout to delete: "))
        cursor.execute("DELETE FROM workouts WHERE id = %s AND user_id = %s", (delete_id, user_id))
        connection.commit()
        print("Workout deleted.")
    # User chose to delete a health 
    elif choice == "2":
        user_id = int(input("User ID: "))
        cursor.execute("SELECT id, health_date FROM health_data WHERE user_id = %s", (user_id,))
        records = cursor.fetchall()

        if not records:
            print("No health records found.")
            return
        # Display health records with id's
        print("\nHealth Records:")
        for rec in records:
            print(f"ID: {rec[0]}, Date: {rec[1]}")
        # Choses which health entry to delete
        delete_id = int(input("Enter the ID of the health record to delete: "))
        cursor.execute("DELETE FROM health_data WHERE id = %s AND user_id = %s", (delete_id, user_id))
        connection.commit()
        print("Health record deleted.")
    else:
        print("Invalid choice.")
# Clears all data in the workouts and health_data tables
def clear_tables():
    cursor.execute("TRUNCATE TABLE workouts;")
    cursor.execute("TRUNCATE TABLE health_data;")
    connection.commit()
    print("All data cleared from workouts and health_data tables.")
# Main program and menu table
while True:
    print("\nHealth & Fitness Tracker")
    print("1. Log Workout")
    print("2. Log Health Data")
    print("3. View My Data")
    print("4. Delete Data")
    print("5. Clear All Data")
    print("6. Exit")
    option = input("Choose an option: ")

    if option == "1":
        log_workout()
    elif option == "2":
        log_health_data()
    elif option == "3":
        view_user_data()
    elif option == "4":
        delete_data()
    elif option == "5":
        clear_tables()
    elif option == "6":
        break
    else:
        print("Invalid choice. Please try again.")
# Close database connection when done
cursor.close()
connection.close()
print("Disconnected from the database.")