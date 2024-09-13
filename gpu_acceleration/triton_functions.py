import triton
import triton.language as tl
import torch

@triton.jit
def relu_kernel(x_ptr, y_ptr, n_elements, BLOCK_SIZE: tl.constexpr):
    idx = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = idx < n_elements
    x = tl.load(x_ptr + idx, mask=mask)
    y = tl.maximum(x, 0)
    tl.store(y_ptr + idx, y, mask=mask)

def relu_triton(x):
    x = x.contiguous()
    y = torch.empty_like(x)
    n_elements = x.numel()
    grid = lambda meta: (triton.cdiv(n_elements, meta['BLOCK_SIZE']),)
    relu_kernel[grid](x, y, n_elements, BLOCK_SIZE=1024)
    return y
