from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
# load json and create model
json_file = open('C:/Users/ankur/.spyder-py3/autosave/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("C:/Users/ankur/.spyder-py3/autosave/weights1.hdf5")
print("Loaded model from disk")

# prediction
img = image.load_img(r'C:\Users\ankur\.spyder-py3\autosave\data\26.jpg',target_size=(224,224))
img = image.img_to_array(img)
img=np.expand_dims(img,axis=0)
predictedclass = loaded_model.predict(img)
	#print(train_generator.class_indices)
print(predictedclass)
print(np.argmax(predictedclass))

arr=["Actinic", "Eczema", "NailFungus", "Psoriasis", "Seborrheic", "Tinea", "Warts"]
print(arr[np.argmax(predictedclass)])