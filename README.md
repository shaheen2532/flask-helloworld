# Flask Hello App

This is a simple Python Flask application that returns "Hello {name}" where `{name}` is the value of `NAME` from the `.env` file.

## Requirements

- Python 3.x
- Flask
- python-dotenv

## Setup

1. Clone this repository:
   ```sh
   git clone https://github.com/shaheen2532/flask-helloworld.git
   cd flask-helloworld
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add the following line:
   ```sh
   NAME=YourName
   ```

5. Run the Flask application:
   ```sh
   flask run
   ```

6. Open a browser and go to `http://127.0.0.1:8080` to see the output.

## File Structure

```
flask-helloworld/
│── app.py
│── .env
│── requirements.txt
│── README.md
```

## Example Output

If `.env` contains `NAME=Alice`, visiting `http://127.0.0.1:5000` will return:

```
Hello Alice!
```

## License

This project is licensed under the MIT License.
