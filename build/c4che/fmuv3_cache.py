APJ_BOARD_ID = '9'
APJ_BOARD_TYPE = 'STM32F427xx'
APJ_TOOL = '/home/pratik/pratik_github/ardupilot_custom/Tools/scripts/apj_tool.py'
AP_HAL_REL = '../../libraries/AP_HAL_ChibiOS'
AP_HAL_ROOT = '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_HAL_ChibiOS'
AP_LIBRARIES = ['AP_HAL_ChibiOS', 'AP_Scripting', 'AP_Scripting/lua/src', 'AP_UAVCAN', 'modules/uavcan/libuavcan/src/**/*.cpp']
AP_LIBRARIES_OBJECTS_KW = {'features': ['ch_ap_library']}
AP_LIB_EXTRA_SOURCES = {'AP_Scripting': ['lua_generated_bindings.cpp']}
AP_PROGRAM_FEATURES = ['ch_ap_program']
AR = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'fmuv3'
BOARD_FLASH_SIZE = 2048
BOARD_MK = '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_HAL_ChibiOS/hwdef/common/chibios_board.mk'
BOOTLOADER = False
BOOTLOADER_EMBED = 1
BOOTLOADER_OPTION = ''
BUILDDIR = '/home/pratik/pratik_github/ardupilot_custom/build/fmuv3/modules/ChibiOS'
BUILDDIR_REL = 'modules/ChibiOS'
BUILDROOT = '/home/pratik/pratik_github/ardupilot_custom/build/fmuv3'
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('9', '3', '1')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Werror=format', '-Wpointer-arith', '-Wcast-align', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-Werror=shadow', '-Werror=return-type', '-Werror=unused-result', '-Werror=unused-variable', '-Werror=narrowing', '-Werror=attributes', '-Werror=overflow', '-Werror=parentheses', '-Werror=format-extra-args', '-Werror=ignored-qualifiers', '-Werror=undef', '-DARDUPILOT_BUILD', '-Wno-format-contains-nul', '-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-DARM_MATH_CM4', '-u_printf_float', '-Wlogical-op', '-Wframe-larger-than=1300', '-fsingle-precision-constant', '-Wno-attributes', '-fno-exceptions', '-Wall', '-Wextra', '-Wno-sign-compare', '-Wfloat-equal', '-Wpointer-arith', '-Wmissing-declarations', '-Wno-unused-parameter', '-Werror=array-bounds', '-Wfatal-errors', '-Werror=uninitialized', '-Werror=init-self', '-Werror=unused-but-set-variable', '-Wno-missing-field-initializers', '-Wno-trigraphs', '-fno-strict-aliasing', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-fno-strength-reduce', '-fno-builtin-printf', '-fno-builtin-fprintf', '-fno-builtin-vprintf', '-fno-builtin-vfprintf', '-fno-builtin-puts', '-mno-thumb-interwork', '-mthumb', '--specs=nano.specs', '--specs=nosys.specs', '-DCHIBIOS_BOARD_NAME="fmuv3"', '-D__USE_CMSIS', '-Werror=deprecated-declarations', '-DNDEBUG=1', '-Wno-error=double-promotion', '-Wno-error=missing-declarations', '-Wno-error=float-equal', '-Wno-error=undef', '-Wno-error=cpp', '-std=c11', '-MMD', '-DHAL_CAN_IFACES=2', '-Os']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CHIBIOS_BOARD_NAME = 'HAL_BOARD_NAME="fmuv3"'
CHIBIOS_BUILD_FLAGS = 'USE_FATFS=yes CHIBIOS_STARTUP_MK=os/common/startup/ARMCMx/compilers/GCC/mk/startup_stm32f4xx.mk CHIBIOS_PLATFORM_MK=os/hal/ports/STM32/STM32F4xx/platform.mk MCU=cortex-m4 ENV_UDEFS=-DCHPRINTF_USE_FLOAT=1 USE_COPT=-Os'
CHIBIOS_SCRIPTS = '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_HAL_ChibiOS/hwdef/scripts'
CH_ROOT = '/home/pratik/pratik_github/ardupilot_custom/modules/ChibiOS'
CH_ROOT_REL = '../../modules/ChibiOS'
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CONFIGURE_FILES = ['/home/pratik/pratik_github/ardupilot_custom/libraries/AP_Scripting/wscript', '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_GPS/wscript', '/usr/lib/python3.8/importlib/_bootstrap.py', '/usr/lib/python3.8/importlib/_bootstrap_external.py', '/usr/lib/python3.8/codecs.py', '/usr/lib/python3.8/encodings/aliases.py', '/usr/lib/python3.8/encodings/__init__.py', '/usr/lib/python3.8/encodings/utf_8.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waf-light', '/usr/lib/python3.8/encodings/latin_1.py', '/usr/lib/python3.8/abc.py', '/usr/lib/python3.8/io.py', '/usr/lib/python3.8/stat.py', '/usr/lib/python3.8/_collections_abc.py', '/usr/lib/python3.8/genericpath.py', '/usr/lib/python3.8/posixpath.py', '/usr/lib/python3.8/os.py', '/usr/lib/python3.8/_sitebuiltins.py', '/usr/lib/python3.8/_bootlocale.py', '/home/pratik/.local/lib/python3.8/site-packages/_distutils_hack/__init__.py', '/usr/lib/python3.8/types.py', '/usr/lib/python3.8/warnings.py', '/usr/lib/python3.8/importlib/__init__.py', '/usr/lib/python3.8/importlib/machinery.py', '/usr/lib/python3.8/importlib/abc.py', '/usr/lib/python3.8/operator.py', '/usr/lib/python3.8/keyword.py', '/usr/lib/python3.8/heapq.py', '/usr/lib/python3.8/reprlib.py', '/usr/lib/python3.8/collections/__init__.py', '/usr/lib/python3.8/functools.py', '/usr/lib/python3.8/contextlib.py', '/usr/lib/python3.8/importlib/util.py', '/usr/lib/python3/dist-packages/mpl_toolkits/__init__.py', '/usr/lib/python3/dist-packages/zope/__init__.py', '/usr/lib/python3/dist-packages/apport_python_hook.py', '/usr/lib/python3.8/sitecustomize.py', '/usr/lib/python3.8/site.py', '/usr/lib/python3.8/lib-dynload/_opcode.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/opcode.py', '/usr/lib/python3.8/dis.py', '/usr/lib/python3.8/collections/abc.py', '/usr/lib/python3.8/enum.py', '/usr/lib/python3.8/sre_constants.py', '/usr/lib/python3.8/sre_parse.py', '/usr/lib/python3.8/sre_compile.py', '/usr/lib/python3.8/copyreg.py', '/usr/lib/python3.8/re.py', '/usr/lib/python3.8/token.py', '/usr/lib/python3.8/tokenize.py', '/usr/lib/python3.8/linecache.py', '/usr/lib/python3.8/inspect.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/__init__.py', '/usr/lib/python3.8/__future__.py', '/usr/lib/python3.8/shlex.py', '/usr/lib/python3.8/fnmatch.py', '/usr/lib/python3.8/_compression.py', '/usr/lib/python3.8/_weakrefset.py', '/usr/lib/python3.8/threading.py', '/usr/lib/python3.8/lib-dynload/_bz2.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/bz2.py', '/usr/lib/python3.8/lib-dynload/_lzma.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/lzma.py', '/usr/lib/python3.8/shutil.py', '/usr/lib/python3.8/traceback.py', '/usr/lib/python3.8/datetime.py', '/usr/lib/python3.8/platform.py', '/usr/lib/python3.8/struct.py', '/usr/lib/python3.8/base64.py', '/usr/lib/python3.8/signal.py', '/usr/lib/python3.8/_compat_pickle.py', '/usr/lib/python3.8/pickle.py', '/usr/lib/python3.8/selectors.py', '/usr/lib/python3.8/subprocess.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Errors.py', '/usr/lib/python3.8/lib-dynload/_hashlib.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/hashlib.py', '/usr/lib/python3.8/encodings/hex_codec.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Utils.py', '/usr/lib/python3.8/weakref.py', '/usr/lib/python3.8/copy.py', '/usr/lib/python3.8/lib-dynload/_ctypes.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/ctypes/_endian.py', '/usr/lib/python3.8/ctypes/__init__.py', '/usr/lib/python3.8/lib-dynload/termios.cpython-38-x86_64-linux-gnu.so', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/ansiterm.py', '/usr/lib/python3.8/string.py', '/usr/lib/python3.8/logging/__init__.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Logs.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/ConfigSet.py', '/usr/lib/python3.8/bisect.py', '/usr/lib/python3.8/random.py', '/usr/lib/python3.8/tempfile.py', '/usr/lib/python3.8/textwrap.py', '/usr/lib/python3.8/locale.py', '/usr/lib/python3.8/gettext.py', '/usr/lib/python3.8/optparse.py', '/usr/lib/python3.8/imp.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Node.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Context.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Options.py', '/usr/lib/python3.8/lib-dynload/_queue.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/queue.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Task.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Runner.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/TaskGen.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Build.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Configure.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Scripting.py', '/usr/lib/python3.8/lib-dynload/_json.cpython-38-x86_64-linux-gnu.so', '/usr/lib/python3.8/json/scanner.py', '/usr/lib/python3.8/json/decoder.py', '/usr/lib/python3.8/json/encoder.py', '/usr/lib/python3.8/json/__init__.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/ap_persistent.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/ardupilotwaf.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/boards.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/__init__.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/c_aliases.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/c_preproc.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/c_config.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/c_osx.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/c_tests.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/ccroot.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/compiler_cxx.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/ar.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/gxx.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/clangxx.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/icpc.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/compiler_c.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/extras/__init__.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/xlc.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/extras/c_bgxlc.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/gcc.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/extras/c_emscripten.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/extras/c_nec.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/clang.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/icc.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/waf_unit_test.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/python.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/build_summary.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/ap_library.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/toolchain.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/cxx.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/Tools/c.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/extras/gccdeps.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/cxx_checks.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/chibios.py', '/home/pratik/.local/lib/python3.8/site-packages/intelhex/compat.py', '/home/pratik/.local/lib/python3.8/site-packages/intelhex/getsizeof.py', '/home/pratik/.local/lib/python3.8/site-packages/intelhex/__init__.py', '/usr/lib/python3.8/pipes.py', '/home/pratik/pratik_github/ardupilot_custom/modules/waf/waflib/extras/clang_compilation_database.py', '/usr/lib/python3.8/xml/__init__.py', '/usr/lib/python3.8/xml/etree/__init__.py', '/usr/lib/python3.8/xml/etree/ElementPath.py', '/usr/lib/python3.8/xml/etree/ElementTree.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/mavgen.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/uavcangen.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/git_submodule.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/gtest.py', '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/static_linking.py', '/home/pratik/pratik_github/ardupilot_custom/wscript']
CONFIGURE_HASH = b'\xa5O4;\xad#\x15\xc1\xb4\x8a$D\x1b\xe3\x17n'
CORTEX = 'cortex-m4'
COVERAGE = False
CPPPATH_ST = '-I%s'
CPU_FLAGS = ['-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-DARM_MATH_CM4', '-u_printf_float']
CXX = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-g++']
CXXFLAGS = ['-Werror=implicit-fallthrough', '-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wpointer-arith', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-expansion-to-defined', '-Werror=cast-align', '-Werror=attributes', '-Werror=format-security', '-Werror=format-extra-args', '-Werror=enum-compare', '-Werror=format', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=narrowing', '-Werror=return-type', '-Werror=switch', '-Werror=sign-compare', '-Werror=type-limits', '-Werror=undef', '-Werror=unused-result', '-Werror=shadow', '-Werror=unused-value', '-Werror=unused-variable', '-Werror=delete-non-virtual-dtor', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=parentheses', '-DARDUPILOT_BUILD', '-Wuninitialized', '-Warray-bounds', '-Wno-format-contains-nul', '-Werror=unused-but-set-variable', '-Werror=suggest-override', '-Werror=implicit-fallthrough', '-Wmaybe-uninitialized', '-Wduplicated-cond', '-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Werror=format', '-Wpointer-arith', '-Wcast-align', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-Werror=shadow', '-Werror=return-type', '-Werror=unused-result', '-Werror=unused-variable', '-Werror=narrowing', '-Werror=attributes', '-Werror=overflow', '-Werror=parentheses', '-Werror=format-extra-args', '-Werror=ignored-qualifiers', '-Werror=undef', '-DARDUPILOT_BUILD', '-Wno-format-contains-nul', '-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-DARM_MATH_CM4', '-u_printf_float', '-Wlogical-op', '-Wframe-larger-than=1300', '-fsingle-precision-constant', '-Wno-attributes', '-fno-exceptions', '-Wall', '-Wextra', '-Wno-sign-compare', '-Wfloat-equal', '-Wpointer-arith', '-Wmissing-declarations', '-Wno-unused-parameter', '-Werror=array-bounds', '-Wfatal-errors', '-Werror=uninitialized', '-Werror=init-self', '-Werror=unused-but-set-variable', '-Wno-missing-field-initializers', '-Wno-trigraphs', '-fno-strict-aliasing', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-fno-strength-reduce', '-fno-builtin-printf', '-fno-builtin-fprintf', '-fno-builtin-vprintf', '-fno-builtin-vfprintf', '-fno-builtin-puts', '-mno-thumb-interwork', '-mthumb', '--specs=nano.specs', '--specs=nosys.specs', '-DCHIBIOS_BOARD_NAME="fmuv3"', '-D__USE_CMSIS', '-Werror=deprecated-declarations', '-DNDEBUG=1', '-Wno-error=double-promotion', '-Wno-error=missing-declarations', '-Wno-error=float-equal', '-Wno-error=undef', '-Wno-error=cpp', '-fno-rtti', '-fno-threadsafe-statics', '-Werror', '-MMD', '-Os', '-include', 'ap_config.h']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/home/pratik/pratik_github/ardupilot_custom"', 'AP_SCRIPTING_CHECKS=1', 'CONFIG_HAL_BOARD=HAL_BOARD_CHIBIOS', 'ENABLE_HEAP=1', 'ENABLE_ONVIF=0', 'ENABLE_SCRIPTING=1', 'HAVE_STD_NULLPTR_T=0', 'LUA_32BITS=1', 'USE_LIBC_REALLOC=0', 'UAVCAN_CPP_VERSION=UAVCAN_CPP03', 'UAVCAN_NO_ASSERTIONS=1', 'UAVCAN_NULLPTR=nullptr']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'WAF_BUILD': '', '__STDC_FORMAT_MACROS': '', 'HAVE_CMATH_ISFINITE': '', 'HAVE_CMATH_ISINF': '', 'HAVE_CMATH_ISNAN': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'HAVE_ENDIAN_H': '', 'HAVE_BYTESWAP_H': '', 'HAVE_MEMRCHR': '', 'PYTHONDIR': '', 'PYTHONARCHDIR': '', '_GNU_SOURCE': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
DOUBLE_PRECISION_SOURCES = {'AP_GPS': ['AP_GPS_SBF.cpp']}
DSDL_COMPILER = '/home/pratik/pratik_github/ardupilot_custom/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/pratik/pratik_github/ardupilot_custom/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_ASSERTS = False
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
ENABLE_MALLOC_GUARD = False
ENABLE_ONVIF = False
ENABLE_STATS = False
EXTERNAL_PROG_FLASH_MB = 0
FLASH_RESERVE_START_KB = '16'
FLASH_TOTAL = 2080768
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['ChibiOS', 'mavlink']
HAL_NUM_CAN_IFACES = '2'
HAS_EXTERNAL_FLASH_SECTIONS = 0
HAS_GTEST = False
HAVE_CMATH_ISFINITE = 1
HAVE_CMATH_ISINF = 1
HAVE_CMATH_ISNAN = 1
HAVE_INTEL_HEX = True
HWDEF = '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_HAL_ChibiOS/hwdef/fmuv3/hwdef.dat'
HWDEF_EXTRA = None
INCLUDES = ['/home/pratik/pratik_github/ardupilot_custom/libraries/', '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_Common/missing', '/home/pratik/pratik_github/ardupilot_custom/libraries/AP_GyroFFT/CMSIS_5/include', '/home/pratik/pratik_github/ardupilot_custom/modules/uavcan/libuavcan/include']
IOMCU_FW = 0
LIB = ['gcc', 'm']
LIBDIR = '/usr/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-DARM_MATH_CM4', '-u_printf_float', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-u_port_lock', '-u_port_unlock', '-u_exit', '-u_kill', '-u_getpid', '-u_errno', '-uchThdExit', '-fno-common', '-nostartfiles', '-mno-thumb-interwork', '-mthumb', '--specs=nano.specs', '--specs=nosys.specs', '-L/home/pratik/pratik_github/ardupilot_custom/build/fmuv3', '-L/home/pratik/pratik_github/ardupilot_custom/modules/ChibiOS/os/common/startup/ARMCMx/compilers/GCC/ld', '-L/home/pratik/pratik_github/ardupilot_custom/libraries/AP_HAL_ChibiOS/hwdef/common', '-Wl,--gc-sections,--no-warn-mismatch,--library-path=/ld,--script=ldscript.ld,--defsym=__process_stack_size__=0x1C00,--defsym=__main_stack_size__=0x600']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-gcc']
LINK_CXX = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-g++']
MAIN_STACK = '0x600'
MAKE = ['/usr/bin/make']
MAVLINK_DIR = '/home/pratik/pratik_github/ardupilot_custom/modules/mavlink'
MKFW_TOOLS = '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf'
NEED_CMATH_ISFINITE_STD_NAMESPACE = 1
NEED_CMATH_ISINF_STD_NAMESPACE = 1
NEED_CMATH_ISNAN_STD_NAMESPACE = 1
OBJCOPY = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-objcopy']
OPTIONS = {'colors': 'auto', 'jobs': 4, 'keep': 0, 'verbose': 0, 'zones': '', 'profile': 0, 'pdb': 0, 'whelp': 0, 'out': '', 'top': '', 'no_lock_in_run': '', 'no_lock_in_out': '', 'no_lock_in_top': '', 'prefix': '/usr', 'bindir': None, 'libdir': None, 'progress_bar': 0, 'targets': '', 'files': '', 'destdir': '', 'force': False, 'distcheck_args': None, 'check_cxx_compiler': None, 'check_c_compiler': None, 'no_tests': False, 'all_tests': False, 'clear_failed_tests': False, 'testcmd': False, 'dump_test_scripts': False, 'pyc': 1, 'pyo': 1, 'nopycache': None, 'python': None, 'pythondir': None, 'pythonarchdir': None, 'program_group': [], 'upload': None, 'upload_port': None, 'check_verbose': None, 'clean_all_sigs': None, 'asan': None, 'summary_all': None, 'board': 'fmuv3', 'debug': False, 'disable_watchdog': False, 'coverage': False, 'Werror': False, 'toolchain': None, 'disable_gccdeps': False, 'enable_asserts': False, 'enable_malloc_guard': False, 'enable_stats': False, 'bootloader': False, 'autoconfig': True, 'submodule_update': True, 'enable_header_checks': False, 'default_parameters': None, 'enable_math_check_indexes': False, 'disable_scripting': False, 'no_gcs': False, 'scripting_checks': True, 'enable_onvif': False, 'apstatedir': '', 'rsync_dest': '', 'enable_benchmarks': False, 'enable_lttng': False, 'disable_libiio': False, 'disable_tests': False, 'enable_sfml': False, 'enable_sfml_joystick': False, 'enable_sfml_audio': False, 'osd': False, 'osd_fonts': False, 'sitl_osd': False, 'sitl_rgbled': False, 'sitl_32bit': False, 'build_dates': False, 'sitl_flash_storage': False, 'disable_ekf2': False, 'disable_ekf3': False, 'ekf_double': False, 'ekf_single': False, 'static': False, 'postype_single': False, 'extra_hwdef': None, 'assert_cc_version': None}
PERIPH_FW = 0
PREFIX = '/usr'
PROCESS_STACK = '0x1C00'
PT_DIR = '/home/pratik/pratik_github/ardupilot_custom/Tools/ardupilotwaf/chibios/image'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-38'
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/lib/python3.8/site-packages'
PYTHONDIR = '/usr/lib/python3.8/site-packages'
PYTHON_VERSION = '3.8'
ROMFS_FILES = [('io_firmware.bin', 'Tools/IO_Firmware/iofirmware_lowpolh.bin'), ('hwdef.dat', '/home/pratik/pratik_github/ardupilot_custom/build/fmuv3/hw.dat'), ('bootloader.bin', '/home/pratik/pratik_github/ardupilot_custom/Tools/bootloaders/fmuv3_bl.bin')]
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SERIAL_PORT = '/home/pratik/pratik_github/ardupilot_custom/dev/serial/by-id/*_STLink*'
SHLIB_MARKER = '-Wl,-Bdynamic'
SITL32BIT = False
SIZE = ['/opt/gcc-arm-none-eabi-9-2020-q2-update/bin/arm-none-eabi-size']
SONAME_ST = '-Wl,-h,%s'
SRCROOT = '/home/pratik/pratik_github/ardupilot_custom'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'arm-none-eabi'
TOOLS_SCRIPTS = '/home/pratik/pratik_github/ardupilot_custom/Tools/scripts'
UPLOAD_TOOLS = '/home/pratik/pratik_github/ardupilot_custom/Tools/scripts'
USBID = '0x1209/0x5741'
WITH_FATFS = '1'
cfg_files = ['/home/pratik/pratik_github/ardupilot_custom/build/fmuv3/ap_config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'