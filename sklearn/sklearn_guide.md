# Intro

It is possible to save a model in scikit-learn by using Python’s built-in persistence model, `pickle`. In the specific case of scikit-learn, it may be more interesting to use `joblib`’s replacement for `pickle`.

Unless otherwise specified, input will be cast to `float64`. Regression targets are cast to float64 and classification targets are maintained.

# Glossary 

- estimator: a Python object that implments the methods `fit(X,  y)` and `predict(T)`.

# API 

## `sklearn.datasets`

utilites to load datasets, including methods to load and fetch popular reference datasets.

scikit-learn comes with a few standard datasets, for instance the iris and digits datasets for classification and the boston house prices dataset for regression.

## `sklearn.preprocessing`

The sklearn.preprocessing module includes scaling, centering, normalization, binarization and imputation methods.

- class `StandardScaler`: Standardize features by removing the mean and scaling to unit variance. The standard score of a sample x is calculated as $z = \dfrac{x - u}{s}$.

## `sklearn.model_selection`

- `train_test_split()`: split arays or matrices into random train and test subsets




