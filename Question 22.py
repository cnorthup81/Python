import pandas as pd

salary = pd.read_csv("Cambridge_Salaries.csv")


#find out the totals and average would do more but im running out of time here proff
depart = salary.groupby("Department")
totaldepart = depart.sum()
avgdepart = depart.mean()
service = salary.groupby("Service")
totalservice = service.sum()
avgservice = service.mean()
sumsal = df['salary'].sum()
#give the data
print("The total salarys for each Department is:")
print(totaldepart)
print("The average salarys for each Department is:")
print(avgdepart)
print("The total salarys for each service is:")
print(totaldepart)
print("The average salarys for each service is:")
print(avgservice)
print ("total salarys are:")
print (sumal)
