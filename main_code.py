import os 
import datetime
import shutil #using copy2('src,'dst') cammand only
ass_list=[] #for associating the date to the image name

os.chdir('G:\\DCIM\\100CANON')
for image in os.listdir(): #listing all files of the Card
	
	timestamp=os.stat(image)[8] #gettingtimestamp
	date_time=datetime.datetime.fromtimestamp(timestamp).strftime('%d-%b') #creating a date_time from the timestamp 
	#fromtimestamp() returns a string
	loc_ass=[image,date_time] #list with image and date
	ass_list.append(loc_ass) #appending to the ass_list
	
os.chdir('F:\\LatestDSLR')
current_folders=[folder for folder in os.listdir() ] #listing current destination folders
for i in range(len(ass_list)):
	date=ass_list[i][1] #getting the dates for each image
	src=f"G:\\DCIM\\100CANON\\{ass_list[i][0]}" #assigning the source to image location


	if os.path.exists(f"F:\\LatestDSLR\\{date}") ==True: #checking if  there's already a date folder or not
	 des=f"F:\\LatestDSLR\\{date}"

	else:
		os.mkdir(f"{date}")
		des=f"F:\\LatestDSLR\\{date}" #creating the date foldee if not already present
	

	shutil.copy(src,des) #copying the file


print("DONE!!")
	
