import ast

# byte ori  : 02 7B C6 1C 00 04 2A
# byte mod  : 17 00 00 00 00 00 2A
# offset    : 0x0016A211


byte_path = 'tbplus-injector/bytes.txt'

def load_patch_data(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    patch_offset = int(lines[0], 16)
    original_bytes = bytearray(ast.literal_eval(lines[1]))
    modified_bytes = bytearray(ast.literal_eval(lines[2]))

    return patch_offset, original_bytes, modified_bytes

patch_offset, original_bytes, modified_bytes = load_patch_data("tbplus-injector/bytes.txt")

# patch_offset = 0x0016A211
# original_bytes = bytearray([0x02, 0x7B, 0xC6, 0x1C, 0x00, 0x04, 0x2A]) # index 1
# modified_bytes = bytearray([0x17, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2A]) # index 2

def apply_patch(file_path):

    with open(file_path, 'r+b') as f:
        f.seek(patch_offset)
        current_bytes = bytearray(f.read(len(original_bytes)))
        if current_bytes != original_bytes:
            print("inject activated")
        f.seek(patch_offset)
        f.write(modified_bytes)
        print(f"Patch applied at offset {hex(patch_offset)}")
        print("Activated Successfully!")
        input()

def revert_patch(file_path):
    with open(file_path, 'r+b') as f:
        f.seek(patch_offset)
        current_bytes = bytearray(f.read(len(modified_bytes)))
        if current_bytes != modified_bytes:
            print("inject deactivated")
        f.seek(patch_offset)
        f.write(original_bytes)
        print(f"Patch reverted at offset {hex(patch_offset)}")
        print("Deactivated Successfully!")
        input()