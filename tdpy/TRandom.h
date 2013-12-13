#ifndef ROOT_TRandom
#define ROOT_TRandom

class TRandom {

public:
    TRandom(unsigned int seed=65539);
    virtual ~TRandom();
    int Binomial(int ntot, double prob);
    double BreitWigner(double mean=0, double gamma=1);
    void Circle(double &x, double &y, double r);
    double Exp(double tau);
    double Gaus(double mean=0, double sigma=1);
    unsigned int GetSeed() {return fSeed;}
    unsigned int Integer(unsigned int imax);
    double Landau(double mean=0, double sigma=1);
    void Rannor(float &a, float &b);
    void Rannor(double &a, double &b);
    void SetSeed(unsigned int seed=65539);
    double Rndm(int i=0);
    void RndmArray(int n, float *array);
    void RndmArray(int n, double *array);
    double Uniform(double x1=1);
    double Uniform(double x1, double x2);

protected:
    int   fSeed;  //Random number generator seed
};

#endif
