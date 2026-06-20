# Magic: The Gathering (Pygame Simulator)

A 2-player digital simulation of the trading card game *Magic: The Gathering (MTG)* built completely from scratch using Python and Pygame. The project features object-oriented gameplay mechanics, custom deck construction loops, turn phases, stack tracking, and dynamic battlefield rendering.

---

## Game Overview

The simulator recreates the mechanical structure of a standard MTG match. Two players (Hero and Villain) duel with custom constructed decks, managing their life totals, tapping lands for colored mana, casting spells, handling state-based triggers, and utilizing priority-driven stack execution.

## Featured Decks
* **Dimir Rogues (`rogues.py`):** A tempo/control deck focused on aggressive evasive creatures, card draw scaling (`Into the Story`), mill strategies (`Ruin Crab`), and synergistic combat value (`Soaring Thought-Thief`).
* **Azorius Control (`azorius.py`):** A defensive deck utilizing life gain (`Revitalize`, `Union of the Third Path`), counterspells (`Absorb`), planeswalker utility (`The Wandering Emperor`), and board-wipes (`Sunfall`).

---

## Components

The codebase uses custom object-oriented design to replicate the rules engine of MTG:

* **`card.py` (The Rules Engine):** Implements the fundamental card hierarchy using inheritance: `Card` $\rightarrow$ `Land` / `Spell` $\rightarrow$ `Creature` / `Planeswalker` / `Artifact` / `Enchantment`. It dictates rules for tapping, spell resolution, entering the battlefield, taking damage, and dying.
* **`player.py` (State Management):** Tracks zones for each duelist, including `Hand`, `Battlefield`, `Library`, `Graveyard`, alongside individual `Life Total` and tracking structures for a user's `ManaPool`.
* **`actions.py` (Game Logic Engine):** Defines state operations like drawing cards, declaration of attackers/blockers, resolution of combat damage steps, priority updates, and static passive ability modifiers (such as Deathtouch or tribal power buffs).
* **`grobal.py` & `render.py` (Graphics Interface):** Houses screen resolution parameters, coordinate offsets for active game zones, and coordinates rendering passes for phase transitions, hand selections, stack configurations, and asset updates.
* **`game.py` (The Game Loop):** Orchestrates structural event retrieval, mapping keystrokes to explicit game actions like phase-passing and casting targets.

---

## Controls

The interface utilizes a dual mouse-and-keyboard mapping system to control phase changes and card positioning:

* **`ENTER` Key:** Cast a highlighted card from your hand (for Spells) or play it directly onto your board state (for Lands).
* **`SPACEBAR` Key:** Progress to the next turn phase or pass priority to your opponent.
* **Left Mouse Button (LMB):** Click on a permanent in your active battlefield zone to trigger its tap/activation ability (e.g., tapping a Land to add mana to your pool).

---

## Prerequisites
`Python 3.x` installed alongside the `pygame` package.
