# LangGraph Learning Project

A comprehensive UV-based Python project for learning and experimenting with LangGraph, LangChain, and related AI/ML workflows.

## 🚀 Project Setup from Scratch

### 1. UV Installation

UV is a fast Python package manager and project manager written in Rust.

```bash
# Install UV using the official installation script
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add UV to PATH (add this to your ~/.bashrc or ~/.zshrc)
export PATH="/home/homelab/.local/bin:$PATH"

# Verify installation
uv --version
```

### 2. Project Initialization

```bash
# Navigate to your desired directory
cd /home/homelab/git/master-python/llm-engineering

# Create and initialize the project
mkdir langgraph-learning
cd langgraph-learning
uv init .

# Rename project to avoid conflicts with langgraph package
# Edit pyproject.toml to change name from "langgraph" to "langgraph-learning"
```

### 3. Dependencies Installation

```bash
# Core LangGraph and LangChain dependencies
uv add langgraph langchain langchain-openai langchain-community

# Jupyter and development dependencies
uv add jupyter ipykernel

# Optional: Development tools (add as needed)
# uv add --dev black ruff pytest
```

### 4. Project Structure

After initialization, your project structure should look like:

```
langgraph-learning/
├── .python-version          # Python version specification (3.12)
├── .venv/                   # Virtual environment (auto-created by UV)
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Lockfile for reproducible installs
├── main.py                 # Basic Python entry point
├── langgraph_test.ipynb    # Jupyter notebook for testing
└── README.md               # This file
```

## 🐍 Python Environment Management

### Finding the Python Interpreter

```bash
# Get the exact Python interpreter path used by UV
uv run python -c "import sys; print(sys.executable)"
# Output: /home/homelab/git/master-python/llm-engineering/langgraph-learning/.venv/bin/python3

# Direct path to virtual environment Python
.venv/bin/python3

# List available Python interpreters
uv python list
```

### Running Python Code

```bash
# Run Python scripts with UV (recommended)
uv run python main.py
uv run python -c "import langgraph; print('LangGraph works!')"

# Alternative: Activate virtual environment manually
source .venv/bin/activate
python main.py
deactivate  # when done
```

## 📓 Jupyter Notebook Setup

### Initial Setup Issues & Solutions

**Problem**: Jupyter notebook was using system Python instead of UV virtual environment.

**Solution**: Install dedicated kernel for the UV environment.

```bash
# Install Jupyter kernel using UV environment
uv run python -m ipykernel install --user --name=langgraph-learning --display-name="LangGraph Learning (UV)"

# Verify kernel installation
jupyter kernelspec list
```

### VS Code Integration

1. **Select Python Interpreter**:
   - Open Command Palette (`Ctrl+Shift+P`)
   - Type "Python: Select Interpreter"
   - Choose: `/home/homelab/git/master-python/llm-engineering/langgraph-learning/.venv/bin/python3`

2. **Configure Notebook Kernel**:
   - Open the notebook
   - Click on the kernel selector in the top-right
   - Select "LangGraph Learning (UV)" kernel

### Testing the Setup

Run the provided `langgraph_test.ipynb` notebook to verify:
- ✅ Python interpreter is correct
- ✅ LangGraph imports successfully
- ✅ Basic workflow creation and execution works

## 🔧 Troubleshooting

### Common Issues

1. **"No module named 'langgraph'" in Jupyter**
   ```bash
   # Ensure kernel is properly installed
   uv run python -m ipykernel install --user --name=langgraph-learning --display-name="LangGraph Learning (UV)"
   
   # Restart VS Code and select the correct kernel
   ```

2. **UV command not found**
   ```bash
   # Add UV to PATH
   export PATH="/home/homelab/.local/bin:$PATH"
   
   # Or use absolute path
   /home/homelab/.local/bin/uv --version
   ```

3. **Wrong Python interpreter in VS Code**
   ```bash
   # Get correct path
   uv run python -c "import sys; print(sys.executable)"
   
   # Use this path in VS Code interpreter selection
   ```

### Debugging Commands

```bash
# Check UV project status
uv tree                    # Show dependency tree
uv pip list               # List installed packages
uv run python --version  # Verify Python version

# Environment verification
uv run python -c "import sys; print('Python:', sys.executable)"
uv run python -c "import langgraph; print('LangGraph: OK')"
uv run python -c "import langchain; print('LangChain:', langchain.__version__)"

# Check virtual environment
ls -la .venv/bin/python*  # List Python executables
cat .python-version       # Check Python version specification
```

## 📦 Package Management

```bash
# Add new dependencies
uv add package-name
uv add --dev package-name     # Development dependencies
uv add package-name==1.2.3   # Specific version

# Remove packages
uv remove package-name

# Update packages
uv lock --upgrade            # Update lockfile
uv sync                      # Sync with lockfile

# Install from lockfile (for reproducible setup)
uv sync --frozen
```

## 🏗️ Project Configuration

### pyproject.toml Key Sections

```toml
[project]
name = "langgraph-learning"
version = "0.1.0"
description = "LangGraph learning and experimentation project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "langchain>=1.0.2",
    "langchain-community>=0.4",
    "langchain-openai>=1.0.1",
    "langgraph>=1.0.1",
    "jupyter>=1.1.1",
    "ipykernel>=7.0.1",
]
```

## 🎯 Next Steps

1. **Explore LangGraph Features**:
   - State management
   - Conditional edges
   - Memory and persistence
   - Tool integration

2. **Advanced Workflows**:
   - Multi-agent systems
   - Custom node types
   - Error handling
   - Streaming responses

3. **Integration Examples**:
   - OpenAI GPT models
   - Local LLMs (Ollama)
   - Vector databases
   - External APIs

## 📚 Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)

## 🤝 Contributing

Feel free to add more examples, improvements, and learning materials to this project!

---

**Note**: This setup was tested on Ubuntu Linux with Python 3.12.3. Commands may vary slightly on other systems.