import pandas as pd
import numpy as np
import faker as fk
import random
from datetime import datetime

# Faker setup
fake = fk.Faker()
fk.Faker.seed(2001)


numC = 21   # number of available courses
numSu = 37  # number of available subjects


def make_students(numS):
    school_list = ['Liceum', 'Technikum', 'Other']
    higher_education_list = (0, 1)
    voivodeship_list = ['mazowieckie', 'slaskie', 'wielkopolskie', 'malopolskie', 'dolnoslaskie', 'lodzkie',
                        'pomorskie', 'lubelskie', 'podkarpackie', 'kujawsko-pomorskie', 'zachodnio-pomorskie',
                        'warminsko-mazurskie', 'swietokrzyskie', 'podlaskie', 'lubuskie', 'opolskie']
    fake_students = []

    for x in range(numS):
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        fake_students.append({'PESEL': fake.unique.random_int(min=10000000000, max=99999999999),
                              'gender': gender,
                              'name1': fake.first_name_male() if gender == "M" else fake.first_name_female(),
                              'name2': fake.first_name_male() if gender == "M" else fake.first_name_female(),
                              'surname': fake.last_name(),
                              'birth date': fake.date_between(start_date='-70y', end_date='-17y'),
                              'phone_number': fake.unique.random_int(min=100000000, max=999999999),
                              'email': fake.ascii_email(),
                              'school': np.random.choice(school_list, p=[0.50, 0.45, 0.05]),
                              'previous_higher_education': np.random.choice(higher_education_list, p=[0.85, 0.15]),
                              'voivodeship': np.random.choice(voivodeship_list,
                                                              p=[0.14, 0.12, 0.09, 0.09, 0.08, 0.06, 0.06,
                                                                 0.06, 0.06, 0.05, 0.04, 0.04, 0.03, 0.03,
                                                                 0.03, 0.02]),
                              'city': fake.city(),
                              'street': fake.street_name(),
                              'number': fake.random_int(min=1, max=1000),
                              'zip-code': fake.zipcode()})

    return fake_students


def make_results(numS, students_df):
    subject_list = ["Polish", "Mathematics", "Foreign Language", "Biology", "Chemistry", "Physics", "Geography",
                    "History", "Informatics", "Other"]
    fake_results = []
    index = 1

    for x in range(numS):
        sub_list = []
        y = 0
        while y < 3:
            subject = np.random.choice(subject_list, p=[0.07, 0.25, 0.3, 0.05, 0.07, 0.11, 0.05, 0.01, 0.08, 0.01])
            if subject not in sub_list:
                sub_list.append(subject)
                fake_results.append({'id': index,
                                     'subject_name': subject,
                                     'percentage_result': fake.random_int(min=0, max=100),
                                     'centile_result': fake.random_int(min=0, max=100),
                                     'weight': random.random(),
                                     'student': students_df['PESEL'][x]})
                index += 1
            else:
                y -= 1
            y += 1

    return fake_results


def make_applications(numS, students_df, year):
    status_list = ["Successful", "Unsuccessful", "NULL"]
    fake_applications = []
    index = 1

    for x in range(numS):
        c_list = []
        y = 0
        while y < 5:
            course = fake.random_int(min=1, max=21)
            if course not in c_list:
                c_list.append(course)
                fake_applications.append({'id': index,
                                          'date': fake.date_between(start_date=datetime(year, 6, 1),
                                                                    end_date=datetime(year, 10, 1)),
                                          'priority': y + 1,
                                          'status': np.random.choice(status_list, p=[0.3, 0.5, 0.2]),
                                          'course': course,
                                          'student': students_df['PESEL'][x]})
                index += 1
            else:
                y -= 1
            y += 1

    return fake_applications


def make_subjects(course_df):
    subject_list = ['sports', 'English', 'physics I', 'databases', 'biology', 'computer graphics',
                    'programming languages', 'programming basics', 'statistics',
                    'artificial intelligence', 'psychology', 'precalculus', 'linear algebra', 'calculus',
                    'engineering physics', 'digital circuits', 'object-oriented programming',
                    'chemistry I', 'chemistry II', 'chemistry III', 'physics II', 'physics III',
                    'crystallography', 'numerical methods', 'internships', 'logistics', 'logic',
                    'business', 'geometry', 'optics', 'anatomy', 'biochemistry', 'human physiology',
                    'diseases', 'viruses', 'legal history', 'civil law']
    stream_list = [fake.color_name() for _ in range(3)]
    form_list = ('test', 'exam')
    fake_subjects = []
    index = 1

    for x in range(numSu):
        c_list = []
        y = 0
        while y < 4:
            course = fake.random_int(min=1, max=21)
            if course not in c_list:
                c_list.append(course)
                fake_subjects.append({'id': index,
                                      'stream': np.random.choice(stream_list),
                                      'name': subject_list[x],
                                      'form': np.random.choice(form_list, p=[0.6, 0.4]),
                                      'ECTS': fake.random_int(min=0, max=10),
                                      'semester': fake.random_int(min=1, max=course_df['number_of_sem'][course - 1]),
                                      'course': course})
                index += 1
            else:
                y -= 1
            y += 1

    return fake_subjects


def make_course():
    course_list = ['Biotechnology', 'Biology', 'Genetics', 'Chemical Business', 'Chemistry', 'Environmental protection',
                   'Economy', 'International relations', 'Physics', 'Computer Science', 'Data Engineering',
                   'Mathematics',
                   'Medical Analytics', 'Physiotherapy', 'Pharmacy', 'Law', 'Canon Law', 'Psychology', 'Journalism',
                   'Sociology', 'Criminology']
    sem_num_list = [6, 6, 6, 7, 6, 6, 6, 6, 6, 7, 7, 6, 10, 10, 11, 10, 10, 10, 6, 6, 6]

    fake_courses = [{'id': x + 1,
                     'name': course_list[x],
                     'number_of_hours': sem_num_list[x] * fake.random_int(min=300, max=340),
                     'number_of_sem': sem_num_list[x],
                     'language': 'english' if course_list[x] in ('Environmental protection', 'Economy',
                                                                 'Data Engineering', 'Canon Law') else 'polish',
                     'place_limit': fake.random_int(min=0, max=400)} for x in range(numC)]

    return fake_courses


def make_achievements(numAc, students_df):
    field_list = ['Sport', 'Knowledge', 'Voluntary work']
    level_list = ['international', 'national', 'provincial', 'district']
    fake_achievements = []

    for x in range(numAc):
        fake_achievements.append({'id': x + 1,
                                  'field': np.random.choice(field_list, p=[0.35, 0.4, 0.25]),
                                  'level': np.random.choice(level_list, p=[0.1, 0.2, 0.3, 0.4]),
                                  'short_description': fake.pystr(min_chars=None, max_chars=500),
                                  'student': students_df['PESEL'][fake.random_int(min=0, max=numS-1)]})

    return fake_achievements


def update_applications(U_applications_df):
    status_list = ['Successful', 'Unsuccessful', 'NULL']

    for index, value in enumerate(U_applications_df['status']):
        if value != value:  # if NaN
            U_applications_df.loc[index, 'status'] = np.random.choice(status_list, p=[0.38, 0.6, 0.02])

    return U_applications_df


def add_new_values_to_csv(numS, numAc, year, mode, header):
    students_df = pd.DataFrame(make_students(numS))
    results_df = pd.DataFrame(make_results(numS, students_df))
    applications_df = pd.DataFrame(make_applications(numS, students_df, year))
    course_df = pd.DataFrame(make_course())
    subjects_df = pd.DataFrame(make_subjects(course_df))
    achievements_df = pd.DataFrame(make_achievements(numAc, students_df))

    students_df.to_csv('students.csv', mode=mode, index=False, header=header)
    results_df.to_csv('results.csv', mode=mode, index=False, header=header)
    applications_df.to_csv('applications.csv', mode=mode, index=False, header=header)
    subjects_df.to_csv('subjects.csv', mode=mode, index=False, header=header)
    course_df.to_csv('course.csv', mode=mode, index=False, header=header)
    achievements_df.to_csv('achievements.csv', mode=mode, index=False, header=header)


# Using this script
# Decide on the setup
numS = 5000     # number of generated applicants
numAc = 3750    # number of saved achievements
year = 2020     # year of the application round
mode = 'w'      # mode of saving data: 'w' for write and 'a' to append
header = True   # header arrangements: if mode = 'w' header = True, else = False

# Create and save/append the data set
add_new_values_to_csv(numS, numAc, year, mode, header)

# Update
U_applications_df = pd.read_csv('applications.csv')
U_applications_df2 = update_applications(U_applications_df)
U_applications_df2.to_csv('applicationsUpdate.csv', index=False)
