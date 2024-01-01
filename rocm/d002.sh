docker run -it \
    --device=/dev/kfd \
    --device=/dev/dri \
    --group-add video \
    rocm/dev-ubuntu-22.04:latest