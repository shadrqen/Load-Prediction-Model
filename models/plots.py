from models.data import data
from models.imports import *

#histogram of applicant income
data['ApplicantIncome'].hist(bins=50)
plt.show()

#applicant income against the coapplicant income
plt.plot([data['ApplicantIncome']],[data['CoapplicantIncome']], 'r^')
plt.show()

#applicant income against the total instances of applicant income
plt.plot([data['ApplicantIncome']],[range(1,614)], 'r^')
plt.show()

# boxplot for applicant income
data.boxplot(column='ApplicantIncome')
plt.show()

#applicant income by the type of education achieved
data.boxplot(column='ApplicantIncome', by = 'Education')
plt.show()

#applicant income by gender
data.boxplot(column='ApplicantIncome', by = 'Gender')
plt.show()

#applicant income by gender and marital status
data.boxplot(column='ApplicantIncome', by = ['Gender','Married'])
plt.show()

#applicant income by marital status and education
data.boxplot(column='ApplicantIncome', by = ['Married', 'Education'])
plt.show()

#applicant income by gender and education
data.boxplot(column='ApplicantIncome', by = ['Gender', 'Education'])
plt.show()

#applicant income by self employment status
data.boxplot(column='ApplicantIncome', by = ['Self_Employed'])
plt.show()

#applicant income by credit history
data.boxplot(column='ApplicantIncome', by = ['Credit_History'])
plt.show()

#applicant income by property area
data.boxplot(column='ApplicantIncome', by = ['Property_Area'])
plt.show()

#applicant income by loan status
data.boxplot(column='ApplicantIncome', by = ['Loan_Status'])
plt.show()

#applicant credit history versus the loan status
data.boxplot(column='Credit_History', by = ['Loan_Status'])
plt.show()

#applicant income versus the loan status
data.boxplot(column='ApplicantIncome', by = ['Loan_Status'])
plt.show()