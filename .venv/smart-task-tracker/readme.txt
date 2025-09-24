HELLOOOOO

task organizing app yessir

started with the api, the original app was really sucky and in one file and not done at all. Still sucks but at a larger scale now.

24SEP converted small file into big project backend type structure, getting practice with breaking
down a project into digestable pieces. Heres what we learned:

1. Importing stuff is fun and easy and good for you! The exact same file can be made ten times as
convoluted. Neccessary for bigger projects. Starting with models, simplest, defined a baseclass for task.
Then in the init file, from .task (pulling from current dirs task.py) and exposes it at the package level
(init files make them packages) so now you save a whole word when Importing.

old:
from app.models.task import task
new:
from app.models import task

Now why dont i need to do that for services when im calling it?
task_service, in this instance, is a module. 
task from models, is a class.
With the service, you're taking the whole module with you, whereas with the class
you only want the one class from the module, not the entire thing.

Back to the topic, now we have multiple files, all focused on their one dedicated task, and
can be expanded upon. So organized. The models create the base classes, the services handle the logic
for what we want to do with those classes, and the routers are gonna call the logic and take care of the endpoints.
That collection of endpoints made w the router file is declared in the main file.
Then when ran, FastAPI creates the app out of main.py, it registers the endpoints into the app,
and FastAPI will know which function to call :D 

2. Lots of hyper specific FastAPI stuff.

Currently running without a database as neo4j sucks balls and so does linux. Running internally works perfectly
fine without async. Although I expect to be very confused when im rewriting everything to work with neo4j. Maybe SQLalchemy
is a fine database to practice with. 

init files can be empty, but they must exist

use a git ignore or everything will get very cluttered

Im sure theres more i forgot. Im tired.

Tomorrow we attempt to containerize

CMDs to remember:

Get into venv -- source .venv/bin/activate
leave venv -- deactivate 

boot the app -- uvicorn app.main:app --reload