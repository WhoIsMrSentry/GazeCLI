# EyeTracker
A lightweight, robust Python eye tracker

## gazecli (single CLI)

This repository is packaged as a single command-line tool: `gazecli`.

Install (recommended: editable):
```bash
pip install -e .
```

Commands:
```bash
gazecli pupil
gazecli pupil-lite
gazecli pupil-rpi
gazecli 3d
gazecli head
gazecli head-cursor
gazecli webcam3d
```

Note: Some commands require extra dependencies:
```bash
pip install -e ".[head]"
pip install -e ".[webcam3d]"
pip install -e ".[three_d]"
```

## Project layout

Python application code lives under:
- `src/gazecli/apps/`

Unity integration:
- `integrations/unity/GazeFollower.cs` (reads a gaze vector file and drives an object)

## 3D eye tracking (near-eye IR camera)

Run:
```bash
gazecli 3d
```

What it does:
- Detects the pupil in each frame, fits an ellipse, and estimates a 3D gaze direction vector.
- (Optional) Renders a 3D visualization window.

Output:
- `gaze_vector.txt`: continuously updated with origin (x,y,z) and direction (x,y,z).
- `integrations/unity/GazeFollower.cs` can read this file in Unity.

## Head tracking mouse control

Run:
```bash
gazecli head
```

What it does:
- Uses webcam + MediaPipe Face Mesh to estimate head pose (yaw/pitch).
- Moves the mouse cursor based on head orientation.

Hotkeys:
- `F7`: toggle mouse control
- `c`: calibrate (look at screen center)
- `q`: quit

Optional cursor overlay:
# GazeCLI
A lightweight, robust Python eye tracking CLI.

## Install
```bash
pip install -e .
```

## Commands
```bash
gazecli pupil
gazecli pupil-lite
gazecli pupil-rpi
gazecli 3d
gazecli head
gazecli head-cursor
gazecli webcam3d
```

Optional dependencies:
```bash
pip install -e ".[head]"
pip install -e ".[webcam3d]"
pip install -e ".[three_d]"
```

## Project layout
- `src/gazecli/apps/`: application modules
- `integrations/unity/GazeFollower.cs`: Unity example that reads `gaze_vector.txt`

## 3D eye tracking (near-eye IR camera)
```bash
gazecli 3d
```

Output:
- `gaze_vector.txt`: origin (x,y,z) and direction (x,y,z)

## Head tracking mouse control
```bash
gazecli head
```

Hotkeys:
- `F7`: toggle mouse control
- `c`: calibrate (look at screen center)
- `q`: quit

Cursor overlay:
```bash
gazecli head-cursor
```

## Webcam 3D tracker (prototype)
```bash
gazecli webcam3d
```

Hotkeys (summary):
- `c`: calibrate (screen center)
- `F7`: toggle mouse control
- `j/l`, `i/k`: orbit yaw/pitch
- `[ / ]`: zoom
- `r`: reset orbit
- `x`: stamp a marker on the virtual monitor
- `q`: quit

## Notes
- NumPy 2.0.0 may cause issues; use 1.26.x if needed.
- Works best with 640x480 input and a full-eye frame.