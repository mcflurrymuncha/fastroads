# f a s t  r o a d s (Desktop Edition)

This is a modded version of [slowroads.io](slowroads.io) that adds two fast cars and some other stuff. I did not make the original game. The original game is at [slowroads.io](slowroads.io), and it was created by [anslo](https://twitter.com/anslogen). Unfortunately the cars in the original game are too slow and he did not make the source code public, so all we have to work with is the minified JS. Some notes:

- There is now a "Lambo" that can reach speeds of about 363 mph. It looks the same as the roadster and doesn't handle too well but it's fun
- There is a "Supercar" that can reach speeds up to about 6000 mph. It looks like the roadster as well and handles as well as a 6000 mph car can
- In addition to the three difficulties ("casual", "normal", "hard") there is now "wide" and "straight." "Wide" generates wider roads, and "straight" generates a straight, flat, wide road.
- There is a graphics option called "ultra+" that increases the render distance. Unfortunately using ultra+ disables tree generation entirely and I'm not sure why.

# Build

From the repo root, run:

```powershell
.\build.ps1
```

This installs `pyinstaller` if needed and produces a local bundled executable in `dist\fastroads`.

To build a single-file executable instead, run:

```powershell
.\build.ps1 -OneFile
```

If the built executable opens but stays blank, build in debug mode so console errors are visible:

```powershell
.\build.ps1 -Debug
```

To clean previous build artifacts:

```powershell
.\build.ps1 -Clean
```

When a tag matching `v*` is pushed, the workflow also creates a GitHub release and uploads both zip packages.

The workflow uploads two artifacts for each build run:
- `fastroads-normal-build`
- `fastroads-debug-build`


