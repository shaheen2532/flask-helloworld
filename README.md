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

## Deployment to Google cloud

1. Create a google cloud account and create a new project
2. instal the google cloud CLI: https://cloud.google.com/sdk/docs/install
3. Initialize gcloud CLI:
   ```sh
   gloud init
   ```
4. Set project for cloud run service:
   ```sh
    gcloud config set project PROJECT_ID  #PROJECT_ID to your project can be found in the console dashboard
   ```
5. Enable the Cloud Run Admin API and the Cloud Build API:
   ```sh
    gcloud services enable run.googleapis.com
    gcloud services enable cloudbuild.googleapis.com
   ```
6. Set IAM rules:
   ```sh
      gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
      --role=roles/run.builder
   ```
7. navigate to project directory, then:
   ```sh
    gcloud run deploy --source .
   ```
   When you are prompted for the service name, press Enter to accept the default name, for example helloworld.

   If you are prompted to enable additional APIs on the project, for example, the Artifact Registry API, respond by pressing y.

   When you are prompted for region: select the region of your choice, for example us-central1.

   If you are prompted to create a repository in the specified region, respond by pressing y.

   If you are prompted to allow unauthenticated invocations: respond y

8. Wait a few minutes and the hosted link will be displayed. Visit the link to access service 
   
## Example Output

If `.env` contains `NAME=Alice`, visiting `http://127.0.0.1:5000` will return:

```
Hello Alice!
```

## License

This project is licensed under the MIT License.
