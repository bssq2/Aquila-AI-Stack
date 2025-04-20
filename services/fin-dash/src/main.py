import sys
from app import app

if __name__ == "__main__":
    # Start the Dash server
    app.run_server(host="0.0.0.0", port=8050, debug=True)