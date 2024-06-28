import sqlite3 as lite

class ManageStudentData(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('student.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS student(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, MAD INTEGER,PYTHON INTEGER,PHP INTEGER)")
        except Exception as e:
            print('Unable to create table:', e)

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO student(NAME,MAD,PYTHON,PHP) VALUES(?,?,?,?)", data)
                return True
        except Exception as e:
            print('Error inserting data:', e)
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM student")
                return cur.fetchall()
        except Exception as e:
            print('Error fetching data:', e)
            return False

    def delete_data(self, ID):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM student WHERE ID = ?"
                cur.execute(sql, [ID])
                return True
        except Exception as e:
            print('Error deleting data:', e)
            return False

    def update_data(self, data):
        try:
            with con:
                cur = con.cursor()
                sql = "UPDATE student SET NAME=?, MAD=?, PYTHON=?, PHP=? WHERE ID=?"
                cur.execute(sql, data)
                return True
        except Exception as e:
            print('Error updating data:', e)
            return False

def main():
    while True:
        print("*" * 40)
        print("*\n:: COURSE MANAGEMENT :: \n")
        print("*" * 40)

        db = ManageStudentData()

        print("#" * 40)
        print("\n :: User Manual :: \n")
        print("#" * 40)

        print('\nPress 1. Insert a new data\n')
        print('Press 2. Show all data\n')
        print('Press 3. Delete a data (NEED ID OF COURSE)\n')
        print('Press 4. Update a data (NEED ID OF COURSE)\n')

        print("#" * 40)
        print("\n")

        choice = input('\nEnter the choice : ')

        if choice == "1":
            name = input('\nEnter name of student : ')
            mad = input('\nEnter marks of MAD : ')
            python = input('\nEnter marks of PYTHON : ')
            php = input('\nEnter marks of PHP : ')
            if db.insert_data((name, mad, python, php)):
                print('Data was inserted successfully')
            else:
                print('OOPS something went wrong')

        elif choice == "2":
            print('\n:: List ::')

            for index, item in enumerate(db.fetch_data()):
                print("\n Sl No     : " + str(index + 1))
                print("\n Student ID : " + str(item[0]))
                print("\n Student Name : " + str(item[1]))
                print("\n Marks in MAD : " + str(item[2]))
                print("\n Marks in PYTHON : " + str(item[3]))
                print("\n Marks in PHP : " + str(item[4]))
                print("\n")

        elif choice == "3":
            record_id = input('Enter the ID of student : ')

            if db.delete_data(record_id):
                print('Data was deleted successfully!')
            else:
                print('Something went wrong!')

        elif choice == "4":
            record_id = input('Enter the ID of student : ')

            name = input('\nEnter name of student : ')
            mad = input('\nEnter marks of MAD : ')
            python = input('\nEnter marks of PYTHON : ')
            php = input('\nEnter marks of PHP : ')
            if db.update_data((name, mad, python, php, record_id)):
                print('Data was updated successfully')
            else:
                print('OOPS something went wrong')

        else:
            print('Wrong Choice!')

if __name__ == '__main__':
    main()
