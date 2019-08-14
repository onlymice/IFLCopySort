from argparse import ArgumentParser

#setup arguments via argparse
parser = ArgumentParser()

#* Provide short usage description for the argparser to show on --help
ArgumentParser(prog='IFLScript', usage='%(prog)s --i {num} --file {path/to/original.ifl} --output {path/to/output.ifl}  ')

#* Arguments
#? --lines:  how many lines should be moved?
#? --file:   where is .ifl file to use *This file is only to make a copy*
#? --output: where to save edited copy of the .ifl file
parser.add_argument('--lines', type=int,
                        help=" how many lines should be moved {Number can't be greater than lines in a file} (default: 1)")
parser.add_argument('--file', type=str,
                        help='which .ifl file to COPY(default: /file.ifl)', required=True)
parser.add_argument('--output', type=str,
                        help="Output location of the сopied .ifl file (default: /out.ifl)", default='out.ifl')
requiredNamed = parser.add_argument_group('required argument')
parser.add_argument('--mode', type=str,
                        help="Which mode should be used? {top2bottom, bottom2top} type '--mode help' for extended list of modes (default: top2bottom)", required=True)
args = parser.parse_args()

def is_file_exists(file_path):
    from os import path
    if (path.isfile(file_path)):
        return  True
    return  False

class ModeSelector:
    def help(self, args):
        print("""Available mods:
        [top2bottom] - move {num of lines} from top to bottom WITHOUT doing copy on each move

        [bottom2top] - the same as top2bottom but from bottom to top

        [copy_on_each_top2bottom] - move line/lines from top to bottom and save a new file
            (example: file1.ifl) after the each line has been moved

        [copy_on_each_bottom2top] - the same as copy_on_each_top2bottom but from bottom to top

        [help] - this exact message
                """)
    def top2bottom(self, args):
        if(is_file_exists(args.file)):
            with open(args.file, "r+") as read:
                file_lines = read.readlines()
                for i in range(0, args.lines):
                    file_lines.sort(key=file_lines[0].__eq__)
                with open(args.output, "w+") as write:
                    write.writelines(file_lines)
        else:
            print("Please check if the path is correct")
            return #!Exit script

    def copy_on_each_top2bottom(self, args):
        if(is_file_exists(args.file)):
            with open(args.file, "r+") as read:
                file_lines = read.readlines()
                for i in range(0, args.lines):
                    file_lines.sort(key=file_lines[i].__eq__)
                    with open(f"{args.output.split('.')[0]}{i+1}.{args.output.split('.')[1]}", "w+") as write:
                        write.writelines(file_lines)
        else:
            print("Please check if the path is correct")
            return #!Exit script

    def bottom2top(self, args):
        if(is_file_exists(args.file)):
            with open(args.file, "r+") as read:
                file_lines = read.readlines()
                for i in range(args.lines, 0, -1):
                    file_lines = file_lines[-1:] + file_lines[:-1]
                with open(args.output, "w+") as write:
                    write.writelines(file_lines)
        else:
            print("Please check if the path is correct")
            return #!Exit script

    def copy_on_each_bottom2top(self, args):
        if(is_file_exists(args.file)):
            with open(args.file, "r+") as read:
                file_lines = read.readlines()
                for i in range(args.lines, 0, -1):
                    file_lines = file_lines[-1:] + file_lines[:-1]
                with open(f"{args.output.split('.')[0]}{i+1}.{args.output.split('.')[1]}", "w+") as write:
                    write.writelines(file_lines)
        else:
            print("Please check if the path is correct")
            return #!Exit script

Modes = {
    'top2bottom' : ModeSelector().top2bottom,
    'bottom2top' : ModeSelector().bottom2top,
    'copy_on_each_top2bottom' : ModeSelector().copy_on_each_top2bottom,
    'copy_on_each_bottom2top' : ModeSelector().copy_on_each_bottom2top,
    'help': ModeSelector().help,
}

#main of the script
def main(args):
    import os
    try:
        mode = Modes[args.mode]
        if callable(mode):
            mode(args)
    except Exception as e:
        print('Error '+ str(e))


main(args)