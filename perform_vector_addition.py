import torch  # Import the PyTorch library
import time  # Import the time library for timing operations

# Define the size of the vectors
# N is set to 1 billion elements for each vector
N = 1000000000

# Create random vectors on CPU
# a_cpu and b_cpu are random vectors, c_cpu is initialized to zeros
a_cpu = torch.randn(N)
print(f"Vector a on the cpu is {a_cpu.data}")
b_cpu = torch.randn(N)
print(f"Vector b on the cpu is {b_cpu.data}")
c_cpu = torch.zeros(N)
print(f"Vector c is created with all zeros {c_cpu.data}")
print()

# Create random vectors on GPU
# a_gpu and b_gpu are random vectors on the GPU, c_gpu is initialized to zeros on the GPU
a_gpu = a_cpu.clone().to('cuda')
print(f"Vector a on the gpu is {a_gpu.data}")
b_gpu = b_cpu.clone().to('cuda')
print(f"Vector b on the gpu is {b_gpu.data}")
c_gpu = torch.zeros(N, device='cuda')
print(f"Vector c is created with all zeros is {c_gpu.data}")
print()

# Vector addition on CPU
# Record the start time
start_time_cpu = time.time()
# Perform vector addition on CPU
c_cpu = a_cpu + b_cpu
# Record the end time
end_time_cpu = time.time()
print(f"Vector c on the cpu after addition is {c_cpu.data}")
print()
# Calculate the time taken on CPU
cpu_time = end_time_cpu - start_time_cpu

# Vector addition on GPU
# Record the start time
start_time_gpu = time.time()
# Perform vector addition on GPU
c_gpu = a_gpu + b_gpu
# Record the end time
end_time_gpu = time.time()
print(f"Vector c on the gpu after addition is {c_gpu.data}")
print()
# Calculate the time taken on GPU
gpu_time = end_time_gpu - start_time_gpu

# Print the results
# Display the time taken for vector addition on CPU and GPU
print(f"Time taken on CPU: {cpu_time:.6f} seconds")
print(f"Time taken on GPU: {gpu_time:.6f} seconds")
