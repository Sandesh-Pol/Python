import sqlite3 as lite

class DatabaseManage(object):

    def __init__(self):
        global con 
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")

        except Exception:
            print('Unable to create db . . !')


    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            return False


    def fetch_data(self):
         try:
             with con:
                 cur = con.cursor()
                 cur.execute("SELECT * FROM course")
                 return cur.fetchall()
         except Exception:
             return False

    def delete_data(self, Id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [Id])
                return True
        except Exception:
            return False

def main():
    while True:
        print("*"*40)
        print("*\n:: COURSE MANAGEMENT :: \n")
        print("*"*40)

        db = DatabaseManage()

        print("#"*40)
        print("\n :: User Manual :: \n")
        print("#"*40)

        print('\nPress 1. Insert a new Course\n')
        print('Press 2. Show all courses\n')
        print('Press 3. Delete a Course (NEED ID OF COURSE)\n')
        print("#"*40)
        print("\n")

        choice = input('\nEnter the choice : ')

        if choice == "1":
            name = input('\nEnter course name : ')
            description = input('\nEnter course description : ')
            price = input('\nEnter course price : ')
            is_private = int(input('\nIs this course private (0/1) : '))

            if db.insert_data([name, description, price, is_private]):
                print('Course was inserted successfully')
            else:
                print('OOPS something went wrong')

        elif choice == "2":
            print('\n:: Course List ::')

            for index, item in enumerate(db.fetch_data()):
                print("\n Sl No     : " + str(index + 1))
                print("\n Course ID : " + str(item[0]))
                print("\n Course Name : " + str(item[1]))
                print("\n Course description : " + str(item[2]))
                print("\n Course Price : " + str(item[3]))
                privat = 'Yes' if item[4] else 'No'
                print("\n Is Private : " + privat)
                print("\n")

        elif choice == "3":
            record_id = input('Enter the course Id : ')

            if db.delete_data(record_id):
                print('Course was deleted successfully!')
            else:
                print('Something went wrong!')
        else:
            print('Wrong Choice!')

if __name__=='__main__':
    main()
