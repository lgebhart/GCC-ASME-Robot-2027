#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
CAMERA_SCRIPT="${REPO_ROOT}/src/computer_vision/obstacle_course.py"

case "${1:-run}" in
    install)
        sudo apt update
        sudo apt install -y python3-opencv v4l-utils
        python3 -c "import cv2; print('OpenCV', cv2.__version__)"
        ;;

    devices)
        v4l2-ctl --list-devices
        ;;

    run)
        if [[ ! -f "${CAMERA_SCRIPT}" ]]; then
            printf 'Error: camera script not found: %s\n' "${CAMERA_SCRIPT}" >&2
            exit 1
        fi
        exec python3 "${CAMERA_SCRIPT}"
        ;;

    *)
        printf 'Usage: bash scripts/jetson_camera.sh [install|devices|run]\n'
        exit 2
        ;;
esac