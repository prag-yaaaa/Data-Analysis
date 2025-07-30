# Data-Analysis
This is a healthcare data analytics project.
The Dataset used has been imported from Kaggle.

The dataset contains a diverse range of health-related attributes, meticulously collected to aid in the development of predictive models for identifying individuals at risk of diabetes. The Dataset consists of columns as :

ID : Unique identifier for each data entry
Pregnancies : Number of times pregnant.
Glucose : Plasma glucose concentration over 2 hours in an oral glucose tolerance test.
BloodPressure : Diastolic blood pressure (mm Hg)
SkinThickness : Triceps skinfold thickness (mm)
BMI : Body mass index (weight in kg/height in m^2)
DiabetesPedigreeFunction : Diabetes pedigree function, a genetic score of diabetes.
Age : Age in years.
Outcome : Binary classification indicating the presence (1) or absence (0) of diabetes.
Insulin : 2 Hour Serum Insulin (mu U/ml) This datset can be useful to explore the relationships between various health indicators and the likelihood of diabetes.

Issue Identification : Does the person have DIABETES?

In this project, data imported from Kaggle has been:
1. Imported
2. Cleaned
3. Performed EDA (Exploratory Data Analysis)
4. Model Building - to predict whether a person has diabetes or not.
5. The created model has been saved to a pickle file.
6. next an app is created through streamlit using the same saved model i.e. pickle file.
7. User can input their health data and predict whether they have diabetes or not.
