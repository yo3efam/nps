# About The Project

**Python notifpal SDK package** is a python packages that wraps complex interaction with notifpal service and make it easier for use.

**Key Features:**

* Function-based
* Easy to configure and usage

# Built With

This project is built using the following technologies:

* Programming language(s): [Python]
* Frameworks/Libraries: []
* Database: []
* Other dependencies: [pip]

# Getting Started

These are the steps to get the project up and running on your local development environment:

1. **Prerequisites:**
   * Have python installed

3. **Configuration:**

-


4. **Start the development server:**

-

5. **Access the application:**
  * install it using pip

# Installation

**For production deployment,** specific steps will vary depending on your chosen hosting environment. However, general guidelines may include:

* run `pip install {PACKAGE PATH OR NAME}`

# Usage

a simple usage code:

```python
from notifsdk.bootstrap import register_server
from notifsdk.actions import create_permission, register_channel, notify, notify_users
import threading
import time

def start():
    while True:
        notify("test", "HELLO FROM SERVER")
        notify_users(["123"], "HELLO MY DEAR USER")
        time.sleep(1)

th = threading.Thread(target=start)
th.start()

register_server("192.168.254.124", 2052, "pedi", "test")
register_channel("test", 120)

perm = create_permission("pedi", "123", ["test"])
print(perm)
```

# Roadmap

-

