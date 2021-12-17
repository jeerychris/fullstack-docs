
some note from github cmake_examples, https://github.com/ttroy50/cmake-examples

## compile_commands.json

` cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=on -DCMAKE_BUILD_TYPE=RelWithDebInfo`

## gcc or clang

```sh
# gcc
export CC=`which gcc`; export CXX=`which g++`
# clang
export CC=`which clang`; export CXX=`which clang++`
```

## cmake build dir

```
.
├── CMakeCache.txt                                    # compiler executable, flags, find_package exported var
├── CMakeFiles
│   ├── 3.20.2
│   │   ├── CMakeCCompiler.cmake
│   │   ├── CMakeCXXCompiler.cmake
│   │   ├── CMakeDetermineCompilerABI_C.bin
│   │   ├── CMakeDetermineCompilerABI_CXX.bin
│   │   ├── CMakeSystem.cmake
│   │   ├── CompilerIdC
│   │   └── CompilerIdCXX
│   ├── CMakeDirectoryInformation.cmake
│   ├── CMakeOutput.log                               # log
│   ├── CMakeTmp
│   ├── Makefile.cmake
│   ├── Makefile2                                     # cmake include, find_package used
│   ├── TargetDirectories.txt
│   ├── cmake.check_cache
│   ├── main.dir
│   │   ├── DependInfo.cmake
│   │   ├── build.make
│   │   ├── cmake_clean.cmake
│   │   ├── compiler_depend.make
│   │   ├── compiler_depend.ts
│   │   ├── depend.make
│   │   ├── flags.make
│   │   ├── link.txt
│   │   ├── main.cpp.o
│   │   ├── main.cpp.o.d
│   │   └── progress.make
│   └── progress.marks
├── Makefile                                          # make help for all target
├── cmake_install.cmake
├── compile_commands.json                             # lsp
└── main
```

## find_package

> build and install first

```cmake
cmake_minimum_required(VERSION 3.0)

project(test)

set(CMAKE_CXX_STANDARD 17)

# find a boost install with the libraries filesystem and system
message("module path" ${CMAKE_MODULE_PATH})
find_package(Boost 1.46.1 REQUIRED COMPONENTS filesystem system)

# check if boost was found
if(Boost_FOUND)
    message ("boost found")
else()
    message (FATAL_ERROR "Cannot find Boost")
endif()

# Add an executable
add_executable(main main.cpp)

# link against the boost libraries
target_link_libraries(main
    PRIVATE
        Boost::filesystem
)
```

## import googletest from source

https://github.com/google/googletest/blob/main/googletest/README.md

1. download as a submodule
2. add it as cmake subproject

> And a more robust and flexible approach is to build GoogleTest as part of that
> project directly. This is done by making the GoogleTest source code available to
> the main build and adding it using CMake's add_subdirectory() command. This has
> the significant advantage that the same compiler and linker settings are used
> between GoogleTest and the rest of your project

```cmake
add_subdirectory(3rd_party/googletest)

add_executable(unit_tests unit_test.cpp)

target_link_libraries(unit_tests
    gtest
    gtest_main
)
```

## package manager conan

https://github.com/ttroy50/cmake-examples/tree/master/07-package-management/D-conan

```sh
~/workdir/github/vcpkg master !1 ❯ conan help
Consumer commands
  install    Installs the requirements specified in a recipe (conanfile.py or conanfile.txt).
  config     Manages Conan configuration.
  get        Gets a file or list a directory of a given reference or package.
  info       Gets information about the dependency graph of a recipe.
  search     Searches package recipes and binaries in the local cache or a remote. Unless a
             remote is specified only the local cache is searched.
Creator commands
  new        Creates a new package recipe template with a 'conanfile.py' and optionally,
             'test_package' testing files.
  create     Builds a binary package for a recipe (conanfile.py).
  upload     Uploads a recipe and binary packages to a remote.
  export     Copies the recipe (conanfile.py & associated files) to your local cache.
  export-pkg Exports a recipe, then creates a package from local source and build folders.
  test       Tests a package consuming it from a conanfile.py with a test() method.
Package development commands
  source     Calls your local conanfile.py 'source()' method.
  build      Calls your local conanfile.py 'build()' method.
  package    Calls your local conanfile.py 'package()' method.
  editable   Manages editable packages (packages that reside in the user workspace, but are
             consumed as if they were in the cache).
  workspace  Manages a workspace (a set of packages consumed from the user workspace that
             belongs to the same project).
Misc commands
  profile    Lists profiles in the '.conan/profiles' folder, or shows profile details.
  remote     Manages the remote list and the package recipes associated with a remote.
  user       Authenticates against a remote with user/pass, caching the auth token.
  imports    Calls your local conanfile.py or conanfile.txt 'imports' method.
  copy       Copies conan recipes and packages to another user/channel.
  remove     Removes packages or binaries matching pattern from local cache or remote.
  alias      Creates and exports an 'alias package recipe'.
  download   Downloads recipe and binaries to the local cache, without using settings.
  inspect    Displays conanfile attributes, like name, version, and options. Works locally,
             in local cache and remote.
  help       Shows help for a specific command.
  lock       Generates and manipulates lock files.
  frogarian  Conan The Frogarian

Conan commands. Type "conan <command> -h" for help
```

### conan config

`~/.conan`

```sh
hong@win10-black:~/workdir/codelab/conan-test/build$ tree ~/.conan/
/home/hong/.conan/
├── LICENSE
├── artifacts.properties
├── cacert.pem
├── conan.conf
├── config_install.json
├── hooks
│   └── attribute_checker.py
├── profiles
│   ├── clang-profile
│   └── default
├── remotes.json
├── settings.yml
├── settings.yml.new
└── version.txt
```

### conanfile.txt

```sh
hong@win10-black:~/workdir/codelab/conan-test$ cat conanfile.txt
[requires]
fmt/5.3.0

[generators]
cmake
```

### install

`mkdir build && cd build && conan install ..`

```sh
hong@win10-black:~/workdir/codelab/conan-test/build$ conan install ..
WARN: Migration: Updating settings.yml
WARN: ****************************************
WARN: settings.yml is locally modified, can't be updated
WARN: The new settings.yml has been stored in: /home/hong/.conan/settings.yml.new
WARN: ****************************************
WARN: ****************************************
WARN: 'cacert.pem' is locally modified, can't be updated
WARN: The new 'cacert.pem' has been stored in: /home/hong/.conan/cacert.pem.new
WARN: ****************************************
Configuration:
[settings]
arch=x86_64
arch_build=x86_64
build_type=Release
compiler=gcc
compiler.libcxx=libstdc++11
compiler.version=7
os=Linux
os_build=Linux
[options]
[build_requires]
[env]

fmt/5.3.0: Not found in local cache, looking in remotes...
fmt/5.3.0: Trying with 'conancenter'...
Downloading conanmanifest.txt completed [0.42k]
Downloading conanfile.py completed [4.33k]
Downloading conan_export.tgz completed [0.29k]
Decompressing conan_export.tgz completed [0.00k]
fmt/5.3.0: Downloaded recipe revision 0
conanfile.txt: Installing package
Requirements
    fmt/5.3.0 from 'conancenter' - Downloaded
Packages
    fmt/5.3.0:66c5327ebdcecae0a01a863939964495fa019a06 - Download

Installing (downloading, building) binaries...
fmt/5.3.0: Retrieving package 66c5327ebdcecae0a01a863939964495fa019a06 from remote 'conancenter'
Downloading conanmanifest.txt completed [0.75k]
Downloading conaninfo.txt completed [0.51k]
Downloading conan_package.tgz completed [141.26k]
Decompressing conan_package.tgz completed [0.00k]
fmt/5.3.0: Package installed 66c5327ebdcecae0a01a863939964495fa019a06
fmt/5.3.0: Downloaded package revision 0
conanfile.txt: Generator txt created conanbuildinfo.txt
conanfile.txt: Generator cmake created conanbuildinfo.cmake
conanfile.txt: Aggregating env generators
conanfile.txt: Generated conaninfo.txt
conanfile.txt: Generated graphinfo

hong@win10-black:~/workdir/codelab/conan-test/build$ tree ~/.conan/
/home/hong/.conan/
├── LICENSE
├── artifacts.properties
├── cacert.pem
├── cacert.pem.new
├── conan.conf
├── config_install.json
├── data
│   └── fmt
│       └── 5.3.0
│           └── _
│               ├── _
│               │   ├── dl
│               │   │   ├── export
│               │   │   │   └── conan_export.tgz
│               │   │   └── pkg
│               │   │       └── 66c5327ebdcecae0a01a863939964495fa019a06
│               │   │           └── conan_package.tgz
│               │   ├── export
│               │   │   ├── conandata.yml
│               │   │   ├── conanfile.py
│               │   │   └── conanmanifest.txt
│               │   ├── locks
│               │   │   └── 66c5327ebdcecae0a01a863939964495fa019a06
│               │   ├── metadata.json
│               │   ├── metadata.json.lock
│               │   └── package
│               │       └── 66c5327ebdcecae0a01a863939964495fa019a06
│               │           ├── conaninfo.txt
│               │           ├── conanmanifest.txt
│               │           ├── include
│               │           │   └── fmt
│               │           │       ├── chrono.h
│               │           │       ├── color.h
│               │           │       ├── core.h
│               │           │       ├── format-inl.h
│               │           │       ├── format.h
│               │           │       ├── locale.h
│               │           │       ├── ostream.h
│               │           │       ├── posix.h
│               │           │       ├── printf.h
│               │           │       ├── ranges.h
│               │           │       └── time.h
│               │           ├── lib
│               │           │   └── libfmt.a
│               │           └── licenses
│               │               └── LICENSE.rst
│               ├── _.count
│               └── _.count.lock
├── hooks
│   └── attribute_checker.py
├── profiles
│   ├── clang-profile
│   └── default
├── remotes.json
├── settings.yml
├── settings.yml.new
└── version.txt
```

### CMakeLists.txt

`conanbuildinfo.cmake`, `CONAN_LIBS`

```cmake
cmake_minimum_required(VERSION 3.5)

project(conan-test)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(conan-test
    main.cpp)

target_link_libraries(conan-test
    PRIVATE
		# ${CONAN_LIBS}
        fmt
)
```

### problem when use

1. Unable to connect to conancenter

https://github.com/conan-io/conan/issues/9695

> There are some other tools that could have been affected by the certificate
> issue, like proxies, VPN, zscaler, etc. It would be great to be able to run
> without that proxy for a moment, to see if that could be the issue (and talk to
> your IT if that is it).

## package manager vcpkg

https://github.com/microsoft/vcpkg/blob/master/docs/examples/installing-and-using-packages.md

```sh
~/workdir/codelab/vcpkg-test/build ❯ vcpkg help
  vcpkg search [pat]              Search for packages available to be built
  vcpkg install <pkg>...          Install a package
  vcpkg remove <pkg>...           Uninstall a package
  vcpkg remove --outdated         Uninstall all out-of-date packages
  vcpkg list                      List installed packages
  vcpkg update                    Display list of packages for updating
  vcpkg upgrade                   Rebuild all outdated packages
  vcpkg x-history <pkg>           (Experimental) Shows the history of CONTROL versions of a package
  vcpkg hash <file> [alg]         Hash a file by specific algorithm, default SHA512
  vcpkg help topics               Display the list of help topics
  vcpkg help <topic>              Display help for a specific topic

  vcpkg integrate install         Make installed packages available user-wide
  vcpkg integrate remove          Remove user-wide integration
  vcpkg integrate bash            Enable bash tab-completion
  vcpkg integrate x-fish          Enable fish tab-completion

  vcpkg export <pkg>... [opt]...  Exports a package
  vcpkg edit <pkg>                Open up a port for editing (uses $EDITOR, default 'code')
  vcpkg create <pkg> <url> [archivename]
                                  Create a new package
  vcpkg x-init-registry <path>    Initializes a registry in the directory <path>
  vcpkg owns <pat>                Search for files in installed packages
  vcpkg depend-info <pkg>...      Display a list of dependencies for packages
  vcpkg env                       Creates a clean shell environment for development or compiling
  vcpkg version                   Display version information
  vcpkg contact                   Display contact information to send feedback
```

`vcpkg install`: download source & build & install, under vcpkg root dir

`CMAKE_TOOLCHAIN_FILE`: cmake .. -DCMAKE_TOOLCHAIN_FILE=~/workdir/github/vcpkg/scripts/buildsystems/vcpkg.cmake