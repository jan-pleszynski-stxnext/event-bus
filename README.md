# Introduction
This repository showcases the use of event bus pattern. The pattern is implemented in memory, but if necessary can
be easily replaced with a message broker like RabbitMQ.

This implementation is not production ready. Also the layout of particular classes and methods should be changed to 
better match the style of the project.

# Pros and cons 

The advantage of using event bus pattern is that it decouples the components of the system. This allows for easy adding 
new behaviours by registering new handlers.

The disadvantage is that it can be hard to follow the flow of the program, as the results of the events are not 
explicitly visible.

# Running the code

```shell
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

# Reading the code.
Start with the main.py file and read through code, comments.
