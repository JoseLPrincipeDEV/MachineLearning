import sklearn 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#cargar el conjunto de datos iris
iris = load_iris()

X, y = iris.data, iris.target

"""
Dividir datos: Antes de entrenar un modelo de aprendizaje automaticó, 
es común dividir tus datos en conjuntos de entrenamiento y prueba:
"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""
Entrenar un modelo: Scikit-Learn proporciona una amplia variedad de algoritmos de aprendizaje automático que puedes utilizar para entrenar modelos en tus datos:
"""

#Crear un modelo de regresión logística 
model = LogisticRegression()

#entrenar el modelo en los dato de entrenamiento
model.fit(X_train,y_train)

"""
Evalular el modelo: Depués de entrenar un modelo, es importante evaluar su rendimiento en datos no vistos
"""
#