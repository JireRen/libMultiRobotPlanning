//
// Created by jire on 2/16/20.
//
#include <iostream>
#include <fstream>

#include <yaml-cpp/yaml.h>
#include <boost/program_options.hpp>

#include "libMultiRobotPlanning/online_testcase.hpp"

int main(int argc, char* argv[]){
    namespace po = boost::program_options;
    po::options_description desc("Allowed options");
    std::string inputFile;
    std::string outputFile;
    desc.add_options()("help", "produce help message")(
            "input,i", po::value<std::string>(&inputFile)->required(),
            "input file (YAML)")("output,o",
                    po::value<std::string>(&outputFile)->required(),
                    "output file (YAML)");

    try{
        po::variables_map vm;
        po::store(po::parse_command_line(argc, argv, desc), vm);
        po::notify(vm);

        if (vm.count("help") != 0u){
            std::cout << desc << std::endl;
            return 0;
        }
    } catch(po::error& e){
        std::cerr << e.what() << std::endl << std::endl;
        std::cerr << desc << std::endl;
        return 1;
    }

    YAML::Node config = YAML::LoadFile(inputFile);

    const auto& dim = config["map"]["dimensions"];
    int dimx = dim[0].as<int>();
    int dimy = dim[1].as<int>();

    std::ofstream out(outputFile);

    int testnum = 10;
    int start_x;
    int start_y;
    int goal_x;
    int goal_y;

    out << "agents:" << std::endl;

    for (int i = 0; i < testnum; i++){
        start_x = rand() % dimx;
        start_y = rand() % dimy;
        goal_x = rand() % dimx;
        goal_y = rand() % dimy;

        out << "-   " << "goal: [" << start_x << ", "<< start_y << "]" << std::endl;
        out << "    name: " << "agent" << i << std::endl;
        out << "    start: [" << goal_x << ", " << goal_y << "]" << std::endl;
    }
    std::cout << "Generation done!" << std::endl;
    return 0;

}
