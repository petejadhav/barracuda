import os
import json

"""
master = 
{
	"general":{

	},
	"flatpages":[],
	"categories":[]
}
"""
content_path = "content"


print("Enter title of page")
title = input()
article_slug = title.lower().replace(" ","_")

isFlat = input("Is this is a standalone flat page? y/n")

# Enter page in master JSON
# {"title":"asdasd","link":""}
master_file = open("content"+os.sep+"master.json","r")
master = json.loads(master_file.read())
print(master)
master_file.close()

fldr = ""
if isFlat == 'y':
	fldr = "flatpages"
	master['flatpages'].append({"title":title,"link":"/"+fldr+"/"+article_slug+".md"})

elif isFlat == 'n':
	print("Currently existing folders...")
	print(os.listdir("./content"))
	fldr = input("Enter folder to create page in... OR enter new folder to create.")

	if fldr not in master['categories']:
		print("Creating New Category")
		master['categories'].append(fldr)
		os.mkdir("content"+os.sep+fldr)
		cat_master = open("content"+os.sep+fldr+os.sep+"index.json","w+")
		init_json = json.dumps({"articles":[]},indent=4)
		chars = cat_master.write(init_json)
		cat_master.close()

	with open("content"+os.sep+fldr+os.sep+"index.json","r+") as cat_master_file:
		category_master = json.loads(cat_master_file.read())
		category_master['articles'].append({"title":title,"link":"/"+fldr+"/"+article_slug+".md"})
		cat_master_file.seek(0)
		cat_master_file.write(json.dumps(category_master,indent=4,sort_keys=True))
		cat_master_file.truncate()
	
f = open("content"+os.sep+fldr+os.sep+article_slug+".md","w")
f.close()

#update master
master_file = open("content"+os.sep+"master.json","w")
master_file.write(json.dumps(master,indent=4,sort_keys=True))
master_file.close()



