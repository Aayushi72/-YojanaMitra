import streamlit as st

# ===============================================================
# SECTION 1: SCHEMES DATA
# ===============================================================
SCHEMES = [
    {
        "name": "PM-KISAN",
        "benefit": "Rs 6,000 per year in three instalments of Rs 2,000 for landholding farmer families.",
        "criteria": {"occupation": "farmer"},
        "also_check": [
            "The land is in your name (land records).",
            "No family member is an income-tax payer, a government employee/pensioner "
            "(pension Rs 10,000+), or a holder of a constitutional post.",
        ],
        "documents": ["Aadhaar", "Land records", "Bank account details"],
        "apply": "https://pmkisan.gov.in",
    },
    {
        "name": "Post Matric Scholarship for SC Students",
        "benefit": "Fee reimbursement and maintenance allowance for SC students after Class 10.",
        "criteria": {"occupation": "student", "category": "SC", "max_income": 250000},
        "also_check": [
            "You passed Class 10 or higher and are in a recognised course.",
            "You are not receiving another scholarship.",
        ],
        "documents": ["Caste certificate", "Income certificate", "Marksheet",
                      "Admission proof", "Aadhaar-linked bank account"],
        "apply": "https://scholarships.gov.in",
    },
    {
        "name": "Post Matric Scholarship for ST Students",
        "benefit": "Fee reimbursement and maintenance allowance for ST students from Class 11 onwards.",
        "criteria": {"occupation": "student", "category": "ST", "max_income": 250000},
        "also_check": [
            "You belong to a Scheduled Tribe of your domicile state.",
            "You are not receiving another scholarship.",
        ],
        "documents": ["Caste certificate", "Income certificate", "Marksheet",
                      "Admission proof", "Aadhaar-linked bank account"],
        "apply": "https://scholarships.gov.in",
    },
    {
        "name": "Indira Gandhi National Old Age Pension (IGNOAPS)",
        "benefit": "Monthly pension for elderly people from BPL households (central share Rs 200, "
                   "Rs 500 for 80+; states may add to it).",
        "criteria": {"min_age": 60, "bpl": True},
        "also_check": ["Your name is on the BPL list of your state/UT."],
        "documents": ["Age proof", "BPL card / certificate", "Aadhaar", "Bank or post office account"],
        "apply": "https://nsap.nic.in",
    },
    {
        "name": "Ayushman Vay Vandana Card (PM-JAY, 70+)",
        "benefit": "Free hospital cover up to Rs 5 lakh per year for every citizen aged 70+, "
                   "whatever their income.",
        "criteria": {"min_age": 70},
        "also_check": [
            "Age is verified through Aadhaar (e-KYC).",
            "If you already have CGHS / ECHS / Ayushman CAPF cover you must choose one scheme. "
            "ESIC and private-insurance holders can add this card.",
        ],
        "documents": ["Aadhaar", "Mobile number linked to Aadhaar"],
        "apply": "https://beneficiary.nha.gov.in",
    },
    {
        "name": "Sukanya Samriddhi Yojana",
        "benefit": "High-interest savings account for a girl child's education and marriage.",
        "criteria": {"gender": "female", "max_age": 9},
        "also_check": [
            "The account is opened by a parent/legal guardian; max 2 girls per family.",
            "Sources say 'below 10 years' - confirm the exact cutoff at your bank/post office.",
        ],
        "documents": ["Girl's birth certificate", "Parent/guardian ID and address proof"],
        "apply": "https://www.indiapost.gov.in",
    },
    {
        "name": "Atal Pension Yojana",
        "benefit": "Guaranteed monthly pension of Rs 1,000 to Rs 5,000 from age 60.",
        "criteria": {"min_age": 18, "max_age": 40},
        "also_check": [
            "You have a savings bank or post office account.",
            "You are not, and have not been, an income-tax payer (rule since 1 Oct 2022).",
        ],
        "documents": ["Aadhaar", "Savings bank account", "Mobile number", "Nominee details"],
        "apply": "https://www.myscheme.gov.in/schemes/apy",
    },
    {
        "name": "PM Shram Yogi Maandhan (PM-SYM)",
        "benefit": "Assured pension of Rs 3,000 per month from age 60 for unorganised workers.",
        "criteria": {"occupation": "worker", "min_age": 18, "max_age": 40, "max_income": 180000},
        "also_check": [
            "Your own monthly income is Rs 15,000 or less (the Rs 1,80,000 above is a yearly approximation).",
            "You are not a member of EPFO / ESIC / NPS and not an income-tax payer.",
        ],
        "documents": ["Aadhaar", "Savings bank / Jan Dhan account", "Mobile number"],
        "apply": "https://maandhan.in/",
    },
    {
        "name": "PM Suraksha Bima Yojana (PMSBY)",
        "benefit": "Rs 2 lakh accident cover (Rs 1 lakh for partial disability) for Rs 20 per year.",
        "criteria": {"min_age": 18, "max_age": 70},
        "also_check": ["You have a bank account linked to Aadhaar."],
        "documents": ["Aadhaar", "Bank account", "Nominee details"],
        "apply": "https://jansuraksha.gov.in",
    },
    {
        "name": "PM Jeevan Jyoti Bima Yojana (PMJJBY)",
        "benefit": "Rs 2 lakh life cover (death from any cause) for Rs 436 per year.",
        "criteria": {"min_age": 18, "max_age": 50},
        "also_check": ["You have a bank or post office account (cover can continue till age 55)."],
        "documents": ["Aadhaar", "Bank account", "Nominee details"],
        "apply": "https://jansuraksha.gov.in",
    },
    {
        "name": "Uttarakhand Old Age Pension",
        "benefit": "Rs 1,500 per month for senior citizens of Uttarakhand.",
        "criteria": {"state": "Uttarakhand", "min_age": 60, "income_or_bpl": 48000},
        "also_check": ["You are not receiving any other pension."],
        "documents": ["Age proof", "Income certificate or BPL card", "Aadhaar", "Bank account"],
        "apply": "https://ssp.uk.gov.in",
    },
    {
        "name": "Uttarakhand Farmer Pension",
        "benefit": "Rs 1,200 per month for elderly farmers of Uttarakhand.",
        "criteria": {"state": "Uttarakhand", "occupation": "farmer", "min_age": 60},
        "also_check": [
            "You own and cultivate up to 2 hectares of land.",
            "Source says 'above 60' - confirm the exact age cutoff with the department.",
        ],
        "documents": ["Land records", "Age proof", "Aadhaar", "Bank account"],
        "apply": "https://www.myscheme.gov.in",  # VERIFY: find the department's own portal link
    },
]

# ===============================================================
# SECTION 2: ELIGIBILITY ENGINE

# ===============================================================
def check_scheme(profile, c):
    checks = []

    def add(text, value):
        checks.append((text, value))

    def unknown(field):
        return profile.get(field) is None

    if "min_age" in c:
        add(f"Age is {c['min_age']} or above",
            None if unknown("age") else profile["age"] >= c["min_age"])
    if "max_age" in c:
        add(f"Age is {c['max_age']} or below",
            None if unknown("age") else profile["age"] <= c["max_age"])
    if "max_income" in c:
        add(f"Annual family income up to Rs {c['max_income']:,}",
            None if unknown("income") else profile["income"] <= c["max_income"])
    if "gender" in c:
        add(f"Gender: {c['gender']}",
            None if unknown("gender") else profile["gender"] == c["gender"])
    if "occupation" in c:
        add(f"Occupation: {c['occupation']}",
            None if unknown("occupation") else profile["occupation"] == c["occupation"])
    if "category" in c:
        add(f"Category: {c['category']}",
            None if unknown("category") else profile["category"] == c["category"])
    if "state" in c:
        add(f"Resident of {c['state']}",
            None if unknown("state") else profile["state"] == c["state"])
    if "bpl" in c:
        add("Belongs to a BPL (below poverty line) household",
            None if unknown("bpl") else profile["bpl"] == c["bpl"])
    if "income_or_bpl" in c:
        # OR condition with three-valued logic: True if either holds,
        # False only if both are known to fail, otherwise unknown.
        limit = c["income_or_bpl"]
        by_income = None if unknown("income") else profile["income"] <= limit
        by_bpl = None if unknown("bpl") else profile["bpl"]
        if by_income is True or by_bpl is True:
            value = True
        elif by_income is False and by_bpl is False:
            value = False
        else:
            value = None
        add(f"Family income up to Rs {limit:,} per year OR BPL household", value)

    values = [v for _, v in checks]
    if False in values:
        status = "not_eligible"
    elif None in values:
        status = "unsure"
    else:
        status = "eligible"
    return status, checks


# ===============================================================
# SECTION 3: USER INTERFACE
# ===============================================================
ICON = {True: "✅", False: "❌", None: "❓"}

st.set_page_config(page_title="YojanaMitra", page_icon="🤝")
st.title("🤝 YojanaMitra")
st.caption("Find government schemes you may be eligible for. "
           "Guidance only - always confirm on the official portal.")

with st.form("profile_form"):
    age = st.number_input("Age (leave 0 to skip)", 0, 120, 0)
    income = st.number_input("Annual family income in Rs (leave 0 to skip)",
                             0, 10_000_000, 0, step=10000)
    gender = st.selectbox("Gender", ["Skip", "female", "male", "other"])
    occupation = st.selectbox("Occupation", ["Skip", "farmer", "student", "worker",
                                             "self-employed", "unemployed", "homemaker"])
    category = st.selectbox("Category", ["Skip", "General", "OBC", "SC", "ST"])
    state = st.selectbox("State", ["Skip", "Uttarakhand", "Other"])
    bpl = st.selectbox("Is your household BPL (below poverty line)?", ["Skip", "Yes", "No"])
    submitted = st.form_submit_button("Find my schemes")


def val(x):
    return None if x == "Skip" else x


def show(group, title, note):
    st.subheader(title)
    if not group:
        st.write("None")
        return
    st.caption(note)
    for s, status, checks in group:
        with st.expander(s["name"]):
            st.write(f"**Benefit:** {s['benefit']}")
            st.write("**Why:**")
            for text, v in checks:
                st.write(f"{ICON[v]} {text}")
            if s.get("also_check"):
                st.write("**Also confirm:**")
                for item in s["also_check"]:
                    st.write(f"🔎 {item}")
            st.write("**Documents needed:** " + ", ".join(s["documents"]))
            st.markdown(f"[Apply / official site]({s['apply']})")


if submitted:
    profile = {
        "age": age or None,
        "income": income or None,
        "gender": val(gender),
        "occupation": val(occupation),
        "category": val(category),
        "state": val(state),
        "bpl": None if bpl == "Skip" else (bpl == "Yes"),
    }
    results = [(s, *check_scheme(profile, s["criteria"])) for s in SCHEMES]
    eligible = [r for r in results if r[1] == "eligible"]
    unsure = [r for r in results if r[1] == "unsure"]

    show(eligible, f"✅ You appear eligible ({len(eligible)})",
         "All checked criteria matched. Read the 'Also confirm' points before applying.")
    show(unsure, f"❓ Possibly eligible ({len(unsure)})",
         "Answer the skipped fields (marked ❓) to confirm.")

# ===============================================================
# SECTION 4: EVALUATION 
# ===============================================================
PMK = "PM-KISAN"
SC = "Post Matric Scholarship for SC Students"
ST = "Post Matric Scholarship for ST Students"
IGNOAPS = "Indira Gandhi National Old Age Pension (IGNOAPS)"
VAY = "Ayushman Vay Vandana Card (PM-JAY, 70+)"
SSY = "Sukanya Samriddhi Yojana"
APY = "Atal Pension Yojana"
PMSYM = "PM Shram Yogi Maandhan (PM-SYM)"
PMSBY = "PM Suraksha Bima Yojana (PMSBY)"
PMJJBY = "PM Jeevan Jyoti Bima Yojana (PMJJBY)"
UKOAP = "Uttarakhand Old Age Pension"
UKFP = "Uttarakhand Farmer Pension"


def P(age, income, gender, occupation, category, state, bpl):
    return {"age": age, "income": income, "gender": gender, "occupation": occupation,
            "category": category, "state": state, "bpl": bpl}


PERSONAS = [
    # 1. Middle-aged farmer, Uttarakhand
    {"profile": P(45, 80000, "male", "farmer", "General", "Uttarakhand", False),
     "expected": [PMK, PMSBY, PMJJBY]},
    # 2. SC student
    {"profile": P(20, 150000, "female", "student", "SC", "Uttarakhand", False),
     "expected": [SC, APY, PMSBY, PMJJBY]},
    # 3. Poor elderly man, BPL
    {"profile": P(68, 40000, "male", "unemployed", "General", "Uttarakhand", True),
     "expected": [IGNOAPS, PMSBY, UKOAP]},
    # 4. Young girl
    {"profile": P(8, 200000, "female", "student", "General", "Uttarakhand", False),
     "expected": [SSY]},
    # 5. Elderly BPL woman farmer
    {"profile": P(65, 50000, "female", "farmer", "OBC", "Uttarakhand", True),
     "expected": [PMK, IGNOAPS, PMSBY, UKOAP, UKFP]},
    # 6. Edge: age 60, income just ABOVE the Uttarakhand pension limit, not BPL
    {"profile": P(60, 49000, "male", "unemployed", "General", "Uttarakhand", False),
     "expected": [PMSBY]},
    # 7. Edge: age 60, income exactly AT the limit
    {"profile": P(60, 48000, "female", "homemaker", "General", "Uttarakhand", False),
     "expected": [UKOAP, PMSBY]},
    # 8. Edge: age exactly 70, well-off (Vay Vandana ignores income)
    {"profile": P(70, 300000, "male", "self-employed", "General", "Uttarakhand", False),
     "expected": [VAY, PMSBY]},
    # 9. Edge: age 71 farmer (too old for PMSBY)
    {"profile": P(71, 100000, "male", "farmer", "General", "Uttarakhand", False),
     "expected": [PMK, VAY, UKFP]},
    # 10. Young worker outside Uttarakhand
    {"profile": P(25, 120000, "male", "worker", "General", "Other", False),
     "expected": [PMSYM, APY, PMSBY, PMJJBY]},
    # 11. Edge: worker at age 40 and income exactly Rs 1,80,000
    {"profile": P(40, 180000, "female", "worker", "OBC", "Other", False),
     "expected": [PMSYM, APY, PMSBY, PMJJBY]},
    # 12. Edge: worker aged 41 (just past APY / PM-SYM age limit)
    {"profile": P(41, 100000, "male", "worker", "General", "Other", False),
     "expected": [PMSBY, PMJJBY]},
    # 13. Edge: worker income Rs 1 above the PM-SYM approximation
    {"profile": P(30, 180001, "male", "worker", "General", "Uttarakhand", False),
     "expected": [APY, PMSBY, PMJJBY]},
    # 14. Edge: ST student with income exactly Rs 2.5 lakh
    {"profile": P(19, 250000, "male", "student", "ST", "Uttarakhand", False),
     "expected": [ST, APY, PMSBY, PMJJBY]},
    # 15. Edge: SC student income Rs 1 above the limit
    {"profile": P(22, 250001, "female", "student", "SC", "Other", False),
     "expected": [APY, PMSBY, PMJJBY]},
    # 16. Minor with no matching scheme
    {"profile": P(17, 100000, "male", "student", "General", "Uttarakhand", False),
     "expected": []},
    # 17. Edge: girl aged 9 (still eligible for Sukanya)
    {"profile": P(9, 60000, "female", "student", "General", "Uttarakhand", True),
     "expected": [SSY]},
    # 18. Girl aged 11 (too old for Sukanya)
    {"profile": P(11, 60000, "female", "student", "General", "Uttarakhand", False),
     "expected": []},
    # 19. Farmer in another state (no Uttarakhand schemes)
    {"profile": P(35, 90000, "female", "farmer", "SC", "Other", False),
     "expected": [PMK, APY, PMSBY, PMJJBY]},
    # 20. Elderly BPL farmer, Uttarakhand
    {"profile": P(61, 30000, "male", "farmer", "General", "Uttarakhand", True),
     "expected": [PMK, IGNOAPS, PMSBY, UKOAP, UKFP]},
]

st.divider()
with st.expander("📊 Evaluation results (test personas)"):
    tp = fp = fn = exact = 0
    for i, p in enumerate(PERSONAS, start=1):
        predicted = {s["name"] for s in SCHEMES
                     if check_scheme(p["profile"], s["criteria"])[0] == "eligible"}
        expected = set(p["expected"])
        tp += len(predicted & expected)
        fp += len(predicted - expected)
        fn += len(expected - predicted)
        if predicted == expected:
            exact += 1
        else:
            st.warning(f"Persona {i} mismatch. Expected: {sorted(expected)} | Got: {sorted(predicted)}")

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0

    st.write(f"**Schemes in database:** {len(SCHEMES)}")
    st.write(f"**Personas tested:** {len(PERSONAS)}")
    st.write(f"**Exact-match personas:** {exact}/{len(PERSONAS)}")
    st.write(f"**Precision:** {precision:.2f} | **Recall:** {recall:.2f} | **F1:** {f1:.2f}")