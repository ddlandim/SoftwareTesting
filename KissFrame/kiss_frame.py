
class KissFrame(object):
	"""docstring for kiss_frame"""
	FEND = bytearray.fromhex('c0')
	CMD = bytearray.fromhex('00')
	def __init__(self, b = bytearray.fromhex('c000c0')):
		super(KissFrame, self).__init__()
		self.payload = self.escape(b)
		self.raw = b
		self.header = FEND.append(CMD)
		self.fend = FEND
	def escape(self, b):
		if(len(b)<3 | b[0] != FEND | b[1]!= CMD | b[-1]!= FEND):
			return bytearray.fromhex('')
		ba = bytearray.fromhex('')
		for byte in b:
			