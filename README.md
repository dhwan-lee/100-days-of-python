# 100 Days of Code: The Complete Python Pro Bootcamp

Welcome to my central Python development repository. This portfolio tracks my daily progression through the **100 Days of Code Bootcamp**, moving systematically from foundational scripting to advanced data extraction, browser automation, and backend system engineering.

---

## 🛠️ Tech Stack & Core Competencies

* **Languages & Core:** Python 3, Object-Oriented Programming (OOP), Functional Programming, Regular Expressions (`re`).
* **Automation & Scraping:** Selenium WebDriver, BeautifulSoup4, Requests, Dynamic DOM Parsing.
* **APIs & Data Engineering:** RESTful APIs, JSON Parsing, Backend Integration (`smtplib`, `os`, `dotenv`).
* **Environment & Tools:** Git/GitHub version control, Virtual Environments (`venv`), macOS Development Environment.

---

## 🌟 Featured Projects & Architecture

Rather than just individual scripts, this repository highlights a progression into fully automated workflows:

### 🤖 High-Speed Browser Automation (Selenium)
* **Dynamic DOM Interaction:** Built an automated gameplay bot for *Cookie Clicker* that bypasses hardcoded limits by polling live elements via partial-match CSS selectors (`div[id^='product']`). 
* **State Machine Logic:** Executes an algorithmic upgrade loop every 5 seconds, evaluating and purchasing the highest-efficiency assets dynamically based on real-time game state.

### 🌐 Advanced Web Scraping & Data Pipelines
* **E-Commerce Price Monitor:** Developed an automated price tracker that spoofs network requests using precise HTTP headers (`User-Agent`, `Accept-Language`) to bypass bot detection, parses pricing strings dynamically, and dispatches automated alerts via secured SMTP tunnels (`starttls`).
* **Historical Data Extraction:** Built a tracking pipeline that extracts text elements using highly specific nested CSS paths (`li ul li h3`) to rebuild historical data aggregates from complex web layouts.

---

## 📁 Repository Directory Structure

The repository is organized by daily modules, tracking the shift from local logic to web-scale tools:

```text
100-days-of-python/
│
├── 01-Foundations/          # Days 1–14: Syntax, control flow, functions, & local applications
├── 02-Object-Oriented/      # Days 15–31: OOP, GUI development (Tkinter), & local data handling
├── 03-Web-&-APIs/           # Days 32–44: API integrations, environment variables, & authentication
│
├── Day_45/                  # Web Scraping with BeautifulSoup (Static Elements)
├── Day_46/                  # Billboard Hot 100 Data Extraction Pipeline
├── Day_47/                  # Automated Amazon Price Tracker & Email Dispatcher
├── Day_48/                  # Browser Automation & Dynamic Upgrades with Selenium
└── Day_49/                  # Automated Gym Class Booking Engine with Session Persistence

