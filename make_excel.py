import pandas as pd
import numpy as np
import faker as fk

fake = fk.Faker()


def make_excel(num):
    dep_shorthead_list = ['FNS', 'FME', 'FCS', 'FHS', 'FHSS']
    departament_list = ['Faculty of Natural Science', 'Faculty of Management and Economics', 'Faculty of Computer Science',
                        'Faculty of Health Sciences', 'Faculty of Humanities and Social Science']
    signs = ['-', ' ']
    city_list = ['Gdansk', 'Gdynia', 'Sopot']
    fake_excel = [{'departament_id': dep_shorthead_list[x]+signs[0]+str(fake.random_int(min=1935, max=2021))
                                     +signs[0]+str(fake.unique.random_int(min=100, max=999)),
                   'departament_name': departament_list[x],
                   'address': fake.street_name()+signs[1]+str(fake.random_int(min=1, max=300)),
                   'zip_code': fake.zipcode(),
                   'city': np.random.choice(city_list, p=[0.7, 0.1, 0.2]),
                   'employees_no': fake.random_int(min=30, max=120),
                   'students_no': fake.random_int(min=99, max=500)} for x in range(num)]

    return fake_excel


excel_df = pd.DataFrame(make_excel(num=5))
excel_df.to_csv('excel.csv', index=False)
