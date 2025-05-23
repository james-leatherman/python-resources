# https://leetcode.com/studyplan/introduction-to-pandas/

import pandas as pd

# 2877. Create a DataFrame from List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# 2878. Get the Size of a DataFrame

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]

# 2879. Display the First Three Rows

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# 2880. Select Data

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

# 2881. Create a New Column

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

# 2882. Drop Duplicate Rows

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers

# 2883. Drop Missing Data

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(axis=0, subset=['name'], inplace=True)
    return students

# 2884. Modify Columns

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

    # Raw Python
def modifySalaryColumnFaster(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = [int(i) * 2 for i in employees['salary']]
    return employees

    # Lambda
def modifySalaryColumnLambda(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].map(lambda x: x * 2)
    return employees

    k = employees.apply(fun, 1)
    return k

# 2885. Rename Columns

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years"
        }
        inplace=True # False is default
    )
    return students

    # Raw Python
def renameColumnsFaster(students: pd.DataFrame) -> pd.DataFrame:
    students.columns=['student_id',
                      'first_name',
                      'last_name',
                      'age_in_years'
                      ]
    return students

# 2886. Change Data Type

def changeDatatype1(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int}) # creates df copy

def changeDataType2(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int) # modifies in place
    return students

def changeDatatype3(students: pd.DataFrame) -> pd.DataFrame:
    students['grade']=students.grade.astype(int)
    return students

    # Use changeDatatype1 if you need to preserve the original DataFrame or perform multiple column type conversions.
    # Use changeDataType2 if you want a memory-efficient solution and are only modifying a single column.
    # Use changeDatatype3 if you prefer dot notation and are confident there are no naming conflicts with the column name.

# 2887. Fill Missing Data

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products

# 2888. Reshape Data: Concatenate

    # List
def concatenateTables1(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

    # Tuple
def concatenateTable2(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat((df1, df2))

    # Database merge
def concatenateTables3(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.merge(df2, how = 'outer')

    # Five ways
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # df = pd.concat([df1,df2])
    # return df
    # return pd.concat([df1, df2], axis=0)
    # return pd.merge(df1, df2, how='outer')
    # return df1.merge(df2, how='outer')
     return df1._append(df2)

# 2889. Reshape Data: Pivot

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    )

# 2890. Reshape Data: Melt

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=['product'], 
        # value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name='quarter',
        value_name='sales'
    )

# 2891. Method Chaining

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_animals = animals[animals['weight'] > 100]
    sorted_animals = filtered_animals.sort_values(by='weight', ascending=False)
    names = sorted_animals[['name']]
    return names

def findHeavyAnimalsOneLiner(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.sort_values(
        by=['weight'],
        ascending=False
    ).loc[
        animals["weight"] > 100,
        : "name"
    ].reset_index(drop=True)