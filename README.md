# python-create-react-app-template

Template for building an application using `React` as the frontend and
`Flask` as the backend.

## Setup for development
Create the virtual environment:

```python3 -m venv venv```

Activate the virtual environment:

```source venv/bin/activate```

Install the requirements:

```pip install -r requirements.txt```

Start the development server. In separate terminals, run:

```flask run``` and  ```npm start```

## Setup for production

Build the production application:

```npm run build```

Start the production server:

```gunicorn -w 2 'app:app'```
