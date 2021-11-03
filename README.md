## Project info 
Data was originally used my biostatistics class and I want to try all classification algorithms and parameter tuning to see how much I can improve auc and accuracy score.

Target variable is risk of in ten year CHD (<i>Coronary heart disease</i>). Coded as binary (0,1). Given all patient medical history calculating predictions risk of ten year may occur CHD.

It's classification problem can be solve logistic regression, decision tree and random forest.



## Variables Descriptions

 * **Sex:** male or female(Nominal)
* **Age:** Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
Behavioral
* **Current Smoker:** whether or not the patient is a current smoker (Nominal)
* **Cigs Per Day:** the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)
Medical( history)
* **BP Meds:** whether or not the patient was on blood pressure medication (Nominal)
* **Prevalent Stroke:** whether or not the patient had previously had a stroke (Nominal)
* **Prevalent Hyp:** whether or not the patient was hypertensive (Nominal)
* **Diabetes:** whether or not the patient had diabetes (Nominal)
Medical(current)
* **Tot Chol:** total cholesterol level (Continuous)
* **Sys BP:** systolic blood pressure (Continuous)
* **Dia BP:** diastolic blood pressure (Continuous)
* **BMI:** Body Mass Index (Continuous)
* **Heart Rate:** heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
* **Glucose:** glucose level (Continuous)
* **Target Variable:** 10 year risk of coronary heart disease CHD (binary: “1”, means “Yes”, “0” means “No”)


**Data and variable source**:  [Kaggle](https://www.kaggle.com/dileep070/heart-disease-prediction-using-logistic-regression)



## File Descriptions

* `notebook.ipynb`  Notebook contains data  preparation, EDA, feature importance, parameter tuning and  model selection.
* `train.py` Python file contains best model and saving model file. (<i>Exported script</i>)
* `predict.py` Python file contains model file and serving as Flask app.
* `predict_test.py` Python file contains one observation for probility and CHD risk result. **(local solution)**
* `cloud_predict.py ` Python file contains model for one observation and includes cloud endpoint. **(cloud solution)**
* `requirements.txt` Txt file contains all dependencies  for notebook.ipynb and predictions scripts. 


## Preparing Python Environments



_This will also be italic_

```bash
git clone https://github.com/yusyel/ML-bookcamp-midterm.git
```


```bash
cd ML-bookcamp-midterm
```

> Activate python environments
```bash
pipenv shell
```
> In python environment installing python dependency:

```bash
pip install -r requirements.txt
```
## Preparing And Running Docker Images


> For building docker images:
```bash
docker build -t midterm .
```
> After building docker images you can run docker images with this command:

```bash
docker run -it --rm -p 9696:9696 midterm
```

## Runing Predictions File

> In your python shell:

```bash
python3 predict_test.py
```
* Result will be randomly selected patient risk of ten year CHD result and probability.

> Cloud test. `cloud_predict.py` contains server endpoint.

```bash
python3 cloud_predict.py
```

* Result will be randomly selected patient risk of ten year CHD result and probability.