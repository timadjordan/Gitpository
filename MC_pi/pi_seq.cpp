#include <math.h>
#include <gsl/gsl_rng.h>
#include <ctime>

void MCpoints(int* counter, long N, gsl_rng* seed)
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
  const long N = pow(2,30);
  gsl_rng* rng_seed = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng_seed,time(NULL));

  int* counter;
  *counter = 0;
  MCpoints(counter,N,rng_seed);
  gsl_rng_free(rng_seed);
  
  double pi = 4*double(*counter)/double(N);
  printf("samples = %ld\ncounter = %d\npi = %f\n",N,*counter,pi);
}
