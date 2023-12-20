import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='Sport_Classes',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_user(self, user_id, phone_number, email, first_name, last_name):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."User"("User_id", "Phone_number", "Email", "First_name", "Last_name") VALUES(%s, %s, %s, %s, %s);', (user_id, phone_number, email, first_name, last_name))
        self.conn.commit()

    def add_class(self, classes_id, title, date_and_Time, duration, location):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Classes"("Classes_id", "Title", "Date_and_Time", "Duration", "Location") VALUES(%s, %s, %s, %s, %s);', (classes_id, title, date_and_Time, duration, location))
        self.conn.commit()

    def add_instructor(self, instructor_id, first_name, last_name, classes_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Instructor"("Instructor_id", "First_name", "Last_name", "Classes_id") VALUES(%s, %s, %s, %s);', (instructor_id, first_name, last_name, classes_id))
        self.conn.commit()

    def add_user_class(self, user_id, classes_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."User_Classes"("User_id", "Classes_id") VALUES(%s, %s);', (user_id, classes_id))
        self.conn.commit()

    def get_users(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."User";')
        return c.fetchall()

    def get_classes(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Classes";')
        return c.fetchall()

    def get_instructors(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Instructor";')
        return c.fetchall()

    def get_user_classes(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."User_Classes";')
        return c.fetchall()

    def get_instructor_classes(self):
        c = self.conn.cursor()
        c.execute('SELECT "Instructor"."First_name" AS "Instructor_FirstName", "Instructor"."Last_name" AS "Instructor_LastName", "Classes"."Title" FROM "Instructor" JOIN "Classes" ON "Instructor"."Classes_id" = "Classes"."Classes_id" ORDER BY "Classes"."Title";')
        return c.fetchall()

    def get_average_class_duration(self):
        c = self.conn.cursor()
        c.execute('SELECT "Instructor"."Instructor_id", "Instructor"."First_name", "Instructor"."Last_name", AVG("Classes"."Duration") AS "Average_Duration" FROM "Instructor" JOIN "Classes" ON "Instructor"."Classes_id" = "Classes"."Classes_id" GROUP BY "Instructor"."Instructor_id", "Instructor"."First_name", "Instructor"."Last_name";')
        return c.fetchall()

    def get_classes_with_number_of_users(self):
        c = self.conn.cursor()
        c.execute('SELECT "Classes"."Title", COUNT("User_Classes"."User_id") AS "User_Count" FROM "Classes" LEFT JOIN "User_Classes" ON "Classes"."Classes_id" = "User_Classes"."Classes_id" GROUP BY "Classes"."Title" ORDER BY "User_Count" DESC LIMIT 5;')
        return c.fetchall()

    def update_user(self, user_id, phone_number, email, first_name, last_name, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."User" SET User_id=%s, Phone_number=%s, Email=%s, First_name=%s, Last_name=%s WHERE User_id=%s', (user_id, phone_number, email, first_name, last_name, id))
        self.conn.commit()

    def update_class(self, classes_id, title, date_time, duration, location, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Classes" SET "Classes_id"=%s, "Title"=%s, "Date_and_Time"=%s, "Duration"=%s, "Location"=%s WHERE "Classes_id"=%s', (classes_id, title, date_time, duration, location, id))
        self.conn.commit()

    def update_instructor(self, instructor_id, first_name, last_name, classes_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Instructor" SET "Instructor_id"=%s, "First_name"=%s, "Last_name"=%s, "Classes_id"=%s WHERE "Instructor_id"=%s', (instructor_id, first_name, last_name, classes_id, id))
        self.conn.commit()

    def update_user_class(self, user_id, classes_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."User_Classes" SET "User_id"=%s, "Classes_id"=%s WHERE "User_id"=%s', (user_id, classes_id, id))
        self.conn.commit()

    def delete_user(self, user_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."User" WHERE "User_id"=%s', (user_id,))
        self.conn.commit()

    def delete_class(self, class_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Classes" WHERE "Classes_id"=%s', (class_id,))
        self.conn.commit()

    def delete_instructor(self, instructor_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Instructor" WHERE "Instructor_id"=%s', (instructor_id,))
        self.conn.commit()

    def delete_user_class(self, user_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."User_Classes" WHERE "User_id"=%s', (user_id,))
        self.conn.commit()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute("""
            WITH max_id AS (
                SELECT COALESCE(MAX("Classes_id"), 0) FROM public."Classes"
            )
            INSERT INTO public."Classes" ("Classes_id", "Title", "Date_and_Time", "Duration", "Location")
            SELECT (SELECT * FROM max_id) + row_number() OVER () as "Classes_id",
                   chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
                   current_date + (random() * 30)::integer * '1 day'::interval,
                   random() * 100,
                   chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int)
            FROM generate_series(1, %s);
        """, (number,))
        self.conn.commit()