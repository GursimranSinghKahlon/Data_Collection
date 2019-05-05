from flask import Flask, render_template, request
import base64
from PIL import Image
from io import BytesIO
import json
import codecs
from final_test import perdict
#from description import description
import numpy as np
import re
import os
import shutil

app = Flask(__name__)

# def pre_process(img):
# 	img = Image.open(img)
# 	img = img.resize((224,224), Image.ANTIALIAS)
# 	img = np.expand_dims(np.array(img), 0)
# 	return imgapp.route('/')



@app.route('/')  
def homepage():
	#name = '1.jpg'
	#img = Image.open('static/'+name)
	#img = img.resize((224,224), Image.ANTIALIAS)
	#image = np.expand_dims(np.array(img), 0)

	#image = pre_process('static/'+name)
	all_links2 = perdict()
	
	category = all_links2[0]
	leaf_path2 = "static/" + all_links2[1].split('/')[-1]
	flower_path2 = "static/" + all_links2[2].split('/')[-1]
	entire_path2 = "static/" + all_links2[3].split('/')[-1]
	stem_path2 = "static/" + all_links2[4].split('/')[-1]

	test_file = ""
	for files in os.listdir("dataset/test"):
	 	test_file = files	
	 	shutil.copyfile("dataset/test/"+files,"static/"+files)

	name = category
	plant_name = name
		

	plant_img = name
	d = {}
	d[category] = "File uploaded belong to :  " + name 
	return render_template('index.html',test_file = "static/" + test_file,leaf_path2 = leaf_path2,stem_path2 = stem_path2, flower_path2 = flower_path2, entire_path2 = entire_path2, plant_name=plant_name, treatment_technique="Thanks for uploading the data", plant_img=plant_img,dictionary=d)

# @app.route('/index3')
# def index3():
# 	return render_template('index3.html')


if __name__ == '__main__':
	app.run(host= '0.0.0.0', port = 5005
                )
	app.run(debug=True)
	app.run(extra_files=['templates/index.html'])
	app.config['TEMPLATES_AUTO_RELOAD'] = True
