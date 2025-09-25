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

25SEP

DOCKER for a single container

Containerizing was very simple, with just the one project. I will use a dockercompose when i add more layers, but for now:

Requirements.txt: in the projects root, list the dependencies and the versions. IE, fastapi==0.115.0 uvicorn[standard]==0.30.6 pydantic==2.9.2
this will be referenced in the dockerfile for the python dependencies.

.dockerignore: allows the container to essentially filter spam, keeps the structure clean and readable, same as git ignore.

dockerfile: essentially a list of commands running to run the project from scratch

Time for frontend:
Starting place being the boiler plate react app. Adds all the random dependencies and a basic react app, with the nothing homepage. 

Now we talk about MIDDLEWARE. What does it handle?
1. CORS or cross-origin resource sharing. what the fuck does that mean? its a browser security rule. It controls which frontend applications are allowed to make requests to your API. Without it, any website could just hit your api and steal all your data. By default browsers will block api calls if they come from a different "origin"
So what the fuck is an origin? protocal + domain + port. might look familiar for example: http://localhost:8000
So by default, the browser wont allow react to call FastAPI unless it specifically states: I trust requests from that "origin"
How does it work though? When react makes a request, the browser sends a "preflight OPTIONS request"

    Pause what the FUCK is a preflight options request? WELL a preflight request is a special OPTIONS HTTP request that the browser sends automatically before your real request (like post put whatever) if the request is considered "non-simple". BASICALLY the browser tells your API "Hey, is it cool if i sent this real request with these headers/methods?" If the server says yes with the right CORS headers, then the browser sends the real request. if not then the browser blocks the request before it reaches the api.

SO when the react app makes a request, the browser will send a preflight OPTIONS request first. FastAPI will respond with the headers that correspond to the react apps information. What else is middleware capable of?
2. Authentication: this will come in handy when we begin incorporating keycloak.
3. Logging: the middleware can log every request and response
4. Error handling: can create custom error pages or JSON errors
5. Performance monitoring: can track response times.

Magical is it not?

Now we begin with a basic frontend, a single page, basic functionality. Starting with the api layer.
Ill start with fetch. fetch() is how your frontend communicates with the backend. Its a build in browser API for making HTTP requests (GET POST PUT DELETE). It returns a promise, which is generally used with async functions. 

Lets break down this block of code:

        export async function getTasks() {
          const res = await fetch("http://localhost:8000/tasks");
          return res.json();
        }
        
        first export will make this function available to other files.
        async then allows us to use await within the function, giving us access to promises.
        the fetch is a get request being sent to the apis tasks list. Anytime fetch is used with just the url, it is interpreted as a basic get request.
        await tells JS "pause until that promise is resolved then give me the result"
        that result is then placed into the res variable, making it a response object with details like:
        Response {
          ok: true,
          status: 200,
          headers: {...},
          body: ReadableStream
        }
                (readablestream is an object that represents a stream of data coming in piece by piece instead of all at once. Essentially, it allows the browser to start processing chunks as they come in, instead of waiting for the entire JSON response to arrive)
                
        .json is a method on the response object. since res is now one, it is able to be used. It takes the body stream (raw text) and converts it into a javascript object.

TLDR: it asks the backend for tasks, waits until the response comes back, parses the JSON body into a JS object, and returns it.

Fetch can be modified to contain any of the different http methods, like for post:
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task),
  });

  first, the method is changed to post instead of the default get.
  then with the headers, it is telling the backend that we're sending JSON
  then it turns the JS object into a JSON object to send.

if using arguments in your function such as get item by id:
export async function getTasksById(id) {
    const res = await fetch(`${API_URL}/${id}`);
    return res.json();
}
remember to format the route to accept variables. the API_URL announced as a global variable at the start of the doc.

Thats all the API calls taken care of HORAY

Now for the components. which ill do tomorrow.

CMDs to remember:

Get into venv -- source .venv/bin/activate
leave venv -- deactivate 

boot the app -- uvicorn app.main:app --reload

DOCKER CMDs
build docker image -- docker build -t fastapi-backend .
run docker container -- docker run -d --name task-backend -p 8000:8000 fastapi-backend
check running containers -- docker ps
shutdown docker container -- docker stop task-backend
remove it -- docker rm task-backend

REACT CMDs
run the dev server -- npm start
