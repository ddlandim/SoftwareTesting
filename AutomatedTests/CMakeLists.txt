cmake_minimum_required(VERSION 3.5)

project(Triangle LANGUAGES CXX)


find_package(Qt5Test REQUIRED)
find_package(Qt5Gui REQUIRED)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
enable_testing()

add_executable(Triangle tst_triangle.cpp)
add_test(NAME Triangle COMMAND Triangle)

target_link_libraries(Triangle PRIVATE Qt5::Gui Qt5::Test)

