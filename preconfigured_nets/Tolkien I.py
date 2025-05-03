import tensorflow
class Tolkien_I:
	Tolkien_I = -1
	
	def __init__(self):
		self.Tolkien_I = tensorflow.keras.models.Sequential([
			tensorflow.keras.layers.Flatten(input_shape=(28, 28)),
			tensorflow.keras.layers.Dense(128, activation='relu'),
			tensorflow.keras.layers.Dropout(0.2),
			tensorflow.keras.layers.Dense(10)]
		)
	
	def getModel(self):
		return self.Tolkien_I
	
	def getLayers(self):
		raise Exception("Method not yet implemented")
