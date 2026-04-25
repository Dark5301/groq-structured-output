# 🤖 Structured AI Agent Output with Instructor + Groq

A Python project that demonstrates how to extract **structured, validated outputs** from a large language model using [Instructor](https://python.useinstructor.com/), [Pydantic](https://docs.pydantic.dev/), and [Groq](https://console.groq.com/). Built as a portfolio project exploring agentic AI patterns with enforced schema validation.

---

## 📌 What It Does

This script sends a natural language question to Groq's `llama-3.3-70b-versatile` model and forces the response into a strict Pydantic schema — returning a structured answer with a summary, key points, a confidence level, and an actionable next step.

Rather than getting a raw text blob back from the LLM, you get a fully validated Python object you can immediately work with programmatically.

---

## 🧱 Output Schema

The response is validated against the following `Answer` model:

| Field        | Type              | Constraints                        |
|--------------|-------------------|------------------------------------|
| `summary`    | `str`             | 10–100 characters                  |
| `key_points` | `list[str]`       | 3–7 items                          |
| `confidence` | `Confidence` enum | `"high"`, `"medium"`, or `"low"`   |
| `next_step`  | `str`             | 10–500 characters, actionable      |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Groq](https://groq.com/) | Fast LLM inference (LLaMA 3.3 70B) |
| [Instructor](https://python.useinstructor.com/) | Structured output enforcement via Pydantic |
| [Pydantic v2](https://docs.pydantic.dev/) | Data validation and schema definition |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Secure API key management |
| `asyncio` | Async-first design for agent-ready patterns |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Dark5301/groq-structured-output.git
cd groq-structured-output
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install groq instructor pydantic python-dotenv
```

### 4. Set up your environment variables

Create a `.env` file in the root of the project:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free Groq API key at [console.groq.com](https://console.groq.com).

### 5. Run the script

```bash
python json_output.py
```

---

## 📤 Example Output

**Input question:**
```
What are the best ways for a beginner Python developer in India to build their first AI agent product in 2026?
```

**Output:**
```
Summary: Beginner Python developers in India can build AI agents using free tools and cloud APIs.
Key Points:
. Start with a simple tool-calling agent using a hosted LLM API like Groq or OpenAI
. Use PydanticAI or LangChain to structure agent logic and tool definitions
. Focus on one vertical (e.g., web search, file I/O) before expanding capabilities
. Deploy on free tiers (Render, Railway, or Hugging Face Spaces) for portfolio visibility
. Contribute to open-source agent frameworks to build credibility
Confidence: high
Next Step: Build a single-tool agent using Groq's free API that answers questions by calling a web search function.
```

---

## 📁 Project Structure

```
.
├── json_output.py      # Main script
└── README.md
```

---

## ⚠️ Known Limitations

- **Instructor + Groq schema strictness**: Groq enforces strict JSON schema validation on tool calls. Complex `Union` or discriminated union types in Pydantic models can cause validation errors with `instructor`. For agentic patterns requiring multi-step tool routing, consider migrating to [PydanticAI](https://ai.pydantic.dev), which uses native function-calling patterns better suited to Groq's API.
- This project is **async-only** by design. Do not call `ask_structured_question` outside of an async context.

---

## 🔮 Roadmap

- [ ] Migrate to [PydanticAI](https://ai.pydantic.dev) for native tool-calling support
- [ ] Add CLI argument support for dynamic question input
- [ ] Expand schema to support multi-step agentic workflows
- [ ] Add unit tests with mocked LLM responses

---

## 👤 Author

**Prince**
Aspiring AI/Cybersecurity Developer · Python · Bash · JavaScript
Building a portfolio at the intersection of AI agents and penetration testing.

---

## 📄 License

MIT License — feel free to fork, modify, and build on this.
