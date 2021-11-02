# %%
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
import sklearn.metrics as metrics

# %%
df = pd.read_csv('framingham.csv')
df.columns = df.columns.str.lower()
df['male'] = df['male'].astype(str)
df['education'] = df['education'].astype(str)
df['currentsmoker'] = df['currentsmoker'].astype(str)
df['bpmeds'] = df['bpmeds'].astype(str)
df['prevalentstroke'] = df['prevalenthyp'].astype(str)
df['diabetes'] = df['diabetes'].astype(str)
df['prevalenthyp'] = df['prevalenthyp'].astype(str)

# %%
numerical = ['age', 'cigsperday', 'totchol', 'sysbp',
             'diabp', 'bmi', 'heartrate', 'glucose']
categorical = ['male', 'education', 'currentsmoker', 'bpmeds',
               'prevalentstroke', 'prevalenthyp', 'diabetes']
# %%
df.education = df.education.fillna(0)
df.bpmeds = df.bpmeds.fillna(0)
df[categorical].isnull().sum()


# %%
df[numerical].isnull().sum()
df.cigsperday = df.cigsperday.fillna(df.cigsperday.mean())
df.heartrate = df.heartrate.fillna(df.heartrate.mean())
df.glucose = df.glucose.fillna(df.glucose.mean())
df.totchol = df.totchol.fillna(df.totchol.mean())
df.bmi = df.bmi.fillna(df.bmi.mean())

df.isnull().sum()
# %%
from sklearn.model_selection import train_test_split
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)
len(df_train), len(df_val), len(df_test)
# %%
df_train = df_train.reset_index(drop = True)
df_val = df_val.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)
# %%
y_train = df_train.tenyearchd.values
y_val = df_val.tenyearchd.values
y_test = df_test.tenyearchd.values
# %%
del df_train['tenyearchd']
del df_val['tenyearchd']
del df_test['tenyearchd']

# %%
train_dicts = df_train.to_dict(orient = 'records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
X_train.shape

#%%

val_dict = df_val.to_dict(orient='records')
dv_val = DictVectorizer(sparse = False)

X_val = dv_val.fit_transform(val_dict)
X_val.shape


# %%
import xgboost as xgb
features = dv.get_feature_names()
# %%
dtrain = xgb.DMatrix(X_train, label = y_train, feature_names=features)
dval = xgb.DMatrix(X_val, label = y_val, feature_names=features)

# %%
xgb_params = {
    'eta': 0.01,
    'max_depth': 3,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
    'alpha' :3,
    'lambda':2,
    'subsample':0.5,
    'colsample_bytree':0.9,
    'tree_method':'exact'
}

model = xgb.train(xgb_params, dtrain, num_boost_round=150)


y_pred = model.predict(dval)
auc = roc_auc_score(y_val, y_pred)
acc = accuracy_score(y_val, y_pred>= 0.5)
print(auc, acc)




# %%

import pickle
# %%
output_file = 'model.bin'


with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)