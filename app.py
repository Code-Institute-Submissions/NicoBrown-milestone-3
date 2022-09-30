"""
app.py
"""

#import dependencies
import os
from baby_journal import app


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"),
            )
