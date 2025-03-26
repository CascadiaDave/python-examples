
ollamasvc.py is a RESTful microservice that accepts an ollama model as a run line argument and connects to a MongoDB to 
save queries and responses to ollama queries. It runs on port 50001

ollamachat.html is a javascript driven web page that displays a prompt box for new AI chat queries, and the
query history, with the ability to delete some or all of past queries.

ollama and mongodb must be installed with mongodb running on the standard port 27017.  These Python modules are required:

from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import os
import logging
import ollama
import argparse
import sys

To use, 

python ollamasvc.py --model modelname

I generally use pyinstaller --onefile ollamasvc.py to make it into a standalone executable.

Currently these models are expected but easy to add more.

models = ["deepseek-r1", "llama3.2","samantha-mistral", "falcon3", "codellama", "codestral","qwen2.5-coder:14B","olmo2"]


This starts the RESTful API microservice

Then open the html file from your local PC in your browser and chat away.

file://...../ollamachat.html

This is intended to run locally since there is no security or authentication to use the ollama server.

In hindsight I should have recorded the model used with each database save.  Maybe I will get around to that later.



