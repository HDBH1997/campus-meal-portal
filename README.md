# 🍲 Campus Meal Portal

A secure, high-performance multi-vendor campus dining operations and automated billing engine built with **FastAPI** and **PostgreSQL (Supabase)**. This system optimizes campus dining logistics, enforces strict operational schedule windows, and completely eliminates manual registration bottlenecks.

---

## 🚀 Key Engineering Solutions & Features

*   **⏱️ Rigid Operational Windows:** Enforces custom server-side time-locks ensuring weekly calendar meal planning configurations take place strictly within designated slots (Friday 17:00 to Sunday 12:00 cutoff).
*   **🤖 Automated Autopilot Fallbacks:** Self-correcting backend algorithms that automatically default missing student planning records to standard hostel-hall meal slots, protecting campus food overhead.
*   **🔒 Boundary Protection Controls:** Secure filters that handle multi-vendor isolation paths, block dual-ordering loops, and instantly invalidate student checkout tokens the exact moment a cashier logs an order as served.
*   **📊 Financial Analytics Suite:** Deploys a vendor-isolated dashboard displaying real-time daily/weekly cash ledgers alongside automated spreadsheet logistics roster generation tools.

---

## 🛠️ Core Technology Stack

*   **Backend Framework:** FastAPI (Python 3)
*   **Database Infrastructure:** Supabase / PostgreSQL (Cloud Host)
*   **Frontend Interface:** JavaScript (ES6+), HTML5, Semantic CSS3 Layouts
*   **Server Engine:** Uvicorn Async Server Gateways

---

## 📂 Architecture Blueprint Directories

*   `main.py` — The core backend operational brain handling security sign-ins, database transaction rules, timeline filters, and API controllers.
*   `interface.py` — The unified visual rendering engine housing the Student Dashboard, Provider Counter Terminal, and Admin Control Grids.
*   `.gitignore` — Safeguards private `.env` database credential hashes from leaking onto the public cloud.

---

## 💻 Local Setup & Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd campus-meal-portal
   ```

2. **Configure your database keys:**
   Create a hidden `.env` file in the root root folder:
   ```text
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_public_key
   ```

3. **Spin up the local production server gateway:**
   ```bash
   python -m uvicorn main:app --host 127.0.0.1 --port 80
   ```
   Open your browser and navigate directly to your local domain at `http://alucampusmeal.com`.
