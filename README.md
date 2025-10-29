# VOID — D O C S  
**The Future of Document Safety**  

> Prototype repo for a hackathon — no license information included.

---

<!-- Hero (styled with a small inline HTML/CSS block so the README looks nice on GitHub) -->
<div align="center">
  <img src="./assets/logo.png" alt="VOID DOCS logo" width="180" />
  <h2>Secure • Verifiable • Decentralised</h2>
  <p><em>Peer-to-peer, blockchain-backed document verification plus AI assistance — built with Flask, MongoDB, Akari (our custom blockchain), Gemini (AI module) and hosted on AWS.</em></p>
</div>

---

## Quick summary
VOID (short for **VOID- D O C S**) is a prototype platform that:

- Lets users upload and encrypt documents locally
- Stores document metadata & secure hashes on a custom blockchain (**Akari**) for immutable verification
- Uses an AI assistant (**Gemini module**) to help users search, categorize, and get legal/property guidance
- Stores encrypted documents in cloud/object storage (AWS S3) and indexes the metadata in MongoDB
- Targets India’s fragmented digital-document ecosystem to improve security, transparency and interoperability

---

## Team 
**Team Akatsuki**  

- **Team Head:** Jai Kishore N H — Jaikishore.n2025@vitstudent.ac.in — +91 95511 55198 — VIT Chennai  
- **Member:** Lalith Adhithiya Saravanan — Lalith.adhithya2025@vitstudent.ac.in — +91 96555 913574 — VIT Chennai  
- **Member:** Fawwaz Ahamed F — fawwazahamed.f2025@vitstudent.ac.in — +91 96291 38749 — VIT Chennai  
- **Member:** Joash Mathew Jiju — joash.mathewjiju2025@vitstudent.ac.in — +91 72007 83718 — VIT Chennai

---

## Problem statement 
> "India’s digital identity and property documentation system lacks security, transparency, and interoperability."  
> Traditional document storage is vulnerable to loss, forgery, and unauthorized access. Centralized platforms create single points of failure. Verification is slow and bureaucratic. There is an opportunity to create an independent, transparent verification system leveraging blockchain & AI. 

---

## Tech stack
- **Backend:** Flask (Python)  
- **Database / Index:** MongoDB (metadata + user records)  
- **Frontend:** HTML / CSS / JavaScript (Vanilla — minimal dependencies for hackathon)  
- **Custom Blockchain:** **Akari** — lightweight, purpose-built chain storing document hashes & minimal metadata (no heavy on-chain docs).  
- **AI module:** Gemini (integrated as an assistant microservice for search, classification, Q&A)  
- **Cloud / Hosting:** AWS (S3 for encrypted blobs, EC2 / Elastic Beanstalk / ECS for services)  
- **Other:** local encryption (AES), signature (ECDSA), hashing (SHA-256)  

---

## Why Blockchain? (simple explanation)
**What is blockchain?**  
A blockchain is an append-only distributed ledger made of blocks. Each block contains data (here: document hashes + metadata), a timestamp, and a cryptographic link (hash) to the previous block — making tampering detectable.

**Why we implemented Akari here**
- **Immutable proof-of-record:** Storing document hashes on Akari gives a tamper-evident record that a certain file existed at a specific time.  
- **Decentralised trust model:** Instead of trusting a single server, verification can be done by checking the ledger. For a hackathon prototype we run a small permissioned Akari network among nodes (team/demo nodes).  
- **Auditability:** Authorities or counterparties can verify authenticity by checking the recorded hash and timestamp.  
- **Interoperability potential:** By exposing verification endpoints, other services can verify documents without central access to raw files.

**Benefits (specific to VOID)**
- **Tamper-evidence:** Any modification to an uploaded file changes its hash and fails verification.  
- **No central single-point-of-failure** for metadata (the ledger is shared).  
- **Faster verification:** Verifiers only need the doc hash + access to the chain to confirm authenticity.  
- **Privacy-first:** Actual files remain encrypted off-chain (S3 / local); only hashes & minimal metadata go on-chain.  
- **Audit trail:** All transactions (uploads, transfers, ownership claims) are recorded with timestamps.

---
<div align="center">
  <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" width="60" />
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" width="60" />
  <img src="https://www.vectorlogo.zone/logos/mongodb/mongodb-icon.svg" width="60" />
  <img src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-icon.svg" width="60" />
  <img src="https://www.vectorlogo.zone/logos/w3_css/w3_css-icon.svg" width="60" />
  <img src="https://www.vectorlogo.zone/logos/javascript/javascript-icon.svg" width="60" />
  <img src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" width="60" />
</div>
