from conans import ConanFile
from conans.model import Generator
from pathlib import Path

class foamGen(Generator):

    @property
    def filename(self):
        opt_path = "options"
        if (not Path(opt_path).exists()):
            opt_temp_path = "Make/options"
        return opt_path

    @property
    def content(self):
        opt_temp_path = "options.template"
        if (not Path(opt_temp_path).exists()):
            opt_temp_path = "Make/options.template"
        opt_temp = Path("options.template")
        opt_temp = Path(opt_temp_path).read_text()

        incl = ""
        for i in self.deps_build_info.include_paths:
            incl += "   -I{} \\ \n".format(i)

        lib_incl = ""
        for lp in self.deps_build_info.lib_paths:
            lib_incl += "   -L{} \\ \n".format(lp)

        for l in self.deps_build_info.libs:
            lib_incl += "   -l{} \\ \n".format(l)

        opt_temp = opt_temp.replace("{{{CONAN_INCS_INCS}}}",incl)
        opt_temp = opt_temp.replace("{{{CONAN_INCS_LIBS}}}",lib_incl)

        return opt_temp


class OpenFOAMGeneratorPackage(ConanFile):
    name = "foamGen"
    version = "0.1"
    url = "https://github.com/..."
    license = "MIT"