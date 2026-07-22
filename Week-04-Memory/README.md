# 🖥️ Week 4: Memory - CS50x 2026

## 🌟 Overview

This folder contains my solutions for Week 4 of Harvard's CS50x 2025 course, focusing on memory management in C programming. Week 4 dives into dynamic memory allocation, pointers, and memory-related concepts like stack and heap. These exercises enhance my ability to manage memory efficiently and understand how programs interact with system resources. 🚀

## 🧩 Problem Sets

Below are the problem sets and labs included in this folder, with brief descriptions:

- **Filter**: A program that applies image filters (e.g., grayscale, sepia, blur) to bitmap images using pointers and memory manipulation. 🖼️
- **Recover**: A program that recovers JPEG images from a raw memory card file by analyzing memory byte patterns. 💾
- **Memory** (if included): A lab that explores pointer arithmetic, dynamic memory allocation, and memory debugging tools like Valgrind. 🛠️

_Note_: If additional problems are included, they likely involve memory management or pointers. Let me know specific files for updates! 😊

## 📚 Learning Objectives

Through these assignments, I aimed to master the following concepts:

- **Pointers**: Understanding and using pointers to manipulate memory addresses directly.
- **Dynamic Memory Allocation**: Allocating and freeing memory using `malloc` and `free`.
- **Memory Management**: Avoiding memory leaks, segmentation faults, and dangling pointers.
- **File I/O**: Reading and writing files using memory-efficient techniques.
- **Debugging**: Using tools like `valgrind` and `debug50` to identify memory issues.

## 🏃‍♂️ How to Run the Code

To compile and run the programs:

1. Ensure a C compiler (e.g., `clang`) is installed.
2. Clone the repository: `git clone https://github.com/yatharthbhatt/CS50x-2026.git`
3. Navigate to the folder: `cd CS50x-2025/Week-04-Memory`
4. Compile a program: `clang program_name.c -o program_name -lcs50`
5. Run it: `./output/program_name`
6. For programs requiring arguments (e.g., Filter): `./filter -g image.bmp output.bmp`

Use CS50 tools like `make` for compilation, `style50` for formatting, and `check50` for testing (e.g., `check50 cs50/problems/2025/x/filter`). 🛠️

## 💭 Reflections

Week 4 was a deep dive into the world of memory management! 🥳 Understanding pointers was initially daunting, but working through Filter and Recover clarified their power and pitfalls. Debugging memory leaks with `valgrind` was a game-changer, and I now appreciate the importance of careful memory allocation. These challenges strengthened my confidence in handling low-level programming tasks.

## 📚 Resources

- 📺 [Lecture Video](https://video.cs50.io/kcRdFGbzR1I)
- 📝 [Lecture Notes](https://cs50.harvard.edu/x/2025/notes/4/)
- 📊 [Slides (PDF)](https://cdn.cs50.net/2024/fall/lectures/4/lecture4.pdf)
- 💾 [Source Code Examples](https://cdn.cs50.net/2024/fall/lectures/4/src4.zip)

## 📂 Directory Structure

Here’s how the repository is organized:

```
Week-04-Memory/
├── output/
│   ├── 01-filter
│   ├── 02-recover
│   └── 03-memory
├── Problem-Set-04/
│   ├── output/
│   │   ├── 01-filter
│   │   └── 02-recover
│   ├── 01-filter.c
│   └── 02-recover.c
├── Exercises/
│   ├── output/
│   │   ├── 01-memory
│   ├── 01-memory.c
└── README.md
```

Thanks for checking out my CS50x project! Looking forward to exploring data structures in Week 5! 💻🚀
