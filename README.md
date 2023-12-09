# Laptop Price Prediction

Simple overview of use/purpose.

For this project, I developed a laptop price prediction model. After several iterations and testing, the best model was deployed using Streamlit, a powerful tool for building interactive web apps.


## Description

The project aims to develop a machine learning model that predicts laptop prices based on key characteristics and specifications. By analyzing various features such as processor type, RAM size, storage capacity, screen resolution, brand, and other relevant attributes, the model will identify the most influential factors impacting laptop prices. The goal is to create a reliable predictive model that assists consumers, retailers, and manufacturers in estimating the price range of laptops given their specifications. This model could significantly benefit consumers in making informed purchasing decisions and assist retailers in setting competitive prices.

### Key Objectives:

Identify Key Characteristics: The primary goal is to determine the most significant features affecting laptop prices through exploratory data analysis. This involves understanding correlations, feature importance, and the impact of different attributes on pricing.
Machine Learning Algorithm Selection: Evaluate and select the most suitable machine learning algorithm for price prediction. Considering the nature of the dataset, algorithms such as linear regression, decision trees, random forests, or gradient boosting was assessed for their predictive performance.
Deployment with Streamlit: The final model was deployed using Streamlit, a user-friendly framework for creating web applications with Python. The deployed application will enable users to input laptop specifications and receive a predicted price range based on the trained machine learning model.

## Getting Started
Before stating, there is need to update some libraries to the latest version to prevent error during the deployment. 


### Dependencies

Windows 10, Visual studio, and streamlit account


### Installing

* streamlit
* scikit-learn
* pandas
* numpy
* joblib
* xgboost == 2.0.1
  
### Executing program

The project contains two executable files, the model and the dowloaded files from the laptop-price-prediction-notebook.

#### The two executable files are:

* laptop-price-prediction-notebook.ipynb : Includes all functions required for classification operations, this notebook will download model "laptop4.sav".
* app.py : This file contains the code for streamlit deployment of the best model, which can be run with the code below in VScode.
```
streamlit run app.py
```


## Help

If there is any issue, you should try and update the libraries used like Sklearn, numpy and pandas during deployment 


## Authors

Contributors names and contact info

* Emeka


## License

This project is licensed under the [Emeka] License.
