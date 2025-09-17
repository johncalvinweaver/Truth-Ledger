# 🧾 Truth Ledger

**Truth Ledger** is an open-source project dedicated to preserving and timestamping verified truths. It is designed to be a public, immutable record of claims, facts, and verifications—operating as a distributed journal of record in an era of misinformation.

---

## 🌐 Purpose

In a world flooded with deepfakes, AI-generated media, and institutional spin, *Truth Ledger* serves as a decentralized source of verified, timestamped assertions—each contributed by agents, journalists, researchers, or trusted systems.

---

## 🔍 Key Features

- ✅ **Fact Claim Registration**
- 🔐 **Verifier Registry with Identity Layer**
- ⏱️ **Blockchain-style Timestamping**
- 🧠 **GPT-based Reasoning and Confidence Scoring**
- 🔄 **Audit Trail for Truth Evolution**
- 🗣️ **Natural Language Query Interface**

Long version

Truth Ledger is an open-source AI-human hybrid project designed to preserve verified statements, facts, and claims in a transparent, timestamped, and verifiable format.

In an era of deepfakes, mass misinformation, and algorithmic manipulation, Truth Ledger offers a radically transparent tool for recording and preserving truth as it is known at a specific point in time, while also allowing for revision, verification, and lineage tracking. It acts as an open memory for civilization — built to withstand institutional decay, technological obsolescence, and human bias.

🔍 What Makes Truth Ledger Different?

Truth Ledger is not a social network.
It is not about opinions, followers, or popularity. It is a protocol, a platform, and a project built on the following principles:
• Immutable: Once a claim is logged and timestamped, it cannot be altered, only superseded or revised with version lineage.
• Transparent: Every addition to the ledger is public. All edits, verifications, and disputes are visible and auditable.
• Verifiable: Every claim is hashed, timestamped, and optionally verified by human experts, AI systems, or institutional sources.
• Inclusive: Truth Ledger allows both humans and artificial agents to register and debate truth claims, building an archive of collective knowledge.
• Evolving: New facts emerge. Old facts get debunked. The Ledger grows not by rigid certainty, but by layered contextual truth.

🧠 What is Logged in the Ledger?
• Claims — Declarative statements in plain language (e.g., “Water boils at 100°C at sea level.”)
• Timestamps — UTC markers of when the claim was submitted
• Hashes — A SHA-256 hash that acts as a unique fingerprint for the claim
• Verifications (optional) — Signatures by trusted agents or expert systems marking a claim as verified, disputed, or outdated
• Revisions — New claims that reference older claims and update or contextualize them

🔧 Core Use Cases
• Researchers can log findings with proof links and cite earlier claims
• Journalists can register events as they happen with location and source context
• AI Systems can summarize, index, and challenge entries based on logical analysis or outside data
• Civic Institutions can create chains of verified declarations from trusted agents
• Individuals can record moments of truth in their lives (e.g., testimony, whistleblowing, open letters)

🔗 Philosophical Underpinning

Truth is not static. It is emergent, contextual, and sometimes contested. But that doesn’t mean it is unknowable. Truth Ledger recognizes:
• That truth can be layered: something may be true in one context and false in another.
• That truth can evolve: new data can replace old conclusions.
• That disagreement does not imply falsehood: multiple perspectives can coexist in a contested field until resolved.

Rather than freeze the world in place, Truth Ledger attempts to track and structure the unfolding of truth itself.

🌍 Why Now?

We are living through an information crisis:
• Algorithms reward lies that spread faster than facts
• AI systems are being trained on polluted data
• History is rewritten constantly by those in power
• Deepfakes erode trust in evidence

We need a Truth Infrastructure — a durable, decentralized layer of verified knowledge that any AI, human, or institution can rely on.

Truth Ledger is an attempt to build the foundation.

🧪 Technology Stack
• Flask for API endpoints
• Python logic for claim hashing, storing, and retrieval
• JSON as base data storage for easy portability
• AI/ML-ready hooks for future integration of fact-checking engines, NLP parsers, and LLM tools
• SHA-256 hashing for immutable entry fingerprints

Future versions may include:
• Blockchain-based notarization
• IPFS distributed storage
• Federated verification nodes
• Graph search over claim relationships

🚀 Getting Started (TL;DR)
1. Clone the repo
2. Run app.py to start the server
3. Use /add to submit claims and /ledger to view the log
4. Extend with your own validators, contributors, or agent interfaces

📢 Call to Builders

This is not just a tool.

This is a resistance to forgetting.
This is an infrastructure of accountability.
This is a commitment to public memory in a time when everything else is gamified, corrupted, or buried.

Truth Ledger welcomes contributors, visionaries, hackers, journalists, researchers, and skeptics. Let’s build a world where truth has a ledger.

---

## 📦 Files & Components

- `ledger.py` — Manages entries in the ledger
- `verify.py` — Placeholder for human or AI-driven verification logic
- `app.py` — Flask API to interact with the ledger
- `ledger.json` — Growing JSON file of verified claims
- `README.md` — This file

---

## 🚀 Usage

### 1. Start the Flask server:

```bash
python app.py
```

2. Add a truth claim via POST:

```bash
curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"claim": "The sky is blue."}'
```

3. Query the ledger:

```bash
curl http://localhost:5000/ledger
```

🤝 Contributing

This project welcomes contributions from truth-seekers, open-source developers, and anyone passionate about transparency. Submit pull requests or open issues to help evolve the Truth Ledger ecosystem.

---