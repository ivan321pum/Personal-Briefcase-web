# 🗄️ Personal Portfolio (Reflex Version) - [DEPRECATED]

[![Status: Deprecated](https://img.shields.io/badge/Status-Deprecated-red.svg)]()
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)]()
[![Reflex](https://img.shields.io/badge/Reflex-000000?logo=reflex&logoColor=white)]()

> ⚠️ **THIS PROJECT IS ABANDONED AND WILL NO LONGER RECEIVE UPDATES.**

This repository contains a first attempt at developing my personal portfolio entirely in Python using the **Reflex** web framework. 

## 📝 Reason for Abandonment (Deprecation Notice)

The project was started with the goal of unifying web development under a 100% Python environment. However, it was eventually abandoned because, at the time of its development, **Reflex was in a very early stage ("too green")**. 

Although it is a promising tool, it presented several critical limitations for this specific use case:
- **Performance and Load Times:** The overhead of running a WebSocket/React-based architecture generated from Python heavily penalized performance for a website that should be purely static.
- **Design Flexibility:** Limitations when implementing complex custom animations and fine-grained control over CSS and layout.
- **Technical SEO:** Difficulties in optimizing dynamic meta tags, hreflang, and Open Graph efficiently and cleanly.

## 🚀 Current Portfolio

Currently, my portfolio has been rewritten from scratch using a modern, static, and ultra-fast stack (Astro, React, Tailwind CSS, and Framer Motion), achieving 100/100 scores in Lighthouse.

👉 **You can view the final and active version here:** [ivansevilla.me](https://ivansevilla.me)

---

## 🛠️ Local Execution (For archive/curiosity only)

If for any reason you need to run this project to review the old code, you can do so by following these steps:

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/reflex-repo-name.git](https://github.com/YOUR-USERNAME/reflex-repo-name.git)
   cd reflex-repo-name
Create and activate a virtual environment:
Bash
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
#Install dependencies:
  pip install -r requirements.txt
#Initialize and run the Reflex server:
  reflex init
  reflex run
