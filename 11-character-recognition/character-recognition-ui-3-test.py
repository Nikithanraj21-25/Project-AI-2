# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import BatchNormalization
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Dense


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BrowseButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseButton.setGeometry(QtCore.QRect(170, 377, 141, 41))
        self.BrowseButton.setObjectName("BrowseButton")
        
        self.ClassifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClassifyButton.setGeometry(QtCore.QRect(170, 450, 141, 41))
        self.ClassifyButton.setObjectName("ClassifyButton")
        
        self.TrainingButton = QtWidgets.QPushButton(self.centralwidget)
        self.TrainingButton.setGeometry(QtCore.QRect(410, 450, 141, 41))
        self.TrainingButton.setObjectName("TrainingButton")
        
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(170, 130, 381, 201))
        self.imageLbl.setObjectName("imageLbl")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 380, 141, 41))
        self.textEdit.setObjectName("textEdit")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 241, 34))
        self.label_2.setMinimumSize(QtCore.QSize(15, 34))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 350, 55, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BrowseButton.clicked.connect(self.loadImage) ###

        self.ClassifyButton.clicked.connect(self.classifyFunction) ###

        self.TrainingButton.clicked.connect(self.trainingFunction) ###

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrowseButton.setText(_translate("MainWindow", "BROWSE"))
        self.ClassifyButton.setText(_translate("MainWindow", "CLASSIFICATION"))
        self.TrainingButton.setText(_translate("MainWindow", "TRAINING"))
        self.imageLbl.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "GUI for Character Recognition"))
        self.label_3.setText(_translate("MainWindow", "output"))

    def loadImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)")
        if fileName: 
            print(fileName)
            self.file = fileName
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)


    def classifyFunction(self):
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")
        label = ["sunna","ek","das","be","tran","char","panc","cha","sat","at","nav","ALA","ANA","B","BHA","CH","CHH","D","DA","DH","DHA","F","G","GH","GNA","H","J","JH","K","KH","KSH","L","M","N","P","R","S","SH","SHH","T","TA","TH","THA","V","Y"]
        path2 = self.file
        print(path2)
        test_image = image.load_img(path2, target_size = (128,128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)

        fresult = np.max(result)
        print(fresult)
        label2 = label[result.argmax()]
        print(label2)
        self.textEdit.setText(label2)

    def trainingFunction(self):
        self.textEdit.setText("Training under process...")

        #neural network design
        model = Sequential()
        model.add(Conv2D(32, kernel_size = (3,3), activation = 'relu', input_shape = (128,128,1)))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size = (3,3), activation = 'relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size = (3,3), activation = 'relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(96, kernel_size = (3,3), activation = 'relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size = (3,3), activation = 'relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(128, activation = 'relu'))
        model.add(Dropout(0.3))
        model.add(Dense(45, activation = 'softmax'))

        model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

        train_datagen = ImageDataGenerator(rescale = None,
                                          shear_range = 0.2,
                                          zoom_range = 0.2,
                                          horizontal_flip = True)

        test_datagen = ImageDataGenerator(rescale = 1./255)

        training_set = train_datagen.flow_from_directory('Dataset/test',
                                                            target_size = (128,128),
                                                            batch_size = 8,
                                                            class_mode = 'categorical')

        labels = (training_set.class_indices)
        print(labels)
        
        test_set = test_datagen.flow_from_directory('Dataset/val',
                                                    target_size = (128,128),
                                                    batch_size = 8,
                                                    class_mode = 'categorical')

        labels2 = (test_set.class_indices)
        print(labels2)
        
        #model training
        model.fit_generator(training_set,
                            steps_per_epoch = 100,
                            epochs = 10,
                            validation_data =test_set,
                            validation_steps = 125)

        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
            model.save_weights("model.h5")
            print("Saved model to disk")
            self.textEdit.setText("Saved model to disk")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
