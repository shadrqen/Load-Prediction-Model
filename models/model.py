from models.imports import *
from models.data import data

#filling the empty or NaN fields in all rows
data['Gender'].fillna(data['Gender'].mode()[0], inplace=True)
data['Married'].fillna(data['Married'].mode()[0], inplace=True)
data['Dependents'].fillna(data['Dependents'].mode()[0], inplace=True)
data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0], inplace=True)
data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)
data['LoanAmount'].fillna(data['LoanAmount'].mean(), inplace=True)
data['Self_Employed'].fillna('No',inplace=True)

# Since, sklearn requires all inputs to be numeric, we should convert all our categorical variables into numeric by encoding the categories.
var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']

le = LabelEncoder()
for i in var_mod:
    data[i] = le.fit_transform(data[i])


# Generic function for making a classification model and accessing performance:
def classification_model(model, data, predictors, outcome):
    # Fit the model:
    model.fit(data[predictors], data[outcome])

    datachoice = input("Which test data should we use? \n"
          "1. The training set \n"
          "2. Enter Manually")

    if int(datachoice) == 1:
        # Make predictions on training set:
        predictions = model.predict(data[predictors])
        # Perform k-fold cross-validation with 5 folds
        # Print accuracy
        accuracy = metrics.accuracy_score(predictions, data[outcome])
        print("Accuracy : %s" % "{0:.3%}".format(accuracy))
        kf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=None)
        error = []
        for train, test in kf.split(np.zeros(data.shape[0])):
            # Filter training data
            train_predictors = (data[predictors].iloc[train, :])

            # The target we're using to train the algorithm.
            train_target = data[outcome].iloc[train]

            # Training the algorithm using the predictors and target.
            model.fit(train_predictors, train_target)

            # Record error from each cross-validation run
            error.append(model.score(data[predictors].iloc[test, :], data[outcome].iloc[test]))
        print("Cross-Validation Score : %s" % "{0:.3%}".format(np.mean(error)))
        print("\n")

    elif int(datachoice) ==2:
        try:
            credithistory = input("Credit History: ")
            education = input("Education")
            married = input("Married")
            selfemployed = input("Self Employed")
            propertyarea = input("Property_Area")
            # data2predict = np.array([credithistory,education,married,selfemployed,propertyarea])

            data2predict = {'Credit_History': [credithistory], 'Education': [education], 'Married': [married],
                            'Self_Employed': [selfemployed], 'Property_Area': [propertyarea]}
            dataframe = pd.DataFrame(data=data2predict)

            predictions = model.predict(dataframe)
            print(dataframe)
            print("The predicted loan status is ---------   ", predictions, "   --------")
        except ValueError as e:
            print("Kindly enter numbers only!", e)
    else:
        return 0

    # Fit the model again so that it can be refered outside the function:
    model.fit(data[predictors], data[outcome])


def predict(model):
    outcome_var = 'Loan_Status'
    predictor_var = ['Credit_History', 'Education', 'Married', 'Self_Employed', 'Property_Area']
    classification_model(model, data, predictor_var, outcome_var)

while 1:
    try:
        choice = input("Please choose the algorithm: \n"
              "1. LogisticRegression. "
              "2. DecisionTreeClassifier. "
              "3. RandomForestClassifier. ")
        if int(choice) == 1:
            model = LogisticRegression(solver='lbfgs')
            predict(model)
        elif int(choice) == 2:
            model = DecisionTreeClassifier()
            predict(model)
        elif int(choice) == 3:
            model = RandomForestClassifier(n_estimators=100)
            predict(model)
        else:
            break

    except ValueError as e:
        print("Kindly enter numbers only when choosing the algorithm!", e)