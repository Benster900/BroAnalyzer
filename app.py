"""
Author: Ben Bornholm
Date: 9-4-16
Description: Webpage for bro logs
"""

# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, redirect, request, url_for
import os
import pygal
from pygraph import *
from logParser import *

# Uploads folder
basedir = os.path.abspath(os.path.dirname(__file__))
uploadpath = basedir + '/uploads'

# Initialize and config the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def homepage():
	# open every file in directory
#	for filename in os.listdir(uploadpath):
#		for line in filename:

	# Get fields and entries from log files
	entryDict, fieldsLst = logParser(uploadpath)

	return render_template('homepage.html',entryDict=entryDict,fieldsLst=fieldsLst)


@app.route('/brograph')
def graphing():
	entryLst, fieldsLst = logParser(uploadpath)

	try:
		pieIP_graph_data, pieQuery_graph_data = createGraph(entryLst)
		return render_template("brograph.html", pieIP_graph_data=pieIP_graph_data, pieQuery_graph_data=pieQuery_graph_data, fieldsLst=fieldsLst)
	except Exception, e:
		return(str(e))



# Run the app :)
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)
