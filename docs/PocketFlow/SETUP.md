# Setting Up the Virtual Environment

1. Navigate to the project directory:
   ```bash
   cd /path/to/your/PocketFlow-Template-Python
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scriptsctivate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install required packages:
   ```bash
   pip install pocketflow openai pyyaml
   ```

5. Save dependencies to `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

To run the project, ensure the virtual environment is activated and execute:
```bash
python main.py
```

