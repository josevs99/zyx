#!/usr/bin/env bash
# Simple wrapper to run the dockerized CLI as 'zyxcli'
IMAGE_NAME=zyxcli:latest
docker run --rm -it \
  -e ZYX_SERVER="$ZYX_SERVER" \
  -e ZYX_USER="$ZYX_USER" \
  -e ZYX_PASS="$ZYX_PASS" \
  $IMAGE_NAME "$@"
