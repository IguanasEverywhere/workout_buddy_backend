# AI Workout Buddy Backend

## Description
AI Workout Buddy provides AI-generated workout advice based on a user's previous exercises and their own descriptions of concerns and goals.

Please see demo & discussion video here: [Loom Demo](https://www.loom.com/share/55652b236896401d919fd09c99775047)

## Instructions for Use with Docker
* Obtain a [Groq API key](https://console.groq.com/keys), if you don't have one already
* Clone this repo to your system
* In the project directory, run `docker build -t workout_buddy_backend .`
* After build is complete, run `docker run -p 5555:5555 -e GROQ_API_KEY=your_groq_key_here workout_buddy_backend`

The server should now be running on your machine on port 5555. Alternatively, if you don't wish to use Docker, you can `run app.py` from the root project directory. The GROQ_API_KEY can be placed in a .env file; example is provided in `.env.example`

Be sure to spin up the [AI Workout Buddy Frontend](https://github.com/IguanasEverywhere/workout_buddy_frontend) repo as well. See the README there for my ideas for future development on this project.