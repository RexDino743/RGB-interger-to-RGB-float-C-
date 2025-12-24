#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <sstream>
#include <iomanip>
#include <windows.h>

using namespace std;

std::string format(double value, int decimals) {
  std::ostringstream oss;
  oss << std::fixed << std::setprecision(decimals) << value;
  return oss.str();
}

double divideInts(int x, int y) {
  if (y == 0) throw std::invalid_argument("Division by zero");
  return static_cast<double>(x) / y;
}

double roundToDecimals(double value, int decimals) {
  double factor = std::pow(10, decimals);
  return std::round(value * factor) / factor;
}

void copyToClipboard(const std::string& text) {
  if (!OpenClipboard(nullptr)) return;
  EmptyClipboard();

  HGLOBAL hMem = GlobalAlloc(GMEM_MOVEABLE, text.size() + 1);
  if (!hMem) {
    CloseClipboard();
    return;
  }

  memcpy(GlobalLock(hMem), text.c_str(), text.size() + 1);
  GlobalUnlock(hMem);

  SetClipboardData(CF_TEXT, hMem);
  CloseClipboard();
}


int main() {
  int decimal = 3;
  string again = "n";
  string copClip = "n";

  while (again == "n" || again == "n") {
    int red = 0, green = 0, blue = 0, alpha = 0;
    double fRed = 0.0, fGreen = 0.0, fBlue = 0.0, fAlpha = 0.0;
    string output = "";
    
    std::cout << "\nRed: ";
    std::cin >> red;
    fRed = divideInts(red, 255);
    fRed = roundToDecimals(fRed, decimal);
  
    std::cout << "Green: ";
    std::cin >> green;
    fGreen = divideInts(green, 255);
    fGreen = roundToDecimals(fGreen, decimal);
    
    std::cout << "Blue: ";
    std::cin >> blue;
    fBlue = divideInts(blue, 255);
    fBlue = roundToDecimals(fBlue, decimal);
    
    std::cout << "Alpha (256 to ignore): ";
    std::cin >> alpha;
    if (alpha <= 255) { 
      fAlpha = divideInts(alpha, 255);
      fAlpha = roundToDecimals(fAlpha, decimal);
    }
    
    if (alpha >= 256) { 
      output = format(fRed, decimal) + ", " +
               format(fGreen, decimal) + ", " +
               format(fBlue, decimal);
    } else {
      output = format(fRed, decimal) + ", " +
               format(fGreen, decimal) + ", " +
               format(fBlue, decimal) + ", " +
               format(fAlpha, decimal);
    }

    std::cout << "\nResult: " << output << "\n";
    std::cout << "Copy to clipboard? (y/n): ";
    std::cin >> copClip;

    if (copClip == "y" || copClip == "Y") {
      copyToClipboard(output);
    }

    std::cout << "\nEnd? (y/n): ";
    std::cin >> again;
  }

  return 0;
}
