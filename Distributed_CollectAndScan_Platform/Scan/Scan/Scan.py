class Scan(object):
	"""docstring for Scan"""
	def __init__(self, url):
		#super(Scan, self).__init__()
		self.url= url
	def run(self):
		print(self.url)
		