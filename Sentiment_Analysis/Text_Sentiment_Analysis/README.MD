## Text semantic analysis
Sentiment and semantic analysis of text allows for a direct and efficient understanding of the key points the writer aims to convey. By setting parameters such as keyword format, quantity, and precision, the desired output can be tailored to help clarify the relationships and differences among numerous texts, as well as uncover the emotions conveyed behind the words.
### Model-llama2
Llama 2 is an open-source large language model developed by Meta.Llama 2 is not only capable of semantic analysis but can also engage in conversations and Q&A sessions similar to ChatGPT and other OpenAI models by providing different prompts. Related models under Ollama can be installed and operated locally on a computer and used within editors such as Anaconda or VS Code. 
Here are the key features of Llama 2:
1. Llama 2 outperforms other open-source LLMs in benchmarks for reasoning, coding abilities, and knowledge testing.
2. The training dataset used for this model is nearly twice the size of Llama 1, totaling 2 trillion tokens. Additionally, the training includes over 1 million newly annotated data points and fine-tuning for dialogue completion.
3. Llama 2 supports a longer context length, accommodating up to 4,096 tokens.
4. The licensing agreement for the second version is more permissive than the first, allowing for commercial use.

### Prompt 
"please summarize the given text with one keywords related to emotions or feelings, and reply only the keywords separated by commas:{text}"

### Run Ollama locally using the Docker as a container
   1. First, install Docker on your computer.

   - [Docker_Installation_Tutorial](/Sentiment_Analysis/Docker_Installation.MD)

   2. Once Docker is set up and the container for running Ollama is functioning properly, return to the editor's page, define the local API URL for the computer, and execute the entire code.

   *Ollama runs by default on port 11434. You can check if the port is in use using the following method.*
   
   ```
   # 定義 Ollama 本地 API URL
   OLLAMA_API_URL = "url_to_your_computer/v1/completions"
   ```

   On Windows: Use PowerShell or Command Prompt:
      ```
      netstat -an | findstr 11434
      ```
      
   If the port is in use, it will display a result similar to the following:
      ```
      TCP    0.0.0.0:11434             0.0.0.0:0              LISTENING
      ```