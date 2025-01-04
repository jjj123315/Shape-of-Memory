## Emotion segmentation in images
By analyzing key objects and their proportions within images, combined with geographical location information, it can help analyze people's existing imagery, environmental perception, or memory construction of a place. The classification of objects and their proportions in the image influence people's perception of the location and also reflect the objects of memory. If we analyze a large number of images from the same location and identify the most prominent objects, it could provide an insight into the collective memory of the public about that place.

### Model
Operating with the Ollama llava-7B model.
LLaVA (Language Vision Assistant) 7B is a powerful multimodal language model designed specifically to handle both text and image inputs. Below are some key features and advantages of LLaVA 7B:

1. Multimodal Capability
LLaVA 7B is not limited to processing text inputs but can also understand and generate content related to images. This makes it highly advantageous for tasks involving both text and images, allowing for more flexible solutions. For instance, it can generate descriptions based on images, answer image-based questions, or generate corresponding images from textual descriptions.

2. Strong Reasoning Abilities
By integrating visual and language information, LLaVA 7B can perform complex reasoning tasks, such as inferring details from image content or understanding the meaning behind images based on descriptions. This makes it highly effective in tasks like Visual Question Answering (VQA).

3. Openness and Scalability
LLaVA 7B is an open-source model, allowing researchers and developers to adjust and expand it according to their needs. This openness enables a variety of applications and ensures continuous improvement and iteration.

4. Multidomain Adaptability
LLaVA 7B is versatile across multiple domains and can be applied to fields like medical image analysis, data visualization interpretation, and creative content generation, providing valuable insights and solutions in each area.

5. Improved Efficiency
Despite its large architecture (7B parameters), LLaVA 7B has been optimized for resource consumption and inference speed, making it more efficient than earlier multimodal models in handling complex tasks.

6. Rich Training Data
LLaVA 7B has been trained on extensive image-text data, which allows it to deeply understand the contextual relationships between images and text. This results in more accurate image descriptions or better understanding of the context within images.

7. Collaboration Between Language and Vision
By processing both language and vision simultaneously, LLaVA 7B is able to bridge the gap between text and images, producing outputs that are contextually appropriate, fluent in language, and visually accurate.

In summary, LLaVA 7B is a powerful and versatile multimodal model with capabilities for handling text-image tasks. It excels in reasoning efficiency, openness, and adaptability, and can play a crucial role in both academic research and practical applications.

- Prompt
Analyze the image and identify the three most significant objects.Be specific about what the objects are (e.g., 'tree', 'car', 'building'). For each object, calculate its approximate proportion of the image (in percentage). Return the results in a single line, separated by commas, in the format: \"Object1: Proportion1%, Object2: Proportion2%, Object3: Proportion3%\".

### Run this code on raccoon's server
By using the studio's server, the running time can be reduced.
ˋˋˋ
#Server URL (adjust to match your Ollama docker setup)
    url = 'http://192.168.30.1:11434/api/generate'

