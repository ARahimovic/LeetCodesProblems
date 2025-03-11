'''
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output: 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation: 
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.

'''

'''
The first method with filtering and count use a lot of time, because each time we filter the rows then count 
the second method using sum() is much simpler, the boolearn will return true(1) or false(0), we just have to use sum() (it is a dtaframe method applicable for dataframe or series)
sum method will summ all the elements column wise (index = 0 )or row wise (index = 1)
'''

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'], 
       # 'accounts_count' : [accounts[accounts.income < 20000].income.count(), accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].income.count(), accounts[accounts.income > 50000].income.count()] 
         'accounts_count' : [(accounts.income < 20000).sum(), ((accounts.income >= 20000) & (accounts.income <= 50000)).sum(), (accounts.income > 50000).sum()] 
        })
   
    return result
    
