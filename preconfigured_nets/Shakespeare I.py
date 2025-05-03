import tensorflow
class ShakespeareI:
	ShakespeareI = -1
	
	def __init__(self):
		self.ShakespeareI = tensorflow.keras.models.Sequential([
			tensorflow.keras.layers.Flatten(input_shape=(28, 28)),
			tensorflow.keras.layers.Dense(128, activation='relu'),
			tensorflow.keras.layers.Dropout(0.2),
			tensorflow.keras.layers.Dense(10)]
		)
	
	def getModel(self):
		return self.ShakespeareI
	
	def getLayers(self):
		raise Exception("Method not yet implemented")
