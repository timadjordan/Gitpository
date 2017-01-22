GPP = /usr/bin/g++
GPP_FLAGS = -std=c++11 -lgsl -lgslcblas
NVCC = /usr/local/cuda/bin/nvcc
NVCC_FLAGS = -g -G -arch=sm_61 -Xcompiler -Wall

all: pi_seq.exe pi_cuda.exe

pi_seq.exe: pi_seq.cpp
	$(GPP) $< -o $@ $(GPP_FLAGS)

pi_cuda.exe: pi_cuda.cu
	$(NVCC) $(NVCC_FLAGS) $^ -o $@ $(GPP_FLAGS)

clean:
	rm -rf pi_seq.exe
	rm -rf pi_cuda.exe
