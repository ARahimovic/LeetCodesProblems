'''
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
'''

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    department.set_index('id', inplace=True)
    employee['Department']= employee['departmentId'].map(department['name'])
    
    #return a panda series wiht departement name as its index
    highest_salaries = employee.groupby('Department').salary.max()
    result = employee[employee.apply(lambda x:x['salary']== highest_salaries[x['Department']], axis=1)]
    result.rename(columns={'name':'Employee'}, inplace=True)
    return result[['Department','Employee','salary']]

    '''
    different type of indexing 
        df['col'] will return panda series, a column
        df[['col]] will return a panda frame , still only a column
        df[['col1','col2']] will return a panda frame with two columns selected
        df[['col1','col2']][1:3] will select two columns and rows 1 to 2 , return a dataframe

        df.iloc[1:3, [indexCol1, indexCol2]]
        df.loc[1:3, ['col1','col2']]
   
    '''