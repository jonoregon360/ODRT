import os, re, datetime


class Tools:
	
	def checkDuplicates(self, name, root):
		addNum = 1
		filename,ext = os.path.splitext(name)
		currFileName = filename
		while os.path.isfile(os.path.join(root, filename + ext)):
			filename = currFileName + ' (%i)' % addNum
			addNum += 1
		return filename + ext

	def changeObjName(self, name, root, illegalChars, oneDrivePath):
		badStart = '[ .]'
	
		#begin logging
		logFile = open(oneDrivePath + '\\OneDrive Rename Log.txt', 'a+')
		logFile.write('\nScript running at ' + str(datetime.datetime.now()))
		logFile.write('\nSync file located at ' + oneDrivePath)
		
		#removes illegal characters from filename, uses global var
		newFileName = name.replace('&', 'and')
		newFileName = re.sub(illegalChars, ' ', newFileName)

		#checks for spaces or . at the beginning of a filename, removes those
		count = 0
		for ch in newFileName:
			if re.search(badStart, ch):
				count += 1
			else:
				break
		if count != 0:
			newFileName = newFileName[count:]

		#checks for empty file name
		if newFileName == '':
			newFileName = 'placeholder'

		#checks for duplicates    
		newFileName = self.checkDuplicates(newFileName, root)
		
		#change file name operation
		try:
			os.rename(os.path.join(root, name), os.path.join(root, newFileName))
			logFile.write('\nChanged ' + name + ' to ' + newFileName + ' at ' + root) 
		except:
			logFile.write('\nCould not change name of file ' + os.path.join(root, name))
		
		#End logging
		logFile.write('\nScript completed at ' + str(datetime.datetime.now()))    
		logFile.close()