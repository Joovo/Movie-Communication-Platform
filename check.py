import pandas as pd

if __name__ == '__main__':

    person_df = pd.read_csv('./share_data/person.csv', header=0)
    person_df.columns = ['id', 'name', 'img', 'sex', 'birthday', 'birthplace', 'summary']
    for i in person_df.columns:
        print(max(person_df.loc[:,i].apply(str).apply(len)))

