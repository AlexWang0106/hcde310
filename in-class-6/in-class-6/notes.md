# In-class 6 notes

## What happens with a wrong key? What status code?
it will reject the request
403 forbidden

## Where does your key live, and why isn't it in earth.py?
My API key is stored in a local .env file and loaded using python-dotenv. It is not written directly in earth.py because that could expose the key when the code is uploaded to GitHub. The .env file is excluded from Git using .gitignore to keep the key private.

## Stuck? Where?

