#include <math.h>
#include <gsl/gsl_rng.h>
#include <ctime>
#include <chrono>

using namespace std;

void MCpoints(int* counter, long int N, gsl_rng* seed)
{
  for(int i=1; i<N; i++)
  {
    double x = gsl_rng_uniform(seed);
    double y = gsl_rng_uniform(seed);
    if (sqrt(x*x+y*y)<1)
    {
      (*counter)++;
    }
  }
}

int main()
{
  gsl_rng* rng_seed = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng_seed,time(NULL));

  const long N = pow(2,30);
  int counter = 0;
  
  auto t1 = chrono::high_resolution_clock::now();
  MCpoints(&counter,N,rng_seed);
  double pi = 4*double(counter)/double(N);
  auto t2 = chrono::high_resolution_clock::now();
  auto t_elapsed = chrono::duration<double>(t2-t1).count();
  
  printf("samples = %ld\ncounter = %d\npi = %f\ntime elapsed: %1.4f sec\n",N,counter,pi,t_elapsed);
  
  gsl_rng_free(rng_seed);

  return 0;
}
