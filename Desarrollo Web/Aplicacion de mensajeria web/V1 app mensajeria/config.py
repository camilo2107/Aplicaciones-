import secrets
secret = secrets.token_urlsafe(32)

app.secret_key = secret