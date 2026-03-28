import os

def check_symlinks(root_dir='.'):
    """
    Recursively checks for symbolic links under root_dir.
    Reports valid (intact) and broken (missing target) symlinks.
    """
    broken_links = []
    valid_links = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.islink(file_path):  # Check if it's a symbolic link
                target = os.readlink(file_path)  # Get the target path string
                # Resolve the full target path (handles relative targets correctly)
                resolved_target = os.path.normpath(os.path.join(dirpath, target))
                
                if os.path.exists(resolved_target):
                    valid_links.append((file_path, target))
                else:
                    broken_links.append((file_path, target))
    
    # Output results
    print("=== Broken Symbolic Links (Missing Targets) ===")
    if broken_links:
        for link, target in broken_links:
            print(f"{link} -> {target}  (BROKEN: target does not exist)")
    else:
        print("No broken symbolic links found.")
    
    print("\n=== Valid Symbolic Links (Intact) ===")
    if valid_links:
        for link, target in valid_links:
            print(f"{link} -> {target}")
    else:
        print("No symbolic links found.")

if __name__ == "__main__":
    check_symlinks()