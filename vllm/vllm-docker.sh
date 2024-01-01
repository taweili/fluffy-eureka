docker run -it \
   --network=host \
   --group-add=video \
   --ipc=host \
   --cap-add=SYS_PTRACE \
   --security-opt seccomp=unconfined \
   --device /dev/kfd \
   --device /dev/dri \
   -v `pwd`/models:/app/model \
   -v `pwd`/apps:/app/apps \
   -v $HOME/.cache/huggingface:/.cache/huggingface \
   embeddedllminfo/vllm-rocm:vllm-v0.2.4 \
   bash