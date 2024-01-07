#include <hip/hip_runtime.h>
#include <stdio.h>

#define HIP_SAFECALL(x) { \
  hipError_t status = x; \
  if (status != hipSuccess) { \
    printf("HIP Error: %s\n", hipGetErrorString(status)); \
  } \
}

int main(void) {
    const int n = 10000;
    float x[n], y[n];
    float *x_, *y_;

    for (int i = 0; i < n; i++) {
        x[i] = y[i] = 1.0f;
    }

    HIP_SAFECALL(hipMalloc((void **)&x_, sizeof(float) * n));
    printf("x_ allocated\n");
    HIP_SAFECALL(hipMalloc((void **)&y_, sizeof(float) * n));
    printf("y_ allocated\n");
    HIP_SAFECALL(hipMemcpy(x_, x, sizeof(float) * n, hipMemcpyHostToDevice));
    printf("x_ copied\n");
    HIP_SAFECALL(hipMemcpy(y_, y, sizeof(float) * n, hipMemcpyHostToDevice));
    printf("y_ copied\n");

    return 0;
}