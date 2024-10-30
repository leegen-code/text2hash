import hashlib
from colorama import Fore, Style, init

def print_banner(title):
    # Initialize Colorama
    init(autoreset=True)

    banner = f"""
    {Fore.BLUE}{Style.BRIGHT}
    
        ___                             ___          ,----,    ,---,                             ,---,     
      ,--.'|_                         ,--.'|_      .'   .' \ ,--.' |                           ,--.' |     
      |  | :,'                        |  | :,'   ,----,'    ||  |  :                           |  |  :     
      :  : ' :            ,--,  ,--,  :  : ' :   |    :  .  ;:  :  :                  .--.--.  :  :  :     
    .;__,'  /     ,---.   |'. \/ .`|.;__,'  /    ;    |.'  / :  |  |,--.  ,--.--.    /  /    ' :  |  |,--. 
    |  |   |     /     \  '  \/  / ;|  |   |     `----'/  ;  |  :  '   | /       \  |  :  /`./ |  :  '   | 
    :__,'| :    /    /  |  \  \.' / :__,'| :       /  ;  /   |  |   /' :.--.  .-. | |  :  ;_   |  |   /' : 
      '  : |__ .    ' / |   \  ;  ;   '  : |__    ;  /  /-,  '  :  | | | \\__\/: . .  \\  \\    `.'  :  | | | 
      |  | '.'|'   ;   /|  / \\  \\  \\  |  | '.'|  /  /  /.`|  |  |  ' | : ,' .--.; |   `----.   \\  |  ' | : 
      ;  :    ;'   |  / |./__;   ;  \\ ;  :    ;./__;      :  |  :  :_:,'/  /  ,.  |  /  /`--'  /  :  :_:,' 
      |  ,   / |   :    ||   :/\\  \\ ; |  ,   / |   :    .'   |  | ,'   ;  :   .'   '--'.     /|  | ,'     
       ---`-'   \\   \\  / `---'  `--`   ---`-'  ;   | .'      `--''     |  ,     .-./  `--'---' `--''       
                 `----'                        `---'                    `--`---'                           
    
    {Style.RESET_ALL}
    """
    print(banner)

def compute_hash(data, hash_type="sha256"):
    """
    Compute the hash of the provided data using the specified hashing algorithm.

    Parameters:
    data (str): The input text to be hashed.
    hash_type (str): The type of hashing algorithm to use. Default is 'sha256'.

    Returns:
    str: The resulting hash value in hexadecimal format.

    Raises:
    ValueError: If an unsupported hash type is provided.
    """
    try:
        hash_object = hashlib.new(hash_type)
        hash_object.update(data.encode())
        return hash_object.hexdigest()
    except ValueError:
        raise ValueError("Unsupported hash type. Choose from: " + ", ".join(hashlib.algorithms_available))


def main():
    print_banner("text2hash")

    user_input = input("Enter the text you want to hash: ")

    # Display available hashing algorithms
    print("Choose hashing algorithm from the following list:")
    algorithms_list = sorted(hashlib.algorithms_available)
    for idx, alg in enumerate(algorithms_list, start=1):
        print(f"{idx}. {alg}")

    # Prompt the user to choose the hashing algorithm
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        hash_type = algorithms_list[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    # Compute and display the hash of the input
    try:
        hashed_value = compute_hash(user_input, hash_type)
        print(f"The {hash_type} hash of the input is: {hashed_value}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()