## Docker installation
### UI Interface
1. Download Docker [Docker](https://www.docker.com/)
2. Open Docker and wait for it to start running.
3. Open Command Prompt (Windows+R - cmd) or Anaconda, then enter the following code to install the UI interface:
   ```
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
   ```
4. Inside Docker, there will be an "open-webui" item. Click the URL in the Port column (http://localhost:3000 or 3000:8000), and it will automatically open the browser interface.
5. Sign up by entering your registration information (the information is stored locally, and the first person to create an account is the system administrator).
6. After completing the registration, you will enter a chat interface similar to ChatGPT.

### Docker Image Setup
1. Open Docker Desktop. Ensure that your Docker Desktop is up and running.
2. Prepare the Dockerfile.
   You need to create a Dockerfile locally, which is the configuration file that defines how to build the image.
   For example, if you want to run Ollama, your Dockerfile might look like this:
   ```
   # 使用官方 Python 映像作為基礎映像
   FROM python:3.9-slim

   # 設定工作目錄
   WORKDIR /app

   # 安裝必要的依賴
   RUN pip install --no-cache-dir ollama

   # 開放必要的端口
   EXPOSE 11434

   # 執行 Ollama 服務
   CMD ["ollama", "serve"]
   ```
