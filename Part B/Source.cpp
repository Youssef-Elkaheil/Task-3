#define _USE_MATH_DEFINES
#include <cmath>
#include <complex>
#include <iostream>
#include <iomanip>

extern "C"
{
	void dft(std::complex<double> *data, int N);
	void fft(std::complex<double> *data, int N);
}

void fft(std::complex<double> *data, int N)
{

	if (N <= 1)
		return;

	int M = N / 2;

	std::complex<double> *even = new std::complex<double>[M];
	std::complex<double> *odd = new std::complex<double>[M];

	for (int i = 0; i < M; i++)
	{
		even[i] = data[2 * i];
		odd[i] = data[2 * i + 1];
	}

	// conquer
	fft(even, M);
	fft(odd, M);

	// combine
	for (size_t k = 0; k < N / 2; ++k)
	{
		std::complex<double> t = std::polar(1.0, -2 * M_PI * k / N) * odd[k];
		data[k] = even[k] + t;
		data[k + N / 2] = even[k] - t;
	}
}

void dft(std::complex<double> *data, int N)
{
	std::complex<double> Sum;
	std::complex<double> *output = new std::complex<double>[N];
	for (int k = 0; k < N; k++)
	{
		Sum = std::complex<double>(0, 0);

		for (int n = 0; n < N; n++)
		{
			double realPart = cos(((2 * M_PI) / N) * k * n);
			double imagPart = sin(((2 * M_PI) / N) * k * n);
			std::complex<double> w(realPart, -imagPart);
			Sum += data[n] * w;
		}
		output[k] = Sum;
	}
	for(int i=0; i<N;i++)
	data[i]=output[i];
	
}

int main()
{


	std::complex<double> arr2[1024];

	double sigK = 500; //freq bta3et el signal

	double sigPhase = 0.0;

	for (int n = 0; n < 1024; ++n)
	{
		auto currentsample = std::complex<double>(cos((2 * M_PI / static_cast<double>(1024)) *
														  sigK * static_cast<double>(n) +
													  sigPhase),
												  0.0); // static_cast : is a unary operation to change on type of data to another

		arr2[n] = currentsample;
	}

	fft(arr2, 1024);

	// std::cout << output[1];

	for (int i = 0; i < 1024; ++i)
	{
		std::cout << i << "\t"

				  << std::setw(12) << arr2[i].real() / static_cast<double>(1024) << "\t" // to normaliz by number of samples
				  << std::setw(12) << arr2[i].imag() / static_cast<double>(1024) << "\t" // setw =  set width
				  << std::endl;
	}
}