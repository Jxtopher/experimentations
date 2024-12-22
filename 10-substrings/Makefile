#
# @Author: *
# @License: *
# @Date: *
# @Version: 1
# @Description: Makefile
#


CC = g++
CFLAGS = -std=c++1z -Wall	# c++17
OFLAGS = -Os # Optimization flags
GFLAGS = #-pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wlogical-op -Wmissing-declarations -Wmissing-include-dirs -Wnoexcept -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-null-sentinel -Wstrict-overflow=5 -Wswitch-default -Wundef -Werror -Wno-unused
DFLAGS = -DDEBUG
FLAGS = $(CFLAGS) $(OFLAGS) $(GFLAGS) $(DFLAGS)

SOURCEDIR = sources
BUILDDIR = build
EXEC_NAME = 10-substrings
MKDIR_P = mkdir -p

#INCLUDES =
#LIBS =
#OBJ_FILES = fichier_1.o fichier_2.o
#INSTALL_DIR = /usr/bin

#all : $(EXEC_NAME)

#$(EXEC_NAME): main.cpp
all : $(SOURCEDIR)/10-substrings.cpp
	
	$(CC) $(FLAGS) $< -o $(BUILDDIR)/$(EXEC_NAME) -lpthread


unittest : $(SOURCEDIR)/unitTest.cpp
	$(CC) $(FLAGS) $< -o $(BUILDDIR)/unittest_$(EXEC_NAME) -lcppunit

rununittest:
	./$(BUILDDIR)/unittest_$(EXEC_NAME)

# https://franckh.developpez.com/tutoriels/outils/doxygen/
doxygen:
	doxygen doxygen.cfg

run:
	./$(BUILDDIR)/$(EXEC_NAME)

packages-debain:
	apt-get install g++ build-essential

.PHONY: clean  mrproper

clean:
	rm ./$(BUILDDIR)/$(EXEC_NAME)

mrproper:
	rm ./$(BUILDDIR)/$(EXEC_NAME) *.o


