👋Welcome to FastAPI
=======
This is a RESTful style API background manager

### The technical architecture used

<p>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-3.10-blue" alt="python">
    </a>
    <a href="https://tortoise.github.io/">
        <img src="https://img.shields.io/badge/tortoise--orm-0.19.3-lightgrey" alt="tortoise">
    </a>
    <a href="https://www.uvicorn.org/">
        <img src="https://img.shields.io/badge/uvicorn-0.21.0-%23fff" alt="uvicorn">
    </a>
    <a href="https://pypi.org/project/redis/">
        <img src="https://img.shields.io/badge/redis-4.5.4-critical" alt="uvicorn">
    </a>
</p>

### Pull the project

```bash
git clone https://github.com/GX88/fastapi.git
```

Enter the project root directory
```bash
cd fastapi
```

### Create a virtual environment
If you don't have the `virtualenv` package globally, install it globally
```python
pip3 install virtualenv
```

Create a virtual environment
```python
virtualenv venv
```

Activate the virtual environment, Choose the following command according to the environment
```python
# (linux\Macos)
source venv/bin/activate

# (windows)
venv\Scripts\activate
```

### Install the dependent package
```python
pip3 install -r requirements.txt
```

### Start the project
```python
python3 main.py
```

### illustrate - 1
#### `Directory Structure`

```
fastapi
├── config  # Configuration file
│  ├── __init__.py  # Configuration file initialization
|  ├── dev.py  # Development environment configuration
|  ├── prod.py  # Production environment configuration
├── core  # Core file
│  ├── __init__.py  # Core file initialization
|  ├── middle.py  # Middleware
|  ├── server.py  # Program initialization file
├── database  # Database
│  ├── __init__.py  # Database initialization
|  ├── mysql.py  # MySQL database
|  ├── redis.py  # Redis database
├── model  # Database model
│  ├── __init__.py  # Database model initialization
|  ├── article.py  # Article model
|  ├── comment.py  # Comment model
|  ├── log.py  # Log model
|  ├── Mixin.py  # Mixin model
├── router  # Routing
│  ├── __init__.py  # Routing initialization
|  ├── article
|  │  ├── index.py  # Article routing
|  │  ├── type.py  # Article type
|  ├── comment
|  │  ├── index.py  # Comment routing
|  │  ├── type.py  # Comment type
|  ├── log
|  │  ├── index.py  # Log routing
|  │  ├── type.py  # Log type
│  ├── ResponseType.py  # Response type
│  ├── test.py  # test 
├── utils  # Tool class
│  ├── __init__.py  # Tool class initialization
|  ├── loggers.py  # logger class
|  ├── paginate.py  # ORM pagination query tool
├── .gitignore  # git ignore file
├── main.py  # Program entry
├── README.md  # Project description
├── requirements.txt  # Dependent package
```