import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '5':
                break
            elif choice in ['1', '2', '3', '4']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if table == '6':
                break

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_show_option(table)
            elif choice == '3':
                self.process_update_option(table)
            elif choice == '4':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding user:")
            self.add_user()
        elif table == '2':
            self.view.show_message("\nAdding class:")
            self.add_class()
        elif table == '3':
            self.view.show_message("\nAdding instructor:")
            self.add_instructor()
        elif table == '4':
            self.view.show_message("\nAdding user class:")
            self.add_user_class()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_show_option(self, table):
        if table == '1':
            self.show_users()
        elif table == '2':
            self.show_classes()
        elif table == '3':
            self.show_instructors()
        elif table == '4':
            self.show_user_classes()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating user:")
            self.update_user()
        elif table == '2':
            self.view.show_message("\nUpdating class:")
            self.update_class()
        elif table == '3':
            self.view.show_message("\nUpdating instructor:")
            self.update_instructor()
        elif table == '4':
            self.view.show_message("\nUpdating user class:")
            self.update_user_class()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting user:")
            self.delete_user()
        elif table == '2':
            self.view.show_message("\nDeleting class:")
            self.delete_class()
        elif table == '3':
            self.view.show_message("\nDeleting instructor:")
            self.delete_instructor()
        elif table == '4':
            self.view.show_message("\nDeleting user class:")
            self.delete_user_class()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def add_user(self):
        try:
            user_id, phone_number, email, first_name, last_name = self.view.get_user_input()
            self.model.insert_user(user_id, phone_number, email, first_name, last_name)
            self.view.show_message("User added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_class(self):
        try:
            class_id, title, date_time, duration, location = self.view.get_class_input()
            self.model.insert_class(class_id, title, date_time, duration, location)
            self.view.show_message("Class added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_instructor(self):
        try:
            instructor_id, first_name, last_name, class_id = self.view.get_instructor_input()
            self.model.insert_instructor(instructor_id, first_name, last_name, class_id)
            self.view.show_message("Instructor added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_user_class(self):
        try:
            user_id, classes_id = self.view.get_user_class_input()
            self.model.insert_user_class(user_id, classes_id)
            self.view.show_message("User Class added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_users(self):
        try:
            users = self.model.show_users()
            self.view.show_users(users)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_classes(self):
        try:
            classes = self.model.show_classes()
            self.view.show_classes(classes)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_instructors(self):
        try:
            instructors = self.model.show_instructors()
            self.view.show_instructors(instructors)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_user_classes(self):
        try:
            user_classes = self.model.show_user_classes()
            self.view.show_user_classes(user_classes)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_user(self):
        try:
            id = self.view.get_user_id()
            user_id, phone_number, email, first_name, last_name = self.view.get_user_input()
            self.model.update_user(user_id, phone_number, email, first_name, last_name, id)
            self.view.show_message("User updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_instructor(self):
        try:
            id = self.view.get_instructor_id()
            instructor_id, first_name, last_name, class_id = self.view.get_instructor_input()
            self.model.update_instructor(instructor_id, first_name, last_name, class_id, id)
            self.view.show_message("Instructor updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_class(self):
        try:
            id = self.view.get_class_id()
            classes_id, title, date_time, duration, location = self.view.get_class_input()
            self.model.update_class(classes_id, title, date_time, duration, location, id)
            self.view.show_message("Class updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_user_class(self):
        try:
            id = self.view.get_user_id()
            user_id, class_id = self.view.get_user_class_input()
            self.model.update_user_class(user_id, class_id, id)
            self.view.show_message("User Class updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_user(self):
        try:
            user_id = self.view.get_user_id()
            self.model.delete_user(user_id)
            self.view.show_message("User deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_class(self):
        try:
            class_id = self.view.get_class_id()
            self.model.delete_class(class_id)
            self.view.show_message("Class deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_instructor(self):
        try:
            instructor_id = self.view.get_instructor_id()
            self.model.delete_instructor(instructor_id)
            self.view.show_message("Instructor deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_user_class(self):
        try:
            user_id = self.view.get_user_id()
            self.model.delete_user_class(user_id)
            self.view.show_message("User Class deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")