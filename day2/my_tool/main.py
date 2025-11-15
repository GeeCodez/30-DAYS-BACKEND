from utils.json_utils import load_json, save_json
from utils.time_utils import timestamp, timestamp_filename
from utils.random_utils import random_user
import os

def main():
    print("===Welcome to My Modular CLI tools ===")

    #Get json input from the user
    user_input=input("Enter the JSON string (example: {\"app\":\"demo\"}): ")

    try:
        data=load_json(user_input)
        print("\nParsed JSON: ", data)
    except ValueError as e:
        print("\n Error:",e)
        return

    #generate random user profile
    profile=random_user()
    print("\nGenerated user profile: ",profile)

    #combining both
    combined={
        "timestamp":timestamp(),
        "input": data,
        "generated_profile":profile
    }

    #saving to a file
    filename=timestamp_filename("session")
    logs_dir="logs"

    os.makedirs(logs_dir,exist_ok=True)
    filepath=os.path.join(logs_dir,filename)

    with open(filepath,"w") as f:
        f.write(save_json(combined))

    print(f"\nData saved to: {filepath}")
    print("\n==Done !===")

if __name__=="__main__":
    main()