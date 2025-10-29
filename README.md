<div align="center" style="background:#000; padding:30px; border-radius:15px;">
  <img src="LOGO_URL_HERE" alt="VOID DOCS Logo" width="220"/>
  <h1> VOID DOCS</h1>
  <h3><i>Secure | Decentralized | Intelligent Document Verification</i></h3>
  <b>Built with Flask | Python | MongoDB | AWS | Akari Blockchain | Gemini AI</b>
  <div align="center">

  ![Python](https://img.shields.io/badge/Python-3.10-blue)
  ![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey)
  ![MongoDB](https://img.shields.io/badge/Database-MongoDB-green)
  ![AWS](https://img.shields.io/badge/Cloud-AWS-orange)
  ![Hackathon](https://img.shields.io/badge/Event-Hackathon-red)
  
  </div>
</div>

---

## ´ Problem
India's document systems face forgery, delays & data leaks.  
VOID DOCS delivers blockchain-backed, AI-powered verification for authentic, tamper-proof records.

---

## ´ Features
- Immutable records on **Akari Blockchain**  
- **Gemini AI** for tagging & Q-A  
- **AWS S3/EC2** encrypted cloud storage  
- Fast hash-based verification  
- Modular **Flask + MongoDB** backend  

---

## ´ Architecture
```text
User -> Flask API -> Akari Blockchain
             ⬇️
        MongoDB + AWS S3
             ⬇️
         Gemini AI Module
```

---

## ´ Core Modules  
**Akari Blockchain:** Lightweight blockchain storing only file hashes & timestamps â€” ensures tamper-proof verification.  
**Gemini AI:** AI module for document summarization, metadata extraction & question answering.  
**AWS Integration:** S3 for encrypted file storage, EC2 for backend hosting, IAM for access control.  

---

## ´ Team Akatsuki  
| Name | Role | Email |
|------|------|-------|
| Jai Kishore N H | Team Head | jaikishore.n2025@vitstudent.ac.in |
| Lalith Adhithiya Saravanan | Backend Lead | lalith.adhithya2025@vitstudent.ac.in |
| Fawwaz Ahamed F | Frontend & AI | fawwazahamed.f2025@vitstudent.ac.in |
| Joash Mathew Jiju | Cloud & Blockchain | joash.mathewjiju2025@vitstudent.ac.in |

---

## 🔴 Why We Used Blockchain (Akari)

We implemented our own blockchain system — **Akari** — to make document verification **trustless, transparent, and tamper-proof**.

Traditional document systems rely on centralized databases that can be:
- Altered or deleted by insiders  
- Compromised by unauthorized access  
- Lost due to server or storage failure  

**Blockchain fixes this by design:**

| Problem | Blockchain Solution |
|----------|--------------------|
| Document forgery or alteration | Each file’s hash is stored in a block — tampering changes the hash, instantly detected. |
| Centralized trust issues | Distributed ledger — verification doesn’t rely on any single authority. |
| Lack of authenticity proof | Time-stamped, cryptographically linked blocks provide verifiable record history. |
| Data loss or corruption | Redundant ledger across nodes ensures persistence and recovery. |

**Akari Blockchain** stores:
- Document hash (SHA-256)  
- Timestamp  
- Owner metadata  
- Previous block hash  

This guarantees **immutability, transparency, and verification** — without storing the actual document, protecting privacy.

> ✅ **In short:** Blockchain removes forgery, builds trust, eliminates intermediaries, and keeps records permanently verifiable.

---

 
