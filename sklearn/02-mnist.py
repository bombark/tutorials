import numpy as np
import sklearn
import pickle
from sklearn                import svm
from sklearn.neighbors      import KNeighborsClassifier
from sklearn.metrics        import confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.metrics        import classification_report


print("1. Carregando os Dados de Treinamento")
file = open("treino_caracteristicas.pickle",'rb')
treino_x = pickle.load(file)
file = open("treino_labels.pickle",'rb')
treino_y = pickle.load(file)
print("  Quantidade de Exemplos para Treinamento:" + str(len(treino_x)) )


print("2. Escolhendo o Classificador")
classificador   = sklearn.neighbors.KNeighborsClassifier()
#classificador  = svm.SVC(kernel='linear')
#classificador  = MLPClassifier()


print("3. Treinando!")
classificador.fit(treino_x, treino_y)


print("4. Classificando!")
file = open("teste_caracteristicas.pickle",'rb')
teste_x = pickle.load(file)
teste_classificado = classificador.predict( teste_x )
print( "  Classificado : {} exemplos".format(len(teste_x)) )


print("5. Metricas")
file = open("teste_labels.pickle",'rb')
teste_verdadeiro = pickle.load(file)
report = classification_report(teste_verdadeiro, teste_classificado)
print(report)


print("5.1. matriz de Confusao")
confusion = confusion_matrix(teste_verdadeiro, teste_classificado)
print(confusion)
