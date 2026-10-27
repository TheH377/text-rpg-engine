#  Text RPG Engine

A modular, data-driven text-based RPG engine built in Python, focusing on Clean Code, Object-Oriented Programming (OOP) principles, and clear English-language standards. Designed as a portfolio project showcasing backend logic structuring and game architecture fundamentals.

---

##  Features

- **Data-Driven Architecture:** The entire game narrative, scenes, text, and item placements are decoupled from the core logic and stored in a structured `story.json` file.
- **Object-Oriented Programming (OOP):** Implements class inheritance (`Character` -> `Player`, `Enemy`) to maintain clean, reusable, and extensible code.
- **Tactical Combat System:** Features turn-based combat mechanics including a **50% chance Parry/Counterattack** mechanic utilizing Python's `random` module.
- **Robust Input Validation:** Protected loops ensure the application handles invalid inputs gracefully without breaking or crashing.
- **Fully Localized:** Built entirely in English for international developer standards.

---

##  Project Structure

```text
text-rpg-engine/
│
├── main.py          # Application entry point
├── engine.py        # Core game loop, scene manager, and combat logic
├── characters.py    # OOP classes (Character, Player, Enemy)
├── story.json       # Game script, dialogues, choices, and encounter data
└── README.md        # Project documentation