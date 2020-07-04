// https://projecteuler.net/problem=426
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>
#include <numeric>

class Boxball : private std::vector<bool> {
    private:
    static constexpr const bool BOX_OCCUPIED = true;
    static constexpr const bool BOX_EMPTY = false;
    static constexpr const bool ALLOWED = true;
    static constexpr const bool FORBIDDEN = false;

    public:
    Boxball(std::list<unsigned int> sequence) : 
        std::vector<bool>(std::accumulate(sequence.begin(), sequence.end(), 0), false) {
        unsigned int index = 0;
        unsigned int occupied_and_empty = BOX_OCCUPIED; // true = occupied box, false = empty box
        for (unsigned int s : sequence) {
            if (!occupied_and_empty)
                index += s;
            else {
                for (unsigned int i = 0 ; i < s ; i++) {
                    (*this)[index] = BOX_OCCUPIED;
                    index++;
                }
            }
            occupied_and_empty = !occupied_and_empty;
        }
    }

	friend std::ostream& operator<<(std::ostream& out, const Boxball&  boxball) {
        std::for_each(boxball.begin(), boxball.end(), [&](bool i) {out << " "<< i;});
		return out;
	}

    void evolves_naive() {
        std::vector<bool> movement_allowed(this->size(), ALLOWED); // true = allowed, false = forbidden

        for (unsigned int i = 0 ; i < this->size() ; i++) {
            if ((*this)[i] == BOX_OCCUPIED && movement_allowed[i] == ALLOWED) {
                unsigned int j = i;
                while (j < this->size() && (*this)[j] == BOX_OCCUPIED) j++;
                if (j < this->size()) {
                    (*this)[j] = BOX_OCCUPIED;
                    movement_allowed[j] = FORBIDDEN;
                } else {
                    this->push_back(BOX_OCCUPIED);
                    movement_allowed.push_back(FORBIDDEN);
                }
                (*this)[i] = BOX_EMPTY;
            }
        }
    }

    // // get ballbox on the sequence
    // std::list<unsigned int> get_sequence() const {
    //     std::list<unsigned int> sequence;
    //     unsigned int box_occupied = 0 , box_empty = 0;
    //     for (bool box : *this) {
    //         if (sequence.empty() && box == BOX_EMPTY) {
    //         } else if (box == BOX_OCCUPIED) {
    //             if (box_empty != 0) {
    //                 sequence.push_back(box_empty);
    //                 box_empty = 0;
    //             }
    //             box_occupied += 1;
    //         } else if (box == BOX_EMPTY) {
    //             if (box_occupied != 0) {
    //                 sequence.push_back(box_occupied);
    //                 box_occupied = 0;
    //             }
    //             box_empty += 1;
    //         }
    //     }
    //     return sequence;
    // }

    std::list<unsigned int> get_occupied_boxes() const {
        std::list<unsigned int> sequence;
        unsigned int box_occupied = 0;

        for (bool box : *this) {
            if (box == BOX_EMPTY && box_occupied != 0) {
                sequence.push_back(box_occupied);
                box_occupied = 0;
            } else if (box == BOX_OCCUPIED) {
                box_occupied += 1;
            }
        }
        if (box_occupied != 0) sequence.push_back(box_occupied);

        return sequence;
    }
};

int main() {

    // Boxball boxball({2, 2, 2, 1, 2});
    Boxball boxball({2,1,2});
    std::cout<<"0"<<" "<<boxball<<std::endl;
    auto r = boxball.get_occupied_boxes();
    for (auto value : r) {
        std::cout<<value<<" ";
    }
    std::cout<<std::endl;

    for (unsigned int i = 1 ; i < 10000 ; i++) {
        boxball.evolves_naive();
    }
    auto r1 = boxball.get_occupied_boxes();
    for (auto value : r1) {
        std::cout<<value<<" ";
    }
    std::cout<<std::endl;
    // std::for_each(r.begin(), r.end(), [&](unsigned int i) {std::cout << " "<< i;});
    // std::cout<<"END "<<r.begin()<<std::endl;
    return EXIT_SUCCESS;
}