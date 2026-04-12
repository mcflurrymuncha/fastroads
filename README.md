# <p align="center">f a s t &nbsp; r o a d s &nbsp; (V2)</p>

<p align="center">
  <img src="https://img.shields.io/github/downloads/mcflurrymuncha/fastroads/total?style=for-the-badge&color=blue" alt="Downloads">
  <img src="https://img.shields.io/github/v/release/mcflurrymuncha/fastroads?style=for-the-badge&color=pink" alt="Release">
  <a href="https://mcflurrymuncha.github.io/fastroads/">
    <img src="https://img.shields.io/badge/Play-Web%20Version-orange?style=for-the-badge" alt="Play Web Version">
  </a>
  <a href="https://mcflurrymuncha.itch.io/fastroads">
    <img src="https://img.shields.io/badge/itch.io-FA5C5C?style=for-the-badge&logo=itch.io&logoColor=white" alt="Play on itch.io">
  </a>
</p>
---

**Fast Roads** (or *fastroads*) is a modification of the original [Slow Roads](https://www.slowroads.io). While the original focused on the zen of driving, V2 focuses on breaking the sound barrier.

## Key Features

### New Vehicles
| Vehicle | Top Speed | Handling | Notes |
| :--- | :--- | :--- | :--- |
| **Lamborghini** | ~363 mph | Low | Uses the Roadster model; higher speed. |
| **Supercar** | ~60,000 mph | Chaotic | just a bit fast lowk |
| **Superbus** | ~30,000 mph | Heavy | Uses the Coach model; speed. |

### New Terrain Generation
* **Wide:** Generates significantly wider roads for easier high-speed maneuvering.
* **Straight:** A perfectly flat, straight, and wide road - ideal for top-speed testing.

### Improved Graphics
* **Ultra+ Mode:** Significantly increases render distance for a more expansive horizon. 
> [!IMPORTANT]
> Enabling **Ultra+** currently disables tree generation entirely. I'm not sure why though.

---

## 🛠️ Building from Source
To build the Windows executable, you will need **Python**, **PowerShell**, and a local copy of this repository.

### Quick Start
Open PowerShell in the root directory and run:
```powershell
.\build.ps1
```
This will install `pyinstaller` and `pywebview` (as this game is html based).

### Debug Version
Run the same command but add this:
```powershell
.\build.ps1 -debug
```

This will make the game open with a terminal window to show what goes wrong and what is happening in game.

### Clean Install
Run this command to make a completely new install of **fastroads**.
```powershell
.\build.ps1 -clean
```

### One-File
To make a Single .exe file of the game with no `_internal` folder, Run this:
```powershell
.\build.ps1 -onefile
```

### Web Version
The Web Version is available at the top of this repo <3

## The Funny Bug that i am not removing
There is a particular bug that i find very funny with the `Supercar`. 
It occurs when you go above 1,000 mph then break.
As you hit the floor you break and accelerate again, sending the car flying.
I will not be removing this and have a name for it:
**breakboosting**
