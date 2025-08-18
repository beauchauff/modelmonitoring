#Script to systematically evaluate API performance
import requests
import json

"""Reads a file from the specified file and sends post request to fastapi url provided"""

url = "http://127.0.0.1:8000/predict"

with open("test.json","r") as f:
    lines =f.readlines()
    print(lines) #list

    for line in lines:
        data = [json.loads(line)]
        df = pd.dataFrame([data])
        response = requests.post(url,headers=headers, data=payload)
        predictions = response.json()

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "text":review_text,
            "predicted_sentiment": predictions.prediction,
            "true_sentiment": predictions.true_review
        }

        try:
            with open("/logs/prediction_logs.json", "a") as g:
                g.write(json.dumps(log_entry) + "\n")
        except (fileNotFoundError, json.JSONDecodeError):
            print("File not found error")

