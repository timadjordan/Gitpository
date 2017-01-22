#include <stdio.h>
#include <cmath>
#include <cuda.h>
#include <curand_kernel.h>
#include <ctime>
#include <chrono>

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
    
    for (int i=0; i<n_for; i++)
    {
	float x = curand_uniform(&localState);
    	float y = curand_uniform(&localState);

    	if (sqrt(x*x+y*y)<1)
    	{
	  d_out[myID]++;
    	}
    	//printf("d_out[%d] = %d\n",myID,d_out[myID]);
    }
}

int main()
{

  const long int N = pow(2,31);
  const int B	   = 1024;
  const int TPB    = 32;
  const int T	   = (B*TPB);
  const int n_for  = N/T; 
  int counter = 0;

  int* out = (int*) calloc(T,sizeof(int));

  int* d_out = 0;
  cudaMalloc(&d_out, T*sizeof(int));

  curandState *devStates;
  cudaMalloc(&devStates, T*sizeof(int));

  auto t1 = std::chrono::high_resolution_clock::now();
  MCpoints<<<B, TPB>>>(d_out, T, n_for, devStates);
  gpuErrchk( cudaMemcpy(out, d_out, T*sizeof(int), cudaMemcpyDeviceToHost) );
  for (int i=0; i<T; i++)
  {
    counter += out[i];
  }
  double pi = 4*double(counter)/double(N);
  auto t2 = std::chrono::high_resolution_clock::now();
  auto t_elapsed = std::chrono::duration<double>(t2-t1).count();

  printf("samples = %ld\ncounter = %d\npi = %f\ntime elapsed: %1.4f sec\n",N,counter,pi,t_elapsed);

  cudaFree(d_out);
  cudaFree(devStates);
  free(out);

}
