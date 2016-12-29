#include <stdio.h>
#include <cmath>
#include <cuda.h>
#include <curand_kernel.h>

#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)
{
   if (code != cudaSuccess) 
   {
      fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
      if (abort) exit(code);
   }
}


__global__ void MCpoints(int* d_out, int n, int n_for, curandState* state)
{
    const int myID = blockIdx.x*blockDim.x + threadIdx.x; 

    curand_init(1234, myID, 0, &state[myID]);
    curandState localState = state[myID];

    d_out[myID] = 0;
    
    for (i=0; i<n_for; i++)
    {
	float x = curand_uniform(&localState);
    	float y = curand_uniform(&localState);

    	if (sqrt(x*x+y*y)<1)
    	{
	  d_out[myID] += 1;
    	}
    	//printf("d_out[%d] = %d\n",myID,d_out[myID]);
    }
}

int main()
{

  const int N   = pow(2,16);
  const int TPB = 32; 
  int counter = 0;

  int* out = (int*) calloc(N,sizeof(int));

  int* d_out = 0;
  cudaMalloc(&d_out, N*sizeof(int));

  curandState *devStates;
  cudaMalloc(&devStates, N*sizeof(int));

  gpuErrchk( cudaMemcpy(d_out, out, N*sizeof(int), cudaMemcpyHostToDevice) );
  MCpoints<<<N/TPB, TPB>>>(d_out, N, devStates);
  printf("size = %lu\n",N*sizeof(int));
  gpuErrchk( cudaMemcpy(out, d_out, N*sizeof(int), cudaMemcpyDeviceToHost) );
  for (int i=0; i<N; i++)
  {
    counter += out[i];
  }

  double pi = 4*double(counter)/double(N);
  printf("samples = %d\ncounter = %d\npi = %f\n",N,counter,pi);

  cudaFree(d_out);
  cudaFree(devStates);
  free(out);

}
