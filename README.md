# image2PDF

This project is helpful in converting images into pdf.

# Getting Started

#### Prerequisites:

1. [Download and install Python](https://www.python.org/downloads/) (Version 3.x is recommended).

#### Setting up the project:

1. Clone the GitHub repository:

```
git clone https://github.com/gautamsagar99/image2PDF.git
```

2. Navigate to the project directory:

```
cd image2PDF
```

3. (Recommended) Create a virtual environment to manage Python packages for your project:

```
python3 -m venv venv
```

4. Activate the virtual environment:
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```
5. Install the required Python packages from `requirements.txt`:

```
pip install -r requirements.txt
```

6. Run the application

```
uvicorn main:app --reload --port 5000
```

7. open browser and type below URL

```
http://localhost:5000/
```

Now you can upload images and convert into pdf.
...
