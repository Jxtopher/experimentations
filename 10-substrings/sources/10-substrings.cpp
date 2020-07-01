// https://projecteuler.net/problem=529
// g++ -Os 10-substrings.cpp -lpthread
#include <cstdlib>
#include <iostream>
#include <list>
#include <vector>
#include <utility>
#include <numeric>
#include <cassert>
#include <cmath>
#include <thread>
#include <future>
#include <chrono>

typedef unsigned long long int U64;

namespace jxtopher {

class Stopwatch {
private:
    std::chrono::high_resolution_clock::time_point t1, t2;
public:
    void start() {
        t1 = std::chrono::high_resolution_clock::now();
    }
    void stop() {
        t2 = std::chrono::high_resolution_clock::now();
    }

    auto duration() {
        return std::chrono::duration_cast<std::chrono::milliseconds>( t2 - t1 ).count();
    }
    
};
class Queue : public std::list<std::pair<U64, unsigned char>> {
    private:
    U64 _sum;
    public:
    Queue() : std::list<std::pair<U64, unsigned char>>(){
        _sum = 0;
    }
    void push(const std::pair<U64, unsigned char>& __x) { 
        _sum += __x.second;
        ((std::list<std::pair<U64, unsigned char>>*)this)->push_back(__x);
    }
    void pop() {
        _sum -= this->front().second;
        ((std::list<std::pair<U64, unsigned char>>*)this)->pop_front();
    }
    U64 get_sum() const {
        return _sum;
    }
};
}

inline bool ten_substring_friendly(const std::vector<unsigned char> &string) {
    jxtopher::Queue queue;
    std::vector<bool> flag(string.size(), false);
    for (U64 i = 0 ; i < string.size() ; i++) {
        queue.push(std::pair<U64, unsigned char>(i, string[i]));
        while (queue.get_sum() > 10) queue.pop();
        if (queue.get_sum() == 10) {
            while (i + 1 < string.size() && string[i + 1] == 0) {
                i++;
                queue.push(std::pair<U64, unsigned char>(i, string[i]));
            }
            
            for (const std::pair<U64, unsigned char> &element : queue)
                flag[element.first] = true;
            queue.pop();
        }
    }
    return std::accumulate(flag.begin(), flag.end(), 0) == string.size();
}

U64 T(const U64  &min, const U64 &max) {
    U64 count = 0;
    for (U64 i = min ; i <= max ; i++) {
        const std::string number = std::to_string(i);
        std::vector<unsigned char> digit_number(number.size());
        
        for (U64 i = 0 ; i < number.size() ; i++) 
            digit_number[i] = number[i] - 48;

        count += ten_substring_friendly(digit_number);
    }
    return count;
}

void T_caca(const U64 &min, U64 max, std::promise<U64>&& accumulate_sum) {
    accumulate_sum.set_value(T(min,max));
}

U64 T(const U64 &n) {
    return T(0, n);
}

U64 parallelization(const U64 &n) {
    unsigned int number_of_core = std::thread::hardware_concurrency();

    std::vector<std::thread> threads;
    std::vector<std::promise<U64>> acc;
    std::vector<std::future<U64>> results;
    U64 part = n / number_of_core;
    for (unsigned int i = 0, j = 0 ; i < number_of_core ; i++) {
        acc.push_back(std::promise<U64>());
        results.push_back(std::future<U64>(acc[acc.size() -1].get_future()));
        threads.push_back(std::thread(T_caca, j, (number_of_core - 1) == i ? n : j + part, std::move(acc[acc.size() -1])));
        j += part;
    }

    // Régner 
    for(std::thread &t : threads)
        t.join();

    // Combiner
    U64 sum = 0;
    for(std::future<U64> &r : results)
        sum += r.get();

    return sum;
}

void test() {
    assert(ten_substring_friendly({3,5,2,3,0,1,4}) == true);
    assert(ten_substring_friendly({2,8,5,4,6}) == false);
    assert(ten_substring_friendly({1,9,0,0,0,0}) == true);
    assert(T(pow(10,2)) == 9);
    assert(T(pow(10,5)) == 3492);
    assert(parallelization(pow(10,5)) == 3492);
}

int main() {
    test();
    jxtopher::Stopwatch sw;
    // sw.start();
    // std::cout<<parallelization(pow(10,15))<<std::endl;
    // sw.stop();
    // std::cout<<sw.duration()<<std::endl;


    sw.start();
    std::cout<<T(pow(10,8))<<std::endl;
    sw.stop();
    std::cout<<sw.duration()<<std::endl;

    // // std::cout<<T(pow(10,18))<<std::endl;
    return EXIT_SUCCESS;
}