#
import jwt
#
from datetime import datetime, timedelta


def generate_jwt(user, refresh=False):
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    if refresh:
        expiration_time += timedelta(days=30)
    jwt_payload = {
        "user_id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "expiration": str(expiration_time),
        "issued_at_time": str(datetime.utcnow()),
    }
    jwt_token = jwt.encode(jwt_payload, "SECRET_KEY", algorithm="HS256")

    return jwt_token
