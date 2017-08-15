# -*- coding: utf-8 -*-
__author__ = 'Edward'
import numpy as np
np.random.seed(1337)
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten,Convolution2D,MaxPooling2D
from keras.utils import np_utils,plot_model
from keras import backend as K
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
(X_train,y_train),(X_test,y_test)=mnist.load_data()
if K.image_dim_ordering()=='th':
    X_train=X_train.reshape(X_train.shape[0],1,28,28)
    X_test=X_test.reshape(X_test.shape[0],1,28,28)
    input_shape=(1,28,28)
else:
    X_train=X_train.reshape(X_train.shape[0],28,28,1)
    X_test=X_test.reshape(X_test.shape[0],28,28,1)
    input_shape=(28,28,1)
'''
img_rows, img_cols = 28, 28

if K.image_data_format() == 'channels_first':
    shape_ord = (1, img_rows, img_cols)
else:  # channel_last
    shape_ord = (img_rows, img_cols, 1)
X_train = X_train.reshape((X_train.shape[0],) + shape_ord)
X_test = X_test.reshape((X_test.shape[0],) + shape_ord)
'''
X_train=X_train.astype('float32')
X_test=X_test.astype('float32')
X_train/=255
X_test/=255
Y_train=np_utils.to_categorical(y_train,10)
Y_test=np_utils.to_categorical(y_test,10)
'''
plt.imshow(X_train[0].reshape(28,28))
plt.show()
print(np.asarray(range(10)))
print(Y_train[0].astype('int'))
'''
early_stop=EarlyStopping(monitor='val_loss',patience=2,verbose=1)
model=Sequential()
model.add(Convolution2D(32,(3,3),input_shape=input_shape))
model.add(Activation('relu'))
model.add(Convolution2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))
model.summary()

plot_model(model,to_file=r'e:/python/keras_test1.png',show_shapes=True)

model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])
hist=model.fit(X_train,Y_train,128,8,callbacks=[early_stop],validation_data=(X_test,Y_test))

hidden_features=model.predict(X_train)

print(hidden_features.shape)
def plot_history(hist):
    plt.figure()
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.legend(['Training','Validation'])
    plt.figure()
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.plot(hist.history['acc'])
    plt.plot(hist.history['val_acc'])
    plt.legend(['Training','Validation'],loc='lower right')
    plt.show()
plot_history(hist)

score=model.evaluate(X_test,Y_test,verbose=0)
print('Test score:',score[0])
print('Test accuracy:',score[1])

from sklearn.manifold import TSNE
tsne=TSNE(n_components=2)
X_tsne=tsne.fit_transform(hidden_features[:1000])
color_map=np.argmax(Y_train,axis=1)
colors=np.array([x for x in 'b-g-r-c-m-y-k-purple-coral-lime'.split('-')])
color_map=color_map[:1000]
plt.figure(figsize=(10,10))
for cl in range(10):
    indices=np.where(color_map==cl)
    plt.scatter(X_tsne[indices,0],X_tsne[indices,1],c=colors[cl],label=cl)
plt.legend()
plt.show()
