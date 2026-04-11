# f a s t  r o a d s (V2)
f a s t  r o a d s (or fastroads / Fast Roads) is a Modified version of [slow roads](https://www.slowroads.io). It has many new additions:

- There is now a "Lamborghini" that can reach speeds of about 363 mph. It looks the same as the roadster and doesn't handle too well but it's fun
- There is a "Supercar" that can reach speeds up to about 60000 mph. It looks like the roadster as well and handles as well as a 60000 mph car can
- In addition to the three maps ("casual", "normal", "hard") there is now "wide" and "straight." "Wide" generates wider roads, and "straight" generates a straight, flat, wide road.
- There is a graphics option called "ultra+" that increases the render distance. Unfortunately using ultra+ disables tree generation entirely and I'm not sure why.
- There is a "Superbus" that can reach speeds of about 30000 mph. it uses the same model as the Coach.

# Build
To Build the game for Windows, You will Need Python, Powershell and a copy of this Repo locally saved to your Computer.

From the downloaded repo's root, run these in powershell:

```powershell
.\build.ps1
```

This installs `Python` if not installed,  `pyinstaller` and `pywebview` if needed and produces a local bundled executable in `[root]\dist\fastroads`.

To build a single-file executable instead, run:

```powershell
.\build.ps1 -OneFile
```
This will make a single .exe file named `fastroads.exe` in `[root]\dist`.

If the built executable opens but stays blank, build in debug mode so console errors are visible:

```powershell
.\build.ps1 -Debug
```

To clean previous build artifacts:

```powershell
.\build.ps1 -Clean
```

## Prebuilt Version:
A Prebuilt version can be found in Releases.

## Web Version
The Web Version is located here: [fastroads](https://mcflurrymuncha.github.io/fastroads/)


