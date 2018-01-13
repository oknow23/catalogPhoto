import os
import sys
import pyexiv2
import shutil

VERSION = '0.1.0'
LOCATION = ' [Taipei]'
DBG = 0
subnameList = ['.jpg','.mov','.cr2','.nef','.raw','.raf','.pef','.arw']
JPG_TYPE = 0
VIDEO_TYPE = 1
dirName = ''

#get file path
if len(sys.argv) > 1:
	photoPath = sys.argv[1].decode('utf8')+'\\'
else:
	# print os.getcwd()
	photoPath = os.getcwd()+'\\'

# Get file name from folder
for fileNames in os.listdir(os.getcwd()):
	i = 0

	# Filter need file type
	for subname in subnameList:
		rc = fileNames.lower().find(subname)
		if rc >= 0:
			break
		i = i+1

	if rc >= 0:
		if i == VIDEO_TYPE:
			# Set video path name
			print dirName
			destPath = dirName +'\\'+ 'video'

		else:
			# Get date and time for folder name
			metadata = pyexiv2.ImageMetadata(fileNames)
			metadata.read()
			# tag = metadata['Exif.Image.DateTime']
			tag = metadata['Exif.Photo.DateTimeOriginal']
			# print tag.raw_value
			dirName = tag.value.strftime('%Y-%m-%d')

			# Make folder name
			dirName = dirName + LOCATION
			print dirName
			if not os.path.isdir(dirName):
				os.makedirs(dirName)

				# detect dealRaw
				if os.path.isfile("dealRaw.exe"):
					print 'detect dealRaw'
					shutil.copyfile("dealRaw.exe",dirName+'\\'+"dealRaw.exe")

			# set destination path name
			if i == JPG_TYPE:
				destPath = dirName
			else:
				destPath = dirName +'\\'+ 'raw'

		# Make folder
		if not os.path.isdir(destPath):
			os.makedirs(destPath)

		
		# Move file to folder
		if not os.path.isfile(destPath+'\\'+fileNames):
			os.rename(fileNames,destPath+'\\'+fileNames)
		else:
			print 'Warning !! file ' +destPath+'\\' +fileNames + ' is exist'


print 'Done!!'

if DBG == 0:
	os.system("pause")