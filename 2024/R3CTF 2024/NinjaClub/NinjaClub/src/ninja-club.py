from jinja2.sandbox import SandboxedEnvironment
from jinja2.exceptions import UndefinedError
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing_extensions import Annotated
from typing import Union

app = FastAPI()


class User(BaseModel):
    name: str
    description: Union[str, None] = None
    age: int


class Template(BaseModel):
    source: str


@app.get("/", response_class=HTMLResponse)
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ninja Club</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: #333;
            color: #fff;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #4CAF50;
        }
        p {
            font-size: 1.2em;
        }
        a {
            display: inline-block;
            background: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            margin: 20px 0;
            border-radius: 5px;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        a:hover {
            background-color: #3e8e41;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #222;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Ninja Club!</h1>
        <p>Join us in the ninja club. We are present even in the sands of the Sahara. Sharpen your skills and become a master of stealth communications. Qualifications for entry are very strict, so preview your application first.</p>
        <a href="/preview">Preview</a>
    </div>
</body>
</html>
"""


@app.get("/preview", response_class=HTMLResponse)
def preview_page():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Preview Ninja Club</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #222;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
        h1, p {
            margin: 20px 0;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            text-align: left;
            color: #ccc;
        }
        input, textarea {
            width: calc(100% - 20px);
            padding: 10px;
            margin-top: 5px;
            border-radius: 4px;
            border: none;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 20px 0;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #3e8e41;
        }
        #output {
            background: #444;
            padding: 10px;
            margin-top: 20px;
            border-radius: 5px;
            min-height: 50px;
            word-wrap: break-word;
        }
        form {
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Mailer Preview</h1>
        <p>Customize your ninja message:</p>
        <form id="form" onsubmit="handleSubmit(event);">
            <label for="name">Name variable:</label>
            <input id="name" name="name" value="John" />

            <label for="description">Description variable:</label>
            <input id="description" name="description" placeholder="Describe yourself here..." />

            <label for="age">Age variable:</label>
            <input id="age" name="age" type="number" value="18" />

            <label for="template">Template:</label>
            <textarea id="template" name="template" rows="10">Hello {{user.name}}, are you older than {{user.age}}?</textarea>
            
            <button type="submit">Preview</button>
        </form>
        <div id="output">Preview will appear here...</div>
    </div>
    <script>
        function handleSubmit(event) {
            event.preventDefault();
            const data = new FormData(event.target);
            const body = {user: {}, template: {source: data.get('template')}};
            body.user.name = data.get('name');
            body.user.description = data.get('description');
            body.user.age = data.get('age');
            
            fetch('/preview', {
                method: 'POST', 
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body)
            })
            .then(response => response.text())
            .then(html => document.getElementById('output').innerHTML = html)
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
"""


@app.post("/preview", response_class=HTMLResponse)
def submit_preview(template: Template, user: User):
    env = SandboxedEnvironment()
    try:
        preview = env.from_string(template.source).render(user=user)
        return preview
    except UndefinedError as e:
        return e
