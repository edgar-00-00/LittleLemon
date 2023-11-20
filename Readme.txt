
Accounts:

Superuser
(1) username: admin2
pw: password12345

Users
(1) test@little.com
testuser
password123!
124282a9a00ce47def566760cb37f22747685884

(2) test2@little.com
testuser2
password123!
16478839a5d1e538ad59740c2d645eae74da6eef

----------------------------------------------------------
URLS:

Static HTML content
http://127.0.0.1:8000/restaurant/

User registration - Post
http://127.0.0.1:8000/auth/users/

Token creation & retrieval - Post
http://127.0.0.1:8000/auth/token/login




Menu list - Get - get all items (require auth token)
http://127.0.0.1:8000/restaurant/menu

Menu item - Post - create item (require auth token)
http://127.0.0.1:8000/restaurant/menu/<id>

Menu item - Get/Put/Delete item (require auth token)
http://127.0.0.1:8000/restaurant/menu/<id>


Booking list - Get all (require auth token)
http://127.0.0.1:8000/restaurant/booking/tables

Booking item - Post - create item (require auth token)
http://127.0.0.1:8000/restaurant/booking/tables/

Booking item - Get/Put/Delete item (require auth token)
http://127.0.0.1:8000/restaurant/booking/tables/<id>

