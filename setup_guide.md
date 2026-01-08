# 🎓 The Refactoring Swarm - Complete Implementation Guide

## 📋 Project Overview

This is a complete implementation of the IGL Lab multi-agent system for autonomous software maintenance using LangChain and Google Gemini.

---

## 📁 Complete Directory Structure

```
refactoring-swarm-template/
│
├── main.py                          ✅ Complete CLI entry point
├── requirements.txt                 ✅ All dependencies listed
├── .env                            ✅ API key configured
├── .env.example                    ✅ Template provided
├── check_setup.py                  ✅ Environment validator
├── .gitignore                      ✅ Proper Git config
│
├── src/
│   ├── agents/
│   │   ├── __init__.py            ⚠️  CREATE THIS (empty file)
│   │   ├── auditor_agent.py       ✅ Analyzes code
│   │   ├── fixer_agent.py         ✅ Applies fixes
│   │   └── judge_agent.py         ✅ Validates results
│   │
│   ├── tools/
│   │   ├── __init__.py            ⚠️  CREATE THIS (empty file)
│   │   ├── file_operations.py     ✅ File I/O with sandbox security
│   │   ├── static_analysis.py     ✅ Pylint integration
│   │   └── test_runner.py         ✅ Pytest integration
│   │
│   ├── orchestrator/
│   │   ├── __init__.py            ⚠️  CREATE THIS (empty file)
│   │   └── refactoring_graph.py   ✅ Agent coordination
│   │
│   └── utils/
│       ├── __init__.py            ⚠️  CREATE THIS (empty file)
│       └── logger.py              ✅ Already provided
│
├── logs/
│   ├── .gitkeep                   ✅ Already exists
│   └── experiment_data.json       ✅ Auto-generated
│
└── sandbox/                        ✅ Working directory (auto-created)
```

---

## 🚀 Installation Steps

### Step 1: Clone and Setup

```bash
# If you already cloned the template, navigate to it
cd refactoring-swarm-template

# Create virtual environment
python3 -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key

The `.env` file has been created with your API key:

```bash
GOOGLE_API_KEY="AIzaSyCtMfSviIJWqAR47PiDZST8gdw9iMNcEP0"
```

**⚠️ CRITICAL**: NEVER commit the `.env` file to Git!

### Step 4: Create `__init__.py` Files

Create empty `__init__.py` files in each module directory:

```bash
# Create all __init__.py files
touch src/__init__.py
touch src/agents/__init__.py
touch src/tools/__init__.py
touch src/orchestrator/__init__.py
touch src/utils/__init__.py
```

Or manually create empty files in VS Code.

### Step 5: Verify Setup

```bash
python check_setup.py
```

Expected output:
```
✅ Python Version: 3.10 (or 3.11)
✅ Fichier .env détecté.
✅ Clé API présente
✅ Dossier logs/ créé.
🚀 TOUT EST PRÊT ! Vous pouvez commencer.
```

---

## 🎯 Usage

### Basic Usage

```bash
python main.py --target_dir "./path/to/buggy/code"
```

### Test with Sample Code

Create a test file to verify the system works:

```bash
mkdir -p sandbox/test_project
```

Create `sandbox/test_project/buggy_code.py`:

```python
def calculate(x,y):
    result=x+y
    return result

def divide(a,b):
    return a/b

class myclass:
    def __init__(self):
        self.value=10
```

Run the refactoring:

```bash
python main.py --target_dir "./sandbox/test_project"
```

---

## 📊 How It Works

### Pipeline Stages

```
1. AUDIT (Auditor Agent)
   ├─ Scans all Python files
   ├─ Runs Pylint static analysis
   ├─ Uses LLM to identify issues
   └─ Creates refactoring plan

2. FIX (Fixer Agent)
   ├─ Reads refactoring plan
   ├─ Uses LLM to fix code
   ├─ Applies corrections file-by-file
   └─ Writes fixed code to sandbox

3. VALIDATE (Judge Agent)
   ├─ Runs Pytest tests
   ├─ Checks Pylint score improvement
   └─ Decision:
       ├─ ✅ Success → Mission Complete
       └─ ❌ Failure → Loop back to FIX (max 10 iterations)
```

### Self-Healing Loop

The system automatically retries failed fixes:

- **Max Iterations**: 10
- **Feedback**: Error logs sent back to Fixer
- **Exit Conditions**:
  - ✅ Tests pass + Quality improved
  - ⚠️ Max iterations reached

---

## 📝 Key Features

### 1. **Sandbox Security**
- All file operations restricted to `sandbox/` directory
- Prevents agents from modifying system files

### 2. **Comprehensive Logging**
- Every agent interaction logged to `logs/experiment_data.json`
- Includes prompts, responses, and metadata
- Required for grading (30% of score)

### 3. **Multi-Tool Integration**
- **Pylint**: Code quality analysis
- **Pytest**: Unit test execution
- **LangChain**: LLM orchestration
- **Google Gemini**: AI-powered code analysis and fixing

### 4. **Iteration Management**
- Automatic retry with feedback
- Loop limit prevents infinite execution
- Progress tracking and reporting

---

## 🧪 Testing Your Implementation

### Create Test Dataset

Create `sandbox/test_cases/` with intentionally buggy files:

**File 1: `buggy_math.py`**
```python
def add(a,b):
    return a+b

def subtract(x,y):
    return x-y

def divide(numerator,denominator):
    return numerator/denominator
```

**File 2: `test_math.py`**
```python
from buggy_math import add, subtract, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5
```

Run:
```bash
python main.py --target_dir "./sandbox/test_cases"
```

---

## 📊 Evaluation Criteria

Your system will be graded on:

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| **Performance** | 40% | • Tests pass?<br>• Pylint score improved? |
| **Technical Robustness** | 30% | • No crashes?<br>• No infinite loops?<br>• Respects `--target_dir`? |
| **Data Quality** | 30% | • Valid `experiment_data.json`?<br>• Complete interaction history?<br>• Prompts logged correctly? |

---

## 🔍 Troubleshooting

### Issue: Import Errors

**Solution**: Make sure all `__init__.py` files exist:
```bash
find src -type d -exec touch {}/__init__.py \;
```

### Issue: API Key Not Working

**Solution**: Verify `.env` file exists and contains:
```bash
cat .env
# Should show: GOOGLE_API_KEY="AIzaSyC..."
```

### Issue: No Logs Generated

**Solution**: Check that logger is being called with all required fields:
```python
log_experiment(
    agent_name="Test",
    model_used="gemini-2.5-flash",
    action=ActionType.ANALYSIS,
    details={
        "input_prompt": "test",      # REQUIRED
        "output_response": "response" # REQUIRED
    },
    status="SUCCESS"
)
```

### Issue: Pylint Not Found

**Solution**: Reinstall requirements:
```bash
pip install --upgrade pylint pytest
```

---

## 🚨 Critical Reminders

### Before Submission

1. **Force add logs** (they're in `.gitignore` by default):
   ```bash
   git add -f logs/experiment_data.json
   git commit -m "DATA: Final experiment logs"
   git push origin main
   ```

2. **Verify logs are not empty**:
   ```bash
   cat logs/experiment_data.json | python -m json.tool
   ```

3. **Check Git history**:
   - Multiple commits showing progress
   - Clear commit messages
   - NO single commit on last day

---

## 🎓 Team Roles Mapping

| Role | Files to Focus On |
|------|-------------------|
| **Orchestrator (Lead)** | `main.py`, `refactoring_graph.py` |
| **Toolsmith** | `file_operations.py`, `static_analysis.py`, `test_runner.py` |
| **Prompt Engineer** | Agent prompts in `*_agent.py` files |
| **Quality Manager** | `logger.py`, test datasets, validation |

---

## 🎯 Next Steps

1. ✅ **Test the basic pipeline** with sample code
2. ✅ **Create diverse test cases** (various bug types)
3. ✅ **Optimize prompts** for better fixes
4. ✅ **Improve error handling** and edge cases
5. ✅ **Document your approach** in commit messages
6. ✅ **Review and test** on hidden dataset simulation

---

## 📚 Additional Resources

- **LangChain Docs**: https://python.langchain.com/docs/
- **Google Gemini API**: https://ai.google.dev/docs
- **Pylint**: https://pylint.pycqa.org/
- **Pytest**: https://docs.pytest.org/

---

## ✅ Checklist Before Submission

- [ ] All `__init__.py` files created
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] `.env` file configured (NOT committed)
- [ ] `check_setup.py` passes
- [ ] Basic test run successful
- [ ] `logs/experiment_data.json` contains data
- [ ] Logs force-committed to Git
- [ ] Multiple commits with clear messages
- [ ] Team repository on GitHub
- [ ] All team members have access

---

**Good luck with your lab! 🚀**
