from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException

# 🔐 Secret key and algorithm — keep secure in production
SECRET_KEY = "your_secret_key_here"  # 🔁 Replace with env variable or config
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# 🔑 Create JWT access token
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 🔍 Decode JWT and extract username (sub)
def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token decoding failed")




