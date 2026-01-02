from __future__ import annotations

import argparse
from . import __version__
from ._internal.runner import run_module


def _modules() -> dict[str, str]:
    return {
        "pupil": "gazecli.apps.pupil_detector",
        "pupil-lite": "gazecli.apps.pupil_detector_lite",
        "pupil-rpi": "gazecli.apps.pupil_detector_raspberry_pi",
        "3d": "gazecli.apps.eye_tracker_3d",
        "head": "gazecli.apps.head_mouse_control",
        "head-cursor": "gazecli.apps.cursor_overlay",
        "webcam3d": "gazecli.apps.webcam_3d_tracker",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gazecli",
        description="EyeTracker depo script'lerini tek bir CLI altında çalıştırır.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"gazecli {__version__}",
    )

    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("pupil", help="Pupil tespiti")
    sub.add_parser("pupil-lite", help="Hızlı pupil tespiti (Lite)")
    sub.add_parser("pupil-rpi", help="Raspberry Pi pupil tespiti")
    sub.add_parser("3d", help="Near-eye IR kamera ile 3D gaze vektörü")
    sub.add_parser("head", help="Kafa takibi ile mouse kontrol")
    sub.add_parser("head-cursor", help="Mouse üstü halka overlay")
    sub.add_parser("webcam3d", help="Webcam ile 3D eye/monitor prototip")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        module_name = _modules()[args.cmd]
        run_module(module_name)
    except KeyError:
        parser.error("Bilinmeyen komut.")
        return 2
    return 0
