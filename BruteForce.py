import itertools
import time
from BlowFish import Blowfish

# Hàm thử nghiệm một khóa
def try_key(encrypted_data, padding_data, possible_key, original_plaintext):
    # Tạo một hệ blowfish với khóa possible_key, thực hiện decrypt dữ liệu encrypt_data với hệ đó 
    bf = Blowfish(possible_key)
    decrypted_text = bf.decrypt(encrypted_data, padding_data)
    # So sánh dữ liệu được decrypt với dữ liệu ban đầu
    return decrypted_text == original_plaintext

def brute_force_attack(encrypted_data, padding_data, original_plaintext, max_key_length):
    # Xác định không gian khóa
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    # Lặp và thử khóa từ độ dài 1 tới max_key_length
    for key_length in range(1, max_key_length + 1):
        # Tạo tổ hợp từ độ dài trên và tạo các khóa thử từ tổ hợp
        for possible_key in itertools.product(characters, repeat=key_length):
            possible_key = ''.join(possible_key)
            if try_key(encrypted_data, padding_data, possible_key, original_plaintext):
                return possible_key
    return None

if __name__ == "__main__":
    input_text = "blowfish"
    key_secret = "abcde"  # Khóa bí mật thực tế

    # Tạo một hệ mật blowfish với khóa bằng key_secret
    bf = Blowfish(key_secret)

    # Mã hóa dữ liệu
    encrypted_data, padding_data = bf.encrypt(input_text)
    print("Encrypted data: ", encrypted_data)
    print("Padding data: ", padding_data)

    # Bắt đầu tấn công Brute Force
    start_time = time.time()
    found_key = brute_force_attack(encrypted_data, padding_data, input_text, 6)  # Độ dài khóa tối đa là 6
    end_time = time.time()

    if found_key:
        print(f"Khóa tìm thấy: {found_key}")
    else:
        print("Không tìm thấy khóa phù hợp")

    print(f"Thời gian tấn công: {end_time - start_time} giây")
