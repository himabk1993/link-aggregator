# Link Aggregator

## Requirements

Building a social link aggregator. At its core, it will be a place where users can submit internet links (URLs),
and upvote/downvote ("Thumb up"/"Thumb down") each other's Links. The difference between **Upvotes** and **Downvotes**, for each **Link**, is their **Score**.

A Link is mostly an URL associated with scoring data. A proposal has been made to represent the resource Link:

### The Link Object
```json
{
  "id": 1,
  "created": "2022-05-19T13:15:06Z",
  "url": "https://www.google.com/",
  "upvotes": 5,
  "downvotes": 2,
  "score": 3
}
```

Our API will allow clients:
- to **create** new Links by sending a `POST` request with the following data to the `/api/links` endpoint:
  ```json
  {
    "url": "https://www.yahoo.com/"
  }
  ```
  The link should be validated as being a valid URL.
- to **retrieve** all Links submitted, sorted by their Score, by sending a `GET` request to the `/api/links` endpoint.
- to perform **actions** on each Link:
  - **Upvote**, by sending a `POST` request to the `/api/links/{linkId}/upvote` endpoint. This should add 1 to the "upvotes" property for that Link.
  - **Downvote**, by sending a `POST` request to the `/api/links/{linkId}/downvote` endpoint. This should add 1 to the "downvotes" property for that Link.


## How to use the repo
- Create a virtual environment (Install if not)
```
  python3 -m venv env
```
- Activate the env
```
  source env/bin/activate
```
- Clone the project
```
git clone git@github.com:betaoab/back-end-interview.git
```
- Install the requirement.txt file (Install pip if not)
```
pip3 install requirements.txt
```
- Create a superuser to access admin pages (e.g., http://127.0.0.1:8000/admin/)
```
python3 manage.py createsuperuser
```
- Run the server to access the feature(e.g., http://127.0.0.1:8000/api/links/)
```
python3 manage.py runserver
```
