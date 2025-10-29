<!-- FUTURISTIC BLACK + RED THEME README -->
<div align="center" style="background-color:#000; padding:40px; border-radius:15px;">

<img src="LOGO_URL_HERE" alt="VOID DOCS Logo" width="250" style="margin-bottom:20px;"/>

# 🚀 VOID DOCS  
### *Secure, Decentralized & Intelligent Document Verification System*

> **Built with:** Flask • Python • MongoDB • AWS • Custom Blockchain *(Akari)* • Gemini AI  

</div>

---

## <span style="color:#ff3c3c;">🔴 Problem Statement</span>
India’s digital identity and document ecosystem lacks **security**, **transparency**, and **interoperability**.  
Existing systems are centralized and prone to forgery, delays, and unauthorized access.  
VOID DOCS tackles this with a **blockchain-backed**, **AI-powered**, and **user-centric** document verification platform that ensures trust and authenticity.

---

## <span style="color:#ff3c3c;">🔴 Features</span>
✨ **Immutable Blockchain Records** — Documents hashed and stored on *Akari*, ensuring tamper-proof verification.  
🤖 **Gemini AI Module** — Smart classification, tagging, and natural-language document insights.  
☁️ **AWS Integration** — Encrypted documents stored safely using S3 & scalable backend on EC2.  
🧠 **Privacy-First Encryption** — Documents encrypted before upload; only hashes stored on-chain.  
💬 **Fast Verification** — Compare file hash to chain record for instant authenticity checks.  
🌐 **Interoperable Design** — APIs for 3rd-party verification systems and integrations.

---

## <span style="color:#ff3c3c;">🔴 System Architecture</span>

```text
[User] → [Flask Backend] → [Akari Blockchain]
                ↓
         [MongoDB Database]
                ↓
             [AWS Cloud]
                ↓
          [Gemini AI Module]

<span style="color:#ff3c3c;">🔴 Tech Stack (icons + official URLs)</span>

<div align="center">
  <!-- Icons with links -->
  <a href="https://www.python.org" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" width="60" alt="Python"/>
  </a>
  <a href="https://flask.palletsprojects.com/" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" width="60" alt="Flask"/>
  </a>
  <a href="https://www.mongodb.com" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/mongodb/mongodb-icon.svg" width="60" alt="MongoDB"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/javascript/javascript-icon.svg" width="60" alt="JavaScript"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-icon.svg" width="60" alt="HTML5"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/w3_css/w3_css-icon.svg" width="60" alt="CSS3"/>
  </a>
  <a href="https://aws.amazon.com" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" width="60" alt="AWS"/>
  </a>
  <a href="https://developers.google.com/experiments/ai/generative" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/google/google-icon.svg" width="60" alt="Gemini (Google)"/>
  </a>
  <a href="https://github.com/TeamAkatsuki/akari" target="_blank" rel="noopener">
    <img src="https://www.vectorlogo.zone/logos/bitcoin/bitcoin-icon.svg" width="60" alt="Akari (blockchain placeholder)"/>
  </a>
</div><!-- Text links for clarity (clickable) --><div align="center" style="margin-top:12px; color:#ddd;">
  <a href="https://www.python.org" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">Python</a> •
  <a href="https://flask.palletsprojects.com/" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">Flask</a> •
  <a href="https://www.mongodb.com" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">MongoDB</a> •
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">JavaScript</a> •
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">HTML5</a> •
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">CSS3</a> •
  <a href="https://aws.amazon.com" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">AWS</a> •
  <a href="https://developers.google.com/experiments/ai/generative" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">Gemini (Google)</a> •
  <a href="https://github.com/TeamAkatsuki/akari" target="_blank" rel="noopener" style="color:#fff; margin:8px; text-decoration:none;">Akari (blockchain)</a>
</div>
---

<span style="color:#ff3c3c;">🔴 Blockchain Implementation – Akari</span>

Akari is a lightweight, custom-built blockchain storing only document hashes and metadata.
Each block contains:

Document hash (SHA-256)

Timestamp

Owner metadata

Previous block hash (for immutability)


This guarantees tamper detection and trustless verification, removing the need for intermediaries.


---

<span style="color:#ff3c3c;">🔴 AI Module – Gemini</span>

The Gemini AI module enhances usability through:

Document summarization

Smart metadata extraction

Ownership validation

Q&A on document content (privacy-safe)


It uses NLP-based pattern recognition to provide human-like assistance while keeping sensitive data offline.


---

<span style="color:#ff3c3c;">🔴 AWS Integration</span>

VOID DOCS leverages Amazon Web Services for:

S3: Secure document storage (encrypted blobs)

EC2 / Elastic Beanstalk: Flask & MongoDB hosting

IAM & Encryption: Controlled access management

Scalability: High availability for document verification requests



---

<span style="color:#ff3c3c;">🔴 Team Akatsuki</span>

Name	Role	Contact

Jai Kishore N H	Team Head	jaikishore.n2025@vitstudent.ac.in
Lalith Adhithiya Saravanan	Backend Lead	lalith.adhithya2025@vitstudent.ac.in
Fawwaz Ahamed F	Frontend & AI	fawwazahamed.f2025@vitstudent.ac.in
Joash Mathew Jiju	Cloud & Blockchain	joash.mathewjiju2025@vitstudent.ac.in



---

<span style="color:#ff3c3c;">🔴 Future Roadmap</span>

🧱 Expand Akari to multi-node permissioned network
📱 Mobile app for document scanning & upload
🔒 Zero-knowledge verification for privacy
🌐 Integration with national e-doc systems
🧠 Advanced Gemini features: multilingual & legal doc parsing


---

<span style="color:#ff3c3c;">🔴 Contact</span>

📧 Email any team member above for collaboration or demo requests.
💬 Repository maintained by Team Akatsuki – VOID DOCS.


---

<div align="center" style="margin-top:30px;">
  <hr style="border: 1px solid #ff3c3c; width:60%;">
  <p style="color:#888;">© 2025 VOID DOCS | Powered by Akari Blockchain & Gemini AI</p>
</div><style>
h2, h3, h4 {
  color: #ff3c3c !important;
  position: relative;
}
h2::after, h3::after, h4::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -6px;
  height: 2px;
  width: 100px;
  background: linear-gradient(90deg, #ff3c3c, #000);
  animation: glow 2s infinite alternate;
}
@keyframes glow {
  from {box-shadow: 0 0 10px #ff3c3c;}
  to {box-shadow: 0 0 25px #ff3c3c;}
}
</style>---
