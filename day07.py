from Utils.tools import *
import re
from collections import deque

class Filesystem:
    def __init__(self):
        self.root = None
        self.directories = []

    def add_root(self, dir):
        self.root = dir

    def add_directory(self, dir):
        self.directories.append(dir)

    def get_directory(self, directory_name):
        for d in self.directories:
            if d.name == directory_name:
                return d

    def print_directories(self):
        for d in self.directories:
            print (f"Directory name {d.name} and size {d.size}")

    def create_adjacency_list(self):
        adjacency_list = {}
        for d in self.directories:
            if len(d.children) > 0:
                adjacency_list[d.name] = d.children
        return adjacency_list

            

class Dir:
    
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children = []

    def add_child_directory(self, child):
        self.children.append(child)
    
    def add_file_to_size(self, filesize):
        self.size += filesize



def create_dir(dir):
    new_dir = Dir(dir)
    return new_dir

 


def main():
    input = get_input("07", False)
    terminal_output = clean_list_strings(input)

    filesystem = Filesystem()

    # create the root directory
    root_dir = Dir("/")
    filesystem.add_root(root_dir)

    # add root to filesytem
    filesystem.add_directory(root_dir)

    current_directory = None

    # loop through terminal output
    for output in terminal_output:
        file = re.search("\A\d", output)
        directory = re.search("\Adir", output)
        command = re.search("\A\$", output)
        if command:
            cd = re.search("cd", output[2:4])
            if cd:
                if output[5:7] == "..":
                    # moving one directory up
                    # removing one dir from the current path
                    temp = current_directory.name.rpartition('/')
                    new_path = temp[0]
                    current_directory = filesystem.get_directory(new_path)
                    
                else:
                    # changing directory
                    directory_name = output[5:]
                    if current_directory is None:
                        new_path = f"{directory_name}"
                    else:
                        new_path = f"{current_directory.name}/{directory_name}"
                    current_directory = filesystem.get_directory(new_path)
        else:
            if directory:
                directory_name = output[4:]
                path_name = f"{current_directory.name}/{directory_name}"
                new_directory = create_dir(path_name)
                current_directory.add_child_directory(new_directory)
                filesystem.add_directory(new_directory)
            if file:
                file_attr = output.split()
                file_size = int(file_attr[0])
                # add file size to current directory size
                current_directory.add_file_to_size(file_size)


    adjlist = filesystem.create_adjacency_list()

    # the filesystem is build, now we must traverse it and calculate total directory sizes

    stack = deque()
    seen = []

    root = filesystem.root

    # add the root to the stack first
    stack.append(root)

    # while there is still something in the stack
    while len(stack) != 0:
        # look at the top of the stack
        top = stack[-1]
        # add it to seen list if not allready in there
        if top.name in seen:
            # we have backtracked to here
            # we can get all the sizes of our children and add it to our size
            for child in top.children:
                top.size += child.size
            # we can remove this directory from the stack
            stack.pop()
        else:
            # we add this directory to the seen list
            seen.append(top.name)
            if top.name in adjlist:
                # add children to the stack
                children = adjlist[top.name]
                for child in children:
                    # if the child has not been seen yet
                    if child.name not in seen:
                        stack.append(child)  
            else:
                # the directory is not in the adjacency list so it is a leaf 
                # it's size is the directory final size since it has no children
                # we can remove this directory from the stack
                stack.pop()
                

    def puzzle_1(filesystem):
        directories = filesystem.directories
        selected_dirs = [directory.size for directory in directories if directory.size <= 100000]
        return sum(selected_dirs)

    def puzzle_2(filesystem):
        root_dir_size = filesystem.root.size
        total_disk_space = 70000000
        required_disk_space = 30000000
        current_unused_space = total_disk_space - root_dir_size
        to_be_removed = required_disk_space - current_unused_space
        directories = filesystem.directories
        selected_dirs = [directory.size for directory in directories if directory.size >= to_be_removed]
        selected_dirs.sort()
        return selected_dirs[0]


            
        
  
    
            
            



            
        



    result_puzzle_1 = puzzle_1(filesystem)
    result_puzzle_2 = puzzle_2(filesystem)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")   


if __name__ == "__main__":
    main()