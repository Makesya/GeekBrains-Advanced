import os


def rename_files(desired_name="", num_digits=3, source_ext="", target_ext="", name_range=[0, 0]):
    counter = 1
    for filename in os.listdir("test_folder"):
        if filename.endswith(source_ext):
            base_name = "".join(filename[name_range[0]:name_range[1]])
            new_name = desired_name + \
                str(counter).zfill(num_digits) + "." + target_ext
            os.rename(os.path.join("test_folder", filename),
                      os.path.join("test_folder", new_name))
            counter += 1
