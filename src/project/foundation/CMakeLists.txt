find_package(pylon 7.4.0 REQUIRED)
find_package(realsense2 REQUIRED)
find_package(OpenCV REQUIRED COMPONENTS core imgproc)

pybind11_add_module(foundation python.cpp realsense.cpp recorder.cpp basler.cpp StampedImageDownscaler.cpp py_resize.cpp)
target_link_libraries(foundation PUBLIC realsense2 TinyTIFFShared PillowResize fmt::fmt pylon::pylon spdlog::spdlog Tracy::TracyClient)
target_link_libraries(foundation PRIVATE opencv_core opencv_imgproc opencv_highgui)
target_include_directories(foundation PUBLIC ../../include)
