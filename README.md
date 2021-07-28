Conan for OpenFOAM

## Installation

Assuming we already have anaconda installed:


```bash
    conda create -n conan python=3.9 # we dont want break our install
    conda activate conan
    pip install conan # conan is required
```

## Usage

### Install OpenFOAM generator

```bash
    cd foamGen
    conan export . myuser/foamGen
```

The generator is now installed


### Compile OpenFOAM with Boost regexp and lohmann json


```bash
    cd test-conan
    conan install . -s compiler=gcc -s compiler.libcxx=libstdc++ --build 
```

boost and the json library are know downloaded and compiled