
# 🛠️ Custom Django Middleware Collection

This project includes **three custom middleware components** to enhance a Django web application by adding maintenance control, request timing, and request logging.

---

## 📦 Middleware List

### 1. MaintenanceModeMiddleware
> 🔒 Puts the site into maintenance mode based on a `MAINTENANCE_MODE` setting.

- Checks if `MAINTENANCE_MODE = True` in `settings.py`.
- If enabled, returns a simple HttpResponse like "Site is under maintenance".
- Useful for updates, deployment downtime, etc.


### 2. RequestTimerMiddleware
> ⏱ Measures how long each request takes to process.

- Stores `start_time` when the request comes in.
- After the response, calculates the duration and prints it to the console.
- Great for debugging performance bottlenecks.

### 3. LoggingRecordsMiddleware
> 🧾 Logs each incoming request to the database.

- Captures:
  - IP Address
  - Path
  - HTTP Method
  - Timestamp
- Saves to a `LoggingRecords` model.
- Helps with traffic tracking, user behavior, or security audits.
---

## ⚙️ Setup Instructions

Clone this repo
pip install requirment.txt
py manage.py runserver

## 📊 Output Examples

**RequestTimerMiddleware**
```
Request to /home/ took 0.37 seconds
```

**LoggingRecordsMiddleware**
```
127.0.0.1 visited /about/ at 2025-04-07 16:20:11
```

**MaintenanceModeMiddleware**
```
🛠️ We're under maintenance. Please check back soon.
```

---

Made with ❤️ by Aman


