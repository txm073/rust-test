#include "Windows.h"
#include <iostream>
#include <string>

typedef void(__cdecl *Print)(void);

int main(int argc, char* argv[]) {
    HINSTANCE lib = LoadLibrary("C:\\Users\\Tom\\Projects\\rust-test\\test.dll");
    if (!lib) {
        std::cerr << "Failed to load the library" << std::endl;
        return 1;
    }
    Print rustPrint = (Print)GetProcAddress(lib, "test_fn");
    if (!rustPrint) {
        std::cerr << "Failed to locate function" << std::endl;
        return 1;
    }

    Print();

    return 0;
}