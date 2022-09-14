'''
# Sample code to perform I/O:

name = input()          # Reading input from STDIN
print('Hi, %s.') % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
T = int(input())
temp = input().split(" ")
N = [int(x) for x in temp]

for j in N:
    for i in range(1, j+1):
        mod3, mod5 = (i%3 == 0), (i%5 == 0)
        if mod3 and mod5:
            print("FizzBuzz")
        elif mod5:
            print("Buzz")
        elif mod3:
            print("Fizz")
        else:
            print(i)


"""
# CREATE DATABASE company
# USE company
# CREATE  TABLE IF NOT EXISTS 'Sales' (
#   'InvoiceNo' INT  AUTOINCREMENT ,
#   'SalesPerson' VARCHAR(150) NOT NULL ,
#   'TotalSale' INT ,
#   `date_of_birth` DATE ,
#   `physical_address` VARCHAR(255) ,
#   `postal_address` VARCHAR(255) ,
#   `contact_number` VARCHAR(75) ,
#   `email` VARCHAR(255) ,
#   PRIMARY KEY (`membership_number`) )
# ENGINE = InnoDB;
# 
# INSERT INTO `members` (`full_names`,`gender`,`physical_address`,`contact_number`) VALUES ('Leonard Hofstadter','Male','Woodcrest',0845738767); 

select
  sum(a) as atotal,
  sum(b) as btotal,
  sum(c) as ctotal
from
  yourtable t
where
  t.id in (1, 2, 3)
  
select max(T.avg_salary)
from (select SalesPerson, avg(TotalSale) AS avg_salary
      from Sales
      group by SalesPerson) AS T;

  
SELECT FORMAT(max(TotalSale), 4) from Sales;
"""