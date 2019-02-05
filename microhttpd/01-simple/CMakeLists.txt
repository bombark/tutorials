cmake_minimum_required (VERSION 2.6)
project (urf-microhttpd)


add_definitions(-std=gnu++0x)


add_executable(teste "src/main.cpp")
target_link_libraries(teste microhttpd dl pqxx pthread)
