import requests
import base64
import json
import os
import time
import csv

def analyze_image_with_ollama(image_path, model='llava:7b', prompt='Describe this image in detail'):
    """
    Send an image to Ollama server for analysis

    :param image_path: Path to the image file
    :param model: Ollama model to use (default: 'llava')
    :param prompt: Analysis prompt (default: general description)
    :return: Analysis response from the Ollama server
    """
    # Read the image file and encode it to base64
    with open(image_path, 'rb') as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    # Prepare the request payload
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [image_base64]
    }

    # Server URL (adjust to match your Ollama docker setup)
    url = 'http://192.168.30.1:11434/api/generate'

    try:
        # Send POST request to Ollama server
        response = requests.post(url, json=payload, stream=True)

        # Check if the request was successful
        response.raise_for_status()

        # Process the streaming response
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    # Parse each JSON line
                    json_response = json.loads(line.decode('utf-8'))

                    # Check if the response contains a text fragment
                    if 'response' in json_response:
                        full_response += json_response['response']

                    # Check if the stream is complete
                    if json_response.get('done', False):
                        break

                except json.JSONDecodeError:
                    print("Error decoding JSON response")

        return full_response.strip()

    except requests.RequestException as e:
        print(f"Error communicating with Ollama server: {e}")
        return None


# Directory containing images
IMAGE_DIR = r"D:\重要資料\文件\studio2024\studio2024\img\可用廣告\聯晟"
PROMPT = "Analyze the image and identify the three most significant objects.Be specific about what the objects are (e.g., 'tree', 'car', 'building'). For each object, calculate its approximate proportion of the image (in percentage). Return the results in a single line, separated by commas, in the format: \"Object1: Proportion1%, Object2: Proportion2%, Object3: Proportion3%\"."
MODEL = "llava:7b"
OUTPUT_CSV = "image_analysis_results.csv"

start_time = time.time()

# Prepare a list to store results
results = []

for image in os.listdir(IMAGE_DIR):
    image_path = os.path.join(IMAGE_DIR, image)
    analysis = analyze_image_with_ollama(image_path, MODEL, PROMPT)
    if analysis:
        print(f"{image}: {analysis}")
        # Add the result to the list
        results.append([image, analysis])

end_time = time.time()

# Print timing information
print(f"Time taken: {end_time - start_time:.2f} seconds")
print(f"Average time taken: {(end_time - start_time)/len(os.listdir(IMAGE_DIR)):.2f} seconds")

# Write results to a CSV file
with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(["Image Name", "Analysis Result"])
    # Write data
    csv_writer.writerows(results)

print(f"Results exported to {OUTPUT_CSV}")