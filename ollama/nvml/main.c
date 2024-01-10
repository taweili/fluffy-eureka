#include <stdio.h>
#include "gpu_info_cuda.h"

cuda_init_resp_t resp;
mem_info_t mem_info;

void main(void)
{
    nvmlReturn_t ret;
    cuda_init(&resp);
    ret = resp.ch.initFn();
    printf("%d\n", ret);

    cuda_check_vram(resp.ch, &mem_info);
}