#include <hip/hip_runtime.h>
#include <iostream>

// Define a simple HIP kernel that increments each element of the array
__global__ void AddOne(int *data, int size)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < size)
    {
        data[idx] += 1; // Increment each element by one
    }
}

int main()
{
    const int size = 256;
    const int bytes = size * sizeof(int);
    int *data;

    // Allocate SVM memory
    hipHostMalloc(&data, bytes, hipHostMallocCoherent);

    // Initialize the array
    for (int i = 0; i < size; i++)
    {
        data[i] = i;
    }

    // Launch the HIP kernel
    dim3 blockSize(64);
    dim3 gridSize((size + blockSize.x - 1) / blockSize.x);
    hipLaunchKernelGGL(AddOne, gridSize, blockSize, 0, 0, data, size);

    // Wait for the GPU to finish
    hipDeviceSynchronize();

    // Check the results
    for (int i = 0; i < size; i++)
    {
        if (data[i] != i + 1)
        {
            std::cerr << "Error: data[" << i << "] = " << data[i] << ", expected " << i + 1 << std::endl;
            hipHostFree(data);
            return 1;
        }
    }

    std::cout << "Success! All data incremented by one." << std::endl;

    // Free the SVM memory
    hipHostFree(data);

    return 0;
}