#include <cuda_runtime.h>
#include <device_launch_parameters.h>

__global__ void compute_action_probabilities(float* inputs, float* outputs, int size) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < size) {
        // Perform computations
        outputs[idx] = tanh(inputs[idx]);
    }
}
