from django.db import models

from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
from keras import backend as K
from keras.applications import imagenet_utils
import numpy as np


# Create your models here.
class ImgClassify(models.Model):
	def __init__(self, img_path):
		self.img_path = models.ImageField(upload_to='images')

	def classify(self):
		K.reset_uids()	#	reset graph identifiers
		model = VGG16(weights='imagenet', include_top=True)	# use keras pretrained model VGG16

		img = image.load_img('/home/grh/Desktop/webProgramming/django-apps/imageInterpretation/media/cat.jpeg', target_size=(224, 224))
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		result_features = model.predict(x)
		result0 = imagenet_utils.decode_predictions(result_features)
		result = ""
		#result['content']=""

		for (i, (predID, pred, probability)) in enumerate(result0[0]):
			result = result + "\n" + "{}.-  {}: {:.2f}%".format(i+1, pred, probability*100)
			#result['content'] = result['content'] + "\n" + "{}.-  {}: {:.2f}%".format(i+1, pred, probability*100)
		return result 
