import os.path
from transformers import AutoTokenizer
import re
import numpy
class Data:
	Text = -1
	file = -1
	def __init__(self):
		# Load text/load right away or just leave it blank?
		pass
	
	def LoadTxtFile(self, FilePath):
		if os.path.exists(FilePath) and FilePath.endswith('.txt'):
			Tekst = open(FilePath).read()
			self.Text = Tekst
		else:
			raise Warning("File doesn't exist. Please check file type and location")
	
	def LoadString(self, Text):
		self.Text = Text
	
	def ReturnTokens(self):
		tokenizer = Tokenizer()
		return tokenizer.fit_on_texts(self.Text)
	
	def ReturnEmbeddings(self):
		# embedding_layer = tensorflow.keras.layers.Embedding(input_dim=10000, output_dim=128)
		pass
	
	def SlideWindow(self, WindowWidth):
		if self.Text == -1:
			raise Warning("You haven't loaded any text or file. Please use .LoadTxt or .LoadString")
		tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
		tokens = tokenizer.encode(self.Text, add_special_tokens=False)
		windows = numpy.lib.stride_tricks.sliding_window_view(tokens, WindowWidth)
		return windows
	
	def Flatten(self):
		if self.Text == -1:
			raise Warning("You haven't loaded any text or file. Please use .LoadTxt or .LoadString")
		single_line_text = self.Text.replace('\n', ' ').replace('\r', ' ')
		single_line_text = re.sub(r'\s+', ' ', single_line_text).strip()
		self.Text = single_line_text
	