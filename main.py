import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    debug_mode = os.getenv("DEBUG")
    print(f"Debug Mode : {debug_mode}")

    print("Hello from algdsnote-python!")

if __name__ == "__main__":
    main()
