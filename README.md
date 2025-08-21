
---

# WhatsApp Competitive Programming Assistant

An AI-powered MCP server for competitive programming with real-time analytics, personalized problem recommendations, and WhatsApp integration.

---

## Features

* Real-time analytics to track competitive programming performance and progress
* Personalized problem recommendations based on history and skill level
* WhatsApp integration for instant access and notifications
* Multi-user support for individuals and groups
* AI-powered insights to boost learning and practice

---

## Technology Stack

* Language: Python
* Integrations: WhatsApp API, machine learning libraries

---

## Getting Started

### Prerequisites

* Python 3.8 or higher
* pip (Python package manager)
* WhatsApp Business API credentials or integration setup
* Python dependencies listed in `requirements.txt`

### Installation

```bash
git clone https://github.com/soumya-1712/Whatsapp-Competitive-Programming-Assistant.git
cd Whatsapp-Competitive-Programming-Assistant
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your API keys and configuration options:

```
WHATSAPP_API_KEY=your_api_key_here
MCP_SERVER_URL=your_mcp_server_url
```

### Running the Server

```bash
python main.py
```

The server will listen for WhatsApp messages and respond accordingly.

---

## Usage

* Start a session: send `start` via WhatsApp
* Get problem recommendations: send `recommend problem`
* View analytics: send `profile stats for <username>`
* Get help: send `need help with commands`

---

## Core Functionality

### User Statistics and Analytics

* Detailed profile analysis for single or multiple Codeforces users
* Rating history tracking and contest performance
* Performance metrics using advanced algorithms
* Activity monitoring for problem-solving patterns

### Problem Recommendation System

* AI-powered problem suggestions based on solving history
* Difficulty targeting with customizable rating ranges
* Unsolved problem detection for fresh recommendations
* Practice optimization for maximum improvement

### Data Visualization Tools

* Rating graphs and multi-user comparisons
* Contest performance charts with rank-based analysis
* Rating distribution histograms
* Success rate and verdict analytics
* Topic proficiency and language usage distributions

### Contest Analysis

* Rating change and rank tracking
* Historical performance analysis
* Upsolve identification for contest completion

---

## Available Tools

**Core Statistics**

* `get_codeforces_user_stats`
* `get_solved_problems`
* `get_rating_changes`
* `get_solved_rating_histogram`

**Recommendation Engine**

* `recommend_problems`
* `get_upsolve_targets`

**Visualization Suite**

* `plot_rating_graph`
* `plot_performance_graph`
* `plot_solved_rating_distribution`
* `plot_verdict_distribution`
* `plot_tag_distribution`
* `plot_language_distribution`

**External Integrations**

* `get_upcoming_contests`
* `get_leetcode_daily_problem`

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## Contact

For support, open an issue or reach out to [soumya-1712](https://github.com/soumya-1712) on GitHub.

---

