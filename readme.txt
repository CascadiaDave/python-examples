
ollamasvc.py is a RESTful microservice that accepts an ollama model in the runstream and connects to a MongoDB to 
save queries and responses to ollama queries. It runs on port 50001

ollamachat.html is a javascript driven web page that displays a prompt box for new AI chat queries, and the
query history, with the ability to delete some or all of past queries.

ollama and mongodb must be installed with mongodb running on the standard port 27017

To use, 

python --model modelname

Currently these models are expected:

models = ["deepseek-r1", "llama3.2","samantha-mistral", "falcon3", "codellama", "codestral","qwen2.5-coder:14B","olmo2"]

This starts the RESTful API microservice

Then open the html file from your local truncate

file://...../ollamachat.html

This is intended to run locally since there is no security or authentication to use the ollama server.




