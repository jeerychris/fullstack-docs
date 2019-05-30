import re
import sys


class CheckUtil:
    @staticmethod
    def get_repeats(filename,
                    pattern=r"(\d{3})$",
                    flag=re.RegexFlag.M | re.RegexFlag.I):
        pattern = re.compile(pattern, flag)
        try:
            file = open(filename, 'r')
            content = file.read()
        except FileNotFoundError as err:
            print("can't find file %s, error message: %s" %
                  (filename, str(err)))
        except Exception as err:
            print("unknow err: %s" % (str(err)))
        else:
            matchs = pattern.findall(content)
            if any(matchs):
                for i in set(matchs):
                    matchs.remove(i)
                repeats = {}
                for i in matchs:
                    repeats[i] = repeats.get(i, 1) + 1 
                    # remove the repeats one time before, now add that
                return repeats
        finally:
            file.close()

    @staticmethod
    def argv_parse():
        argv = {}
        for arg in sys.argv:
            equal_index = arg.find("=")
            if equal_index != -1:
                argv[arg[:equal_index].strip()] = arg[equal_index +
                                                      1:len(arg)].strip()
            else:
                argv[arg] = ""
        return argv


if __name__ == "__main__":
    argv = CheckUtil.argv_parse()
    print(CheckUtil.get_repeats(argv["--filename"]))
