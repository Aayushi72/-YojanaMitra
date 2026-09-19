# 🤝 YojanaMitra

### An explainable eligibility checker that helps citizens discover the central and Uttar Pradesh government schemes they qualify for

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b)
![Status](https://img.shields.io/badge/Status-Hackathon%20Prototype-green)

> **Live demo / video:** `<add link here>`  |  **Team / Author:** `<your name>`  |  **Hackathon:** `<hackathon name>`

---

## 📌 Table of Contents
1. [Problem Statement](#-problem-statement)
2. [Project Description](#-project-description)
3. [Key Features](#-key-features)
4. [How It Works](#-how-it-works)
5. [Technology Used](#-technology-used)
6. [Schemes Covered](#-schemes-covered)
7. [Installation and Usage](#-installation-and-usage)
8. [Evaluation](#-evaluation)
9. [Project Structure](#-project-structure)
10. [Adding a New Scheme](#-adding-a-new-scheme)
11. [Limitations](#-limitations)
12. [Future Scope](#-future-scope)
13. [Disclaimer](#-disclaimer)

---

## 🎯 Problem Statement

India runs hundreds of welfare schemes for farmers, students, women, the elderly, and workers, yet many eligible people never claim them. The reasons are practical:

- Information is scattered across many portals, PDFs, and news pages.
- Eligibility rules are written in dense, official language.
- People don't know **which** schemes apply to them, or **which documents** to carry.
- Rules change, and it is hard to tell whether a page is current.

The result is that benefits meant for the people who need them most go unclaimed.

## 📖 Project Description

**YojanaMitra** ("friend of schemes") is a web app where a person enters a few simple details, such as age, income, occupation, category, state, and area. The app instantly shows:

- ✅ the schemes they **appear eligible** for,
- ❓ the schemes they are **possibly eligible** for, along with exactly which missing detail would settle it,
- the **benefit**, **documents required**, and the **official link** to apply for each scheme.

The core idea is **honest, explainable eligibility**. Eligibility is a high-stakes decision, so YojanaMitra does not guess. Every rule is checked deterministically and shown to the user with ✅ (met), ❌ (not met), or ❓ (unknown). When a detail is missing, the app says so instead of assuming. Conditions that a short form cannot capture (for example, "you own the land in your name") are shown separately under **"Also confirm"** so the tool never claims more certainty than it has.

## ✨ Key Features

| Feature | What it does |
|---|---|
| **Three-valued eligibility engine** | Every criterion returns *True*, *False*, or *Unknown*, so a scheme is *eligible*, *not eligible*, or *possibly eligible*. |
| **Explainable results** | Each card shows *why*, with a ✅ / ❌ / ❓ line for every criterion. |
| **Handles OR-conditions** | For example, "BPL **or** income under the limit" uses proper three-valued logic. |
| **Rural / urban aware** | The UP pension has different income limits for rural and urban areas, and the engine handles a skipped area correctly. |
| **"Also confirm" section** | Shows conditions the form cannot verify, such as land ownership or tax-payer status. |
| **Documents and apply links** | Shows what to carry and where to apply, so users can act right away. |
| **Built-in evaluation** | 26 hand-labelled test personas with precision, recall, and F1 shown inside the app. |
| **Privacy by design** | No database, no login, and the app does not store the details you enter. |

## ⚙️ How It Works

```
   User enters details (age, income, gender, occupation,
   category, state, area, BPL)  ── any field can be skipped
                      │
                      ▼
        Profile  (missing fields = None / unknown)
                      │
                      ▼
   ┌────────────────────────────────────────────────┐
   │        Rule-based Eligibility Engine           │
   │  for each scheme, check every criterion →      │
   │  True / False / None  (three-valued logic)     │
   └────────────────────────────────────────────────┘
                      │
        ┌─────────────┼───────────────┐
        ▼             ▼               ▼
   any False      any None        all True
  not eligible   possibly         eligible
                 eligible
                      │
                      ▼
   Result cards: benefit · why (✅❌❓) · also confirm
                 · documents · official apply link
```

**Design decision: rules, not a black box.** Eligibility decides whether someone gets government money, so the decision is made by transparent, testable rules and never by a model that might hallucinate. This also makes every result explainable, which builds trust.

## 🛠️ Technology Used

| Layer | Technology |
|---|---|
| Language | **Python 3** |
| Web framework / UI | **Streamlit** |
| Eligibility logic | Custom **rule-based engine** with **three-valued (Kleene-style) logic** |
| Data store | Python data structures (a list of scheme dictionaries), so no database is needed |
| Evaluation | Hand-labelled test personas with **precision / recall / F1** computed in pure Python |
| Development tools | Visual Studio Code, Git and GitHub |

## 📋 Schemes Covered

13 schemes (11 central and 2 Uttar Pradesh), with rules checked against government portals and reliable summaries in September 2026.

| # | Scheme | Level | Key rule encoded |
|---|---|---|---|
| 1 | PM-KISAN | Central | Landholding farmer families (with exclusions) |
| 2 | PM Kisan Maandhan Yojana | Central | Small/marginal farmers aged 18-40 |
| 3 | Post Matric Scholarship (SC) | Central | SC student, family income up to ₹2.5 lakh |
| 4 | Post Matric Scholarship (ST) | Central | ST student, family income up to ₹2.5 lakh |
| 5 | IGNOAPS (Old Age Pension) | Central | Age 60+ and BPL household |
| 6 | Ayushman Vay Vandana Card | Central | Age 70+, regardless of income |
| 7 | Sukanya Samriddhi Yojana | Central | Girl child below 10 years |
| 8 | Atal Pension Yojana | Central | Age 18-40, not an income-tax payer |
| 9 | PM Shram Yogi Maandhan | Central | Unorganised worker, age 18-40, monthly income ≤ ₹15,000 |
| 10 | PM Suraksha Bima Yojana | Central | Age 18-70 with a bank account |
| 11 | PM Jeevan Jyoti Bima Yojana | Central | Age 18-50 with a bank account |
| 12 | UP Old Age Pension | Uttar Pradesh | Age 60+, and BPL **or** income ≤ ₹46,080 (rural) / ₹56,460 (urban) |
| 13 | UP Mukhyamantri Kanya Sumangala Yojana | Uttar Pradesh | UP girl child, family income ≤ ₹3 lakh |

## 🚀 Installation and Usage

**Prerequisites:** Python 3.9 or newer.

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd yojanamitra

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python -m streamlit run app.py
```

The app opens at **http://localhost:8501**.

**Using the app:**
1. Fill in whatever you know. Any field can stay on **Skip**.
2. Click **Find my schemes**.
3. Open a card to see the benefit, the ✅ / ❌ / ❓ reasoning, the *Also confirm* points, the documents, and the apply link.
4. Scroll to **📊 Evaluation results** to see the accuracy on the test personas.

> 💡 For girl-child schemes (Sukanya Samriddhi, Kanya Sumangala), enter the **girl's** age.

## 📊 Evaluation

The engine is tested on **26 hand-labelled personas**. The expected list for each persona was written by reading the official rules, **not** copied from the program's output. The personas deliberately include boundary cases:

- income exactly **at** a limit and ₹1 **above** it (rural ₹46,080, urban ₹56,460, ₹1.8 lakh, ₹2.5 lakh, ₹3 lakh),
- ages exactly at the edges (18, 40, 41, 60, 70, 71),
- a skipped area where the answer must *not* be called eligible,
- people who match no scheme at all.

| Metric | Result |
|---|---|
| Schemes in database | 13 |
| Personas tested | 26 |
| Exact-match personas | 26 / 26 |
| Precision | 1.00 |
| Recall | 1.00 |
| F1 score | 1.00 |

Precision = correct eligible predictions ÷ all eligible predictions. Recall = correct eligible predictions ÷ all truly eligible cases.

**How to read these numbers honestly:** they show that the *code* correctly implements the rules, including the tricky edge cases. They do not prove that the scheme data is current, because government rules change. Always confirm on the official portal.

## 📁 Project Structure

```
yojanamitra/
├── app.py              # Scheme data + eligibility engine + Streamlit UI + evaluation
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

Inside `app.py`:
1. **Scheme data:** the `SCHEMES` list.
2. **Eligibility engine:** `check_scheme()`.
3. **User interface:** the Streamlit form and result cards.
4. **Evaluation:** `PERSONAS` and the precision / recall calculation.

## ➕ Adding a New Scheme

Add one block to the `SCHEMES` list. No other code needs to change.

```python
{
    "name": "Scheme name",
    "benefit": "One or two lines on what the person gets.",
    "criteria": {"min_age": 18, "max_income": 300000, "state": "Uttar Pradesh"},
    "also_check": ["Conditions the form cannot capture."],
    "documents": ["Aadhaar", "Income certificate"],
    "apply": "https://official-website",
},
```

Supported criteria: `min_age`, `max_age`, `max_income`, `gender`, `occupation`, `category`, `state`, `bpl`, `income_or_bpl` (a single limit, or a rural/urban dictionary).

## ⚠️ Limitations

- The form cannot capture every condition, such as land ownership, tax-payer status, or education level. These are shown as **Also confirm** notes instead of being guessed.
- Scheme rules change. The data reflects September 2026 and must be re-verified regularly.
- A few sources disagree on boundary values (for example, whether Sukanya Samriddhi allows a girl of exactly 10). The conservative reading is used and flagged on the card.
- The Kanya Sumangala age limit depends on the year (girls born on or after 1 April 2019) and needs a yearly update.
- Coverage is limited to 13 schemes, central plus Uttar Pradesh.

## 🔭 Future Scope

- **Voice and multilingual input** (Hindi and regional languages) using speech recognition such as Whisper, for users who prefer speaking.
- **Free-text understanding:** an LLM that turns "I am a 45-year-old farmer from UP" into the profile fields, with strict structured output and the same deterministic engine making the final decision.
- **Smart follow-up questions:** ask the one question that would resolve the most ❓ schemes (an information-gain approach).
- **RAG over scheme documents** to scale from tens of schemes to hundreds with grounded explanations.
- **OCR** to auto-fill the profile from income certificates and ration cards.
- **WhatsApp / Telegram bot** and an offline mode for low-connectivity villages.
- **More states** and a scheme-data update pipeline with change alerts.

## 📜 Disclaimer

YojanaMitra gives **guidance only**. It is not an official government service and does not guarantee eligibility or approval. Always confirm the current rules and apply through the official portal linked on each scheme card.

---

**Built for a 24-hour hackathon** to make welfare information simpler, clearer, and easier to act on.
