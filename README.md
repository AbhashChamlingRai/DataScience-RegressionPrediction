# Regression: Predictions for car prices
This repository contains my first complete data science project from web scrapping for data to data preprocessing, cleaning and model training.

If you wish to continue without reading everything, open "Scripts/ModelTraining.ipynb" which is notebook(jupyter) of the model training stage.
It has links to all other scripts(python-web scrapping), csv files(dataset) and notebooks(data preprocessing and exploratory data anaysis).

Tools used:
1. pandas
2. matplotlib
3. seaborn
4. scipy
5. regex
6. numpy
7. missingno
8. pickle
9. sklearn
10. beautifulsoup4
11. jupyter lab

The webscrapped data was very messey and took a lot of time and coding to get it cleaned. Hence, in addition to the web scrapper(python script), there are 3 different notebook(jupyter) for data cleaning, exploratory data analysis and model training respectively. Read below for the directory of each notebooks.

This project consists of 4 parts:

Web scrapping(Folder --> Scripts/Step1-WebScrapper) :
1. Information about cars were scrapped from "ccarprice.com/au/" and stored as a csv file in tabular form.<br>
   For the web scrapper(go to) --> Scripts/Step1-WebScrapper/scrapper.py
   
2. Price of cars in Australian dollars is the target feature and to predict it, there are many other independent features.<br>
   For the unprocessed csv(go to) --> Scripts/Step1-WebScrapper/car_prices_australia.csv

Data preprocessing and cleaning (Folder --> Scripts/Step2-DataCleaning) : 
1. Step 1 (Folder --> Scripts/Step2-DataCleaning/Step1) : <br>
    In step 1 :<br>
        a. Dataset is imported (Scripts/Step1-WebScrapper/car_prices_australia.csv).<br>
        b. Duplicates are handeled.<br>
        c. Feature selection is performed.<br>
        d. Features are modified; the structural errors are fixed and hence turned into usable features.<br>
        e. Data types are properly set for each features to its accurate one.<br>
        f. Columns names are renamed.<br>
        g. Null values are dealt with by using median or mode imputation.<br>
        h. With the help of visualization tools (matplotlib & seaborn), outiers are figured out and dealt with by either trimming it or using quantile based flooring and capping.<br>
        i. Unique values with very low frequency of categorical and interval(numerical) are either removed or replaced.<br>
        j. Processed and cleaned dataset is saved (Scripts/Step2-DataCleaning/Step1/step1-Completed.csv)<br><br>
    
      For the notebook(jupyter) of step 1(go to) --> Scripts/Step2-DataCleaning/Step1/Step1-FixingStructuralErrors.ipynb<br><br>
      For the step 1 completed csv(go to) --> Scripts/Step2-DataCleaning/Step1/step1-Completed.csv<br><br>
    
    Hence, the dataset as result of step 1 is clean and can be directly used to train model, but exploratory data analysis is done in step 2 to get to know the dataset better and possibly figure out any errors in the dataset if there are any.<br><br>
 
2. Step 2 (Folder --> Scripts/Step2-DataCleaning/Step2) :
    In step 2 of data preprocessing :
    a. 
    b. Exploratory data analysis is performed, 
    c. feature distribution and correlations are visualized.
    d. The features distribution are still skewed so, the best transformation(QuantileTransformer) is figured out which will be used later in model training.
        For the notebook(jupyter) of step 2(go to) --> Scripts/Step2-DataCleaning/Step2/Step2-EDA.ipynb
        For the step 2 completed csv(go to) --> Scripts/Step2-DataCleaning/Step2/Step2-Completed.csv
    
Model Training:
For the notebook(jupyter) of model training(go to) --> Scripts/ModelTraining.ipynb
1. The names of features and any nominal values are stored for future use.
    For the stored file(go to) --> Scripts/Models/Feature-Options/options.txt

1. In this stage, numeric features are transformed using "QuantileTransformer" from sklearn which are then fed into several supervised regression models for choosing the best one. The tranformer object of the test dataset are stored using "pickle"; a python library which are used to perform inverse transformation.
    For saved transformer object of independent variables(go to) --> Scripts/Models/Independent_Features_QuantileTransformer.pkl
    For saved transformer object of target variable(go to) --> Scripts/Models/Target_Feature_QuantileTransformer.pkl
    
2. Hyperparameters tuning of the choosen model(RandomForestRegressor) is performed using "RandomizedSearchCV" from sklearn. The tuned model is stored using "pickle" again.
    For the saved model(go to) --> Scripts/Models/Model.pkl

3. A scatter plot of actual unsclaled target values vs predicted(which is also inverse transformed) values is created.