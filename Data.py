import os.path
from tensorflow.keras.preprocessing.text import Tokenizer
import re

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
	
	
	def Flatten(self):
		if self.Text == -1:
			raise Warning("You haven't loaded any text or file. Please use .LoadTxt or .LoadString")
		single_line_text = self.Text.replace('\n', ' ').replace('\r', ' ')
		single_line_text = re.sub(r'\s+', ' ', single_line_text).strip()
	