## Project info 
**TODO**

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

* `notebook.ipynb`  Notebook contains data  preparation, EDA and model selection.
* `train.py` Python file contains best model and saving model file. 
* `predict.py` Python file contains model file and serving as Flask app.
* `predict_test.py` Python file contains one observation for probility and CHD risk result. **(local solution)**
* `cloud_predict.py ` Python file contains model for one observation and includes cloud endpoint. **(cloud solution)**
* `requirements.txt` Txt file contains all dependencies  for notebook.ipynb and predictions scripts. 


## Preparing And Running Docker Images



_This will also be italic_

```bash
git clone https://github.com/yusyel/ML-bookcamp-midterm.git
```


```bash
cd ML-bookcamp-midterm
```

> In your python shell
```bash
pip install -r requirements.txt
```

> For building docker images:
```bash
docker build -t midterm .
```
> After building docker images you can run docker images with this command:

```bash
docker run -it --rm -p 9696:9696 midterm
```