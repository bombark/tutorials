import numpy as np
import sklearn
from sklearn                import svm
from sklearn.neighbors      import KNeighborsClassifier
from sklearn.metrics        import confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.metrics        import classification_report



print("1. Carregando os Dados de Treinamento")
treino_x = [
    [-2,-2],
    [2,2],
    [2,-2],
    [-2,2],
    [0,0]
]

treino_y = [1,2,1,2,3]


print("2. Escolhendo o Classificador")
classificador = sklearn.neighbors.KNeighborsClassifier(n_neighbors=1)
#classificador = svm.SVC(kernel='linear')
#classificador  = MLPClassifier()

print("3. Treinando!")
classificador.fit(treino_x, treino_y)


print("4. Classificando!")
teste_x = [ [-3,-3], [3,3], [3,4], [-2,0] ]
teste_classificado = classificador.predict(teste_x)


print("5. Metricas")
teste_y = [1,2,2,3]
report = classification_report(teste_y, teste_classificado)
print(report)

print("5.1. matriz de Confusao")
confusion = confusion_matrix(teste_y, teste_classificado)
print(confusion)
print()
print()


print("6. Como foi classificado")
print(teste_x)
print(teste_classificado)
