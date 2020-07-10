# SEFR: A Fast Linear-Time Classifier for Ultra-Low Power Devices

A Python package for the paper [SEFR: A Fast Linear-Time Classifier for Ultra-Low Power Devices](https://arxiv.org/abs/2006.04620) 
by Hamidreza Keshavarz, Mohammad Saniee Abadeh, Reza Rawassizadeh

Copied from [original implementation](https://github.com/sefr-classifier/sefr)

### How to install

```bash
pip install sefr
```

### How to use

```python
from sefr import SEFR
from sklearn.datasets import load_iris


iris = load_iris()
X, y = iris.data, iris.target
X = X[y < 2]
y = y[y < 2]
clf = SEFR()
clf.fit(X, y)
print(clf.predict(X) == y)
```