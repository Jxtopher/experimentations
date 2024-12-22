//
// @brief It was proposed by Christian Goldbach that every odd composite *
//        number can be written as the sum of a prime and twice a square.
//
// 9 = 7 + 2×12
// 15 = 7 + 2×22
// 21 = 3 + 2×32
// 25 = 7 + 2×32
// 27 = 19 + 2×22
// 33 = 31 + 2×12
// 
// It turns out that the conjecture was false.
//
// What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
//
// Page: https://projecteuler.net/problem=46
// Composite number: https://en.wikipedia.org/wiki/Composite_number
// 

#include <iostream>
#include <cmath>
#include <list>
#include <cstdlib>

//
// @brief Determines if it is a composite number
// 
// @param n a natural number
// @return true is an composite number, otherwise false
//
inline bool is_composite_number(const unsigned int n) {
    for (unsigned int i = n - 1 ; i > 1 ; i--)
        if (n % i == 0) return true;
    return false;
}


//
// @brief  Determines if it is a prime number
// 
// @param n a natural number
// @return true is a prime number, otherwise false
//
inline bool is_prime(const unsigned int n) {
    if (n < 3 || n % 2 == 0)
        return n == 2;
    for (unsigned int i = 3 ; i < static_cast<unsigned int>(sqrt(n)) + 1 ; i+=2) 
        if (n % i == 0) return false;
    return true;
}


// 
// @brief solve a quadratic_equation
// 
// @param ax^2+ bx+ c = 0
// @return solutions
//
std::list<float> quadratic_equation_solving(const float a, const float b, const float c) {
    std::list<float> solution;
    float d = b * b - (4 * a * c);

    if(a == 0) {
        if(b != 0) solution.push_back(-c / b);
    } else {
        if(d > 0){
                solution.push_back((-b - sqrt(d)) / (2 * a));
                solution.push_back((-b + sqrt(d)) / (2 * a));
        } else if(d == 0) solution.push_back((-b) / (2 * a));
    }

    return solution;
}


//
// @brief check odd composite that cannot be written as the sum of a prime and twice a square
// 
// @param n a natural number
// @return true is valided, otherwise false
//
inline bool check(const unsigned int n, const bool show = false) {
    if (is_composite_number(n)) {
        if (show) std::cout<<n<<" ";
        bool find = false;
        
        // Primer number
        for (unsigned int j = n ; 0 < j ; j--) {
            if (is_prime(j)) {

                float c = static_cast<float>(j) - static_cast<float>(n);
                std::list<float> x = quadratic_equation_solving(2, 0, c);

                if (x.size() > 0 && *x.begin() >= 0 && truncf(*x.begin()) == *x.begin()) {
                    if (show) std::cout<<j<<" "<<*x.begin()<<std::endl;
                    find = true;
                    break;
                } else if (x.size() > 1 && *++x.begin() >= 0 && truncf(*++x.begin()) == *++x.begin()) {
                    if (show) std::cout<<j<<" "<<*++x.begin()<<std::endl;
                    find = true;
                    break;
                }
            }
        }
        if (!find) return true;
    }
    return false;
}


int main() {
    for (unsigned int i = 1 ; i < 100000 ; i+=2)
        if (check(i)) std::cout<<"Found: "<<i<<std::endl;
    return EXIT_SUCCESS;
}
