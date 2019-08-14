import subprocess, os, sys
clear = lambda: os.system('cls' if sys.platform.startswith('win32') else 'clear') #Clearing command line depends on system Windows and Linux supported Only!


def test_top2bottom_mode():
    test_result = []
    with open('tests/test_top2bottom_mode/test_top2bottom_mode.ifl', "w+") as f:
        file = open("test.ifl", "r+").readlines()
        f.writelines(file)

    ifl = open('tests/test_top2bottom_mode/test_top2bottom_mode.ifl', "r+").readlines()
    for i in range(0, len(ifl) + 1):
        #print(subprocess.run(["python", "Script.py", "--lines", str(i), "--mode", "top2bottom",  "--file", "test.ifl", "--output", "tests/test_top2bottom_mode/test_top2bottom_mode.ifl"]))
        ifl = open('tests/test_top2bottom_mode/test_top2bottom_mode.ifl', "r+").readlines()
        #print(open('tests/test_top2bottom_mode/test_top2bottom_mode.ifl', "r+").read())
    import re
    for lane in ifl:
        test_result.append(int(re.sub("\D", "", lane)[0]))
    return test_result

def test_bottom2top_mode():
    test_result = []
    with open('tests/test_bottom2top_mode/test_bottom2top_mode.ifl', "w+") as f:
        file = open("test.ifl", "r+").readlines()
        f.writelines(file)
    ifl = open('tests/test_bottom2top_mode/test_bottom2top_mode.ifl', "r+").readlines()
    for i in range(0, len(ifl) + 1):
        #print(subprocess.run(["python", "Script.py", "--lines", str(i), "--mode", "bottom2top",  "--file", "test.ifl", "--output", "tests/test_bottom2top_mode/test_bottom2top_mode.ifl"]))
        ifl = open('tests/test_bottom2top_mode/test_bottom2top_mode.ifl', "r+").readlines()
        #print(open('tests/test_bottom2top_mode/test_bottom2top_mode.ifl', "r+").read())
    import re
    for lane in ifl:
        test_result.append(int(re.sub("\D", "", lane)[0]))
    return test_result


def main():
    #Test of the module top2bottom
    print("|Test case {1} for the module top2bottom:")
    test_case_top2bottom = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    returned_case_top2bottom = test_top2bottom_mode()
    print(f"|Test numbers - {str(test_case_top2bottom)}\n|Returned numbers - {str(returned_case_top2bottom)}\n|They are should be equal")
    if test_case_top2bottom != returned_case_top2bottom:
        print("|Test Fail")
        return("Test {1} Fail")
    print("|Pass\n")
    #Test of the module bottom2top
    print("|Test case {2} for the module bottom2top:")
    test_case_bottom2top = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    returned_case_bottom2top = test_bottom2top_mode()
    print(f"|Test numbers - {str(test_case_bottom2top)}\n|Returned numbers - {str(returned_case_bottom2top)}\n|They are should be equal")
    if test_case_bottom2top != returned_case_bottom2top:
        print("|Test Fail")
        return("Test {2} Fail")
    print("|Pass\n")
    return("\nAll Pass")
##ToDo Add tests for other modes

print(main())
