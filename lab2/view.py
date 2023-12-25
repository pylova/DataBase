from datetime import datetime


class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message("2. Show table")
        self.show_message("3. Update row")
        self.show_message("4. Delete row")
        self.show_message("5. Exit")
        choice = input("Select your choice: ")
        return choice

    def show_tables(self):
        self.show_message("\nTables:")
        self.show_message("1. Users")
        self.show_message("2. Classes")
        self.show_message("3. Instructors")
        self.show_message("4. User Classes")
        self.show_message("5. Back to menu")
        table = input("Select table: ")
        return table

    def show_users(self, users):
        print("\nUsers:")
        for user in users:
            print(f"User_id: {user[0]}, Phone_number: {user[1]}, Email: {user[2]}, First_name: {user[3]}, Last_name: {user[4]}")

    def show_classes(self, classes):
        print("\nClasses:")
        for clas in classes:
            print(f"Class_id: {clas[0]}, Title: {clas[1]}, Date_and_Time: {clas[2]}, Duration: {clas[3]}, Location: {clas[4]}")

    def show_instructors(self, instructors):
        print("\nInstructors:")
        for instructor in instructors:
            print(f"Instructor_id: {instructor[0]}, First_name: {instructor[1]}, Last_name: {instructor[2]}, Specialization: {instructor[3]}")

    def show_user_classes(self, user_classes):
        print("\nUser Classes:")
        for user_class in user_classes:
            print(f"User_id: {user_class[0]}, Classes_id: {user_class[1]}")


    def get_user_input(self):
        while True:
            try:
                user_id = input("Enter user_id: ")
                if user_id.strip():
                    user_id = int(user_id)
                    break
                else:
                    print("User_id cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                phone_number = input("Enter phone number: ")
                if phone_number.strip():
                    break
                else:
                    print("Phone number cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                email = input("Enter email: ")
                if email.strip():
                    break
                else:
                    print("Email cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                first_name = input("Enter first name: ")
                if first_name.strip():
                    break
                else:
                    print("First name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                last_name = input("Enter last name: ")
                if last_name.strip():
                    break
                else:
                    print("Last name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return user_id, phone_number, email, first_name, last_name


    def get_class_input(self):
        while True:
            try:
                class_id = input("Enter class_id: ")
                if class_id.strip():
                    class_id = int(class_id)
                    break
                else:
                    print("Class_id cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                title = input("Enter title: ")
                if title.strip():
                    break
                else:
                    print("Title cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
                if date_time.strip():
                    datetime.strptime(date_time, "%Y-%m-%d %H:%M")
                    break
                else:
                    print("Date and time cannot be empty.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        while True:
            try:
                duration = input("Enter duration: ")
                if duration.strip():
                    duration = int(duration)
                    break
                else:
                    print("Duration cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                location = input("Enter location: ")
                if location.strip():
                    break
                else:
                    print("Location cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return class_id, title, date_time, duration, location


    def get_instructor_input(self):
        while True:
            try:
                instructor_id = input("Enter instructor_id: ")
                if instructor_id.strip():
                    instructor_id = int(instructor_id)
                    break
                else:
                    print("Instructor_id cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                first_name = input("Enter first name: ")
                if first_name.strip():
                    break
                else:
                    print("First name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                last_name = input("Enter last name: ")
                if last_name.strip():
                    break
                else:
                    print("Last name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                class_id = input("Enter class_id: ")
                if class_id.strip():
                    class_id = int(class_id)
                    break
                else:
                    print("Class_id cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return instructor_id, first_name, last_name, class_id


    def get_user_class_input(self):
        while True:
            try:
                user_id = input("Enter user_id: ")
                if user_id.strip():
                    user_id = int(user_id)
                    break
                else:
                    print("User_id cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                class_id = input("Enter class_id: ")
                if class_id.strip():
                    class_id = int(class_id)
                    break
                else:
                    print("Class_id cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return user_id, class_id


    def get_user_id(self):
        while True:
            try:
                id = int(input("Enter user ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id



    def get_instructor_id(self):
        while True:
            try:
                id = int(input("Enter instructor ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id



    def get_class_id(self):
        while True:
            try:
                id = int(input("Enter class ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)